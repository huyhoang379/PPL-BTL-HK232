from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):
    
    # //program is list of declaration, vardecl or funcdecl
    # program: (newlinelist | ) decllist EOF;
    # decllist: decl decllist | decl ;
    # decl: (vardecl | funcdecl) newlinelist;
    # newlinelist: NEW_LINE newlinelist | NEW_LINE;

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))
    
    def visitDecllist(self, ctx: ZCodeParser.DecllistContext):
        if ctx.decllist(): return [self.visit(ctx.decl())] + self.visit(ctx.decllist())
        return [self.visit(ctx.decl())]
    
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        if ctx.vardecl(): return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())
    
    # //variable declaration
    # vardecl: (typdecl | implicit_keyworddecl);
    # //declaration start with type
    # typdecl: typ_kw IDENTIFIER (arr_size | )(val_init | );
    # typ_kw: NUMBER_KW | BOOL_KW | STRING_KW;
    # val_init: ASSIGN_OP expr;
    # arr_size: LSB sizelist RSB;
    # sizelist: dimension CM sizelist | dimension;
    # dimension: NUMBERLIT;
    
    def visitVardecl(self, ctx: ZCodeParser.VardeclContext):
        if ctx.typdecl(): return self.visit(ctx.typdecl())
        return self.visit(ctx.implicit_keyworddecl())
    
    def visitTypdecl(self, ctx: ZCodeParser.TypdeclContext):
        if ctx.arr_size() and ctx.val_init(): return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.arr_size()), self.visit(ctx.typ_kw())), None, self.visit(ctx.val_init()))
        elif ctx.arr_size(): return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.arr_size()), self.visit(ctx.typ_kw())))
        elif ctx.val_init(): return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ_kw()), None, self.visit(ctx.val_init()))
        else: return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ_kw()))
        
    def visitTyp_kw(self, ctx: ZCodeParser.Typ_kwContext):
        if ctx.NUMBER_KW(): return NumberType()
        elif ctx.BOOL_KW(): return BoolType()
        else: return StringType()
        
    def visitVal_init(self, ctx: ZCodeParser.Val_initContext):
        return self.visit(ctx.expr())
    
    def visitArr_size(self, ctx: ZCodeParser.Arr_sizeContext):
        return self.visit(ctx.sizelist())
    
    def visitSizelist(self, ctx: ZCodeParser.SizelistContext):
        if ctx.sizelist(): return [self.visit(ctx.dimension())] + self.visit(ctx.sizelist())
        return [self.visit(ctx.dimension())]
    
    def visitDimension(self, ctx: ZCodeParser.DimensionContext):
        return float(ctx.NUMBERLIT().getText())
    
    # //declaration start witch implicitkeyword
    # implicit_keyworddecl: varkwdecl | dynamickwdecl;
    # varkwdecl: VAR_KW IDENTIFIER val_init;
    # dynamickwdecl: DYNAMIC_KW IDENTIFIER (val_init | );
    
    def visitImplicit_keyworddecl(self, ctx: ZCodeParser.Implicit_keyworddeclContext):
        return self.visit(ctx.varkwdecl()) if ctx.varkwdecl() else self.visit(ctx.dynamickwdecl())
        
    def visitVarkwdecl(self, ctx: ZCodeParser.VarkwdeclContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.VAR_KW().getText(), self.visit(ctx.val_init()))
    
    def visitDynamickwdecl(self, ctx: ZCodeParser.DynamickwdeclContext):
        if ctx.val_init(): return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.DYNAMIC_KW().getText(), self.visit(ctx.val_init()))
        else: return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.DYNAMIC_KW().getText())

    # funcdecl: FUNC_KW IDENTIFIER LB paramlist RB ((newlinelist | ) returnstmt | (newlinelist | ) blockstmt |);
    # paramlist: paramlistprime | ;
    # paramlistprime: paramdecl CM paramlistprime | paramdecl;
    # paramdecl: typ_kw IDENTIFIER (arr_size | );
    
    def visitFuncdecl(self, ctx: ZCodeParser.FuncdeclContext):
        if ctx.returnstmt(): return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.paramlist()), self.visit(ctx.returnstmt()))
        elif ctx.blockstmt(): return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.paramlist()), self.visit(ctx.blockstmt()))
        else: return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.paramlist()))
        
    def visitParamlist(self, ctx: ZCodeParser.ParamlistContext):
        if ctx.getChildCount() == 0: return []
        return self.visit(ctx.paramlistprime())
    
    def visitParamlistprime(self, ctx: ZCodeParser.ParamlistprimeContext):
        if ctx.paramlistprime(): return [self.visit(ctx.paramdecl())] + self.visit(ctx.paramlistprime())
        return [self.visit(ctx.paramdecl())]
    
    def visitParamdecl(self, ctx: ZCodeParser.ParamdeclContext):
        if ctx.arr_size(): return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.arr_size()), self.visit(ctx.typ_kw())))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.typ_kw()))

    # stmtlist: stmtele stmtlist | ;
    # stmtele: stmt newlinelist;
    # stmt: vardecl | assignstmt | ifstmt | forstmt | breakstmt | continuestmt | returnstmt | func_callstmt | blockstmt;
    
    def visitStmtlist(self, ctx: ZCodeParser.StmtlistContext):
        if ctx.getChildCount() == 0: return []
        return [self.visit(ctx.stmtele())] + self.visit(ctx.stmtlist())
    
    def visitStmtele(self, ctx: ZCodeParser.StmteleContext):
        return self.visit(ctx.stmt())
    
    def visitStmt(self, ctx: ZCodeParser.StmtContext):
        if ctx.vardecl(): return self.visit(ctx.vardecl())
        elif ctx.assignstmt(): return self.visit(ctx.assignstmt())
        elif ctx.ifstmt(): return self.visit(ctx.ifstmt())
        elif ctx.forstmt(): return self.visit(ctx.forstmt())
        elif ctx.breakstmt(): return self.visit(ctx.breakstmt())
        elif ctx.continuestmt(): return self.visit(ctx.continuestmt())
        elif ctx.returnstmt(): return self.visit(ctx.returnstmt())
        elif ctx.func_callstmt(): return self.visit(ctx.func_callstmt())
        else: return self.visit(ctx.blockstmt())

    # returnstmt: RETURN_KW (expr | );
    # func_callstmt: IDENTIFIER LB exprlist RB;
    # assignstmt: IDENTIFIER (LSB index_operator RSB | ) val_init;
    
    def visitReturnstmt(self, ctx: ZCodeParser.ReturnstmtContext):
        if ctx.expr(): return Return(self.visit(ctx.expr()))
        return Return()
    
    def visitFunc_callstmt(self, ctx: ZCodeParser.Func_callContext):
        return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))
    
    def visitAssignstmt(self, ctx: ZCodeParser.AssignstmtContext):
        if ctx.index_operator(): return Assign(ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.index_operator())), self.visit(ctx.val_init()))
        return Assign(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.val_init()))
    
    # forstmt: FOR_KW IDENTIFIER UNTIL_KW expr BY_KW expr (newlinelist | ) stmt;
    # breakstmt: BREAK_KW;
    # continuestmt: CONTINUE_KW;
    # blockstmt: BEGIN_KW newlinelist stmtlist END_KW;
    
    def visitForstmt(self, ctx: ZCodeParser.ForstmtContext):
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.stmt()))
    
    def visitBreakstmt(self, ctx: ZCodeParser.BreakstmtContext):
        return Break()
    
    def visitContinuestmt(self, ctx: ZCodeParser.ContinuestmtContext):
        return Continue()
    
    def visitBlockstmt(self, ctx: ZCodeParser.BlockstmtContext):
        return Block(self.visit(ctx.stmtlist()))
    
    # ifstmt: IF_KW LB expr RB (newlinelist | ) stmt eliflist elsestmt;
    # eliflist: (newlinelist | ) elifstmt eliflist | ;
    # elifstmt: ELIF_KW LB expr RB (newlinelist | ) stmt;
    # elsestmt: (newlinelist ELSE_KW (newlinelist | ) stmt) | ;
    
    def visitIfstmt(self, ctx: ZCodeParser.IfstmtContext):
        return If(self.visit(ctx.expr()), self.visit(ctx.stmt()), self.visit(ctx.eliflist()), self.visit(ctx.elsestmt()))
    
    def visitEliflist(self, ctx: ZCodeParser.EliflistContext):
        if ctx.getChildCount() == 0: return []
        return [self.visit(ctx.elifstmt())] + self.visit(ctx.eliflist())
    
    def visitElifstmt(self, ctx: ZCodeParser.ElifstmtContext):
        return (self.visit(ctx.expr()), self.visit(ctx.stmt()))
    
    def visitElsestmt(self, ctx: ZCodeParser.ElsestmtContext):
        if ctx.getChildCount() == 0: return None
        return self.visit(ctx.stmt())     

    # //expression
    # exprlist: exprprime | ;
    # exprprime: expr CM exprprime | expr;
    
    def visitExprlist(self, ctx: ZCodeParser.ExprlistContext):
        if ctx.getChildCount() == 0: return []
        return self.visit(ctx.exprprime())
    
    def visitExprprime(self, ctx: ZCodeParser.ExprprimeContext):
        if ctx.exprprime(): return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())
        return [self.visit(ctx.expr())]
    
    # expr: expr1 CONCAT_STR_OP expr1 | expr1;
    def visitExpr(self, ctx: ZCodeParser.ExprContext):
        if ctx.CONCAT_STR_OP(): return BinaryOp(ctx.CONCAT_STR_OP().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        return self.visit(ctx.expr1(0))
    
    # expr1: expr2 (EQL_OP | DBL_EQL | NEQL_OP | LESS_THAN_OP | MORE_THAN_OP | LESS_EQL_OP | MORE_EQL_OP) expr2 | expr2;
    def visitExpr1(self, ctx: ZCodeParser.Expr1Context):
        if ctx.MORE_EQL_OP(): return BinaryOp(ctx.MORE_EQL_OP().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.EQL_OP(): return BinaryOp(ctx.EQL_OP().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.DBL_EQL(): return BinaryOp(ctx.DBL_EQL().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.NEQL_OP(): return BinaryOp(ctx.NEQL_OP().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.LESS_THAN_OP(): return BinaryOp(ctx.LESS_THAN_OP().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.MORE_THAN_OP(): return BinaryOp(ctx.MORE_THAN_OP().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        elif ctx.LESS_EQL_OP(): return BinaryOp(ctx.LESS_EQL_OP().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        else: return self.visit(ctx.expr2(0))
        
    # expr2: expr2 (AND_KW | OR_KW) expr3 | expr3;
    def visitExpr2(self, ctx: ZCodeParser.Expr2Context):
        if ctx.OR_KW(): return BinaryOp(ctx.OR_KW().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        elif ctx.AND_KW(): return BinaryOp(ctx.AND_KW().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        else: return self.visit(ctx.expr3())
        
    # expr3: expr3 (ADD_OP | SUB_OP) expr4 | expr4;
    def visitExpr3(self, ctx: ZCodeParser.Expr3Context):
        if ctx.SUB_OP(): return BinaryOp(ctx.SUB_OP().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        elif ctx.ADD_OP(): return BinaryOp(ctx.ADD_OP().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        else: return self.visit(ctx.expr4())
        
    # expr4: expr4 (MUL_OP | DIV_OP | MOD_OP) expr5 | expr5;
    def visitExpr4(self, ctx: ZCodeParser.Expr4Context):
        if ctx.MOD_OP(): return BinaryOp(ctx.MOD_OP().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.MUL_OP(): return BinaryOp(ctx.MUL_OP().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.DIV_OP(): return BinaryOp(ctx.DIV_OP().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        else: return self.visit(ctx.expr5())
    
    # expr5: NOT_KW expr5 | expr6;
    def visitExpr5(self, ctx: ZCodeParser.Expr5Context):
        if ctx.NOT_KW(): return UnaryOp(ctx.NOT_KW().getText(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())
    
    # expr6: SUB_OP expr6 | expr7;
    def visitExpr6(self, ctx: ZCodeParser.Expr6Context):
        if ctx.SUB_OP(): return UnaryOp(ctx.SUB_OP().getText(), self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())
    
    # expr7: element_expression | literal;
    def visitExpr7(self, ctx: ZCodeParser.Expr7Context):
        if ctx.literal(): return self.visit(ctx.literal())
        return self.visit(ctx.element_expression())
    
    # element_expression: (IDENTIFIER | func_call) LSB index_operator RSB;
    # index_operator: expr | expr CM index_operator;
    
    def visitElement_expression(self, ctx: ZCodeParser.Element_expressionContext):
        if ctx.IDENTIFIER(): return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.index_operator()))
        return ArrayCell(self.visit(ctx.func_call()), self.visit(ctx.index_operator()))
    
    def visitIndex_operator(self, ctx: ZCodeParser.Index_operatorContext):
        if ctx.index_operator(): return [self.visit(ctx.expr())] + self.visit(ctx.index_operator())
        return [self.visit(ctx.expr())]
    
    # literal: IDENTIFIER | NUMBERLIT | BOOLLIT | STRINGLIT | arrtyp | func_call | LB expr RB;
    # arrtyp: LSB index_operator RSB;
    # func_call: IDENTIFIER LB exprlist RB;
    
    def visitLiteral(self, ctx: ZCodeParser.LiteralContext):
        if ctx.IDENTIFIER(): return Id(ctx.IDENTIFIER().getText())
        elif ctx.NUMBERLIT(): return NumberLiteral(float(ctx.NUMBERLIT().getText()))
        elif ctx.BOOLLIT(): return BooleanLiteral(ctx.BOOLLIT().getText() == "true")
        elif ctx.STRINGLIT(): return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.arrtyp(): return self.visit(ctx.arrtyp())
        elif ctx.func_call(): return self.visit(ctx.func_call())
        else: return self.visit(ctx.expr())
        
    def visitArrtyp(self, ctx: ZCodeParser.ArrtypContext):
        return ArrayLiteral(self.visit(ctx.index_operator()))
    
    def visitFunc_call(self, ctx: ZCodeParser.Func_callContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprlist()))
            
    
    
