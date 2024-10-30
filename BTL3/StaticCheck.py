from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class VarSym:
    def __init__(self, name: str, typ: Type = None) -> None:
        self.name = name
        self.typ = typ
        
class FuncSym:
    def __init__(self, name: str, param: List[VarSym] = [], typ: Type = None, body: Stmt = None) -> None:
        self.name = name
        self.param = param
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
        self.has_return = False
        self.func_name = None
        self.resolved = True
        self.no_body = [] # Store function without body
        self.in_loop = []
        self.is_called = False
        self.return_list = []
        self.arr_ast = []
        self.curr_var_name = None
        
    def check(self) -> None:
        self.visit(self.ast, self.env)
        
    def resolveType(self, expr: Id | CallExpr | CallStmt | ArrayLiteral, typ: Type, param): # Assume that name is found
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
                    param[-1][idx] = FuncSym(sym.name, sym.params, sym.body)
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
            return Redeclared(Variable(), ast.name.name)
        
        self.curr_var_name = ast.name.name
        lhsType = ast.varType
        if ast.varInit is not None:
            rhsType = self.visit(ast.varInit, param)
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
                            
    def visitNumberLiteral(self, ast: NumberLiteral, param):
        return NumberType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, param):
        return BoolType()

    def visitStringLiteral(self, ast: StringLiteral, param):
        return StringType()
    
    def visitNumberType(self, ast: NumberType, param):
        return NumberType()

    def visitBoolType(self, ast: BoolType, param):
        return BoolType()

    def visitStringType(self, ast: StringType, param):
        return StringType()

    def visitArrayType(self, ast: ArrayType, param):
        return ArrayType(ast.size, ast.eleType)
    
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
                raise TypeMismacthInExpression(ast)
            
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
                raise TypeMismacthInExpression(ast)
            
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
                raise TypeMismacthInExpression(ast)
            
            return StringType() if ast.op == '...' else BoolType()
        
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
    
    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        if ast not in self.arr_ast:
            self.arr_ast += [ast]
        
        typ = None
        for val in ast.value:
            typ = self.visit(val, param)
            if typ is not None:
                break
            
        if typ is not None:
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