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
        buf.write("\u019e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\3\2\5\2c\n\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3l\n\3\3\4\3\4\5\4p\n\4\3\4\3\4\3\5\3\5\3\5\5")
        buf.write("\5w\n\5\3\6\3\6\5\6{\n\6\3\7\3\7\3\7\3\7\5\7\u0081\n\7")
        buf.write("\3\7\3\7\5\7\u0085\n\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\5\13\u0095\n\13\3\f\3\f")
        buf.write("\3\r\3\r\5\r\u009b\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\5\17\u00a5\n\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\5\20\u00b1\n\20\3\21\3\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00c3\n\23\3\23\3\23\3\23\5\23\u00c8\n")
        buf.write("\23\3\23\3\23\5\23\u00cc\n\23\3\24\3\24\5\24\u00d0\n\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\5\25\u00d7\n\25\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u00dd\n\26\3\27\3\27\3\27\3\27\5\27\u00e3")
        buf.write("\n\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u00f1\n\31\3\32\3\32\3\32\5\32\u00f6\n")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u0103\n\34\3\34\3\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u010f\n\35\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\5!\u0122\n")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\5\"\u012a\n\"\3\"\3\"\3\"\3\"\5")
        buf.write("\"\u0130\n\"\3#\3#\3#\3#\3#\3#\5#\u0138\n#\3#\3#\3$\3")
        buf.write("$\3$\3$\5$\u0140\n$\3$\3$\3$\5$\u0145\n$\3%\3%\5%\u0149")
        buf.write("\n%\3&\3&\3&\3&\3&\5&\u0150\n&\3\'\3\'\3\'\3\'\3\'\5\'")
        buf.write("\u0157\n\'\3(\3(\3(\3(\3(\5(\u015e\n(\3)\3)\3)\3)\3)\3")
        buf.write(")\7)\u0166\n)\f)\16)\u0169\13)\3*\3*\3*\3*\3*\3*\7*\u0171")
        buf.write("\n*\f*\16*\u0174\13*\3+\3+\3+\3+\3+\3+\7+\u017c\n+\f+")
        buf.write("\16+\u017f\13+\3,\3,\3,\5,\u0184\n,\3-\3-\3-\5-\u0189")
        buf.write("\n-\3.\3.\5.\u018d\n.\3/\3/\5/\u0191\n/\3/\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\5\60\u019c\n\60\3\60\2\5PRT\61")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^\2\7\3\2\4\6\4\2\35\35\37$")
        buf.write("\3\2\26\27\3\2\30\31\3\2\32\34\2\u01a3\2b\3\2\2\2\4k\3")
        buf.write("\2\2\2\6o\3\2\2\2\bv\3\2\2\2\nz\3\2\2\2\f|\3\2\2\2\16")
        buf.write("\u0086\3\2\2\2\20\u0088\3\2\2\2\22\u008b\3\2\2\2\24\u0094")
        buf.write("\3\2\2\2\26\u0096\3\2\2\2\30\u009a\3\2\2\2\32\u009c\3")
        buf.write("\2\2\2\34\u00a0\3\2\2\2\36\u00b0\3\2\2\2 \u00b2\3\2\2")
        buf.write("\2\"\u00b6\3\2\2\2$\u00bb\3\2\2\2&\u00cf\3\2\2\2(\u00d6")
        buf.write("\3\2\2\2*\u00d8\3\2\2\2,\u00e2\3\2\2\2.\u00e4\3\2\2\2")
        buf.write("\60\u00f0\3\2\2\2\62\u00f2\3\2\2\2\64\u00f7\3\2\2\2\66")
        buf.write("\u00fc\3\2\2\28\u0106\3\2\2\2:\u0112\3\2\2\2<\u0114\3")
        buf.write("\2\2\2>\u0116\3\2\2\2@\u011b\3\2\2\2B\u012f\3\2\2\2D\u0131")
        buf.write("\3\2\2\2F\u0144\3\2\2\2H\u0148\3\2\2\2J\u014f\3\2\2\2")
        buf.write("L\u0156\3\2\2\2N\u015d\3\2\2\2P\u015f\3\2\2\2R\u016a\3")
        buf.write("\2\2\2T\u0175\3\2\2\2V\u0183\3\2\2\2X\u0188\3\2\2\2Z\u018c")
        buf.write("\3\2\2\2\\\u0190\3\2\2\2^\u019b\3\2\2\2`c\5\b\5\2ac\3")
        buf.write("\2\2\2b`\3\2\2\2ba\3\2\2\2cd\3\2\2\2de\5\4\3\2ef\7\2\2")
        buf.write("\3f\3\3\2\2\2gh\5\6\4\2hi\5\4\3\2il\3\2\2\2jl\5\6\4\2")
        buf.write("kg\3\2\2\2kj\3\2\2\2l\5\3\2\2\2mp\5\n\6\2np\5$\23\2om")
        buf.write("\3\2\2\2on\3\2\2\2pq\3\2\2\2qr\5\b\5\2r\7\3\2\2\2st\7")
        buf.write(".\2\2tw\5\b\5\2uw\7.\2\2vs\3\2\2\2vu\3\2\2\2w\t\3\2\2")
        buf.write("\2x{\5\f\7\2y{\5\30\r\2zx\3\2\2\2zy\3\2\2\2{\13\3\2\2")
        buf.write("\2|}\5\16\b\2}\u0080\7/\2\2~\u0081\5\22\n\2\177\u0081")
        buf.write("\3\2\2\2\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081\u0084")
        buf.write("\3\2\2\2\u0082\u0085\5\20\t\2\u0083\u0085\3\2\2\2\u0084")
        buf.write("\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085\r\3\2\2\2\u0086")
        buf.write("\u0087\t\2\2\2\u0087\17\3\2\2\2\u0088\u0089\7\36\2\2\u0089")
        buf.write("\u008a\5L\'\2\u008a\21\3\2\2\2\u008b\u008c\7(\2\2\u008c")
        buf.write("\u008d\5\24\13\2\u008d\u008e\7)\2\2\u008e\23\3\2\2\2\u008f")
        buf.write("\u0090\5\26\f\2\u0090\u0091\7*\2\2\u0091\u0092\5\24\13")
        buf.write("\2\u0092\u0095\3\2\2\2\u0093\u0095\5\26\f\2\u0094\u008f")
        buf.write("\3\2\2\2\u0094\u0093\3\2\2\2\u0095\25\3\2\2\2\u0096\u0097")
        buf.write("\7+\2\2\u0097\27\3\2\2\2\u0098\u009b\5\32\16\2\u0099\u009b")
        buf.write("\5\34\17\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b")
        buf.write("\31\3\2\2\2\u009c\u009d\7\b\2\2\u009d\u009e\7/\2\2\u009e")
        buf.write("\u009f\5\20\t\2\u009f\33\3\2\2\2\u00a0\u00a1\7\t\2\2\u00a1")
        buf.write("\u00a4\7/\2\2\u00a2\u00a5\5\20\t\2\u00a3\u00a5\3\2\2\2")
        buf.write("\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\35\3\2")
        buf.write("\2\2\u00a6\u00b1\7/\2\2\u00a7\u00b1\7+\2\2\u00a8\u00b1")
        buf.write("\7\3\2\2\u00a9\u00b1\7,\2\2\u00aa\u00b1\5 \21\2\u00ab")
        buf.write("\u00b1\5\"\22\2\u00ac\u00ad\7&\2\2\u00ad\u00ae\5L\'\2")
        buf.write("\u00ae\u00af\7\'\2\2\u00af\u00b1\3\2\2\2\u00b0\u00a6\3")
        buf.write("\2\2\2\u00b0\u00a7\3\2\2\2\u00b0\u00a8\3\2\2\2\u00b0\u00a9")
        buf.write("\3\2\2\2\u00b0\u00aa\3\2\2\2\u00b0\u00ab\3\2\2\2\u00b0")
        buf.write("\u00ac\3\2\2\2\u00b1\37\3\2\2\2\u00b2\u00b3\7(\2\2\u00b3")
        buf.write("\u00b4\5^\60\2\u00b4\u00b5\7)\2\2\u00b5!\3\2\2\2\u00b6")
        buf.write("\u00b7\7/\2\2\u00b7\u00b8\7&\2\2\u00b8\u00b9\5H%\2\u00b9")
        buf.write("\u00ba\7\'\2\2\u00ba#\3\2\2\2\u00bb\u00bc\7\n\2\2\u00bc")
        buf.write("\u00bd\7/\2\2\u00bd\u00be\7&\2\2\u00be\u00bf\5&\24\2\u00bf")
        buf.write("\u00cb\7\'\2\2\u00c0\u00c3\5\b\5\2\u00c1\u00c3\3\2\2\2")
        buf.write("\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c4\3")
        buf.write("\2\2\2\u00c4\u00cc\5\62\32\2\u00c5\u00c8\5\b\5\2\u00c6")
        buf.write("\u00c8\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6\3\2\2\2")
        buf.write("\u00c8\u00c9\3\2\2\2\u00c9\u00cc\5> \2\u00ca\u00cc\3\2")
        buf.write("\2\2\u00cb\u00c2\3\2\2\2\u00cb\u00c7\3\2\2\2\u00cb\u00ca")
        buf.write("\3\2\2\2\u00cc%\3\2\2\2\u00cd\u00d0\5(\25\2\u00ce\u00d0")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0")
        buf.write("\'\3\2\2\2\u00d1\u00d2\5*\26\2\u00d2\u00d3\7*\2\2\u00d3")
        buf.write("\u00d4\5(\25\2\u00d4\u00d7\3\2\2\2\u00d5\u00d7\5*\26\2")
        buf.write("\u00d6\u00d1\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7)\3\2\2")
        buf.write("\2\u00d8\u00d9\5\16\b\2\u00d9\u00dc\7/\2\2\u00da\u00dd")
        buf.write("\5\22\n\2\u00db\u00dd\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dd+\3\2\2\2\u00de\u00df\5.\30\2\u00df")
        buf.write("\u00e0\5,\27\2\u00e0\u00e3\3\2\2\2\u00e1\u00e3\3\2\2\2")
        buf.write("\u00e2\u00de\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3-\3\2\2")
        buf.write("\2\u00e4\u00e5\5\60\31\2\u00e5\u00e6\5\b\5\2\u00e6/\3")
        buf.write("\2\2\2\u00e7\u00f1\5\n\6\2\u00e8\u00f1\5\66\34\2\u00e9")
        buf.write("\u00f1\5@!\2\u00ea\u00f1\58\35\2\u00eb\u00f1\5:\36\2\u00ec")
        buf.write("\u00f1\5<\37\2\u00ed\u00f1\5\62\32\2\u00ee\u00f1\5\64")
        buf.write("\33\2\u00ef\u00f1\5> \2\u00f0\u00e7\3\2\2\2\u00f0\u00e8")
        buf.write("\3\2\2\2\u00f0\u00e9\3\2\2\2\u00f0\u00ea\3\2\2\2\u00f0")
        buf.write("\u00eb\3\2\2\2\u00f0\u00ec\3\2\2\2\u00f0\u00ed\3\2\2\2")
        buf.write("\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\61\3\2")
        buf.write("\2\2\u00f2\u00f5\7\7\2\2\u00f3\u00f6\5L\'\2\u00f4\u00f6")
        buf.write("\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6")
        buf.write("\63\3\2\2\2\u00f7\u00f8\7/\2\2\u00f8\u00f9\7&\2\2\u00f9")
        buf.write("\u00fa\5H%\2\u00fa\u00fb\7\'\2\2\u00fb\65\3\2\2\2\u00fc")
        buf.write("\u0102\7/\2\2\u00fd\u00fe\7(\2\2\u00fe\u00ff\5^\60\2\u00ff")
        buf.write("\u0100\7)\2\2\u0100\u0103\3\2\2\2\u0101\u0103\3\2\2\2")
        buf.write("\u0102\u00fd\3\2\2\2\u0102\u0101\3\2\2\2\u0103\u0104\3")
        buf.write("\2\2\2\u0104\u0105\5\20\t\2\u0105\67\3\2\2\2\u0106\u0107")
        buf.write("\7\13\2\2\u0107\u0108\7/\2\2\u0108\u0109\7\f\2\2\u0109")
        buf.write("\u010a\5L\'\2\u010a\u010b\7\r\2\2\u010b\u010e\5L\'\2\u010c")
        buf.write("\u010f\5\b\5\2\u010d\u010f\3\2\2\2\u010e\u010c\3\2\2\2")
        buf.write("\u010e\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\5")
        buf.write("\60\31\2\u01119\3\2\2\2\u0112\u0113\7\16\2\2\u0113;\3")
        buf.write("\2\2\2\u0114\u0115\7\17\2\2\u0115=\3\2\2\2\u0116\u0117")
        buf.write("\7\23\2\2\u0117\u0118\5\b\5\2\u0118\u0119\5,\27\2\u0119")
        buf.write("\u011a\7\24\2\2\u011a?\3\2\2\2\u011b\u011c\7\20\2\2\u011c")
        buf.write("\u011d\7&\2\2\u011d\u011e\5L\'\2\u011e\u0121\7\'\2\2\u011f")
        buf.write("\u0122\5\b\5\2\u0120\u0122\3\2\2\2\u0121\u011f\3\2\2\2")
        buf.write("\u0121\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\5")
        buf.write("\60\31\2\u0124\u0125\5B\"\2\u0125\u0126\5F$\2\u0126A\3")
        buf.write("\2\2\2\u0127\u012a\5\b\5\2\u0128\u012a\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u0129\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b")
        buf.write("\u012c\5D#\2\u012c\u012d\5B\"\2\u012d\u0130\3\2\2\2\u012e")
        buf.write("\u0130\3\2\2\2\u012f\u0129\3\2\2\2\u012f\u012e\3\2\2\2")
        buf.write("\u0130C\3\2\2\2\u0131\u0132\7\22\2\2\u0132\u0133\7&\2")
        buf.write("\2\u0133\u0134\5L\'\2\u0134\u0137\7\'\2\2\u0135\u0138")
        buf.write("\5\b\5\2\u0136\u0138\3\2\2\2\u0137\u0135\3\2\2\2\u0137")
        buf.write("\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\5\60\31")
        buf.write("\2\u013aE\3\2\2\2\u013b\u013c\5\b\5\2\u013c\u013f\7\21")
        buf.write("\2\2\u013d\u0140\5\b\5\2\u013e\u0140\3\2\2\2\u013f\u013d")
        buf.write("\3\2\2\2\u013f\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("\u0142\5\60\31\2\u0142\u0145\3\2\2\2\u0143\u0145\3\2\2")
        buf.write("\2\u0144\u013b\3\2\2\2\u0144\u0143\3\2\2\2\u0145G\3\2")
        buf.write("\2\2\u0146\u0149\5J&\2\u0147\u0149\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0148\u0147\3\2\2\2\u0149I\3\2\2\2\u014a\u014b")
        buf.write("\5L\'\2\u014b\u014c\7*\2\2\u014c\u014d\5J&\2\u014d\u0150")
        buf.write("\3\2\2\2\u014e\u0150\5L\'\2\u014f\u014a\3\2\2\2\u014f")
        buf.write("\u014e\3\2\2\2\u0150K\3\2\2\2\u0151\u0152\5N(\2\u0152")
        buf.write("\u0153\7%\2\2\u0153\u0154\5N(\2\u0154\u0157\3\2\2\2\u0155")
        buf.write("\u0157\5N(\2\u0156\u0151\3\2\2\2\u0156\u0155\3\2\2\2\u0157")
        buf.write("M\3\2\2\2\u0158\u0159\5P)\2\u0159\u015a\t\3\2\2\u015a")
        buf.write("\u015b\5P)\2\u015b\u015e\3\2\2\2\u015c\u015e\5P)\2\u015d")
        buf.write("\u0158\3\2\2\2\u015d\u015c\3\2\2\2\u015eO\3\2\2\2\u015f")
        buf.write("\u0160\b)\1\2\u0160\u0161\5R*\2\u0161\u0167\3\2\2\2\u0162")
        buf.write("\u0163\f\4\2\2\u0163\u0164\t\4\2\2\u0164\u0166\5R*\2\u0165")
        buf.write("\u0162\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0168Q\3\2\2\2\u0169\u0167\3\2\2")
        buf.write("\2\u016a\u016b\b*\1\2\u016b\u016c\5T+\2\u016c\u0172\3")
        buf.write("\2\2\2\u016d\u016e\f\4\2\2\u016e\u016f\t\5\2\2\u016f\u0171")
        buf.write("\5T+\2\u0170\u016d\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173S\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0175\u0176\b+\1\2\u0176\u0177\5V,\2\u0177\u017d")
        buf.write("\3\2\2\2\u0178\u0179\f\4\2\2\u0179\u017a\t\6\2\2\u017a")
        buf.write("\u017c\5V,\2\u017b\u0178\3\2\2\2\u017c\u017f\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017eU\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0181\7\25\2\2\u0181\u0184\5V,\2")
        buf.write("\u0182\u0184\5X-\2\u0183\u0180\3\2\2\2\u0183\u0182\3\2")
        buf.write("\2\2\u0184W\3\2\2\2\u0185\u0186\7\31\2\2\u0186\u0189\5")
        buf.write("X-\2\u0187\u0189\5Z.\2\u0188\u0185\3\2\2\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189Y\3\2\2\2\u018a\u018d\5\\/\2\u018b\u018d")
        buf.write("\5\36\20\2\u018c\u018a\3\2\2\2\u018c\u018b\3\2\2\2\u018d")
        buf.write("[\3\2\2\2\u018e\u0191\7/\2\2\u018f\u0191\5\"\22\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191\u0192\3\2\2\2")
        buf.write("\u0192\u0193\7(\2\2\u0193\u0194\5^\60\2\u0194\u0195\7")
        buf.write(")\2\2\u0195]\3\2\2\2\u0196\u019c\5L\'\2\u0197\u0198\5")
        buf.write("L\'\2\u0198\u0199\7*\2\2\u0199\u019a\5^\60\2\u019a\u019c")
        buf.write("\3\2\2\2\u019b\u0196\3\2\2\2\u019b\u0197\3\2\2\2\u019c")
        buf.write("_\3\2\2\2*bkovz\u0080\u0084\u0094\u009a\u00a4\u00b0\u00c2")
        buf.write("\u00c7\u00cb\u00cf\u00d6\u00dc\u00e2\u00f0\u00f5\u0102")
        buf.write("\u010e\u0121\u0129\u012f\u0137\u013f\u0144\u0148\u014f")
        buf.write("\u0156\u015d\u0167\u0172\u017d\u0183\u0188\u018c\u0190")
        buf.write("\u019b")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'number'", "'bool'", "'string'", 
                     "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
                     "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'=='", "'...'", 
                     "'('", "')'", "'['", "']'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "BOOLLIT", "NUMBER_KW", "BOOL_KW", "STRING_KW", 
                      "RETURN_KW", "VAR_KW", "DYNAMIC_KW", "FUNC_KW", "FOR_KW", 
                      "UNTIL_KW", "BY_KW", "BREAK_KW", "CONTINUE_KW", "IF_KW", 
                      "ELSE_KW", "ELIF_KW", "BEGIN_KW", "END_KW", "NOT_KW", 
                      "AND_KW", "OR_KW", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
                      "MOD_OP", "EQL_OP", "ASSIGN_OP", "NEQL_OP", "LESS_THAN_OP", 
                      "LESS_EQL_OP", "MORE_THAN_OP", "MORE_EQL_OP", "DBL_EQL", 
                      "CONCAT_STR_OP", "LB", "RB", "LSB", "RSB", "CM", "NUMBERLIT", 
                      "STRINGLIT", "COMMENT", "NEW_LINE", "IDENTIFIER", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_newlinelist = 3
    RULE_vardecl = 4
    RULE_typdecl = 5
    RULE_typ_kw = 6
    RULE_val_init = 7
    RULE_arr_size = 8
    RULE_sizelist = 9
    RULE_dimension = 10
    RULE_implicit_keyworddecl = 11
    RULE_varkwdecl = 12
    RULE_dynamickwdecl = 13
    RULE_literal = 14
    RULE_arrtyp = 15
    RULE_func_call = 16
    RULE_funcdecl = 17
    RULE_paramlist = 18
    RULE_paramlistprime = 19
    RULE_paramdecl = 20
    RULE_stmtlist = 21
    RULE_stmtele = 22
    RULE_stmt = 23
    RULE_returnstmt = 24
    RULE_func_callstmt = 25
    RULE_assignstmt = 26
    RULE_forstmt = 27
    RULE_breakstmt = 28
    RULE_continuestmt = 29
    RULE_blockstmt = 30
    RULE_ifstmt = 31
    RULE_eliflist = 32
    RULE_elifstmt = 33
    RULE_elsestmt = 34
    RULE_exprlist = 35
    RULE_exprprime = 36
    RULE_expr = 37
    RULE_expr1 = 38
    RULE_expr2 = 39
    RULE_expr3 = 40
    RULE_expr4 = 41
    RULE_expr5 = 42
    RULE_expr6 = 43
    RULE_expr7 = 44
    RULE_element_expression = 45
    RULE_index_operator = 46

    ruleNames =  [ "program", "decllist", "decl", "newlinelist", "vardecl", 
                   "typdecl", "typ_kw", "val_init", "arr_size", "sizelist", 
                   "dimension", "implicit_keyworddecl", "varkwdecl", "dynamickwdecl", 
                   "literal", "arrtyp", "func_call", "funcdecl", "paramlist", 
                   "paramlistprime", "paramdecl", "stmtlist", "stmtele", 
                   "stmt", "returnstmt", "func_callstmt", "assignstmt", 
                   "forstmt", "breakstmt", "continuestmt", "blockstmt", 
                   "ifstmt", "eliflist", "elifstmt", "elsestmt", "exprlist", 
                   "exprprime", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "element_expression", "index_operator" ]

    EOF = Token.EOF
    BOOLLIT=1
    NUMBER_KW=2
    BOOL_KW=3
    STRING_KW=4
    RETURN_KW=5
    VAR_KW=6
    DYNAMIC_KW=7
    FUNC_KW=8
    FOR_KW=9
    UNTIL_KW=10
    BY_KW=11
    BREAK_KW=12
    CONTINUE_KW=13
    IF_KW=14
    ELSE_KW=15
    ELIF_KW=16
    BEGIN_KW=17
    END_KW=18
    NOT_KW=19
    AND_KW=20
    OR_KW=21
    ADD_OP=22
    SUB_OP=23
    MUL_OP=24
    DIV_OP=25
    MOD_OP=26
    EQL_OP=27
    ASSIGN_OP=28
    NEQL_OP=29
    LESS_THAN_OP=30
    LESS_EQL_OP=31
    MORE_THAN_OP=32
    MORE_EQL_OP=33
    DBL_EQL=34
    CONCAT_STR_OP=35
    LB=36
    RB=37
    LSB=38
    RSB=39
    CM=40
    NUMBERLIT=41
    STRINGLIT=42
    COMMENT=43
    NEW_LINE=44
    IDENTIFIER=45
    WS=46
    UNCLOSE_STRING=47
    ILLEGAL_ESCAPE=48
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
            if token in [ZCodeParser.NEW_LINE]:
                self.state = 94
                self.newlinelist()
                pass
            elif token in [ZCodeParser.NUMBER_KW, ZCodeParser.BOOL_KW, ZCodeParser.STRING_KW, ZCodeParser.VAR_KW, ZCodeParser.DYNAMIC_KW, ZCodeParser.FUNC_KW]:
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
            if token in [ZCodeParser.NUMBER_KW, ZCodeParser.BOOL_KW, ZCodeParser.STRING_KW, ZCodeParser.VAR_KW, ZCodeParser.DYNAMIC_KW]:
                self.state = 107
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC_KW]:
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

        def NEW_LINE(self):
            return self.getToken(ZCodeParser.NEW_LINE, 0)

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
                self.match(ZCodeParser.NEW_LINE)
                self.state = 114
                self.newlinelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(ZCodeParser.NEW_LINE)
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

        def typdecl(self):
            return self.getTypedRuleContext(ZCodeParser.TypdeclContext,0)


        def implicit_keyworddecl(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_keyworddeclContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_KW, ZCodeParser.BOOL_KW, ZCodeParser.STRING_KW]:
                self.state = 118
                self.typdecl()
                pass
            elif token in [ZCodeParser.VAR_KW, ZCodeParser.DYNAMIC_KW]:
                self.state = 119
                self.implicit_keyworddecl()
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


    class TypdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ_kw(self):
            return self.getTypedRuleContext(ZCodeParser.Typ_kwContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arr_size(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_sizeContext,0)


        def val_init(self):
            return self.getTypedRuleContext(ZCodeParser.Val_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_typdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypdecl" ):
                return visitor.visitTypdecl(self)
            else:
                return visitor.visitChildren(self)




    def typdecl(self):

        localctx = ZCodeParser.TypdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.typ_kw()
            self.state = 123
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LSB]:
                self.state = 124
                self.arr_size()
                pass
            elif token in [ZCodeParser.ELIF_KW, ZCodeParser.ASSIGN_OP, ZCodeParser.NEW_LINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN_OP]:
                self.state = 128
                self.val_init()
                pass
            elif token in [ZCodeParser.ELIF_KW, ZCodeParser.NEW_LINE]:
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


    class Typ_kwContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_KW(self):
            return self.getToken(ZCodeParser.NUMBER_KW, 0)

        def BOOL_KW(self):
            return self.getToken(ZCodeParser.BOOL_KW, 0)

        def STRING_KW(self):
            return self.getToken(ZCodeParser.STRING_KW, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ_kw

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp_kw" ):
                return visitor.visitTyp_kw(self)
            else:
                return visitor.visitChildren(self)




    def typ_kw(self):

        localctx = ZCodeParser.Typ_kwContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typ_kw)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_KW) | (1 << ZCodeParser.BOOL_KW) | (1 << ZCodeParser.STRING_KW))) != 0)):
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


    class Val_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_val_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_init" ):
                return visitor.visitVal_init(self)
            else:
                return visitor.visitChildren(self)




    def val_init(self):

        localctx = ZCodeParser.Val_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_val_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(ZCodeParser.ASSIGN_OP)
            self.state = 135
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_size" ):
                return visitor.visitArr_size(self)
            else:
                return visitor.visitChildren(self)




    def arr_size(self):

        localctx = ZCodeParser.Arr_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arr_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ZCodeParser.LSB)
            self.state = 138
            self.sizelist()
            self.state = 139
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def sizelist(self):
            return self.getTypedRuleContext(ZCodeParser.SizelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sizelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizelist" ):
                return visitor.visitSizelist(self)
            else:
                return visitor.visitChildren(self)




    def sizelist(self):

        localctx = ZCodeParser.SizelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_sizelist)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.dimension()
                self.state = 142
                self.match(ZCodeParser.CM)
                self.state = 143
                self.sizelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.dimension()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = ZCodeParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ZCodeParser.NUMBERLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_keyworddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varkwdecl(self):
            return self.getTypedRuleContext(ZCodeParser.VarkwdeclContext,0)


        def dynamickwdecl(self):
            return self.getTypedRuleContext(ZCodeParser.DynamickwdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_keyworddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_keyworddecl" ):
                return visitor.visitImplicit_keyworddecl(self)
            else:
                return visitor.visitChildren(self)




    def implicit_keyworddecl(self):

        localctx = ZCodeParser.Implicit_keyworddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_implicit_keyworddecl)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR_KW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.varkwdecl()
                pass
            elif token in [ZCodeParser.DYNAMIC_KW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.dynamickwdecl()
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


    class VarkwdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_KW(self):
            return self.getToken(ZCodeParser.VAR_KW, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def val_init(self):
            return self.getTypedRuleContext(ZCodeParser.Val_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varkwdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarkwdecl" ):
                return visitor.visitVarkwdecl(self)
            else:
                return visitor.visitChildren(self)




    def varkwdecl(self):

        localctx = ZCodeParser.VarkwdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_varkwdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ZCodeParser.VAR_KW)
            self.state = 155
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 156
            self.val_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DynamickwdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC_KW(self):
            return self.getToken(ZCodeParser.DYNAMIC_KW, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def val_init(self):
            return self.getTypedRuleContext(ZCodeParser.Val_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamickwdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamickwdecl" ):
                return visitor.visitDynamickwdecl(self)
            else:
                return visitor.visitChildren(self)




    def dynamickwdecl(self):

        localctx = ZCodeParser.DynamickwdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dynamickwdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(ZCodeParser.DYNAMIC_KW)
            self.state = 159
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN_OP]:
                self.state = 160
                self.val_init()
                pass
            elif token in [ZCodeParser.ELIF_KW, ZCodeParser.NEW_LINE]:
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def BOOLLIT(self):
            return self.getToken(ZCodeParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def arrtyp(self):
            return self.getTypedRuleContext(ZCodeParser.ArrtypContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_literal)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(ZCodeParser.NUMBERLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                self.match(ZCodeParser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 167
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 168
                self.arrtyp()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 169
                self.func_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 170
                self.match(ZCodeParser.LB)
                self.state = 171
                self.expr()
                self.state = 172
                self.match(ZCodeParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrtypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrtyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrtyp" ):
                return visitor.visitArrtyp(self)
            else:
                return visitor.visitChildren(self)




    def arrtyp(self):

        localctx = ZCodeParser.ArrtypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arrtyp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(ZCodeParser.LSB)
            self.state = 177
            self.index_operator()
            self.state = 178
            self.match(ZCodeParser.RSB)
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 32, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 181
            self.match(ZCodeParser.LB)
            self.state = 182
            self.exprlist()
            self.state = 183
            self.match(ZCodeParser.RB)
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

        def FUNC_KW(self):
            return self.getToken(ZCodeParser.FUNC_KW, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


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
        self.enterRule(localctx, 34, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(ZCodeParser.FUNC_KW)
            self.state = 186
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 187
            self.match(ZCodeParser.LB)
            self.state = 188
            self.paramlist()
            self.state = 189
            self.match(ZCodeParser.RB)
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 192
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEW_LINE]:
                    self.state = 190
                    self.newlinelist()
                    pass
                elif token in [ZCodeParser.RETURN_KW]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 194
                self.returnstmt()
                pass

            elif la_ == 2:
                self.state = 197
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEW_LINE]:
                    self.state = 195
                    self.newlinelist()
                    pass
                elif token in [ZCodeParser.BEGIN_KW]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 199
                self.blockstmt()
                pass

            elif la_ == 3:
                pass


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

        def paramlistprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramlist)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_KW, ZCodeParser.BOOL_KW, ZCodeParser.STRING_KW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.paramlistprime()
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


    class ParamlistprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamdeclContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def paramlistprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlistprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlistprime" ):
                return visitor.visitParamlistprime(self)
            else:
                return visitor.visitChildren(self)




    def paramlistprime(self):

        localctx = ZCodeParser.ParamlistprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_paramlistprime)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.paramdecl()
                self.state = 208
                self.match(ZCodeParser.CM)
                self.state = 209
                self.paramlistprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.paramdecl()
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

        def typ_kw(self):
            return self.getTypedRuleContext(ZCodeParser.Typ_kwContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arr_size(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_sizeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecl" ):
                return visitor.visitParamdecl(self)
            else:
                return visitor.visitChildren(self)




    def paramdecl(self):

        localctx = ZCodeParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.typ_kw()
            self.state = 215
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LSB]:
                self.state = 216
                self.arr_size()
                pass
            elif token in [ZCodeParser.RB, ZCodeParser.CM]:
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
        self.enterRule(localctx, 42, self.RULE_stmtlist)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_KW, ZCodeParser.BOOL_KW, ZCodeParser.STRING_KW, ZCodeParser.RETURN_KW, ZCodeParser.VAR_KW, ZCodeParser.DYNAMIC_KW, ZCodeParser.FOR_KW, ZCodeParser.BREAK_KW, ZCodeParser.CONTINUE_KW, ZCodeParser.IF_KW, ZCodeParser.BEGIN_KW, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.stmtele()
                self.state = 221
                self.stmtlist()
                pass
            elif token in [ZCodeParser.END_KW]:
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
        self.enterRule(localctx, 44, self.RULE_stmtele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.stmt()
            self.state = 227
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


        def continuestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def func_callstmt(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callstmtContext,0)


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
        self.enterRule(localctx, 46, self.RULE_stmt)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 232
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 233
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 234
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 235
                self.returnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 236
                self.func_callstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 237
                self.blockstmt()
                pass


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

        def RETURN_KW(self):
            return self.getToken(ZCodeParser.RETURN_KW, 0)

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
        self.enterRule(localctx, 48, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(ZCodeParser.RETURN_KW)
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOLLIT, ZCodeParser.NOT_KW, ZCodeParser.SUB_OP, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.state = 241
                self.expr()
                pass
            elif token in [ZCodeParser.ELIF_KW, ZCodeParser.NEW_LINE]:
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


    class Func_callstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_callstmt" ):
                return visitor.visitFunc_callstmt(self)
            else:
                return visitor.visitChildren(self)




    def func_callstmt(self):

        localctx = ZCodeParser.Func_callstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_func_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 246
            self.match(ZCodeParser.LB)
            self.state = 247
            self.exprlist()
            self.state = 248
            self.match(ZCodeParser.RB)
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def val_init(self):
            return self.getTypedRuleContext(ZCodeParser.Val_initContext,0)


        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LSB]:
                self.state = 251
                self.match(ZCodeParser.LSB)
                self.state = 252
                self.index_operator()
                self.state = 253
                self.match(ZCodeParser.RSB)
                pass
            elif token in [ZCodeParser.ASSIGN_OP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 258
            self.val_init()
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

        def FOR_KW(self):
            return self.getToken(ZCodeParser.FOR_KW, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL_KW(self):
            return self.getToken(ZCodeParser.UNTIL_KW, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY_KW(self):
            return self.getToken(ZCodeParser.BY_KW, 0)

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
        self.enterRule(localctx, 54, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(ZCodeParser.FOR_KW)
            self.state = 261
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 262
            self.match(ZCodeParser.UNTIL_KW)
            self.state = 263
            self.expr()
            self.state = 264
            self.match(ZCodeParser.BY_KW)
            self.state = 265
            self.expr()
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEW_LINE]:
                self.state = 266
                self.newlinelist()
                pass
            elif token in [ZCodeParser.NUMBER_KW, ZCodeParser.BOOL_KW, ZCodeParser.STRING_KW, ZCodeParser.RETURN_KW, ZCodeParser.VAR_KW, ZCodeParser.DYNAMIC_KW, ZCodeParser.FOR_KW, ZCodeParser.BREAK_KW, ZCodeParser.CONTINUE_KW, ZCodeParser.IF_KW, ZCodeParser.BEGIN_KW, ZCodeParser.IDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 270
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

        def BREAK_KW(self):
            return self.getToken(ZCodeParser.BREAK_KW, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ZCodeParser.BREAK_KW)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE_KW(self):
            return self.getToken(ZCodeParser.CONTINUE_KW, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = ZCodeParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(ZCodeParser.CONTINUE_KW)
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

        def BEGIN_KW(self):
            return self.getToken(ZCodeParser.BEGIN_KW, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END_KW(self):
            return self.getToken(ZCodeParser.END_KW, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ZCodeParser.BEGIN_KW)
            self.state = 277
            self.newlinelist()
            self.state = 278
            self.stmtlist()
            self.state = 279
            self.match(ZCodeParser.END_KW)
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

        def IF_KW(self):
            return self.getToken(ZCodeParser.IF_KW, 0)

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
        self.enterRule(localctx, 62, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(ZCodeParser.IF_KW)
            self.state = 282
            self.match(ZCodeParser.LB)
            self.state = 283
            self.expr()
            self.state = 284
            self.match(ZCodeParser.RB)
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEW_LINE]:
                self.state = 285
                self.newlinelist()
                pass
            elif token in [ZCodeParser.NUMBER_KW, ZCodeParser.BOOL_KW, ZCodeParser.STRING_KW, ZCodeParser.RETURN_KW, ZCodeParser.VAR_KW, ZCodeParser.DYNAMIC_KW, ZCodeParser.FOR_KW, ZCodeParser.BREAK_KW, ZCodeParser.CONTINUE_KW, ZCodeParser.IF_KW, ZCodeParser.BEGIN_KW, ZCodeParser.IDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 289
            self.stmt()
            self.state = 290
            self.eliflist()
            self.state = 291
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
        self.enterRule(localctx, 64, self.RULE_eliflist)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEW_LINE]:
                    self.state = 293
                    self.newlinelist()
                    pass
                elif token in [ZCodeParser.ELIF_KW]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 297
                self.elifstmt()
                self.state = 298
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

        def ELIF_KW(self):
            return self.getToken(ZCodeParser.ELIF_KW, 0)

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
        self.enterRule(localctx, 66, self.RULE_elifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.ELIF_KW)
            self.state = 304
            self.match(ZCodeParser.LB)
            self.state = 305
            self.expr()
            self.state = 306
            self.match(ZCodeParser.RB)
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEW_LINE]:
                self.state = 307
                self.newlinelist()
                pass
            elif token in [ZCodeParser.NUMBER_KW, ZCodeParser.BOOL_KW, ZCodeParser.STRING_KW, ZCodeParser.RETURN_KW, ZCodeParser.VAR_KW, ZCodeParser.DYNAMIC_KW, ZCodeParser.FOR_KW, ZCodeParser.BREAK_KW, ZCodeParser.CONTINUE_KW, ZCodeParser.IF_KW, ZCodeParser.BEGIN_KW, ZCodeParser.IDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 311
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


        def ELSE_KW(self):
            return self.getToken(ZCodeParser.ELSE_KW, 0)

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
        self.enterRule(localctx, 68, self.RULE_elsestmt)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.newlinelist()
                self.state = 314
                self.match(ZCodeParser.ELSE_KW)
                self.state = 317
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEW_LINE]:
                    self.state = 315
                    self.newlinelist()
                    pass
                elif token in [ZCodeParser.NUMBER_KW, ZCodeParser.BOOL_KW, ZCodeParser.STRING_KW, ZCodeParser.RETURN_KW, ZCodeParser.VAR_KW, ZCodeParser.DYNAMIC_KW, ZCodeParser.FOR_KW, ZCodeParser.BREAK_KW, ZCodeParser.CONTINUE_KW, ZCodeParser.IF_KW, ZCodeParser.BEGIN_KW, ZCodeParser.IDENTIFIER]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 319
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
        self.enterRule(localctx, 70, self.RULE_exprlist)
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOLLIT, ZCodeParser.NOT_KW, ZCodeParser.SUB_OP, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
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


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

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
        self.enterRule(localctx, 72, self.RULE_exprprime)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.expr()
                self.state = 329
                self.match(ZCodeParser.CM)
                self.state = 330
                self.exprprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.expr()
                pass


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

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT_STR_OP(self):
            return self.getToken(ZCodeParser.CONCAT_STR_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.expr1()
                self.state = 336
                self.match(ZCodeParser.CONCAT_STR_OP)
                self.state = 337
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def EQL_OP(self):
            return self.getToken(ZCodeParser.EQL_OP, 0)

        def DBL_EQL(self):
            return self.getToken(ZCodeParser.DBL_EQL, 0)

        def NEQL_OP(self):
            return self.getToken(ZCodeParser.NEQL_OP, 0)

        def LESS_THAN_OP(self):
            return self.getToken(ZCodeParser.LESS_THAN_OP, 0)

        def MORE_THAN_OP(self):
            return self.getToken(ZCodeParser.MORE_THAN_OP, 0)

        def LESS_EQL_OP(self):
            return self.getToken(ZCodeParser.LESS_EQL_OP, 0)

        def MORE_EQL_OP(self):
            return self.getToken(ZCodeParser.MORE_EQL_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.expr2(0)
                self.state = 343
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQL_OP) | (1 << ZCodeParser.NEQL_OP) | (1 << ZCodeParser.LESS_THAN_OP) | (1 << ZCodeParser.LESS_EQL_OP) | (1 << ZCodeParser.MORE_THAN_OP) | (1 << ZCodeParser.MORE_EQL_OP) | (1 << ZCodeParser.DBL_EQL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 344
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND_KW(self):
            return self.getToken(ZCodeParser.AND_KW, 0)

        def OR_KW(self):
            return self.getToken(ZCodeParser.OR_KW, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 352
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 353
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND_KW or _la==ZCodeParser.OR_KW):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 354
                    self.expr3(0) 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD_OP(self):
            return self.getToken(ZCodeParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(ZCodeParser.SUB_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 363
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 364
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD_OP or _la==ZCodeParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 365
                    self.expr4(0) 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL_OP(self):
            return self.getToken(ZCodeParser.MUL_OP, 0)

        def DIV_OP(self):
            return self.getToken(ZCodeParser.DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(ZCodeParser.MOD_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL_OP) | (1 << ZCodeParser.DIV_OP) | (1 << ZCodeParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 376
                    self.expr5() 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_KW(self):
            return self.getToken(ZCodeParser.NOT_KW, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr5)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_KW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(ZCodeParser.NOT_KW)
                self.state = 383
                self.expr5()
                pass
            elif token in [ZCodeParser.BOOLLIT, ZCodeParser.SUB_OP, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OP(self):
            return self.getToken(ZCodeParser.SUB_OP, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr6)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(ZCodeParser.SUB_OP)
                self.state = 388
                self.expr6()
                pass
            elif token in [ZCodeParser.BOOLLIT, ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.NUMBERLIT, ZCodeParser.STRINGLIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.expr7()
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_expressionContext,0)


        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr7)
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.element_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_element_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expression" ):
                return visitor.visitElement_expression(self)
            else:
                return visitor.visitChildren(self)




    def element_expression(self):

        localctx = ZCodeParser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 396
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 397
                self.func_call()
                pass


            self.state = 400
            self.match(ZCodeParser.LSB)
            self.state = 401
            self.index_operator()
            self.state = 402
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = ZCodeParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_index_operator)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.expr()
                self.state = 406
                self.match(ZCodeParser.CM)
                self.state = 407
                self.index_operator()
                pass


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
        self._predicates[39] = self.expr2_sempred
        self._predicates[40] = self.expr3_sempred
        self._predicates[41] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




