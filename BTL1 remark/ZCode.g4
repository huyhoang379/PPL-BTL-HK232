/*---2110181------------------*/
/*---Ho Huy Hoang-------------*/

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: (newlinelist | ) decllist EOF;
decllist: decl decllist | decl;
decl: (vardecl | funcdecl) newlinelist;
newlinelist: NEWLINE newlinelist | NEWLINE;

vardecl: (param | DYNAMIC ID) (ASSIGN expr)? | VAR ID ASSIGN expr;

funcdecl: FUNC ID paramdecl ((newlinelist | ) body | );
paramdecl: LB paramlist RB;
paramlist: paramprime | ;
paramprime: param COMMA paramprime | param;
param: typ ID (LSB size RSB)?;
typ: NUMBER | BOOL | STRING;
size: NUMLIT COMMA size | NUMLIT;

body: returnstmt | blockstmt;

stmtlist: stmtele stmtlist | ;
stmtele: stmt newlinelist;
stmt: vardecl | assignstmt | ifstmt | forstmt | breakstmt | contstmt | returnstmt | callstmt | blockstmt;

assignstmt: lhs ASSIGN expr;
lhs: index_expr | scalar_varibale;
index_expr: ID LSB index_op RSB;
scalar_varibale: ID;

arrlist: LSB (arrprime | ) RSB;
arrprime: (literal COMMA arrprime | literal) | (arrlist COMMA arrprime | arrlist) | (expr COMMA arrprime | expr);

ifstmt: IF LB expr RB (newlinelist | ) stmt eliflist elsestmt;
eliflist: (newlinelist | ) elifstmt eliflist | ;
elifstmt: ELIF LB expr RB (newlinelist | ) stmt;
elsestmt: (newlinelist ELSE (newlinelist | ) stmt) | ;

forstmt: FOR scalar_varibale UNTIL expr BY expr (newlinelist | ) stmt;

breakstmt: BREAK;

contstmt: CONT;

returnstmt: RETURN expr?;

callstmt: func_call;
func_call: ID LB exprlist RB;
exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr;

blockstmt: BEGIN newlinelist stmtlist END;

expr: str_expr CONCAT str_expr | str_expr;
str_expr: bin_log_expr (EQ | COMPARE_STR | NEQ | LT | GT | LEQ | GEQ) bin_log_expr 
		| bin_log_expr;
bin_log_expr: bin_log_expr (AND | OR) add_expr | add_expr;
add_expr: add_expr (ADD | SUB) mul_expr | mul_expr;
mul_expr: mul_expr (MUL | DIV | MOD) un_log_expr | un_log_expr;
un_log_expr: NOT un_log_expr | sign_expr;
sign_expr: SUB sign_expr | ele_expr;
ele_expr: (ID|func_call) LSB index_op RSB | operand;
index_op: expr | expr COMMA index_op; 

operand: literal | ID | subexpr | func_call | LSB index_op RSB;
literal: NUMLIT | BOOLLIT | STRLIT;
subexpr: LB expr RB;

LINECMT: '##' ~[\n\r]*	-> skip	;
WS: [ \t\b\f]+	-> skip ; // skip spaces, tabs, newlines

NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONT: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '=';
ASSIGN: '<-';
NEQ: '!=';
LT: '<';
LEQ: '<=';
GT: '>';
GEQ: '>=';
CONCAT: '...';
COMPARE_STR: '==';

LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
NEWLINE: '\r'? '\n' {self.text = self.text.replace('\r','')};
COMMA: ',';

fragment IntegerPart: [0-9]+;
fragment DecimalPart: '.'[0-9]*;
fragment ExponentPart: [Ee][+-]?[0-9]+;
NUMLIT: IntegerPart DecimalPart? ExponentPart?;

fragment TRUE: 'true';
fragment FALSE: 'false';
BOOLLIT: TRUE | FALSE;

fragment Char: (EscapeStr | DQ | ~["\\\r\n]);
fragment EscapeStr: '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\');
fragment DQ: '\'''"';
STRLIT: '"' Char* '"'
{
    a = str(self.text)
    self.text = a[1:-1]
};

ID: [a-zA-Z_][a-zA-Z0-9_]*;

ILLEGAL_ESCAPE: '"' Char* '\\' ~[bfnrt'\\]
{
	raise IllegalEscape(self.text[1:])
};
UNCLOSE_STRING: '"' Char* ([\n\r]|EOF)
{
	if self.text[-1] in ["\n","\r"] :
		raise UncloseString(self.text[1:-1])
	else: raise UncloseString(self.text[1:])
};
ERROR_CHAR: . {raise ErrorToken(self.text)};