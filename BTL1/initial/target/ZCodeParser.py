# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("\u01a8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\3\2\5\2c\n\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3l\n\3\3\4\3\4\5\4p\n\4\3\4\3\4\3\5\3\5\3\5\5")
        buf.write("\5w\n\5\3\6\3\6\3\6\5\6|\n\6\3\6\3\6\5\6\u0080\n\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u0086\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u008d")
        buf.write("\n\7\3\7\3\7\5\7\u0091\n\7\3\b\3\b\3\b\3\b\3\t\3\t\5\t")
        buf.write("\u0099\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u00a0\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00a8\n\13\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\5\r\u00b0\n\r\3\16\3\16\5\16\u00b4\n\16\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u00ba\n\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00c8\n\21\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\5\23\u00d0\n\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\26\5\26\u00dc\n")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\5\27\u00e5\n\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u00ec\n\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u00f3\n\27\5\27\u00f5\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\5\30\u00fd\n\30\3\30\3\30\3\30\3")
        buf.write("\30\3\31\3\31\5\31\u0105\n\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u010b\n\31\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0113\n")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\33\5\33\u011b\n\33\3\33")
        buf.write("\3\33\3\33\5\33\u0120\n\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\5\34\u012a\n\34\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\5\37\u0134\n\37\3 \3 \3!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\5\"\u013f\n\"\3#\3#\3#\3#\3#\5#\u0146\n#\3$\3$")
        buf.write("\3$\3$\3$\3%\3%\3%\3%\3%\5%\u0152\n%\3&\3&\3&\3&\3&\5")
        buf.write("&\u0159\n&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0161\n\'\f\'\16")
        buf.write("\'\u0164\13\'\3(\3(\3(\3(\3(\3(\7(\u016c\n(\f(\16(\u016f")
        buf.write("\13(\3)\3)\3)\3)\3)\3)\7)\u0177\n)\f)\16)\u017a\13)\3")
        buf.write("*\3*\3*\5*\u017f\n*\3+\3+\3+\5+\u0184\n+\3,\3,\5,\u0188")
        buf.write("\n,\3,\3,\3,\3,\3,\5,\u018f\n,\3-\3-\3-\3-\3-\5-\u0196")
        buf.write("\n-\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01a0\n.\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\2\5LNP\61\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^\2")
        buf.write("\b\3\2\5\7\5\2\36\36 $&&\3\2\27\30\3\2\31\32\3\2\33\35")
        buf.write("\3\2-/\2\u01ae\2b\3\2\2\2\4k\3\2\2\2\6o\3\2\2\2\bv\3\2")
        buf.write("\2\2\n\u0085\3\2\2\2\f\u0087\3\2\2\2\16\u0092\3\2\2\2")
        buf.write("\20\u0098\3\2\2\2\22\u009f\3\2\2\2\24\u00a1\3\2\2\2\26")
        buf.write("\u00a9\3\2\2\2\30\u00af\3\2\2\2\32\u00b3\3\2\2\2\34\u00b9")
        buf.write("\3\2\2\2\36\u00bb\3\2\2\2 \u00c7\3\2\2\2\"\u00c9\3\2\2")
        buf.write("\2$\u00cf\3\2\2\2&\u00d1\3\2\2\2(\u00d6\3\2\2\2*\u00d8")
        buf.write("\3\2\2\2,\u00f4\3\2\2\2.\u00f6\3\2\2\2\60\u010a\3\2\2")
        buf.write("\2\62\u010c\3\2\2\2\64\u011f\3\2\2\2\66\u0121\3\2\2\2")
        buf.write("8\u012d\3\2\2\2:\u012f\3\2\2\2<\u0131\3\2\2\2>\u0135\3")
        buf.write("\2\2\2@\u0137\3\2\2\2B\u013e\3\2\2\2D\u0145\3\2\2\2F\u0147")
        buf.write("\3\2\2\2H\u0151\3\2\2\2J\u0158\3\2\2\2L\u015a\3\2\2\2")
        buf.write("N\u0165\3\2\2\2P\u0170\3\2\2\2R\u017e\3\2\2\2T\u0183\3")
        buf.write("\2\2\2V\u018e\3\2\2\2X\u0195\3\2\2\2Z\u019f\3\2\2\2\\")
        buf.write("\u01a1\3\2\2\2^\u01a3\3\2\2\2`c\5\b\5\2ac\3\2\2\2b`\3")
        buf.write("\2\2\2ba\3\2\2\2cd\3\2\2\2de\5\4\3\2ef\7\2\2\3f\3\3\2")
        buf.write("\2\2gh\5\6\4\2hi\5\4\3\2il\3\2\2\2jl\5\6\4\2kg\3\2\2\2")
        buf.write("kj\3\2\2\2l\5\3\2\2\2mp\5\n\6\2np\5\f\7\2om\3\2\2\2on")
        buf.write("\3\2\2\2pq\3\2\2\2qr\5\b\5\2r\7\3\2\2\2st\7+\2\2tw\5\b")
        buf.write("\5\2uw\7+\2\2vs\3\2\2\2vu\3\2\2\2w\t\3\2\2\2x|\5\24\13")
        buf.write("\2yz\7\n\2\2z|\7\60\2\2{x\3\2\2\2{y\3\2\2\2|\177\3\2\2")
        buf.write("\2}~\7\37\2\2~\u0080\5H%\2\177}\3\2\2\2\177\u0080\3\2")
        buf.write("\2\2\u0080\u0086\3\2\2\2\u0081\u0082\7\t\2\2\u0082\u0083")
        buf.write("\7\60\2\2\u0083\u0084\7\37\2\2\u0084\u0086\5H%\2\u0085")
        buf.write("{\3\2\2\2\u0085\u0081\3\2\2\2\u0086\13\3\2\2\2\u0087\u0088")
        buf.write("\7\13\2\2\u0088\u0089\7\60\2\2\u0089\u0090\5\16\b\2\u008a")
        buf.write("\u008d\5\b\5\2\u008b\u008d\3\2\2\2\u008c\u008a\3\2\2\2")
        buf.write("\u008c\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0091\5")
        buf.write("\32\16\2\u008f\u0091\3\2\2\2\u0090\u008c\3\2\2\2\u0090")
        buf.write("\u008f\3\2\2\2\u0091\r\3\2\2\2\u0092\u0093\7\'\2\2\u0093")
        buf.write("\u0094\5\20\t\2\u0094\u0095\7(\2\2\u0095\17\3\2\2\2\u0096")
        buf.write("\u0099\5\22\n\2\u0097\u0099\3\2\2\2\u0098\u0096\3\2\2")
        buf.write("\2\u0098\u0097\3\2\2\2\u0099\21\3\2\2\2\u009a\u009b\5")
        buf.write("\24\13\2\u009b\u009c\7,\2\2\u009c\u009d\5\22\n\2\u009d")
        buf.write("\u00a0\3\2\2\2\u009e\u00a0\5\24\13\2\u009f\u009a\3\2\2")
        buf.write("\2\u009f\u009e\3\2\2\2\u00a0\23\3\2\2\2\u00a1\u00a2\5")
        buf.write("\26\f\2\u00a2\u00a7\7\60\2\2\u00a3\u00a4\7)\2\2\u00a4")
        buf.write("\u00a5\5\30\r\2\u00a5\u00a6\7*\2\2\u00a6\u00a8\3\2\2\2")
        buf.write("\u00a7\u00a3\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\25\3\2")
        buf.write("\2\2\u00a9\u00aa\t\2\2\2\u00aa\27\3\2\2\2\u00ab\u00ac")
        buf.write("\7-\2\2\u00ac\u00ad\7,\2\2\u00ad\u00b0\5\30\r\2\u00ae")
        buf.write("\u00b0\7-\2\2\u00af\u00ab\3\2\2\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00b0\31\3\2\2\2\u00b1\u00b4\5<\37\2\u00b2\u00b4\5F$")
        buf.write("\2\u00b3\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\33\3")
        buf.write("\2\2\2\u00b5\u00b6\5\36\20\2\u00b6\u00b7\5\34\17\2\u00b7")
        buf.write("\u00ba\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00b5\3\2\2\2")
        buf.write("\u00b9\u00b8\3\2\2\2\u00ba\35\3\2\2\2\u00bb\u00bc\5 \21")
        buf.write("\2\u00bc\u00bd\5\b\5\2\u00bd\37\3\2\2\2\u00be\u00c8\5")
        buf.write("\n\6\2\u00bf\u00c8\5\"\22\2\u00c0\u00c8\5.\30\2\u00c1")
        buf.write("\u00c8\5\66\34\2\u00c2\u00c8\58\35\2\u00c3\u00c8\5:\36")
        buf.write("\2\u00c4\u00c8\5<\37\2\u00c5\u00c8\5> \2\u00c6\u00c8\5")
        buf.write("F$\2\u00c7\u00be\3\2\2\2\u00c7\u00bf\3\2\2\2\u00c7\u00c0")
        buf.write("\3\2\2\2\u00c7\u00c1\3\2\2\2\u00c7\u00c2\3\2\2\2\u00c7")
        buf.write("\u00c3\3\2\2\2\u00c7\u00c4\3\2\2\2\u00c7\u00c5\3\2\2\2")
        buf.write("\u00c7\u00c6\3\2\2\2\u00c8!\3\2\2\2\u00c9\u00ca\5$\23")
        buf.write("\2\u00ca\u00cb\7\37\2\2\u00cb\u00cc\5H%\2\u00cc#\3\2\2")
        buf.write("\2\u00cd\u00d0\5&\24\2\u00ce\u00d0\5(\25\2\u00cf\u00cd")
        buf.write("\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0%\3\2\2\2\u00d1\u00d2")
        buf.write("\7\60\2\2\u00d2\u00d3\7)\2\2\u00d3\u00d4\5X-\2\u00d4\u00d5")
        buf.write("\7*\2\2\u00d5\'\3\2\2\2\u00d6\u00d7\7\60\2\2\u00d7)\3")
        buf.write("\2\2\2\u00d8\u00db\7)\2\2\u00d9\u00dc\5,\27\2\u00da\u00dc")
        buf.write("\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00da\3\2\2\2\u00dc")
        buf.write("\u00dd\3\2\2\2\u00dd\u00de\7*\2\2\u00de+\3\2\2\2\u00df")
        buf.write("\u00e0\5\\/\2\u00e0\u00e1\7,\2\2\u00e1\u00e2\5,\27\2\u00e2")
        buf.write("\u00e5\3\2\2\2\u00e3\u00e5\5\\/\2\u00e4\u00df\3\2\2\2")
        buf.write("\u00e4\u00e3\3\2\2\2\u00e5\u00f5\3\2\2\2\u00e6\u00e7\5")
        buf.write("*\26\2\u00e7\u00e8\7,\2\2\u00e8\u00e9\5,\27\2\u00e9\u00ec")
        buf.write("\3\2\2\2\u00ea\u00ec\5*\26\2\u00eb\u00e6\3\2\2\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00ec\u00f5\3\2\2\2\u00ed\u00ee\5H%\2\u00ee")
        buf.write("\u00ef\7,\2\2\u00ef\u00f0\5,\27\2\u00f0\u00f3\3\2\2\2")
        buf.write("\u00f1\u00f3\5H%\2\u00f2\u00ed\3\2\2\2\u00f2\u00f1\3\2")
        buf.write("\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00e4\3\2\2\2\u00f4\u00eb")
        buf.write("\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5-\3\2\2\2\u00f6\u00f7")
        buf.write("\7\21\2\2\u00f7\u00f8\7\'\2\2\u00f8\u00f9\5H%\2\u00f9")
        buf.write("\u00fc\7(\2\2\u00fa\u00fd\5\b\5\2\u00fb\u00fd\3\2\2\2")
        buf.write("\u00fc\u00fa\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd\u00fe\3")
        buf.write("\2\2\2\u00fe\u00ff\5 \21\2\u00ff\u0100\5\60\31\2\u0100")
        buf.write("\u0101\5\64\33\2\u0101/\3\2\2\2\u0102\u0105\5\b\5\2\u0103")
        buf.write("\u0105\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0103\3\2\2\2")
        buf.write("\u0105\u0106\3\2\2\2\u0106\u0107\5\62\32\2\u0107\u0108")
        buf.write("\5\60\31\2\u0108\u010b\3\2\2\2\u0109\u010b\3\2\2\2\u010a")
        buf.write("\u0104\3\2\2\2\u010a\u0109\3\2\2\2\u010b\61\3\2\2\2\u010c")
        buf.write("\u010d\7\23\2\2\u010d\u010e\7\'\2\2\u010e\u010f\5H%\2")
        buf.write("\u010f\u0112\7(\2\2\u0110\u0113\5\b\5\2\u0111\u0113\3")
        buf.write("\2\2\2\u0112\u0110\3\2\2\2\u0112\u0111\3\2\2\2\u0113\u0114")
        buf.write("\3\2\2\2\u0114\u0115\5 \21\2\u0115\63\3\2\2\2\u0116\u0117")
        buf.write("\5\b\5\2\u0117\u011a\7\22\2\2\u0118\u011b\5\b\5\2\u0119")
        buf.write("\u011b\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u0119\3\2\2\2")
        buf.write("\u011b\u011c\3\2\2\2\u011c\u011d\5 \21\2\u011d\u0120\3")
        buf.write("\2\2\2\u011e\u0120\3\2\2\2\u011f\u0116\3\2\2\2\u011f\u011e")
        buf.write("\3\2\2\2\u0120\65\3\2\2\2\u0121\u0122\7\f\2\2\u0122\u0123")
        buf.write("\5(\25\2\u0123\u0124\7\r\2\2\u0124\u0125\5H%\2\u0125\u0126")
        buf.write("\7\16\2\2\u0126\u0129\5H%\2\u0127\u012a\5\b\5\2\u0128")
        buf.write("\u012a\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u0128\3\2\2\2")
        buf.write("\u012a\u012b\3\2\2\2\u012b\u012c\5 \21\2\u012c\67\3\2")
        buf.write("\2\2\u012d\u012e\7\17\2\2\u012e9\3\2\2\2\u012f\u0130\7")
        buf.write("\20\2\2\u0130;\3\2\2\2\u0131\u0133\7\b\2\2\u0132\u0134")
        buf.write("\5H%\2\u0133\u0132\3\2\2\2\u0133\u0134\3\2\2\2\u0134=")
        buf.write("\3\2\2\2\u0135\u0136\5@!\2\u0136?\3\2\2\2\u0137\u0138")
        buf.write("\7\60\2\2\u0138\u0139\7\'\2\2\u0139\u013a\5B\"\2\u013a")
        buf.write("\u013b\7(\2\2\u013bA\3\2\2\2\u013c\u013f\5D#\2\u013d\u013f")
        buf.write("\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013d\3\2\2\2\u013f")
        buf.write("C\3\2\2\2\u0140\u0141\5H%\2\u0141\u0142\7,\2\2\u0142\u0143")
        buf.write("\5D#\2\u0143\u0146\3\2\2\2\u0144\u0146\5H%\2\u0145\u0140")
        buf.write("\3\2\2\2\u0145\u0144\3\2\2\2\u0146E\3\2\2\2\u0147\u0148")
        buf.write("\7\24\2\2\u0148\u0149\5\b\5\2\u0149\u014a\5\34\17\2\u014a")
        buf.write("\u014b\7\25\2\2\u014bG\3\2\2\2\u014c\u014d\5J&\2\u014d")
        buf.write("\u014e\7%\2\2\u014e\u014f\5J&\2\u014f\u0152\3\2\2\2\u0150")
        buf.write("\u0152\5J&\2\u0151\u014c\3\2\2\2\u0151\u0150\3\2\2\2\u0152")
        buf.write("I\3\2\2\2\u0153\u0154\5L\'\2\u0154\u0155\t\3\2\2\u0155")
        buf.write("\u0156\5L\'\2\u0156\u0159\3\2\2\2\u0157\u0159\5L\'\2\u0158")
        buf.write("\u0153\3\2\2\2\u0158\u0157\3\2\2\2\u0159K\3\2\2\2\u015a")
        buf.write("\u015b\b\'\1\2\u015b\u015c\5N(\2\u015c\u0162\3\2\2\2\u015d")
        buf.write("\u015e\f\4\2\2\u015e\u015f\t\4\2\2\u015f\u0161\5N(\2\u0160")
        buf.write("\u015d\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0162\u0163\3\2\2\2\u0163M\3\2\2\2\u0164\u0162\3\2\2")
        buf.write("\2\u0165\u0166\b(\1\2\u0166\u0167\5P)\2\u0167\u016d\3")
        buf.write("\2\2\2\u0168\u0169\f\4\2\2\u0169\u016a\t\5\2\2\u016a\u016c")
        buf.write("\5P)\2\u016b\u0168\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016d\u016e\3\2\2\2\u016eO\3\2\2\2\u016f\u016d")
        buf.write("\3\2\2\2\u0170\u0171\b)\1\2\u0171\u0172\5R*\2\u0172\u0178")
        buf.write("\3\2\2\2\u0173\u0174\f\4\2\2\u0174\u0175\t\6\2\2\u0175")
        buf.write("\u0177\5R*\2\u0176\u0173\3\2\2\2\u0177\u017a\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179Q\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017b\u017c\7\26\2\2\u017c\u017f\5R*\2")
        buf.write("\u017d\u017f\5T+\2\u017e\u017b\3\2\2\2\u017e\u017d\3\2")
        buf.write("\2\2\u017fS\3\2\2\2\u0180\u0181\7\32\2\2\u0181\u0184\5")
        buf.write("T+\2\u0182\u0184\5V,\2\u0183\u0180\3\2\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0184U\3\2\2\2\u0185\u0188\7\60\2\2\u0186\u0188")
        buf.write("\5@!\2\u0187\u0185\3\2\2\2\u0187\u0186\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189\u018a\7)\2\2\u018a\u018b\5X-\2\u018b\u018c")
        buf.write("\7*\2\2\u018c\u018f\3\2\2\2\u018d\u018f\5Z.\2\u018e\u0187")
        buf.write("\3\2\2\2\u018e\u018d\3\2\2\2\u018fW\3\2\2\2\u0190\u0196")
        buf.write("\5H%\2\u0191\u0192\5H%\2\u0192\u0193\7,\2\2\u0193\u0194")
        buf.write("\5X-\2\u0194\u0196\3\2\2\2\u0195\u0190\3\2\2\2\u0195\u0191")
        buf.write("\3\2\2\2\u0196Y\3\2\2\2\u0197\u01a0\5\\/\2\u0198\u01a0")
        buf.write("\7\60\2\2\u0199\u01a0\5^\60\2\u019a\u01a0\5@!\2\u019b")
        buf.write("\u019c\7)\2\2\u019c\u019d\5X-\2\u019d\u019e\7*\2\2\u019e")
        buf.write("\u01a0\3\2\2\2\u019f\u0197\3\2\2\2\u019f\u0198\3\2\2\2")
        buf.write("\u019f\u0199\3\2\2\2\u019f\u019a\3\2\2\2\u019f\u019b\3")
        buf.write("\2\2\2\u01a0[\3\2\2\2\u01a1\u01a2\t\7\2\2\u01a2]\3\2\2")
        buf.write("\2\u01a3\u01a4\7\'\2\2\u01a4\u01a5\5H%\2\u01a5\u01a6\7")
        buf.write("(\2\2\u01a6_\3\2\2\2-bkov{\177\u0085\u008c\u0090\u0098")
        buf.write("\u009f\u00a7\u00af\u00b3\u00b9\u00c7\u00cf\u00db\u00e4")
        buf.write("\u00eb\u00f2\u00f4\u00fc\u0104\u010a\u0112\u011a\u011f")
        buf.write("\u0129\u0133\u013e\u0145\u0151\u0158\u0162\u016d\u0178")
        buf.write("\u017e\u0183\u0187\u018e\u0195\u019f")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "<INVALID>", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "LINECMT", "WS", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONT", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQ", "ASSIGN", "NEQ", "LT", "LEQ", "GT", "GEQ", 
                      "CONCAT", "COMPARE_STR", "LB", "RB", "LSB", "RSB", 
                      "NEWLINE", "COMMA", "NUMLIT", "BOOLLIT", "STRLIT", 
                      "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_newlinelist = 3
    RULE_vardecl = 4
    RULE_funcdecl = 5
    RULE_paramdecl = 6
    RULE_paramlist = 7
    RULE_paramprime = 8
    RULE_param = 9
    RULE_typ = 10
    RULE_size = 11
    RULE_body = 12
    RULE_stmtlist = 13
    RULE_stmtele = 14
    RULE_stmt = 15
    RULE_assignstmt = 16
    RULE_lhs = 17
    RULE_index_expr = 18
    RULE_scalar_varibale = 19
    RULE_arrlist = 20
    RULE_arrprime = 21
    RULE_ifstmt = 22
    RULE_eliflist = 23
    RULE_elifstmt = 24
    RULE_elsestmt = 25
    RULE_forstmt = 26
    RULE_breakstmt = 27
    RULE_contstmt = 28
    RULE_returnstmt = 29
    RULE_callstmt = 30
    RULE_func_call = 31
    RULE_exprlist = 32
    RULE_exprprime = 33
    RULE_blockstmt = 34
    RULE_expr = 35
    RULE_str_expr = 36
    RULE_bin_log_expr = 37
    RULE_add_expr = 38
    RULE_mul_expr = 39
    RULE_un_log_expr = 40
    RULE_sign_expr = 41
    RULE_ele_expr = 42
    RULE_index_op = 43
    RULE_operand = 44
    RULE_literal = 45
    RULE_subexpr = 46

    ruleNames =  [ "program", "decllist", "decl", "newlinelist", "vardecl", 
                   "funcdecl", "paramdecl", "paramlist", "paramprime", "param", 
                   "typ", "size", "body", "stmtlist", "stmtele", "stmt", 
                   "assignstmt", "lhs", "index_expr", "scalar_varibale", 
                   "arrlist", "arrprime", "ifstmt", "eliflist", "elifstmt", 
                   "elsestmt", "forstmt", "breakstmt", "contstmt", "returnstmt", 
                   "callstmt", "func_call", "exprlist", "exprprime", "blockstmt", 
                   "expr", "str_expr", "bin_log_expr", "add_expr", "mul_expr", 
                   "un_log_expr", "sign_expr", "ele_expr", "index_op", "operand", 
                   "literal", "subexpr" ]

    EOF = Token.EOF
    LINECMT=1
    WS=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONT=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    EQ=28
    ASSIGN=29
    NEQ=30
    LT=31
    LEQ=32
    GT=33
    GEQ=34
    CONCAT=35
    COMPARE_STR=36
    LB=37
    RB=38
    LSB=39
    RSB=40
    NEWLINE=41
    COMMA=42
    NUMLIT=43
    BOOLLIT=44
    STRLIT=45
    ID=46
    ILLEGAL_ESCAPE=47
    UNCLOSE_STRING=48
    ERROR_CHAR=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 94
                self.newlinelist()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 98
            self.decllist()
            self.state = 99
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.decl()
                self.state = 102
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 107
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.state = 108
                self.funcdecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 111
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlinelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlinelist" ):
                return visitor.visitNewlinelist(self)
            else:
                return visitor.visitChildren(self)




    def newlinelist(self):

        localctx = ZCodeParser.NewlinelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_newlinelist)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(ZCodeParser.NEWLINE)
                self.state = 114
                self.newlinelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                    self.state = 118
                    self.param()
                    pass
                elif token in [ZCodeParser.DYNAMIC]:
                    self.state = 119
                    self.match(ZCodeParser.DYNAMIC)
                    self.state = 120
                    self.match(ZCodeParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 123
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 124
                    self.expr()


                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(ZCodeParser.VAR)
                self.state = 128
                self.match(ZCodeParser.ID)
                self.state = 129
                self.match(ZCodeParser.ASSIGN)
                self.state = 130
                self.expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def paramdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamdeclContext,0)


        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(ZCodeParser.FUNC)
            self.state = 134
            self.match(ZCodeParser.ID)
            self.state = 135
            self.paramdecl()
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 138
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEWLINE]:
                    self.state = 136
                    self.newlinelist()
                    pass
                elif token in [ZCodeParser.RETURN, ZCodeParser.BEGIN]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 140
                self.body()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecl" ):
                return visitor.visitParamdecl(self)
            else:
                return visitor.visitChildren(self)




    def paramdecl(self):

        localctx = ZCodeParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ZCodeParser.LB)
            self.state = 145
            self.paramlist()
            self.state = 146
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramlist)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.paramprime()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = ZCodeParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramprime)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.param()
                self.state = 153
                self.match(ZCodeParser.COMMA)
                self.state = 154
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def size(self):
            return self.getTypedRuleContext(ZCodeParser.SizeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.typ()
            self.state = 160
            self.match(ZCodeParser.ID)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LSB:
                self.state = 161
                self.match(ZCodeParser.LSB)
                self.state = 162
                self.size()
                self.state = 163
                self.match(ZCodeParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def size(self):
            return self.getTypedRuleContext(ZCodeParser.SizeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = ZCodeParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_size)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(ZCodeParser.NUMLIT)
                self.state = 170
                self.match(ZCodeParser.COMMA)
                self.state = 171
                self.size()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(ZCodeParser.NUMLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = ZCodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_body)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.blockstmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtele(self):
            return self.getTypedRuleContext(ZCodeParser.StmteleContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmtlist)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONT, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.stmtele()
                self.state = 180
                self.stmtlist()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmteleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtele" ):
                return visitor.visitStmtele(self)
            else:
                return visitor.visitChildren(self)




    def stmtele(self):

        localctx = ZCodeParser.StmteleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmtele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.stmt()
            self.state = 186
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def contstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(ZCodeParser.CallstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 192
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 193
                self.contstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 194
                self.returnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 195
                self.callstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 196
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.lhs()
            self.state = 200
            self.match(ZCodeParser.ASSIGN)
            self.state = 201
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_exprContext,0)


        def scalar_varibale(self):
            return self.getTypedRuleContext(ZCodeParser.Scalar_varibaleContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lhs)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.index_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.scalar_varibale()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = ZCodeParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(ZCodeParser.ID)
            self.state = 208
            self.match(ZCodeParser.LSB)
            self.state = 209
            self.index_op()
            self.state = 210
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varibaleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_scalar_varibale

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_varibale" ):
                return visitor.visitScalar_varibale(self)
            else:
                return visitor.visitChildren(self)




    def scalar_varibale(self):

        localctx = ZCodeParser.Scalar_varibaleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_scalar_varibale)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(ZCodeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def arrprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArrprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrlist" ):
                return visitor.visitArrlist(self)
            else:
                return visitor.visitChildren(self)




    def arrlist(self):

        localctx = ZCodeParser.ArrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arrlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(ZCodeParser.LSB)
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRLIT, ZCodeParser.ID]:
                self.state = 215
                self.arrprime()
                pass
            elif token in [ZCodeParser.RSB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 219
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arrprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArrprimeContext,0)


        def arrlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArrlistContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrprime" ):
                return visitor.visitArrprime(self)
            else:
                return visitor.visitChildren(self)




    def arrprime(self):

        localctx = ZCodeParser.ArrprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arrprime)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 221
                    self.literal()
                    self.state = 222
                    self.match(ZCodeParser.COMMA)
                    self.state = 223
                    self.arrprime()
                    pass

                elif la_ == 2:
                    self.state = 225
                    self.literal()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 228
                    self.arrlist()
                    self.state = 229
                    self.match(ZCodeParser.COMMA)
                    self.state = 230
                    self.arrprime()
                    pass

                elif la_ == 2:
                    self.state = 232
                    self.arrlist()
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 235
                    self.expr()
                    self.state = 236
                    self.match(ZCodeParser.COMMA)
                    self.state = 237
                    self.arrprime()
                    pass

                elif la_ == 2:
                    self.state = 239
                    self.expr()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def elsestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElsestmtContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(ZCodeParser.IF)
            self.state = 245
            self.match(ZCodeParser.LB)
            self.state = 246
            self.expr()
            self.state = 247
            self.match(ZCodeParser.RB)
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 248
                self.newlinelist()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONT, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 252
            self.stmt()
            self.state = 253
            self.eliflist()
            self.state = 254
            self.elsestmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliflistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstmtContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_eliflist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliflist" ):
                return visitor.visitEliflist(self)
            else:
                return visitor.visitChildren(self)




    def eliflist(self):

        localctx = ZCodeParser.EliflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_eliflist)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEWLINE]:
                    self.state = 256
                    self.newlinelist()
                    pass
                elif token in [ZCodeParser.ELIF]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 260
                self.elifstmt()
                self.state = 261
                self.eliflist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifstmt" ):
                return visitor.visitElifstmt(self)
            else:
                return visitor.visitChildren(self)




    def elifstmt(self):

        localctx = ZCodeParser.ElifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(ZCodeParser.ELIF)
            self.state = 267
            self.match(ZCodeParser.LB)
            self.state = 268
            self.expr()
            self.state = 269
            self.match(ZCodeParser.RB)
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 270
                self.newlinelist()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONT, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 274
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlinelist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NewlinelistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,i)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elsestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




    def elsestmt(self):

        localctx = ZCodeParser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elsestmt)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.newlinelist()
                self.state = 277
                self.match(ZCodeParser.ELSE)
                self.state = 280
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEWLINE]:
                    self.state = 278
                    self.newlinelist()
                    pass
                elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONT, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 282
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def scalar_varibale(self):
            return self.getTypedRuleContext(ZCodeParser.Scalar_varibaleContext,0)


        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(ZCodeParser.FOR)
            self.state = 288
            self.scalar_varibale()
            self.state = 289
            self.match(ZCodeParser.UNTIL)
            self.state = 290
            self.expr()
            self.state = 291
            self.match(ZCodeParser.BY)
            self.state = 292
            self.expr()
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 293
                self.newlinelist()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONT, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 297
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONT(self):
            return self.getToken(ZCodeParser.CONT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_contstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContstmt" ):
                return visitor.visitContstmt(self)
            else:
                return visitor.visitChildren(self)




    def contstmt(self):

        localctx = ZCodeParser.ContstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_contstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(ZCodeParser.CONT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.RETURN)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LB) | (1 << ZCodeParser.LSB) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLLIT) | (1 << ZCodeParser.STRLIT) | (1 << ZCodeParser.ID))) != 0):
                self.state = 304
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = ZCodeParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.func_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(ZCodeParser.ID)
            self.state = 310
            self.match(ZCodeParser.LB)
            self.state = 311
            self.exprlist()
            self.state = 312
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = ZCodeParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exprlist)
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRLIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.exprprime()
                pass
            elif token in [ZCodeParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exprprime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprprime" ):
                return visitor.visitExprprime(self)
            else:
                return visitor.visitChildren(self)




    def exprprime(self):

        localctx = ZCodeParser.ExprprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exprprime)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.expr()
                self.state = 319
                self.match(ZCodeParser.COMMA)
                self.state = 320
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(ZCodeParser.BEGIN)
            self.state = 326
            self.newlinelist()
            self.state = 327
            self.stmtlist()
            self.state = 328
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def str_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Str_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Str_exprContext,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.str_expr()
                self.state = 331
                self.match(ZCodeParser.CONCAT)
                self.state = 332
                self.str_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.str_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bin_log_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Bin_log_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Bin_log_exprContext,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def COMPARE_STR(self):
            return self.getToken(ZCodeParser.COMPARE_STR, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LEQ(self):
            return self.getToken(ZCodeParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(ZCodeParser.GEQ, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_str_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr_expr" ):
                return visitor.visitStr_expr(self)
            else:
                return visitor.visitChildren(self)




    def str_expr(self):

        localctx = ZCodeParser.Str_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_str_expr)
        self._la = 0 # Token type
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.bin_log_expr(0)
                self.state = 338
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.NEQ) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LEQ) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GEQ) | (1 << ZCodeParser.COMPARE_STR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 339
                self.bin_log_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.bin_log_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bin_log_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Add_exprContext,0)


        def bin_log_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Bin_log_exprContext,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_bin_log_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBin_log_expr" ):
                return visitor.visitBin_log_expr(self)
            else:
                return visitor.visitChildren(self)



    def bin_log_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Bin_log_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_bin_log_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Bin_log_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bin_log_expr)
                    self.state = 347
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 348
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 349
                    self.add_expr(0) 
                self.state = 354
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Mul_exprContext,0)


        def add_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Add_exprContext,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_add_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_expr" ):
                return visitor.visitAdd_expr(self)
            else:
                return visitor.visitChildren(self)



    def add_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Add_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_add_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.mul_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 358
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 359
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 360
                    self.mul_expr(0) 
                self.state = 365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def un_log_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Un_log_exprContext,0)


        def mul_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Mul_exprContext,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_mul_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_expr" ):
                return visitor.visitMul_expr(self)
            else:
                return visitor.visitChildren(self)



    def mul_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Mul_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_mul_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.un_log_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Mul_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_expr)
                    self.state = 369
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 370
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 371
                    self.un_log_expr() 
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Un_log_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def un_log_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Un_log_exprContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_un_log_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUn_log_expr" ):
                return visitor.visitUn_log_expr(self)
            else:
                return visitor.visitChildren(self)




    def un_log_expr(self):

        localctx = ZCodeParser.Un_log_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_un_log_expr)
        try:
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match(ZCodeParser.NOT)
                self.state = 378
                self.un_log_expr()
                pass
            elif token in [ZCodeParser.SUB, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRLIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.sign_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def ele_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Ele_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = ZCodeParser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_sign_expr)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(ZCodeParser.SUB)
                self.state = 383
                self.sign_expr()
                pass
            elif token in [ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.NUMLIT, ZCodeParser.BOOLLIT, ZCodeParser.STRLIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.ele_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ele_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ele_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle_expr" ):
                return visitor.visitEle_expr(self)
            else:
                return visitor.visitChildren(self)




    def ele_expr(self):

        localctx = ZCodeParser.Ele_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_ele_expr)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 387
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 388
                    self.func_call()
                    pass


                self.state = 391
                self.match(ZCodeParser.LSB)
                self.state = 392
                self.index_op()
                self.state = 393
                self.match(ZCodeParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = ZCodeParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_index_op)
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.expr()
                self.state = 400
                self.match(ZCodeParser.COMMA)
                self.state = 401
                self.index_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def subexpr(self):
            return self.getTypedRuleContext(ZCodeParser.SubexprContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index_op(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_operand)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 407
                self.subexpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 408
                self.func_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 409
                self.match(ZCodeParser.LSB)
                self.state = 410
                self.index_op()
                self.state = 411
                self.match(ZCodeParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def BOOLLIT(self):
            return self.getToken(ZCodeParser.BOOLLIT, 0)

        def STRLIT(self):
            return self.getToken(ZCodeParser.STRLIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.BOOLLIT) | (1 << ZCodeParser.STRLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = ZCodeParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(ZCodeParser.LB)
            self.state = 418
            self.expr()
            self.state = 419
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[37] = self.bin_log_expr_sempred
        self._predicates[38] = self.add_expr_sempred
        self._predicates[39] = self.mul_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def bin_log_expr_sempred(self, localctx:Bin_log_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def add_expr_sempred(self, localctx:Add_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def mul_expr_sempred(self, localctx:Mul_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




