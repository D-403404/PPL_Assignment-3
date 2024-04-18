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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u019e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\7\2~\n\2\f\2\16\2\u0081\13")
        buf.write("\2\3\2\3\2\3\3\6\3\u0086\n\3\r\3\16\3\u0087\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\6\4\u0093\n\4\r\4\16\4\u0094")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u00a8\n\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*")
        buf.write("\3*\3*\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\3\60\3\60\5\60\u0148\n\60\3\61\3\61\7\61\u014c")
        buf.write("\n\61\f\61\16\61\u014f\13\61\3\62\3\62\5\62\u0153\n\62")
        buf.write("\3\62\5\62\u0156\n\62\3\63\3\63\3\64\6\64\u015b\n\64\r")
        buf.write("\64\16\64\u015c\3\65\3\65\7\65\u0161\n\65\f\65\16\65\u0164")
        buf.write("\13\65\3\66\3\66\5\66\u0168\n\66\3\66\6\66\u016b\n\66")
        buf.write("\r\66\16\66\u016c\3\67\3\67\3\67\3\67\3\67\38\38\38\3")
        buf.write("8\78\u0178\n8\f8\168\u017b\138\39\39\39\39\39\39\39\3")
        buf.write("9\39\39\39\39\59\u0189\n9\3:\3:\3:\3;\3;\3;\3;\3;\3;\5")
        buf.write(";\u0194\n;\3;\3;\3<\3<\3<\3<\3<\3<\3<\2\2=\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\2\31\2\33\r\35\16")
        buf.write("\37\17!\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31\65")
        buf.write("\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,")
        buf.write("[-]._/a\60c\61e\2g\2i\2k\2m\62o\2q\2s\63u\64w\65\3\2\13")
        buf.write("\4\2\f\f\17\17\5\2\n\13\16\16\"\"\5\2C\\aac|\6\2\62;C")
        buf.write("\\aac|\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\t\2)")
        buf.write(")^^ddhhppttvv\2\u01af\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2m\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\3y\3\2\2\2\5\u0085\3\2\2\2\7")
        buf.write("\u0092\3\2\2\2\t\u0098\3\2\2\2\13\u009a\3\2\2\2\r\u009c")
        buf.write("\3\2\2\2\17\u009e\3\2\2\2\21\u00a0\3\2\2\2\23\u00a7\3")
        buf.write("\2\2\2\25\u00ab\3\2\2\2\27\u00ae\3\2\2\2\31\u00b3\3\2")
        buf.write("\2\2\33\u00b9\3\2\2\2\35\u00c0\3\2\2\2\37\u00c5\3\2\2")
        buf.write("\2!\u00cc\3\2\2\2#\u00d3\3\2\2\2%\u00d7\3\2\2\2\'\u00df")
        buf.write("\3\2\2\2)\u00e4\3\2\2\2+\u00e8\3\2\2\2-\u00ee\3\2\2\2")
        buf.write("/\u00f1\3\2\2\2\61\u00f7\3\2\2\2\63\u0100\3\2\2\2\65\u0103")
        buf.write("\3\2\2\2\67\u0108\3\2\2\29\u010d\3\2\2\2;\u0113\3\2\2")
        buf.write("\2=\u0117\3\2\2\2?\u0119\3\2\2\2A\u011b\3\2\2\2C\u011d")
        buf.write("\3\2\2\2E\u011f\3\2\2\2G\u0121\3\2\2\2I\u0124\3\2\2\2")
        buf.write("K\u0126\3\2\2\2M\u0129\3\2\2\2O\u012b\3\2\2\2Q\u012d\3")
        buf.write("\2\2\2S\u0130\3\2\2\2U\u0133\3\2\2\2W\u0137\3\2\2\2Y\u013a")
        buf.write("\3\2\2\2[\u013e\3\2\2\2]\u0142\3\2\2\2_\u0147\3\2\2\2")
        buf.write("a\u0149\3\2\2\2c\u0150\3\2\2\2e\u0157\3\2\2\2g\u015a\3")
        buf.write("\2\2\2i\u015e\3\2\2\2k\u0165\3\2\2\2m\u016e\3\2\2\2o\u0179")
        buf.write("\3\2\2\2q\u0188\3\2\2\2s\u018a\3\2\2\2u\u018d\3\2\2\2")
        buf.write("w\u0197\3\2\2\2yz\7%\2\2z{\7%\2\2{\177\3\2\2\2|~\n\2\2")
        buf.write("\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2")
        buf.write("\2\2\u0080\u0082\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083")
        buf.write("\b\2\2\2\u0083\4\3\2\2\2\u0084\u0086\t\3\2\2\u0085\u0084")
        buf.write("\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0085\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\b\3\2\2")
        buf.write("\u008a\6\3\2\2\2\u008b\u0093\7\"\2\2\u008c\u008d\7^\2")
        buf.write("\2\u008d\u0093\7v\2\2\u008e\u008f\7^\2\2\u008f\u0093\7")
        buf.write("d\2\2\u0090\u0091\7^\2\2\u0091\u0093\7h\2\2\u0092\u008b")
        buf.write("\3\2\2\2\u0092\u008c\3\2\2\2\u0092\u008e\3\2\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0092\3\2\2\2")
        buf.write("\u0094\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\b")
        buf.write("\4\2\2\u0097\b\3\2\2\2\u0098\u0099\7*\2\2\u0099\n\3\2")
        buf.write("\2\2\u009a\u009b\7+\2\2\u009b\f\3\2\2\2\u009c\u009d\7")
        buf.write("]\2\2\u009d\16\3\2\2\2\u009e\u009f\7_\2\2\u009f\20\3\2")
        buf.write("\2\2\u00a0\u00a1\7.\2\2\u00a1\22\3\2\2\2\u00a2\u00a3\7")
        buf.write("\17\2\2\u00a3\u00a8\7\f\2\2\u00a4\u00a8\t\2\2\2\u00a5")
        buf.write("\u00a6\7^\2\2\u00a6\u00a8\7p\2\2\u00a7\u00a2\3\2\2\2\u00a7")
        buf.write("\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\3\2\2\2")
        buf.write("\u00a9\u00aa\b\n\3\2\u00aa\24\3\2\2\2\u00ab\u00ac\7^\2")
        buf.write("\2\u00ac\u00ad\7t\2\2\u00ad\26\3\2\2\2\u00ae\u00af\7v")
        buf.write("\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1\7w\2\2\u00b1\u00b2")
        buf.write("\7g\2\2\u00b2\30\3\2\2\2\u00b3\u00b4\7h\2\2\u00b4\u00b5")
        buf.write("\7c\2\2\u00b5\u00b6\7n\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\32\3\2\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb")
        buf.write("\7w\2\2\u00bb\u00bc\7o\2\2\u00bc\u00bd\7d\2\2\u00bd\u00be")
        buf.write("\7g\2\2\u00be\u00bf\7t\2\2\u00bf\34\3\2\2\2\u00c0\u00c1")
        buf.write("\7d\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4")
        buf.write("\7n\2\2\u00c4\36\3\2\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7")
        buf.write("\7v\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7i\2\2\u00cb \3\2\2\2\u00cc\u00cd")
        buf.write("\7t\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0")
        buf.write("\7w\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2\7p\2\2\u00d2\"")
        buf.write("\3\2\2\2\u00d3\u00d4\7x\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6")
        buf.write("\7t\2\2\u00d6$\3\2\2\2\u00d7\u00d8\7f\2\2\u00d8\u00d9")
        buf.write("\7{\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7c\2\2\u00db\u00dc")
        buf.write("\7o\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de\7e\2\2\u00de&\3")
        buf.write("\2\2\2\u00df\u00e0\7h\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2\u00e3\7e\2\2\u00e3(\3\2\2\2\u00e4\u00e5")
        buf.write("\7h\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7t\2\2\u00e7*\3")
        buf.write("\2\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb")
        buf.write("\7v\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7n\2\2\u00ed,\3")
        buf.write("\2\2\2\u00ee\u00ef\7d\2\2\u00ef\u00f0\7{\2\2\u00f0.\3")
        buf.write("\2\2\2\u00f1\u00f2\7d\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7m\2\2\u00f6\60")
        buf.write("\3\2\2\2\u00f7\u00f8\7e\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa")
        buf.write("\7p\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff\7g\2\2\u00ff\62")
        buf.write("\3\2\2\2\u0100\u0101\7k\2\2\u0101\u0102\7h\2\2\u0102\64")
        buf.write("\3\2\2\2\u0103\u0104\7g\2\2\u0104\u0105\7n\2\2\u0105\u0106")
        buf.write("\7u\2\2\u0106\u0107\7g\2\2\u0107\66\3\2\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109\u010a\7n\2\2\u010a\u010b\7k\2\2\u010b\u010c")
        buf.write("\7h\2\2\u010c8\3\2\2\2\u010d\u010e\7d\2\2\u010e\u010f")
        buf.write("\7g\2\2\u010f\u0110\7i\2\2\u0110\u0111\7k\2\2\u0111\u0112")
        buf.write("\7p\2\2\u0112:\3\2\2\2\u0113\u0114\7g\2\2\u0114\u0115")
        buf.write("\7p\2\2\u0115\u0116\7f\2\2\u0116<\3\2\2\2\u0117\u0118")
        buf.write("\7-\2\2\u0118>\3\2\2\2\u0119\u011a\7/\2\2\u011a@\3\2\2")
        buf.write("\2\u011b\u011c\7,\2\2\u011cB\3\2\2\2\u011d\u011e\7\61")
        buf.write("\2\2\u011eD\3\2\2\2\u011f\u0120\7\'\2\2\u0120F\3\2\2\2")
        buf.write("\u0121\u0122\7>\2\2\u0122\u0123\7/\2\2\u0123H\3\2\2\2")
        buf.write("\u0124\u0125\7?\2\2\u0125J\3\2\2\2\u0126\u0127\7#\2\2")
        buf.write("\u0127\u0128\7?\2\2\u0128L\3\2\2\2\u0129\u012a\7>\2\2")
        buf.write("\u012aN\3\2\2\2\u012b\u012c\7@\2\2\u012cP\3\2\2\2\u012d")
        buf.write("\u012e\7>\2\2\u012e\u012f\7?\2\2\u012fR\3\2\2\2\u0130")
        buf.write("\u0131\7@\2\2\u0131\u0132\7?\2\2\u0132T\3\2\2\2\u0133")
        buf.write("\u0134\7\60\2\2\u0134\u0135\7\60\2\2\u0135\u0136\7\60")
        buf.write("\2\2\u0136V\3\2\2\2\u0137\u0138\7?\2\2\u0138\u0139\7?")
        buf.write("\2\2\u0139X\3\2\2\2\u013a\u013b\7p\2\2\u013b\u013c\7q")
        buf.write("\2\2\u013c\u013d\7v\2\2\u013dZ\3\2\2\2\u013e\u013f\7c")
        buf.write("\2\2\u013f\u0140\7p\2\2\u0140\u0141\7f\2\2\u0141\\\3\2")
        buf.write("\2\2\u0142\u0143\7q\2\2\u0143\u0144\7t\2\2\u0144^\3\2")
        buf.write("\2\2\u0145\u0148\5\27\f\2\u0146\u0148\5\31\r\2\u0147\u0145")
        buf.write("\3\2\2\2\u0147\u0146\3\2\2\2\u0148`\3\2\2\2\u0149\u014d")
        buf.write("\t\4\2\2\u014a\u014c\t\5\2\2\u014b\u014a\3\2\2\2\u014c")
        buf.write("\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2")
        buf.write("\u014eb\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0152\5g\64")
        buf.write("\2\u0151\u0153\5i\65\2\u0152\u0151\3\2\2\2\u0152\u0153")
        buf.write("\3\2\2\2\u0153\u0155\3\2\2\2\u0154\u0156\5k\66\2\u0155")
        buf.write("\u0154\3\2\2\2\u0155\u0156\3\2\2\2\u0156d\3\2\2\2\u0157")
        buf.write("\u0158\t\6\2\2\u0158f\3\2\2\2\u0159\u015b\5e\63\2\u015a")
        buf.write("\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015a\3\2\2\2")
        buf.write("\u015c\u015d\3\2\2\2\u015dh\3\2\2\2\u015e\u0162\7\60\2")
        buf.write("\2\u015f\u0161\5e\63\2\u0160\u015f\3\2\2\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("j\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0167\t\7\2\2\u0166")
        buf.write("\u0168\t\b\2\2\u0167\u0166\3\2\2\2\u0167\u0168\3\2\2\2")
        buf.write("\u0168\u016a\3\2\2\2\u0169\u016b\5e\63\2\u016a\u0169\3")
        buf.write("\2\2\2\u016b\u016c\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d")
        buf.write("\3\2\2\2\u016dl\3\2\2\2\u016e\u016f\7$\2\2\u016f\u0170")
        buf.write("\5o8\2\u0170\u0171\7$\2\2\u0171\u0172\b\67\4\2\u0172n")
        buf.write("\3\2\2\2\u0173\u0178\n\t\2\2\u0174\u0178\5q9\2\u0175\u0176")
        buf.write("\7)\2\2\u0176\u0178\7$\2\2\u0177\u0173\3\2\2\2\u0177\u0174")
        buf.write("\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u017b\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017ap\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017c\u017d\7^\2\2\u017d\u0189\7d\2\2\u017e")
        buf.write("\u017f\7^\2\2\u017f\u0189\7v\2\2\u0180\u0181\7^\2\2\u0181")
        buf.write("\u0189\7h\2\2\u0182\u0183\7^\2\2\u0183\u0189\7t\2\2\u0184")
        buf.write("\u0185\7^\2\2\u0185\u0189\7)\2\2\u0186\u0187\7^\2\2\u0187")
        buf.write("\u0189\7^\2\2\u0188\u017c\3\2\2\2\u0188\u017e\3\2\2\2")
        buf.write("\u0188\u0180\3\2\2\2\u0188\u0182\3\2\2\2\u0188\u0184\3")
        buf.write("\2\2\2\u0188\u0186\3\2\2\2\u0189r\3\2\2\2\u018a\u018b")
        buf.write("\13\2\2\2\u018b\u018c\b:\5\2\u018ct\3\2\2\2\u018d\u018e")
        buf.write("\7$\2\2\u018e\u0193\5o8\2\u018f\u0194\t\2\2\2\u0190\u0191")
        buf.write("\7^\2\2\u0191\u0194\7p\2\2\u0192\u0194\7\2\2\3\u0193\u018f")
        buf.write("\3\2\2\2\u0193\u0190\3\2\2\2\u0193\u0192\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0196\b;\6\2\u0196v\3\2\2\2\u0197")
        buf.write("\u0198\7$\2\2\u0198\u0199\5o8\2\u0199\u019a\7^\2\2\u019a")
        buf.write("\u019b\n\n\2\2\u019b\u019c\3\2\2\2\u019c\u019d\b<\7\2")
        buf.write("\u019dx\3\2\2\2\24\2\177\u0087\u0092\u0094\u00a7\u0147")
        buf.write("\u014d\u0152\u0155\u015c\u0162\u0167\u016c\u0177\u0179")
        buf.write("\u0188\u0193\b\b\2\2\3\n\2\3\67\3\3:\4\3;\5\3<\6")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    WS = 2
    WS2 = 3
    SB_LEFTBRACKET = 4
    SB_RIGHTBRACKET = 5
    SB_LEFTSQUARE = 6
    SB_RIGHTSQUARE = 7
    SB_COMMA = 8
    SB_NEWLINE = 9
    SB_CR = 10
    KW_NUMBER = 11
    KW_BOOL = 12
    KW_STRING = 13
    KW_RETURN = 14
    KW_VAR = 15
    KW_DYNAMIC = 16
    KW_FUNC = 17
    KW_FOR = 18
    KW_UNTIL = 19
    KW_BY = 20
    KW_BREAK = 21
    KW_CONTINUE = 22
    KW_IF = 23
    KW_ELSE = 24
    KW_ELIF = 25
    KW_BEGIN = 26
    KW_END = 27
    OP_PLUS = 28
    OP_MINUS = 29
    OP_MULT = 30
    OP_DIV = 31
    OP_MOD = 32
    OP_ASSIGN = 33
    OP_EQUAL_NUM = 34
    OP_UNEQUAL = 35
    OP_LESS = 36
    OP_MORE = 37
    OP_LESSOREQUAL = 38
    OP_MOREOREQUAL = 39
    OP_CONCAT = 40
    OP_EQUAL_STR = 41
    OP_NOT = 42
    OP_AND = 43
    OP_OR = 44
    BOOL = 45
    IDENTIFIER = 46
    NUMBER = 47
    STRING = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "','", "'\\r'", "'number'", "'bool'", 
            "'string'", "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
            "'until'", "'by'", "'break'", "'continue'", "'if'", "'else'", 
            "'elif'", "'begin'", "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'<-'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'...'", 
            "'=='", "'not'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "WS", "WS2", "SB_LEFTBRACKET", "SB_RIGHTBRACKET", 
            "SB_LEFTSQUARE", "SB_RIGHTSQUARE", "SB_COMMA", "SB_NEWLINE", 
            "SB_CR", "KW_NUMBER", "KW_BOOL", "KW_STRING", "KW_RETURN", "KW_VAR", 
            "KW_DYNAMIC", "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", 
            "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", "KW_END", 
            "OP_PLUS", "OP_MINUS", "OP_MULT", "OP_DIV", "OP_MOD", "OP_ASSIGN", 
            "OP_EQUAL_NUM", "OP_UNEQUAL", "OP_LESS", "OP_MORE", "OP_LESSOREQUAL", 
            "OP_MOREOREQUAL", "OP_CONCAT", "OP_EQUAL_STR", "OP_NOT", "OP_AND", 
            "OP_OR", "BOOL", "IDENTIFIER", "NUMBER", "STRING", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "WS", "WS2", "SB_LEFTBRACKET", "SB_RIGHTBRACKET", 
                  "SB_LEFTSQUARE", "SB_RIGHTSQUARE", "SB_COMMA", "SB_NEWLINE", 
                  "SB_CR", "KW_TRUE", "KW_FALSE", "KW_NUMBER", "KW_BOOL", 
                  "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", "KW_FUNC", 
                  "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", "KW_CONTINUE", 
                  "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", "KW_END", "OP_PLUS", 
                  "OP_MINUS", "OP_MULT", "OP_DIV", "OP_MOD", "OP_ASSIGN", 
                  "OP_EQUAL_NUM", "OP_UNEQUAL", "OP_LESS", "OP_MORE", "OP_LESSOREQUAL", 
                  "OP_MOREOREQUAL", "OP_CONCAT", "OP_EQUAL_STR", "OP_NOT", 
                  "OP_AND", "OP_OR", "BOOL", "IDENTIFIER", "NUMBER", "Digit", 
                  "IntPart", "DecPart", "ExpPart", "STRING", "StringContent", 
                  "EscSequence", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[8] = self.SB_NEWLINE_action 
            actions[53] = self.STRING_action 
            actions[56] = self.ERROR_CHAR_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def SB_NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('\r\n','\n').replace('\r','\n')
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:].replace('\r','').replace('\n','').replace('\\n',''); raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     


