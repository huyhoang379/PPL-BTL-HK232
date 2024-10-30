from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [[Symbol("readNumber", MType(list(), NumberType()), CName(self.libName)),
                Symbol("writeNumber", MType([NumberType()], VoidType()), CName(self.libName)),
                Symbol("readString", MType(list(), StringType()), CName(self.libName)),
                Symbol("writeString", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("readBool", MType(list(), BoolType()), CName(self.libName)),
                Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
                ]]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value

class ClassType(Type):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "Class({0})".format(str(self.name))

class ClassDecl(Decl):
    def __init__(self, name, memlist: list[VarDecl]):
        self.name = name
        self.memlist = memlist

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path    
        self.className = 'ZCodeClass'   
        self.emit = Emitter(self.path + "/" + self.className + ".j")    
        self.stage = 0  
        self.has_break = False  
        self.arr_type = None
        self.func_lst = []    
        self.classEnv = []  
        self.has_return = False
        self.clinit = None
        self.lhs_type = None
        
    def update(self, name, typ_, o):    
        # name: name of function with type None 
        # typ_: Type to change  
        # o: Any    
        for x in o.sym[-1]: 
            if x.name == name:   
                x.mtype.rettype = typ_   
                break   
        
    def defaultValue(self, typ_):   
        varType = type(typ_)    
        if varType is NumberType:   
            return NumberLiteral(0.0)   
        elif varType is StringType: 
            return StringLiteral("")    
        elif varType is BoolType:   
            return BooleanLiteral(False)   
        else:   
            expr = []   
            if len(typ_.size) == 1: 
                for x in range(typ_.size[0]):   
                    expr += [self.defaultValue(typ_.eleType)]   
                return ArrayLiteral(expr)   
            else:   
                dimen = typ_.size   
                for x in range(dimen[0]):   
                    temp = self.defaultValue(ArrayType(dimen[1:], typ_.eleType))    
                    expr += [temp]  
                return ArrayLiteral(expr)   

    def visitProgram(self, ast, c):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))    
        e = SubBody(None, self.env) 
        vardecl_has_init = []   
        var_decl_lst = []       
        flag = []   
        for x in ast.decl: 
            if type(x) is FuncDecl:
                e.sym[0] += [Symbol(x.name.name, MType(list(map(lambda y: y.varType, x.param)), None), CName(self.className))] 
                self.func_lst = [(x,None)] + self.func_lst if x.name.name != 'main' else self.func_lst + [(x,None)]    
                flag += [False] 
            else:   
                if x.varInit is not None:     
                    vardecl_has_init += [AssignStmt(x.name, x.varInit)]    
                elif x.varInit is None and type(x.varType) is ArrayType:   
                    vardecl_has_init += [x] 
                var_decl_lst += [x] 

        for x in var_decl_lst:  
            e.sym[0] += [self.visit(x, e)]  
        
        self.genMETHOD(FuncDecl(Id("<init>"), [], None), e, Frame("<init>", VoidType)) 
        self.func_lst.reverse() 
        t = self.func_lst.pop(0)    
        self.func_lst.append(t) 
        
        for x in self.func_lst: 
            self.visit(x[0], e)    
        
        if vardecl_has_init != []:  
            self.clinit = "<clinit>"    
            self.genMETHOD(FuncDecl(Id("<clinit>"), [], Block(vardecl_has_init)), e, Frame("<clinit>", VoidType))   
            self.clinit = None  
        self.emit.emitEPILOG()  
        return c    

    def visitClassDecl(self, ast, c):   
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        [self.visit(ele, SubBody(None, self.env))
         for ele in ast.memlist if type(ele) == MethodDecl]
        self.classEnv += [(ast.name, attrSym)]
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
        ), None, Block([], [])), c, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, ast, o, frame): 
        # for x in ast.param:
        #     if type(x.typ) is AutoType:
        #         return None
        self.has_return = False
        isInit = ast.name.name == "<init>"
        isMain = (ast.name.name == "main" and len(ast.param) == 0)
        returnType = None
        methodName = ast.name.name
        intype = [ArrayType([], StringType())] if isMain else list(map(lambda x: x.varType, ast.param))

        if returnType is None:
            if type(ast.body) is Block:
                o.sym = [[]] + o.sym
                for x in ast.param:
                    o.sym[0] += [Symbol(x.name.name, x.varType, Index(frame.getNewIndex()))]
                frame.setCurrIndex(0)
                for x in ast.body.stmt:
                    if type(x) is Return and x.expr is not None:
                        code, typ = self.visit(x.expr, Access(frame, o.sym, False, True))
                        returnType = typ
                        break
                    elif type(x) is Return and x.expr is None:
                        returnType = VoidType()
                        break
                returnType = VoidType()
                o.sym = o.sym[1:]
            else:
                if type(ast.body) is Return and ast.body.expr is not None:
                    code, typ = self.visit(ast.body.expr, Access(frame, o.sym, False, True))
                    returnType = typ
                elif (type(ast.body) is Return and ast.body.expr is None) or ast.body is None:
                    returnType = VoidType()
                
        self.update(ast.name.name, returnType, o)
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o.sym
                    
        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(frame, [self.visit(ele, env)] + env.sym), ast.param, SubBody(frame, []))

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        if ast.body is not None:
            self.visit(ast.body, SubBody(frame, glenv)) 
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType and not self.has_return:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitMethodDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name.name, MType([x.typ for x in ast.param], ast.returnType), CName(self.className))
    
    def visitVarDecl(self, ast, o):
        if type(ast.varType) is ArrayType:  
            self.arr_type = ast.varType 
        if o.frame is None: 
            frame = Frame(ast.name.name, ast.varType)   
            if ast.varInit is None: 
                code = self.emit.emitATTRIBUTE(ast.name.name, ast.varType, False, CName(self.className))    
                self.emit.printout(code)    
                return Symbol(ast.name.name, ast.varType, CName(self.className)) 
            else:   
                self.lhs_type = ast.varType 
                init, rt = self.visit(ast.varInit, SubBody(frame, o.sym)) 
                if rt is None:
                    self.update(ast.varInit if type(ast.varInit) is Id else ast.varInit.name, ast.varType, o.sym)
                    rt = ast.varType  
                code = self.emit.emitATTRIBUTE(ast.name.name, rt, False, CName(self.className)) 
                self.emit.printout(code)    
                return Symbol(ast.name.name, rt, CName(self.className))  
        else:   
            idx = o.frame.getNewIndex() 
            if ast.varInit is None:    
                if type(ast.varType) is ArrayType:  
                    if self.clinit == "<clinit>":   
                        ret_code = ""   
                        if len(ast.varType.size) == 1:  
                            lit, typ = self.visit(NumberLiteral(ast.varType.size[0]), o)    
                            ret_code = lit + self.emit.emitNEWARRAY(ast.varType.eleType, o.frame) + self.emit.emitPUTSTATIC(self.className + "." + ast.name.name, ast.varType, o.frame) 
                        else:   
                            for x in ast.varType.size:  
                                lit, typ = self.visit(NumberLiteral(x), o)  
                                ret_code += lit 
                            ret_code += self.emit.emitMULTIANEWARRAY(ast.varType, o.frame) + self.emit.emitPUTSTATIC(self.className + "." + ast.name.name, ast.varType, o.frame)     
                        self.emit.printout(ret_code)    
                        return Symbol(ast.name.name, ast.varType, Index(idx) )
                    else:   
                        return self.visit(VarDecl(ast.name, ast.varType, self.defaultValue(ast.varType)), o)    
                else:   
                    return self.visit(VarDecl(ast.name, ast.varType, self.defaultValue(ast.varType)), o)    
            else:   
                self.lhs_type = ast.varType 
                init, rt = self.visit(ast.varInit, Access(o.frame, o.sym, False, True)) 
                init = init + self.emit.emitALOAD(rt, o.frame) if type(ast.varInit) is ArrayCell else init
                if rt is None:
                    self.update(ast.varInit if type(ast.varInit) is Id else ast.varInit.name, ast.varType, o.sym)
                    rt = ast.varType
                code = self.emit.emitVAR(idx, ast.name.name, rt, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
                self.emit.printout(code + init + self.emit.emitWRITEVAR(ast.name.name, rt, idx, o.frame))
                return Symbol(ast.name.name, rt, Index(idx))
    
    def visitFuncDecl(self, ast, o):
        self.func = ast.name
        frame = Frame(ast.name, None)
        self.genMETHOD(ast, o, frame)

    def visitBinaryOp(self, ast, o):
        if type(ast.left) is CallExpr:
            for x in self.func_lst:
                if x[0].name == ast.left.name and x[1] is None:
                    e1c, self.lhs_type = self.visit(ast.right, o)
                    x[1] = self.lhs_type
        
        elif type(ast.right) is CallExpr:
            for x in self.func_lst:
                if x[0].name == ast.right.name and x[1] is None:
                    e1c, self.lhs_type = self.visit(ast.left, o)
                    x[1] = self.lhs_type
                    
        e1c, e1t = self.visit(ast.left, o)  
        e2c, e2t = self.visit(ast.right, o) 
        if type(e1t) is type(e2t):  
            if type(e1t) is StringType: 
                if type(ast.left) is StringLiteral and type(ast.right) is StringLiteral:    
                    o.frame.pop()   
                    o.frame.pop()      
                    if ast.op in ['...']:   
                        return self.visit(StringLiteral(ast.left.value + ast.right.value), o)   
                    else:   
                        return e1c + e2c + self.emit.emitREOP(ast.op, e1t, o.frame), BoolType() 
                else:
                    code1 = e1c + ("" if type(ast.left) is not ArrayCell else self.emit.emitALOAD(e1t, o.frame))    
                    code2 = e2c + ("" if type(ast.right) is not ArrayCell else self.emit.emitALOAD(e2t, o.frame))   
                    code = code1 + code2 + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), o.frame) 
                    return code, StringType()   
            else:   
                code1 = e1c + ("" if type(ast.left) is not ArrayCell else self.emit.emitALOAD(e1t, o.frame))    
                code2 = e2c + ("" if type(ast.right) is not ArrayCell else self.emit.emitALOAD(e2t, o.frame))   
                if ast.op in ['+', '-']:    
                    if isinstance(ast.left, NumberLiteral) and isinstance(ast.right, NumberLiteral):    
                        if ast.op == '+':   
                            return self.visit(NumberLiteral(ast.left.value + ast.right.value), o)   
                        return self.visit(NumberLiteral(ast.left.value - ast.right.value), o)   
                    return code1 + code2 + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t   
                elif ast.op in ['*', '/']:  
                    if isinstance(ast.left, NumberLiteral) and isinstance(ast.right, NumberLiteral):    
                        if ast.op == '*':   
                            return self.visit(NumberLiteral(ast.left.value * ast.right.value), o)   
                        else:   
                            if ast.right.val != 0:  
                                return self.visit(NumberLiteral(ast.left.value / ast.right.value), o)   
                    return code1 + code2 + self.emit.emitMULOP(ast.op, e1t, o.frame), e1t   
                elif ast.op in ['<', '>', '<=', '>=', '!=', '=']:   
                    return code1 + code2 + self.emit.emitREOP(ast.op, e1t, o.frame), BoolType() 
                elif ast.op == 'and':   
                    label1 = o.frame.getNewLabel()  
                    label2 = o.frame.getNewLabel()  
                    code1 = code1 + self.emit.emitIFTRUE(label1, o.frame) + self.emit.emitPUSHICONST(0, o.frame) + self.emit.emitGOTO(label2, o.frame)  
                    code2 = self.emit.emitLABEL(label1, o.frame) + code2 + self.emit.emitLABEL(label2, o.frame) 
                    return code1 + code2, BoolType()        
                elif ast.op == 'or':    
                    label1 = o.frame.getNewLabel()  
                    label2 = o.frame.getNewLabel()  
                    code1 = code1 + self.emit.emitIFFALSE(label1, o.frame) + self.emit.emitPUSHICONST(1, o.frame) + self.emit.emitGOTO(label2, o.frame) 
                    code2 = self.emit.emitLABEL(label1, o.frame) + code2 + self.emit.emitLABEL(label2, o.frame) 
                    return code1 + code2, BoolType()    
                elif ast.op == '%': 
                    return code1 + code2 + self.emit.emitMOD(o.frame), NumberType() 
    
    def visitUnaryOp(self, ast, o):
        ctxt = o    
        frame = ctxt.frame  
        bodyCode, bodyType = self.visit(ast.operand, o) 
        if ast.op == 'not': 
            return bodyCode + self.emit.emitNOT(BoolType(), frame), BoolType()  
        elif ast.op == '-': 
            return bodyCode + self.emit.emitNEGOP(bodyType, frame), bodyType    
    
    def visitCallExpr(self, ast, o):
        frame = o.frame 
        nenv = o.sym[-1]    
        sym = None  
        for x in range(len(nenv)):  
            if nenv[x].mtype.rettype is None:
                nenv[x].mtype.rettype = self.lhs_type
                sym = nenv[x]
            else:
                sym = nenv[x]  
        cname = sym.value.value     
        ctype = sym.mtype   
        in_ = ("", list())  
        for x in range(len(ast.args)):
            if type(ast.args[x]) is CallExpr:
                for y in self.func_lst:
                    if y[0].name == ast.args[x].name and y[1] is None:
                        self.lhs_type = ctype.partype[x]
                        y[1] = ctype.partype[x]
            str1, typ1 = self.visit(ast.args[x], Access(frame, o.sym, False, True)) 
            if type(ast.args[x]) is ArrayCell:    
                str1 += self.emit.emitALOAD(typ1, frame)   
            temp = in_[1] + [typ1]  
            in_ = (in_[0] + str1, in_[1] + temp)         
        return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.name.name, ctype, frame), ctype.rettype 
    
    def visitId(self, ast, o):
        frame = o.frame 
        idx = ast.name.find('.')    
        if idx != -1:   
            className = ast.name[:idx]  
            varName = ast.name[(idx + 1):]  
            _type = None    
            for x in self.classEnv: 
                if x[0] == className:   
                    for y in x[1]:  
                        if y.name == varName:   
                            _type = y.mtype 
            if isinstance(o, Access) and o.isLeft is True:
                return self.emit.emitPUTSTATIC(className + "." + varName, _type, frame), _type  
            else:   
                return self.emit.emitGETSTATIC(className + "." + varName, _type, frame), _type  
        sym = None  
        for x in o.sym: 
            flag = False    
            for y in x: 
                if y.name == ast:   
                    sym = y 
                    flag = True 
                    break   
            if flag == True:    
                break   
        _type = sym.mtype   
        if not isinstance(sym.value, Index):    
            if isinstance(o, Access) and o.isLeft is True:  
                return self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name.name, _type, frame), sym.mtype   
            else:   
                return self.emit.emitGETSTATIC(sym.value.value + "." + sym.name.name, _type, frame), sym.mtype   
        else:   
            if isinstance(o, Access) and o.isLeft is True:  
                return self.emit.emitWRITEVAR(sym.name.name, _type, sym.value.value, frame), sym.mtype   
            else:   
                return self.emit.emitREADVAR(sym.name.name, _type, sym.value.value, frame), sym.mtype    
    
    def visitArrayCell(self, ast, o):
        frame = o.frame 
        sym = None  
        name1 = ast.arr if type(ast.arr) is Id else ast.arr.name 
        for x in o.sym: 
            flag = False    
            for y in x: 
                if y == name1:  
                    sym = y 
                    flag = True 
                    break   
            if flag == True:    
                break   
        _type = sym.mtype   
        code = None 
        rt = None   
        if not isinstance(sym.value, Index):    
            code, rt = self.emit.emitGETSTATIC(sym.value.value + "." + sym.name.name, _type, frame), sym.mtype   
        else:   
            code, rt = self.emit.emitREADVAR(sym.name.name, _type, sym.value.value, frame), sym.mtype    
        dimension = _type.size  
        max_dimension = dimension   
        for x in range(len(ast.idx)):   
            dimension = dimension[1:]   
            e1c, e1t = self.visit(ast.idx[x], Access(frame, o.sym, False, False))   
            code += e1c 
            if x < len(max_dimension) - 1:  
                code += self.emit.emitALOAD(ArrayType(dimension, _type.eleType), o.frame)   
        if dimension == []: 
            return code, _type.eleType  
        else:       
            return code, ArrayType(dimension, _type.eleType)    
          
    def visitBlock(self, ast, o):
        self.stage += 1 
        glenv = SubBody(o.frame, [[]] + o.sym) if self.stage > 1 else o 
        self.has_return = False 
        self.has_break = False  
        for x in ast.stmt:
            if type(x) is VarDecl:  
                glenv.sym[0] += [self.visit(x, glenv)]  
            else:   
                self.visit(x, glenv)    
        self.stage -= 1 
           
    def visitIf(self, ast, o):
        if_exprCode, if_exprType = self.visit(ast.expr, Access(o.frame, o.sym, False, True))    
        self.emit.printout(if_exprCode) 
        if len(ast.elifStmt) == 0:  
            if ast.elseStmt is not None:    
                labelElse = o.frame.getNewLabel()   
                labelExit = o.frame.getNewLabel()   
                self.emit.printout(self.emit.emitIFFALSE(labelElse, o.frame))   
                self.visit(ast.thenStmt, o) 
                self.emit.printout(self.emit.emitGOTO(labelExit, o.frame))  
                self.emit.printout(self.emit.emitLABEL(labelElse, o.frame)) 
                self.visit(ast.elseStmt, o) 
                self.emit.printout(self.emit.emitLABEL(labelExit, o.frame)) 
            else:   
                labelExit = o.frame.getNewLabel()   
                self.emit.printout(self.emit.emitIFFALSE(labelExit, o.frame))   
                self.visit(ast.thenStmt, o) 
                self.emit.printout(self.emit.emitLABEL(labelExit, o.frame)) 
        else:   
            if ast.elseStmt is not None:    
                labelElse = o.frame.getNewLabel()   
                labelExit = o.frame.getNewLabel()   
                labelElif = [o.frame.getNewLabel()] 
                self.emit.printout(self.emit.emitIFFALSE(labelElif[0], o.frame))    
                self.visit(ast.thenStmt, o) 
                self.emit.printout(self.emit.emitGOTO(labelExit, o.frame))  
                for x in range(len(ast.elifStmt)):  
                    self.emit.printout(self.emit.emitLABEL(labelElif[x], o.frame))  
                    elif_exprCode, elif_exprType = self.visit(ast.elifStmt[x][0], Access(o.frame, o.sym, False, True))  
                    self.emit.printout(elif_exprCode)   
                    
                    if x + 1 == len(ast.elifStmt):  
                        self.emit.printout(self.emit.emitIFFALSE(labelElse, o.frame))   
                        self.visit(ast.elifStmt[x][1], o)   
                        self.emit.printout(self.emit.emitGOTO(labelExit, o.frame))  
                        self.emit.printout(self.emit.emitLABEL(labelElse, o.frame)) 
                        self.visit(ast.elseStmt, o) 
                        self.emit.printout(self.emit.emitLABEL(labelExit, o.frame)) 
                    else:   
                        labelElif.append(o.frame.getNewLabel()) 
                        self.emit.printout(self.emit.emitIFFALSE(labelElif[x+1], o.frame))  
                        self.visit(ast.elifStmt[x][1], o)   
                        self.emit.printout(self.emit.emitGOTO(labelExit, o.frame))  
            else:   
                labelExit = o.frame.getNewLabel()   
                labelElif = [o.frame.getNewLabel()] 
                self.emit.printout(self.emit.emitIFFALSE(labelElif[0], o.frame))    
                self.visit(ast.thenStmt, o) 
                self.emit.printout(self.emit.emitGOTO(labelExit, o.frame))  
                for x in range(len(ast.elifStmt)):  
                    self.emit.printout(self.emit.emitLABEL(labelElif[x], o.frame))  
                    elif_exprCode, elif_exprType = self.visit(ast.elifStmt[x][0], Access(o.frame, o.sym, False, True))  
                    self.emit.printout(elif_exprCode)   
                    
                    if x + 1 == len(ast.elifStmt):  
                        self.emit.printout(self.emit.emitIFFALSE(labelExit, o.frame))   
                        self.visit(ast.elifStmt[x][1], o)   
                        self.emit.printout(self.emit.emitLABEL(labelExit, o.frame)) 
                    else:   
                        labelElif.append(o.frame.getNewLabel()) 
                        self.emit.printout(self.emit.emitIFFALSE(labelElif[x+1], o.frame))  
                        self.visit(ast.elifStmt[x][1], o)   
                        self.emit.printout(self.emit.emitGOTO(labelExit, o.frame))  
    
    def visitFor(self, ast, o):
        ctxt = o    
        frame = ctxt.frame  
        nenv = ctxt.sym 
        exp, exptype = self.visit(ast.condExpr, Access(frame, nenv, False, True))   
        frame.enterLoop()   
        label1 = frame.getContinueLabel()   
        label2 = frame.getBreakLabel()  
        label3 = frame.getNewLabel()    
        self.emit.printout(self.emit.emitLABEL(label3, frame))  
        self.emit.printout(exp) 
        self.emit.printout(self.emit.emitIFFALSE(label2, frame))    
        self.visit(ast.body, o) 
        self.emit.printout(self.emit.emitLABEL(label1, frame))  
        self.visit(Assign(ast.name, BinExpr('+', ast.name, ast.updExpr)), o)    
        self.emit.printout(self.emit.emitGOTO(label3, frame))   
        self.emit.printout(self.emit.emitLABEL(label2, frame))  
        frame.exitLoop()    
    
    def visitContinue(self, ast, o):
        ctxt = o    
        frame = ctxt.frame  
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame)) 
                
    def visitBreak(self, ast, o):
        ctxt = o    
        frame = ctxt.frame  
        self.has_break = True   
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))    
      
    def visitReturn(self, ast, o):
        self.has_return = True  
        frame = o.frame 
        if ast.expr is None:    
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        else:   
            expcode, exptype = self.visit(ast.expr, Access(frame, o.sym, False, True))  
            if type(ast.expr) is ArrayCell: 
                expcode += self.emit.emitALOAD(exptype, frame)  
            self.emit.printout(expcode + self.emit.emitRETURN(exptype, frame))  
       
    def visitAssign(self, ast, o):
        frame = o.frame 
        frame.push()    
        frame.push()    
        expCode, expType = self.visit(ast.rhs, Access(frame, o.sym, False, True))   
        lhsCode, lhsType = self.visit(ast.lhs, Access(frame, o.sym, True, True))    
        if type(ast.rhs) is ArrayCell:  
            expCode += self.emit.emitALOAD(expType, frame)  
        self.emit.printout(expCode + lhsCode) if type(ast.lhs) is not ArrayCell else self.emit.printout(lhsCode + expCode + self.emit.emitASTORE(lhsType, frame))   
        frame.pop() 
        frame.pop() 
    
    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym[-1]
        sym = next(filter(lambda x: ast.name.name == x.name, nenv), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        for x in range(len(ast.args)):
            if type(ast.args[x]) is CallExpr:
                for y in self.func_lst:
                    if y[0].name == ast.args[x].name and y[1] is None:
                        self.lhs_type = ctype.partype[x]
                        y[1] = ctype.partype[x]
            str1, typ1 = self.visit(ast.args[x], Access(frame, o.sym, False, True)) 
            if type(ast.args[x]) is ArrayCell:    
                str1 += self.emit.emitALOAD(typ1, frame)   
            temp = in_[1] + [typ1]  
            in_ = (in_[0] + str1, in_[1] + temp)  
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.name.name, ctype, frame))
      
    def visitNumberLiteral(self, ast, o):
        if type(o) is Frame:    
            return self.emit.emitPUSHFCONST(str(ast.value), o), NumberType()    
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), NumberType()  
    
    def visitBooleanLiteral(self, ast, o):
        if type(o) is Frame:
            return self.emit.emitPUSHICONST(str(ast.value).lower(), o), BoolType()  
        return self.emit.emitPUSHICONST(str(ast.value).lower(), o.frame), BoolType()    
    
    def visitStringLiteral(self, ast, o):
        if type(o) is Frame:    
            return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o), StringType()  
        return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o.frame), StringType()    
    
    def visitArrayLiteral(self, ast, o):
        frame = o.frame if type(o) is not Frame else o  
        code = self.emit.emitPUSHICONST(str(len(ast.value)), frame)    
        if type(ast.value[0]) is not ArrayLiteral:  
            code += self.emit.emitNEWARRAY(self.arr_type.eleType, frame)    
            for x in range(len(ast.value)): 
                code += self.emit.emitDUP(frame)    
                e1c, e1t = self.visit(ast.value[x], o)  
                code += self.emit.emitPUSHICONST(str(x), frame)    
                code += e1c + self.emit.emitASTORE(e1t, frame)  
            return code, ArrayType([len(ast.value)], self.arr_type.eleType) 
        else:
            e1c, e1t = self.visit(ast.value[0], o)  
            code += self.emit.emitANEWARRAY(e1t, frame) 
            rt = None   
            for x in range(len(ast.value)): 
                code += self.emit.emitDUP(frame)    
                e1c, e1t = self.visit(ast.value[x], o)  
                rt = e1t    
                code += self.emit.emitPUSHICONST(str(x), frame)    
                code += e1c + self.emit.emitASTORE(e1t, frame)  
            return code, ArrayType([len(ast.value)] + rt.size, self.arr_type.eleType)   