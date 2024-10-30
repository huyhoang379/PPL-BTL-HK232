grammar ZCode;

@lexer::header {
2115129
from lexererr import *
}

options {
	language=Python3;
}
//program is list of declaration, vardecl or funcdecl
program: (newlinelist | ) decllist EOF;
decllist: decl decllist | decl ;
decl: (vardecl | funcdecl) newlinelist;
newlinelist: NEW_LINE newlinelist | NEW_LINE;
//variable declaration
vardecl: (typdecl | implicit_keyworddecl);
//declaration start with type
typdecl: typ_kw IDENTIFIER (arr_size | )(val_init | );
typ_kw: NUMBER_KW | BOOL_KW | STRING_KW;
val_init: ASSIGN_OP expr;
arr_size: LSB sizelist RSB;
sizelist: dimension CM sizelist | dimension;
dimension: NUMBERLIT;
//declaration start witch implicitkeyword
implicit_keyworddecl: varkwdecl | dynamickwdecl;
varkwdecl: VAR_KW IDENTIFIER val_init;
dynamickwdecl: DYNAMIC_KW IDENTIFIER (val_init | );


literal: IDENTIFIER | NUMBERLIT | BOOLLIT | STRINGLIT | arrtyp | func_call | LB expr RB;
arrtyp: LSB index_operator RSB;
func_call: IDENTIFIER LB exprlist RB;

funcdecl: FUNC_KW IDENTIFIER LB paramlist RB ((newlinelist | ) returnstmt | (newlinelist | ) blockstmt |);
paramlist: paramlistprime | ;
paramlistprime: paramdecl CM paramlistprime | paramdecl;
paramdecl: typ_kw IDENTIFIER (arr_size | );

stmtlist: stmtele stmtlist | ;
stmtele: stmt newlinelist;
stmt: vardecl | assignstmt | ifstmt | forstmt | breakstmt | continuestmt | returnstmt | func_callstmt | blockstmt;

returnstmt: RETURN_KW (expr | );
func_callstmt: IDENTIFIER LB exprlist RB;
assignstmt: IDENTIFIER (LSB index_operator RSB | ) val_init;
forstmt: FOR_KW IDENTIFIER UNTIL_KW expr BY_KW expr (newlinelist | ) stmt;
breakstmt: BREAK_KW;
continuestmt: CONTINUE_KW;
blockstmt: BEGIN_KW newlinelist stmtlist END_KW;
ifstmt: IF_KW LB expr RB (newlinelist | ) stmt eliflist elsestmt;
eliflist: (newlinelist | ) elifstmt eliflist | ;
elifstmt: ELIF_KW LB expr RB (newlinelist | ) stmt;
elsestmt: (newlinelist ELSE_KW (newlinelist | ) stmt) | ;

//expression
exprlist: exprprime | ;
exprprime: expr CM exprprime | expr;
expr: expr1 CONCAT_STR_OP expr1 | expr1;
expr1: expr2 (EQL_OP | DBL_EQL | NEQL_OP | LESS_THAN_OP | MORE_THAN_OP | LESS_EQL_OP | MORE_EQL_OP) expr2 | expr2;
expr2: expr2 (AND_KW | OR_KW) expr3 | expr3;
expr3: expr3 (ADD_OP | SUB_OP) expr4 | expr4;
expr4: expr4 (MUL_OP | DIV_OP | MOD_OP) expr5 | expr5;
expr5: NOT_KW expr5 | expr6;
expr6: SUB_OP expr6 | expr7;
expr7: element_expression | literal;

element_expression: (IDENTIFIER | func_call) LSB index_operator RSB;
index_operator: expr | expr CM index_operator;


//Keywords

BOOLLIT: TRUE_VAL | FALSE_VAL;
fragment TRUE_VAL: 'true';
fragment FALSE_VAL: 'false';

NUMBER_KW: 'number';
BOOL_KW: 'bool';
STRING_KW: 'string';

RETURN_KW: 'return';
VAR_KW: 'var';
DYNAMIC_KW: 'dynamic';
FUNC_KW: 'func';

FOR_KW: 'for';
UNTIL_KW: 'until';
BY_KW: 'by';
BREAK_KW: 'break';
CONTINUE_KW: 'continue';

IF_KW: 'if';
ELSE_KW: 'else';
ELIF_KW: 'elif';

BEGIN_KW: 'begin';
END_KW: 'end';

NOT_KW: 'not';
AND_KW: 'and';
OR_KW: 'or';

//operator
ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
MOD_OP: '%';
EQL_OP: '=';
ASSIGN_OP: '<-';

NEQL_OP: '!=';
LESS_THAN_OP: '<';
LESS_EQL_OP: '<=';
MORE_THAN_OP: '>';
MORE_EQL_OP: '>=';
DBL_EQL: '==';

CONCAT_STR_OP: '...';
//Separators
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
CM: ',';
//Number
NUMBERLIT: [0-9]+('.'[0-9]*)?([eE][+-]?[0-9]+)?;
//String
STRINGLIT: STR_SC STR STR_SC {
	self.text = self.text[1:-1]};
fragment STR_SC: '"';
fragment STR_ESCAPE_SEQUENCE: '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\');
fragment STR: (~[\r\n\f\\"]|STR_ESCAPE_SEQUENCE|'\'"')*;
//IO function
// READNUMBER_FUNC: 'readNumber';
// WRITENUMER_FUNC: 'writeNumber';
// READBOOL_FUNC: 'readBool';
// WRITEBOOL_FUNC: 'writeBool';
// READSTRING_FUNC: 'readString';
// WRITESTRING_FUNC: 'writeString';
//Comment
COMMENT: '##' ~[\r\n\f]*-> skip;
//New line character
NEW_LINE: '\n';
//Identifier
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;


WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: STR_SC STR ILLEGAL_STREND {
	if (self.text[-1] == '\n' or self.text[-1] == '\r'):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
fragment ILLEGAL_STREND: '\n' | '\r' | EOF;

ILLEGAL_ESCAPE: STR_SC STR '\\' ~('b'|'t'|'n'|'f'|'r'|'\''|'\\')  {
	raise IllegalEscape(self.text[1:])
};

ERROR_CHAR: . {raise ErrorToken(self.text)};