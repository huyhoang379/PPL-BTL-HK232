from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import Union

class VarSym:
    def __init__(self, name: str, typ: Type = None) -> None:
        self.name = name
        self.typ = typ
        
class FuncSym:
    def __init__(self, name: str, params: List[VarSym] = [], typ: Type = None, body: Stmt = None) -> None:
        self.name = name
        self.params = params
        self.typ = typ
        self.body = body

class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast: AST) -> None:
        self.ast = ast
        self.env = [[
            FuncSym("readNumber", [], NumberType()),
            FuncSym("readString", [], StringType()),
            FuncSym("readBool", [], BoolType()),
            FuncSym("writeBool", [VarSym("", BoolType())], VoidType()),
            FuncSym("writeString", [VarSym("", StringType())], VoidType()),
            FuncSym("writeNumber", [VarSym("", NumberType())], VoidType())
        ]] # Store from local to non-local to function to global scope
        self.return_type = None
        self.has_return = False # True if function has key return so that not to have another return
        self.func_name = None # Store func_name use for visitReturn
        self.resolved = True
        self.no_body = [] # Store function without body
        self.in_loop = [] # Empty if not in loop use for break and continue, use list not bool because it can loop in loop
        self.is_called = False # True if function is called
        self.return_list = []
        self.arr_ast = []
        self.curr_var_name = None # Store lhs of assign stmt or vardecl
        # self.arr_size = []
        
    def check(self) -> None:
        self.visit(self.ast, self.env)
        
    def resolveType(self, expr: Union[Id, CallExpr, CallStmt, ArrayLiteral], typ: Type, param): # Assume that name is found
        if type(expr) is Id:
            idex = None
            for idx in range(len(param)):
                sym = self.lookup(expr.name, param[idx], lambda x: x.name)
                if sym is not None and type(sym) is VarSym:
                    idex = idx
                    break
                
            if idex is not None:
                for idx in range(len(param[idex])):
                    if type(param[idex][idx]) is VarSym and param[idex][idx].name == expr.name and param[idex][idx].typ is None:
                        param[idex][idx] = VarSym(sym.name, typ)
        elif type(expr) in [CallExpr, CallStmt]:
            for idx in range(len(param[-1])):
                if type(param[-1][idx]) is FuncSym and param[-1][idx].name == expr.name.name and param[-1][idx].typ is None:
                    sym = param[-1][idx]
                    param[-1][idx] = FuncSym(sym.name, sym.params, typ, sym.body)
                    self.is_called = True
                    self.visit(FuncDecl(Id(sym.name), list(map(lambda x: VarDecl(Id(x.name), x.typ, None, None), sym.params)), sym.body), param)
                    self.is_called = False
        else:
            if type(typ) is not ArrayType:
                self.resolved = False
            else:
                for val in expr.value:
                    self.resolveType(val, typ.eleType if len(typ.size) == 1 else ArrayType(typ.size[1:], typ.eleType), param)
    
    def visitProgram(self, ast: Program, param):
        # decls: List[Decl] = []
        # flag = False
        for decl in ast.decl:
            # decls += [decl]
        # for decl in decls:
            self.visit(decl, param)
            
        if self.no_body != []:
            raise NoDefinition(self.no_body[0].name.name)
        
        flag = False
        for func in param[-1]: # param[-1] for safe, 0 is OK
            if type(func) is FuncSym and func.name == "main" and type(func.typ) is VoidType and func.params == []:
                flag = True
                break
            
        if not flag:
            raise NoEntryPoint()
        
    def visitVarDecl(self, ast: VarDecl, param):
        if self.lookup(ast.name.name, param[0], lambda x: x.name) is not None:
            raise Redeclared(Variable(), ast.name.name)
        
        self.curr_var_name = ast.name.name
        lhsType = ast.varType
        if ast.varInit is not None:
            rhsType = self.visit(ast.varInit, param)
            # if type(lhsType) is ArrayType and rhsType is None and self.arr_size != []:
            #     if lhsType.size[0] != self.arr_size[0]:
            #         raise TypeMismatchInStatement(ast)
            #     else:
            #         self.arr_size = []
            if lhsType is not None and rhsType is not None:
                if type(lhsType) is not type(rhsType):
                    raise TypeMismatchInStatement(ast)
                else:
                    if type(lhsType) is ArrayType:
                        if lhsType.size[:len(rhsType.size)] != rhsType.size:
                            raise TypeMismatchInStatement(ast)
                        else:
                            if rhsType.eleType is None:
                                self.resolveType(ast.varInit, lhsType, param)
                                if self.resolved == False:
                                    raise TypeCannotBeInferred(ast)
                                # param[0] += [VarSym(ast.name.name, lhsType)]
                            else:
                                if type(rhsType.eleType) is not type(lhsType.eleType):
                                    raise TypeMismatchInStatement(ast)
                    param[0] += [VarSym(ast.name.name, lhsType)]
            else:
                if rhsType is None and lhsType is None:
                    raise TypeCannotBeInferred(ast)
                elif rhsType is None and lhsType is not None:
                    if type(ast.varInit) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.varInit, lhsType, param)
                        if self.resolved == False:
                            raise TypeCannotBeInferred(ast)
                        param[0] += [VarSym(ast.name.name, lhsType)]
                    else:
                        raise TypeCannotBeInferred(ast)
                else:
                    param[0] += [VarSym(ast.name.name, rhsType)]
        else:
            param[0] += [VarSym(ast.name.name, lhsType)]
        
        self.arr_ast = []
        self.curr_var_name = None
        
    def visitFuncDecl(self, ast: FuncDecl, param):
        params = []
        for param_decl in ast.param:
            if self.lookup(param_decl.name.name, params, lambda x: x.name) is not None:
                raise Redeclared(Parameter(), param_decl.name.name)
            else:
                params += [VarSym(param_decl.name.name, self.visit(param_decl.varType, param))]

        # Store new scope
        param = [params] + param
        
        func = self.lookup(ast.name.name, param[-1], lambda x: x.name)
        if func is not None and type(func) is VarSym:
            raise Redeclared(Function(), ast.name.name)
        
        if func is not None and ast.body is None and self.is_called == False:
            raise Redeclared(Function(), ast.name.name)
        
        if func is not None and func.body is not None and self.is_called == False:
            raise Redeclared(Function(), ast.name.name)
        
        if ast.body is None:
            if self.is_called == False:
                self.no_body += [ast]
            # Store to global scope
            param[-1] += [FuncSym(ast.name.name, params, None, None)]
        else:
            self.func_name = ast.name.name
            for f in self.no_body:
                if f.name.name == self.func_name:
                    self.no_body.remove(f)
                    
            func_found = False
            for idx in range(len(param[-1])):
                if type(param[-1][idx]) is FuncSym and param[-1][idx].name == ast.name.name:
                    func_found = True
                    if len(param[-1][idx].params) != len(params):
                        raise Redeclared(Function(), ast.name.name)
                    
                    for idex in range(len(params)):
                        if type(param[-1][idx].params[idex].typ) is not type(params[idex].typ) or (type(param[-1][idx].params[idex].typ) is ArrayType and type(params[idex].typ) is ArrayType and (param[-1][idx].params[idex].typ.size != params[idex].typ.size or (type(param[-1][idx].params[idex].typ.eleType) is not type(params[idex].typ.eleType)))):
                            raise Redeclared(Function(), ast.name.name)
                        
                    self.visit(ast.body, param)
                    param[-1][idx] = FuncSym(ast.name.name, params, self.return_type if self.return_type is not None else (VoidType() if self.return_list == [] else None), ast.body)
                    break
                
            if not func_found:
                param[-1] += [FuncSym(ast.name.name, params, self.return_type, ast.body)]
                self.visit(ast.body, param)
                rettype = self.return_type if self.return_type is not None else (VoidType() if self.return_list == [] else None)
                print(type(rettype))
                if param[-1][-1].typ is None:
                    param[-1][-1] = FuncSym(ast.name.name, params, rettype, ast.body)
                    
        self.return_type = None
        self.has_return = False
        param = param[1:] # Remove Function Scope after visit success
        self.return_list = []
                                
    def visitNumberType(self, ast: NumberType, param):
        return NumberType()

    def visitBoolType(self, ast: BoolType, param):
        return BoolType()

    def visitStringType(self, ast: StringType, param):
        return StringType()

    def visitArrayType(self, ast: ArrayType, param):
        return ArrayType(ast.size, ast.eleType)
    
    def visitBinaryOp(self, ast: BinaryOp, param):
        expr1 = self.visit(ast.left, param)
        expr2 = self.visit(ast.right, param)
        if ast.op in ['+', '-', '*', '/', '%', '=', '!=', '>', '<', '>=', '<=']:
            if expr1 is None:
                if type(ast.left) in [Id, CallExpr]:
                    self.resolveType(ast.left, NumberType(), param)
                    expr1 = NumberType()
                    if self.resolved == False:
                        return None
                # Sai vì ở đây cần xử lý trường hợp Array Cell
                else:
                    return None
                
            if expr2 is None:
                if type(ast.right) in [Id, CallExpr]:
                    self.resolveType(ast.right, NumberType(), param)
                    expr2 = NumberType()
                    if self.resolved == False:
                        return None
                # Sai vì ở đây cần xử lý trường hợp Array Cell
                else:
                    return None
                
            if type(expr1) is not NumberType or type(expr2) is not NumberType:
                raise TypeMismatchInExpression(ast)
            
            return NumberType() if ast.op in ['+', '-', '*', '/', '%'] else BoolType()
        
        elif ast.op in ['and', 'or']:
            if expr1 is None:
                if type(ast.left) in [Id, CallExpr]:
                    self.resolveType(ast.left, BoolType(), param)
                    expr1 = BoolType()
                    if self.resolved == False:
                        return None
                # Sai vì ở đây cần xử lý trường hợp Array Cell
                else:
                    return None
                
            if expr2 is None:
                if type(ast.right) in [Id, CallExpr]:
                    self.resolveType(ast.right, BoolType(), param)
                    expr2 = BoolType()
                    if self.resolved == False:
                        return None
                # Sai vì ở đây cần xử lý trường hợp Array Cell
                else:
                    return None
                
            if type(expr1) is not BoolType or type(expr2) is not BoolType:
                raise TypeMismatchInExpression(ast)
            
            return BoolType()
        
        else:
            if expr1 is None:
                if type(ast.left) in [Id, CallExpr]:
                    self.resolveType(ast.left, StringType(), param)
                    expr1 = StringType()
                    if self.resolved == False:
                        return None
                # Sai vì ở đây cần xử lý trường hợp Array Cell
                else:
                    return None
                
            if expr2 is None:
                if type(ast.right) in [Id, CallExpr]:
                    self.resolveType(ast.right, StringType(), param)
                    expr2 = StringType()
                    if self.resolved == False:
                        return None
                # Sai vì ở đây cần xử lý trường hợp Array Cell
                else:
                    return None
                
            if type(expr1) is not StringType or type(expr2) is not StringType:
                raise TypeMismatchInExpression(ast)
            
            return StringType() if ast.op == '...' else BoolType()
    
    def visitUnaryOp(self, ast: UnaryOp, param):
        exprType = self.visit(ast.operand, param)
        if ast.op == '-':
            if exprType is None:
                if type(ast.operand) in [Id, CallExpr]:
                    self.resolveType(ast.operand, NumberType(), param)
                    if self.resolved == False:
                        return None
                    else:
                        return NumberType()
                # Sai vì ở đây cần xử lý trường hợp Array Cell
                else:
                    return None
            else:
                if type(exprType) is not NumberType:
                    raise TypeMismatchInExpression(ast)
                else:
                    return NumberType()
        else:
            if exprType is None:
                if type(ast.operand) in [Id, CallExpr]:
                    self.resolveType(ast.operand, BoolType(), param)
                    if self.resolved == False:
                        return None
                    else:
                        return BoolType()
                # Sai vì ở đây cần xử lý trường hợp Array Cell
                else:
                    return None
            else:
                if type(exprType) is not BoolType:
                    raise TypeMismatchInExpression(ast)
                else:
                    return BoolType()
                
    def visitCallExpr(self, ast: CallExpr, param):
        if self.curr_var_name is not None and ast.name.name == self.curr_var_name:
            raise TypeMismatchInExpression(ast)
        
        self.resolved = True
        exclude_last = param[:-1] # Temp not use global scope for Check if vardecl has same name with funcdecl in global scope
        for para in exclude_last:
            if self.lookup(ast.name.name, para, lambda x: x.name) is not None:
                raise TypeMismatchInExpression(ast)
            
        found = self.lookup(ast.name.name, param[-1], lambda x: x.name)
        if found is None or (found is not None and type(found) is not FuncSym):
            raise Undeclared(Function(), ast.name.name)
        else:
            if type(found.typ) is VoidType:
                raise TypeMismatchInExpression(ast)
            
            if len(ast.args) != len(found.params):
                raise TypeMismatchInExpression(ast)

            for idx in range(len(ast.args)):
                arg_typ = self.visit(ast.args[idx], param)
                if arg_typ is None:
                    if type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.args[idx], found.params[idx].typ, param)
                        if self.resolved == False:
                            return None
                    else:
                        return None
                # elif arg_typ is None:
                #     self.resolved = False
                #     return None
                else:
                    if type(arg_typ) is not type(found.params[idx].typ):
                        raise TypeMismatchInExpression(ast)
                    else:
                        if type(arg_typ) is ArrayType:
                            if found.params[idx].typ.size[:len(arg_typ.size)] != arg_typ.size:
                                raise TypeMismatchInExpression(ast)
                            
                            if arg_typ.eleType is None:
                                if type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                                    self.resolveType(ast.args[idx], found.params[idx].typ, param)
                                    if self.resolved == False:
                                        raise TypeCannotBeInferred(ast)
                                    
                                    arg_typ = found.params[idx].typ
                                else:
                                    raise TypeCannotBeInferred(ast)
                            
                            if type(arg_typ.eleType) is not type(found.params[idx].typ.eleType) or found.params[idx].typ.size != arg_typ.size:
                                raise TypeMismatchInExpression(ast)
            
            return found.typ    
    
    def visitId(self, ast: Id, param):
        if self.curr_var_name is not None and ast.name == self.curr_var_name:
            raise Undeclared(Identifier(), ast.name)
        
        self.resolved = True
        found = None
        for para in param:
            sym = self.lookup(ast.name, para, lambda x: x.name)
            if sym is not None and isinstance(sym, VarSym):
                found = para
                break
            
        if found is None:
            raise Undeclared(Identifier(), ast.name)
        else:
            for idx in range(len(found)):
                if found[idx].name == ast.name and type(found[idx]) is VarSym:
                    return found[idx].typ
        
    def visitArrayCell(self, ast: ArrayCell, param):
        self.resolved = True
        first = self.visit(ast.arr, param)
        if first is None:
            self.resolved = False
            return None
        else:
            if type(first) is not ArrayType:
                raise TypeMismatchInExpression(ast)
            else:
                # Số chiều khai báo ít hơn số chiều truy cập
                if len(first.size) < len(ast.idx):
                    raise TypeMismatchInExpression(ast)
                else:
                    for idx in range(len(ast.idx)):
                        typ = self.visit(ast.idx[idx], param)
                        if typ is None:
                            if type(ast.idx[idx]) in [Id, CallExpr]:
                                self.resolveType(ast.idx[idx], NumberType(), param)
                                if self.resolved == False:
                                    return None
                                else:
                                    typ = NumberType()
                            # Sai vì ở đây cần xử lý trường hợp Array Cell
                            else:
                                return None
                            
                        if type(typ) is not NumberType:
                            raise TypeMismatchInExpression(ast)
                    
                    # Chiều khai báo = chiều truy cập thì trả về kiểu của phần tử, > thì trả về mảng    
                    return first.eleType if len(first.size) == len(ast.idx) else ArrayType(first.size[len(ast.idx):], first.eleType)
    
    def visitBlock(self, ast: Block, param):
        param = [[]] + param
        for stmt in ast.stmt:
            self.visit(stmt, param)
            
        self.has_return = False
        param = param[1:]
        self.arr_ast = []

    def visitIf(self, ast: If, param):
        cond_typ = self.visit(ast.expr, param)
        if cond_typ is None:
            if type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
                self.resolveType(ast.expr, BoolType(), param)
                if self.resolved == False:
                    raise TypeCannotBeInferred(ast)
                cond_typ = BoolType()
            else:
                raise TypeCannotBeInferred(ast)
        
        if type(cond_typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, param)
        self.has_return = False
        for elifExpr, elif_stmt in ast.elifStmt:
            cond_typ = self.visit(elifExpr, param)
            if cond_typ is None:
                if type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
                    self.resolveType(elifExpr, BoolType(), param)
                    if self.resolved == False:
                        raise TypeCannotBeInferred(ast)
                    
                    cond_typ = BoolType()
                else:
                    raise TypeCannotBeInferred(ast)
                
            if type(cond_typ) is not BoolType:
                raise TypeMismatchInStatement(ast)
            
            self.visit(elif_stmt, param)
            self.has_return = False
        
        if ast.elseStmt:
            self.visit(ast.elseStmt, param)
            
        self.arr_ast = []    

    def visitFor(self, ast: For, param):
        self.in_loop += ["H"]
        scala_typ = self.visit(ast.name, param)
        if scala_typ is None:
            self.resolveType(ast.name, NumberType(), param)
            scala_typ = NumberType()
            
        if type(scala_typ) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        cond_typ = self.visit(ast.condExpr, param)
        if cond_typ is None:
            if type(ast.condExpr) in [Id, CallExpr]:
                self.resolveType(ast.condExpr, BoolType(), param)
                cond_typ = BoolType()
                if self.resolved == False:
                    raise TypeCannotBeInferred(ast)
            else:
                raise TypeCannotBeInferred(ast)
        
        if type(cond_typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        update_typ = self.visit(ast.updExpr, param)
        if update_typ is None:
            if type(ast.updExpr) in [Id, CallExpr]:
                self.resolveType(ast.updExpr, NumberType(), param)
                update_typ = NumberType()
                if self.resolved == False:
                    raise TypeCannotBeInferred(ast)    
            else:
                raise TypeCannotBeInferred(ast)
            
        if type(update_typ) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.body, param)
        self.arr_ast = []
        self.in_loop = self.in_loop[:-1]

    def visitContinue(self, ast: Continue, param):
        if self.in_loop == []:
            raise MustInLoop(ast)
        
        self.arr_ast = []

    def visitBreak(self, ast: Break, param):
        if self.in_loop == []:
            raise MustInLoop(ast)
        
        self.arr_ast = []
    
    def visitReturn(self, ast: Return, param):
        if self.has_return:
            return
        
        self.has_return = True
        if ast.expr is None:
            self.return_type = VoidType()
            func = self.lookup(self.func_name, param[-1], lambda x: x.name)
            if func.typ is not None and type(func.typ) is not VoidType:
                raise TypeMismatchInStatement(ast)
        else:
            rettype = self.visit(ast.expr, param)
            func = self.lookup(self.func_name, param[-1], lambda x: x.name)
            if func.typ is None:
                if rettype is None:
                    if self.resolved == False:
                        raise TypeCannotBeInferred(ast)
                    else:
                        self.return_list += [ast] # Store temp for resolved later
                else:
                    self.return_type = rettype
                    for idx in range(len(param[-1])):
                        if type(param[-1][idx]) is FuncSym and param[-1][idx].name == self.func_name:
                            sym = param[-1][idx]
                            param[-1][idx] = FuncSym(sym.name, sym.params, rettype, sym.body)
                    
                    if self.return_list != []:
                        while self.return_list != []:
                            if type(self.return_list[0].expr) in [Id, CallExpr, ArrayLiteral]:
                                self.resolveType(self.return_list[0].expr, rettype, param)
                                if self.resolved == False:
                                    raise TypeCannotBeInferred(self.return_list[0])
                                else:
                                    self.return_list = self.return_list[1:]
                            else:
                                raise TypeCannotBeInferred(self.return_list[0])
            else:
                if type(func.typ) is VoidType: # return has expr but func.typ is VoidType
                    raise TypeMismatchInStatement(ast)
                
                if rettype is None:
                    if self.resolved == False:
                        raise TypeCannotBeInferred(ast)
                    elif type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.expr, func_typ, param)
                        if self.resolved == False:
                            raise TypeCannotBeInferred(ast)
                    else:
                        raise TypeCannotBeInferred(ast)
                else:
                    if type(func.typ) is not type(rettype):
                        raise TypeMismatchInStatement(ast)
                    else:
                        if type(func.typ) is ArrayType:
                            if func.typ.size[:len(rettype.size)] != rettype.size:
                                raise TypeMismatchInStatement(ast)
                            
                            if rettype.eleType is None:
                                if type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
                                    self.resolveType(ast.expr, func_typ, param)
                                    if self.resolved == False:
                                        raise TypeCannotBeInferred(ast)
                                    rettype = func.typ
                                else:
                                    raise TypeCannotBeInferred(ast)
                            
                            if type(rettype.eleType) is not type(func.typ.eleType) or func.typ.size != rettype.size:
                                raise TypeMismatchInExpression(ast)
                    
                    self.return_type = func.typ 
                    
        self.arr_ast = []
    
    def visitAssign(self, ast: Assign, param):
        rhsType = self.visit(ast.rhs, param)
        lhsType = self.visit(ast.lhs, param)
        if rhsType is None and lhsType is None:
            raise TypeCannotBeInferred(ast)
        
        if rhsType is not None and lhsType is None:
            if type(ast.lhs) is Id:
                self.resolveType(ast.lhs, rhsType, param)
            # thiếu biết kiểu ArrayCell lhs
            else:
                raise TypeCannotBeInferred(ast)
        elif rhsType is None and lhsType is not None:
            if type(ast.rhs) in [Id, CallExpr, ArrayLiteral]:
                self.resolveType(ast.rhs, lhsType, param)
                if self.resolved == False:
                    raise TypeCannotBeInferred(ast)
            else:
                raise TypeCannotBeInferred(ast)
        else:
            if type(lhsType) is VoidType:
                raise TypeMismatchInStatement(ast)
            elif type(lhsType) is not type(rhsType):
                raise TypeMismatchInStatement(ast)
            else:
                if type(lhsType) is ArrayType:
                    if lhsType.size[:len(rhsType.size)] != rhsType.size:
                        raise TypeMismatchInStatement(ast)
                    else:
                        if rhsType.eleType is None:
                            if type(ast.rhs) in [Id, CallExpr, ArrayLiteral]:
                                self.resolveType(ast.rhs, lhsType, param)
                                if self.resolved == False:
                                    raise TypeCannotBeInferred(ast)
                                
                                rhsType = lhsType
                            else:
                                raise TypeCannotBeInferred(ast)
                            
                        if type(lhsType.eleType) is not type(rhsType.eleType) or lhsType.size != rhsType.size:
                            raise TypeMismatchInStatement(ast)
                        
        self.arr_ast = []  

    def visitCallStmt(self, ast: CallStmt, param):
        self.resolved = True
        exclude_last = param[:-1] # Temp not use global scope for Check if vardecl has same name with funcdecl in global scope
        for para in exclude_last:
            if self.lookup(ast.name.name, para, lambda x: x.name) is not None:
                raise TypeMismatchInStatement(ast)
            
        found = self.lookup(ast.name.name, param[-1], lambda x: x.name)
        if found is None or (found is not None and type(found) is not FuncSym):
            raise Undeclared(Function(), ast.name.name)
        else:
            if found.typ is not None and type(found.typ) is not VoidType:
                raise TypeMismatchInStatement(ast)
            
            if len(ast.args) != len(found.params):
                raise TypeMismatchInStatement(ast)

            for idx in range(len(ast.args)):
                arg_typ = self.visit(ast.args[idx], param)
                if arg_typ is None and type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                    self.resolveType(ast.args[idx], found.params[idx].typ, param)
                    if self.resolved == False:
                        raise TypeCannotBeInferred(ast)
                elif arg_typ is None:
                    raise TypeCannotBeInferred(ast)
                else:
                    if type(arg_typ) is not type(found.params[idx].typ):
                        raise TypeMismatchInStatement(ast)
                    else:
                        if type(arg_typ) is ArrayType:
                            if found.params[idx].typ.size[:len(arg_typ.size)] != arg_typ.size:
                                raise TypeMismatchInStatement(ast)
                            
                            if arg_typ.eleType is None:
                                if type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                                    self.resolveType(ast.args[idx], found.params[idx].typ, param)
                                    if self.resolved == False:
                                        raise TypeCannotBeInferred(ast)
                                    
                                    arg_typ = found.params[idx].typ
                                else:
                                    raise TypeCannotBeInferred(ast)
                            
            if found.typ is None:
                self.resolveType(ast, VoidType(), param)
                    
        self.arr_ast = []          
    
    def visitNumberLiteral(self, ast: NumberLiteral, param):
        return NumberType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, param):
        return BoolType()

    def visitStringLiteral(self, ast: StringLiteral, param):
        return StringType()
    
    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        # if ast not in self.arr_ast:
        self.arr_ast += [ast]
        
        typ = None
        # temp_size = 0
        for val in ast.value:
            # if type(val) in [Id, CallExpr, ArrayLiteral]:
            #     temp_size += 1
            typ = self.visit(val, param)
            if typ is not None:
                break
        # self.arr_size += [temp_size]
            
        if typ is not None:
            # self.arr_size = []
            for idx in range(len(ast.value)):
                val_typ = self.visit(ast.value[idx], param)
                if val_typ is None:
                    if type(ast.value[idx]) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.value[idx], typ, param)
                        if self.resolved == False:
                            return None
                        else:
                            val_typ = typ
                    else:
                        return None
                    
                if type(val_typ) is not type(typ):
                    raise TypeMismatchInExpression(self.arr_ast[0])
                else:
                    if type(val_typ) is ArrayType:
                        if val_typ.size[:len(typ.size)] != typ.size:
                            raise TypeMismatchInExpression(self.arr_ast[0])
                        else:
                            if val_typ.eleType is None:
                                if type(ast.value) in [Id, CallExpr, ArrayLiteral]:
                                    self.resolveType(ast.value, typ, param)
                                    if self.resolved == False:
                                        return None
                                    val_typ = typ
                                else:
                                    return None
                            
                            if type(val_typ.eleType) is not type(typ.eleType) or val_typ.size != typ.size:
                                raise TypeMismatchInExpression(self.arr_ast[0])
                             
            if type(typ) is not ArrayType:
                self.arr_ast = self.arr_ast[:-1]
                return ArrayType([len(ast.value)], typ)
            else:
                self.arr_ast = self.arr_ast[:-1]
                return ArrayType([len(ast.value)] + typ.size, typ.eleType)
        # return None 