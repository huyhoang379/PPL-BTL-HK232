# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0184\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\7\2z\n\2\f\2\16\2}\13\2\3\2\3\2\3\3\6")
        buf.write("\3\u0082\n\3\r\3\16\3\u0083\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%")
        buf.write("\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\5*\u011d\n*\3*\3*\3*\3+")
        buf.write("\3+\3,\6,\u0125\n,\r,\16,\u0126\3-\3-\7-\u012b\n-\f-\16")
        buf.write("-\u012e\13-\3.\3.\5.\u0132\n.\3.\6.\u0135\n.\r.\16.\u0136")
        buf.write("\3/\3/\5/\u013b\n/\3/\5/\u013e\n/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\5\62\u014d")
        buf.write("\n\62\3\63\3\63\3\63\5\63\u0152\n\63\3\64\3\64\3\64\3")
        buf.write("\65\3\65\3\65\3\66\3\66\7\66\u015c\n\66\f\66\16\66\u015f")
        buf.write("\13\66\3\66\3\66\3\66\3\67\3\67\7\67\u0166\n\67\f\67\16")
        buf.write("\67\u0169\13\67\38\38\78\u016d\n8\f8\168\u0170\138\38")
        buf.write("\38\38\38\39\39\79\u0178\n9\f9\169\u017b\139\39\59\u017e")
        buf.write("\n9\39\39\3:\3:\3:\2\2;\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W\2Y\2[\2]-_\2a\2c.e\2")
        buf.write("g\2i\2k/m\60o\61q\62s\63\3\2\f\4\2\f\f\17\17\5\2\n\13")
        buf.write("\16\16\"\"\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t")
        buf.write("\2))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\4\3\f\f\17")
        buf.write("\17\2\u018b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2]\3\2\2\2\2c\3\2\2\2\2k\3")
        buf.write("\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3u")
        buf.write("\3\2\2\2\5\u0081\3\2\2\2\7\u0087\3\2\2\2\t\u008e\3\2\2")
        buf.write("\2\13\u0093\3\2\2\2\r\u009a\3\2\2\2\17\u00a1\3\2\2\2\21")
        buf.write("\u00a5\3\2\2\2\23\u00ad\3\2\2\2\25\u00b2\3\2\2\2\27\u00b6")
        buf.write("\3\2\2\2\31\u00bc\3\2\2\2\33\u00bf\3\2\2\2\35\u00c5\3")
        buf.write("\2\2\2\37\u00ce\3\2\2\2!\u00d1\3\2\2\2#\u00d6\3\2\2\2")
        buf.write("%\u00db\3\2\2\2\'\u00e1\3\2\2\2)\u00e5\3\2\2\2+\u00e9")
        buf.write("\3\2\2\2-\u00ed\3\2\2\2/\u00f0\3\2\2\2\61\u00f2\3\2\2")
        buf.write("\2\63\u00f4\3\2\2\2\65\u00f6\3\2\2\2\67\u00f8\3\2\2\2")
        buf.write("9\u00fa\3\2\2\2;\u00fc\3\2\2\2=\u00ff\3\2\2\2?\u0102\3")
        buf.write("\2\2\2A\u0104\3\2\2\2C\u0107\3\2\2\2E\u0109\3\2\2\2G\u010c")
        buf.write("\3\2\2\2I\u0110\3\2\2\2K\u0113\3\2\2\2M\u0115\3\2\2\2")
        buf.write("O\u0117\3\2\2\2Q\u0119\3\2\2\2S\u011c\3\2\2\2U\u0121\3")
        buf.write("\2\2\2W\u0124\3\2\2\2Y\u0128\3\2\2\2[\u012f\3\2\2\2]\u0138")
        buf.write("\3\2\2\2_\u013f\3\2\2\2a\u0144\3\2\2\2c\u014c\3\2\2\2")
        buf.write("e\u0151\3\2\2\2g\u0153\3\2\2\2i\u0156\3\2\2\2k\u0159\3")
        buf.write("\2\2\2m\u0163\3\2\2\2o\u016a\3\2\2\2q\u0175\3\2\2\2s\u0181")
        buf.write("\3\2\2\2uv\7%\2\2vw\7%\2\2w{\3\2\2\2xz\n\2\2\2yx\3\2\2")
        buf.write("\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2~")
        buf.write("\177\b\2\2\2\177\4\3\2\2\2\u0080\u0082\t\3\2\2\u0081\u0080")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0081\3\2\2\2\u0083")
        buf.write("\u0084\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\b\3\2\2")
        buf.write("\u0086\6\3\2\2\2\u0087\u0088\7p\2\2\u0088\u0089\7w\2\2")
        buf.write("\u0089\u008a\7o\2\2\u008a\u008b\7d\2\2\u008b\u008c\7g")
        buf.write("\2\2\u008c\u008d\7t\2\2\u008d\b\3\2\2\2\u008e\u008f\7")
        buf.write("d\2\2\u008f\u0090\7q\2\2\u0090\u0091\7q\2\2\u0091\u0092")
        buf.write("\7n\2\2\u0092\n\3\2\2\2\u0093\u0094\7u\2\2\u0094\u0095")
        buf.write("\7v\2\2\u0095\u0096\7t\2\2\u0096\u0097\7k\2\2\u0097\u0098")
        buf.write("\7p\2\2\u0098\u0099\7i\2\2\u0099\f\3\2\2\2\u009a\u009b")
        buf.write("\7t\2\2\u009b\u009c\7g\2\2\u009c\u009d\7v\2\2\u009d\u009e")
        buf.write("\7w\2\2\u009e\u009f\7t\2\2\u009f\u00a0\7p\2\2\u00a0\16")
        buf.write("\3\2\2\2\u00a1\u00a2\7x\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\20\3\2\2\2\u00a5\u00a6\7f\2\2\u00a6\u00a7")
        buf.write("\7{\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa")
        buf.write("\7o\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac\7e\2\2\u00ac\22")
        buf.write("\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af\7w\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\u00b1\7e\2\2\u00b1\24\3\2\2\2\u00b2\u00b3")
        buf.write("\7h\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7t\2\2\u00b5\26")
        buf.write("\3\2\2\2\u00b6\u00b7\7w\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7n\2\2\u00bb\30")
        buf.write("\3\2\2\2\u00bc\u00bd\7d\2\2\u00bd\u00be\7{\2\2\u00be\32")
        buf.write("\3\2\2\2\u00bf\u00c0\7d\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7m\2\2\u00c4\34")
        buf.write("\3\2\2\2\u00c5\u00c6\7e\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8")
        buf.write("\7p\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb")
        buf.write("\7p\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd\7g\2\2\u00cd\36")
        buf.write("\3\2\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7h\2\2\u00d0 ")
        buf.write("\3\2\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4")
        buf.write("\7u\2\2\u00d4\u00d5\7g\2\2\u00d5\"\3\2\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da")
        buf.write("\7h\2\2\u00da$\3\2\2\2\u00db\u00dc\7d\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7i\2\2\u00de\u00df\7k\2\2\u00df\u00e0")
        buf.write("\7p\2\2\u00e0&\3\2\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3")
        buf.write("\7p\2\2\u00e3\u00e4\7f\2\2\u00e4(\3\2\2\2\u00e5\u00e6")
        buf.write("\7p\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7v\2\2\u00e8*\3")
        buf.write("\2\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec")
        buf.write("\7f\2\2\u00ec,\3\2\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef")
        buf.write("\7t\2\2\u00ef.\3\2\2\2\u00f0\u00f1\7-\2\2\u00f1\60\3\2")
        buf.write("\2\2\u00f2\u00f3\7/\2\2\u00f3\62\3\2\2\2\u00f4\u00f5\7")
        buf.write(",\2\2\u00f5\64\3\2\2\2\u00f6\u00f7\7\61\2\2\u00f7\66\3")
        buf.write("\2\2\2\u00f8\u00f9\7\'\2\2\u00f98\3\2\2\2\u00fa\u00fb")
        buf.write("\7?\2\2\u00fb:\3\2\2\2\u00fc\u00fd\7>\2\2\u00fd\u00fe")
        buf.write("\7/\2\2\u00fe<\3\2\2\2\u00ff\u0100\7#\2\2\u0100\u0101")
        buf.write("\7?\2\2\u0101>\3\2\2\2\u0102\u0103\7>\2\2\u0103@\3\2\2")
        buf.write("\2\u0104\u0105\7>\2\2\u0105\u0106\7?\2\2\u0106B\3\2\2")
        buf.write("\2\u0107\u0108\7@\2\2\u0108D\3\2\2\2\u0109\u010a\7@\2")
        buf.write("\2\u010a\u010b\7?\2\2\u010bF\3\2\2\2\u010c\u010d\7\60")
        buf.write("\2\2\u010d\u010e\7\60\2\2\u010e\u010f\7\60\2\2\u010fH")
        buf.write("\3\2\2\2\u0110\u0111\7?\2\2\u0111\u0112\7?\2\2\u0112J")
        buf.write("\3\2\2\2\u0113\u0114\7*\2\2\u0114L\3\2\2\2\u0115\u0116")
        buf.write("\7+\2\2\u0116N\3\2\2\2\u0117\u0118\7]\2\2\u0118P\3\2\2")
        buf.write("\2\u0119\u011a\7_\2\2\u011aR\3\2\2\2\u011b\u011d\7\17")
        buf.write("\2\2\u011c\u011b\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e")
        buf.write("\3\2\2\2\u011e\u011f\7\f\2\2\u011f\u0120\b*\3\2\u0120")
        buf.write("T\3\2\2\2\u0121\u0122\7.\2\2\u0122V\3\2\2\2\u0123\u0125")
        buf.write("\t\4\2\2\u0124\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127X\3\2\2\2\u0128")
        buf.write("\u012c\7\60\2\2\u0129\u012b\t\4\2\2\u012a\u0129\3\2\2")
        buf.write("\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012dZ\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0131")
        buf.write("\t\5\2\2\u0130\u0132\t\6\2\2\u0131\u0130\3\2\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\u0134\3\2\2\2\u0133\u0135\t\4\2\2")
        buf.write("\u0134\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0134\3")
        buf.write("\2\2\2\u0136\u0137\3\2\2\2\u0137\\\3\2\2\2\u0138\u013a")
        buf.write("\5W,\2\u0139\u013b\5Y-\2\u013a\u0139\3\2\2\2\u013a\u013b")
        buf.write("\3\2\2\2\u013b\u013d\3\2\2\2\u013c\u013e\5[.\2\u013d\u013c")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013e^\3\2\2\2\u013f\u0140")
        buf.write("\7v\2\2\u0140\u0141\7t\2\2\u0141\u0142\7w\2\2\u0142\u0143")
        buf.write("\7g\2\2\u0143`\3\2\2\2\u0144\u0145\7h\2\2\u0145\u0146")
        buf.write("\7c\2\2\u0146\u0147\7n\2\2\u0147\u0148\7u\2\2\u0148\u0149")
        buf.write("\7g\2\2\u0149b\3\2\2\2\u014a\u014d\5_\60\2\u014b\u014d")
        buf.write("\5a\61\2\u014c\u014a\3\2\2\2\u014c\u014b\3\2\2\2\u014d")
        buf.write("d\3\2\2\2\u014e\u0152\5g\64\2\u014f\u0152\5i\65\2\u0150")
        buf.write("\u0152\n\7\2\2\u0151\u014e\3\2\2\2\u0151\u014f\3\2\2\2")
        buf.write("\u0151\u0150\3\2\2\2\u0152f\3\2\2\2\u0153\u0154\7^\2\2")
        buf.write("\u0154\u0155\t\b\2\2\u0155h\3\2\2\2\u0156\u0157\7)\2\2")
        buf.write("\u0157\u0158\7$\2\2\u0158j\3\2\2\2\u0159\u015d\7$\2\2")
        buf.write("\u015a\u015c\5e\63\2\u015b\u015a\3\2\2\2\u015c\u015f\3")
        buf.write("\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0160")
        buf.write("\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161\7$\2\2\u0161")
        buf.write("\u0162\b\66\4\2\u0162l\3\2\2\2\u0163\u0167\t\t\2\2\u0164")
        buf.write("\u0166\t\n\2\2\u0165\u0164\3\2\2\2\u0166\u0169\3\2\2\2")
        buf.write("\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168n\3\2\2")
        buf.write("\2\u0169\u0167\3\2\2\2\u016a\u016e\7$\2\2\u016b\u016d")
        buf.write("\5e\63\2\u016c\u016b\3\2\2\2\u016d\u0170\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0171\3\2\2\2")
        buf.write("\u0170\u016e\3\2\2\2\u0171\u0172\7^\2\2\u0172\u0173\n")
        buf.write("\b\2\2\u0173\u0174\b8\5\2\u0174p\3\2\2\2\u0175\u0179\7")
        buf.write("$\2\2\u0176\u0178\5e\63\2\u0177\u0176\3\2\2\2\u0178\u017b")
        buf.write("\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017e\t\13\2")
        buf.write("\2\u017d\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180")
        buf.write("\b9\6\2\u0180r\3\2\2\2\u0181\u0182\13\2\2\2\u0182\u0183")
        buf.write("\b:\7\2\u0183t\3\2\2\2\23\2{\u0083\u011c\u0126\u012c\u0131")
        buf.write("\u0136\u013a\u013d\u014c\u0151\u015d\u0167\u016e\u0179")
        buf.write("\u017d\b\b\2\2\3*\2\3\66\3\38\4\39\5\3:\6")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINECMT = 1
    WS = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONT = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQ = 28
    ASSIGN = 29
    NEQ = 30
    LT = 31
    LEQ = 32
    GT = 33
    GEQ = 34
    CONCAT = 35
    COMPARE_STR = 36
    LB = 37
    RB = 38
    LSB = 39
    RSB = 40
    NEWLINE = 41
    COMMA = 42
    NUMLIT = 43
    BOOLLIT = 44
    STRLIT = 45
    ID = 46
    ILLEGAL_ESCAPE = 47
    UNCLOSE_STRING = 48
    ERROR_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
            "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
            "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
            "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'('", "')'", 
            "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "LINECMT", "WS", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONT", "IF", 
            "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "EQ", "ASSIGN", "NEQ", "LT", "LEQ", "GT", 
            "GEQ", "CONCAT", "COMPARE_STR", "LB", "RB", "LSB", "RSB", "NEWLINE", 
            "COMMA", "NUMLIT", "BOOLLIT", "STRLIT", "ID", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "LINECMT", "WS", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONT", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", 
                  "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "ASSIGN", 
                  "NEQ", "LT", "LEQ", "GT", "GEQ", "CONCAT", "COMPARE_STR", 
                  "LB", "RB", "LSB", "RSB", "NEWLINE", "COMMA", "IntegerPart", 
                  "DecimalPart", "ExponentPart", "NUMLIT", "TRUE", "FALSE", 
                  "BOOLLIT", "Char", "EscapeStr", "DQ", "STRLIT", "ID", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[40] = self.NEWLINE_action 
            actions[52] = self.STRLIT_action 
            actions[54] = self.ILLEGAL_ESCAPE_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('\r','')
     

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                a = str(self.text)
                self.text = a[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise IllegalEscape(self.text[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	if self.text[-1] in ["\n","\r"] :
            		raise UncloseString(self.text[1:-1])
            	else: raise UncloseString(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


