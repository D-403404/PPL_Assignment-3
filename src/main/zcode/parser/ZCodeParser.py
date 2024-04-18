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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0232\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\3\2\3\2\3\3\7\3\177\n\3\f\3\16\3\u0082")
        buf.write("\13\3\3\3\3\3\3\3\3\3\7\3\u0088\n\3\f\3\16\3\u008b\13")
        buf.write("\3\3\3\5\3\u008e\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u0095\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\u00a0\n\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\5\20\u00b9")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00c0\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\7\22\u00c9\n\22\f\22\16\22")
        buf.write("\u00cc\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00d5")
        buf.write("\n\23\f\23\16\23\u00d8\13\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\7\24\u00e1\n\24\f\24\16\24\u00e4\13\24\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u00ea\n\25\3\26\3\26\3\26\3\26\5")
        buf.write("\26\u00f0\n\26\3\27\3\27\5\27\u00f4\n\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0100\n\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33\5\33")
        buf.write("\u010c\n\33\3\34\3\34\6\34\u0110\n\34\r\34\16\34\u0111")
        buf.write("\3\34\3\34\6\34\u0116\n\34\r\34\16\34\u0117\3\34\3\34")
        buf.write("\6\34\u011c\n\34\r\34\16\34\u011d\5\34\u0120\n\34\3\35")
        buf.write("\3\35\3\35\5\35\u0125\n\35\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\5\36\u012e\n\36\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u0135\n\37\3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\5\"\u0145\n\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\5$\u0150")
        buf.write("\n$\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\5\'\u015d\n")
        buf.write("\'\3(\3(\3(\3(\3(\3(\7(\u0165\n(\f(\16(\u0168\13(\3(\3")
        buf.write("(\3)\3)\3)\3)\5)\u0170\n)\3*\3*\3*\3*\3*\5*\u0177\n*\3")
        buf.write("+\3+\3+\3+\3+\3+\5+\u017f\n+\3,\3,\3,\5,\u0184\n,\3-\3")
        buf.write("-\6-\u0188\n-\r-\16-\u0189\3-\3-\6-\u018e\n-\r-\16-\u018f")
        buf.write("\3-\3-\6-\u0194\n-\r-\16-\u0195\3-\3-\3-\3-\6-\u019c\n")
        buf.write("-\r-\16-\u019d\3-\3-\6-\u01a2\n-\r-\16-\u01a3\3-\3-\6")
        buf.write("-\u01a8\n-\r-\16-\u01a9\3-\3-\6-\u01ae\n-\r-\16-\u01af")
        buf.write("\3-\3-\6-\u01b4\n-\r-\16-\u01b5\5-\u01b8\n-\3.\3.\3.\3")
        buf.write("/\3/\5/\u01bf\n/\3\60\3\60\3\60\3\60\3\60\7\60\u01c6\n")
        buf.write("\60\f\60\16\60\u01c9\13\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\61\3\61\7\61\u01d2\n\61\f\61\16\61\u01d5\13\61\3\61\3")
        buf.write("\61\3\62\3\62\7\62\u01db\n\62\f\62\16\62\u01de\13\62\3")
        buf.write("\62\3\62\5\62\u01e2\n\62\3\63\3\63\7\63\u01e6\n\63\f\63")
        buf.write("\16\63\u01e9\13\63\3\63\3\63\3\63\3\64\3\64\7\64\u01f0")
        buf.write("\n\64\f\64\16\64\u01f3\13\64\3\64\3\64\3\64\5\64\u01f8")
        buf.write("\n\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u0201\n")
        buf.write("\65\f\65\16\65\u0204\13\65\3\65\3\65\3\66\3\66\3\67\3")
        buf.write("\67\38\38\38\58\u020f\n8\39\39\39\39\39\3:\3:\3:\3:\5")
        buf.write(":\u021a\n:\3;\3;\3;\3;\3;\5;\u0221\n;\3<\3<\6<\u0225\n")
        buf.write("<\r<\16<\u0226\3<\3<\3<\3=\3=\3=\3=\5=\u0230\n=\3=\2\5")
        buf.write("\"$&>\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.")
        buf.write("\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvx\2\7\3\2")
        buf.write(" \"\3\2\36\37\3\2-.\4\2$)++\3\2\r\17\2\u023b\2z\3\2\2")
        buf.write("\2\4\u008d\3\2\2\2\6\u0094\3\2\2\2\b\u0096\3\2\2\2\n\u009f")
        buf.write("\3\2\2\2\f\u00a1\3\2\2\2\16\u00a3\3\2\2\2\20\u00a5\3\2")
        buf.write("\2\2\22\u00a7\3\2\2\2\24\u00a9\3\2\2\2\26\u00ab\3\2\2")
        buf.write("\2\30\u00ad\3\2\2\2\32\u00af\3\2\2\2\34\u00b1\3\2\2\2")
        buf.write("\36\u00b8\3\2\2\2 \u00bf\3\2\2\2\"\u00c1\3\2\2\2$\u00cd")
        buf.write("\3\2\2\2&\u00d9\3\2\2\2(\u00e9\3\2\2\2*\u00ef\3\2\2\2")
        buf.write(",\u00f3\3\2\2\2.\u00ff\3\2\2\2\60\u0101\3\2\2\2\62\u0106")
        buf.write("\3\2\2\2\64\u010b\3\2\2\2\66\u011f\3\2\2\28\u0124\3\2")
        buf.write("\2\2:\u012d\3\2\2\2<\u0134\3\2\2\2>\u0136\3\2\2\2@\u013a")
        buf.write("\3\2\2\2B\u0144\3\2\2\2D\u0146\3\2\2\2F\u014f\3\2\2\2")
        buf.write("H\u0151\3\2\2\2J\u0153\3\2\2\2L\u015c\3\2\2\2N\u015e\3")
        buf.write("\2\2\2P\u016f\3\2\2\2R\u0176\3\2\2\2T\u017e\3\2\2\2V\u0183")
        buf.write("\3\2\2\2X\u01b7\3\2\2\2Z\u01b9\3\2\2\2\\\u01be\3\2\2\2")
        buf.write("^\u01c0\3\2\2\2`\u01cc\3\2\2\2b\u01e1\3\2\2\2d\u01e3\3")
        buf.write("\2\2\2f\u01f7\3\2\2\2h\u01f9\3\2\2\2j\u0207\3\2\2\2l\u0209")
        buf.write("\3\2\2\2n\u020e\3\2\2\2p\u0210\3\2\2\2r\u0219\3\2\2\2")
        buf.write("t\u0220\3\2\2\2v\u0222\3\2\2\2x\u022f\3\2\2\2z{\5\4\3")
        buf.write("\2{|\7\2\2\3|\3\3\2\2\2}\177\7\13\2\2~}\3\2\2\2\177\u0082")
        buf.write("\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0083")
        buf.write("\3\2\2\2\u0082\u0080\3\2\2\2\u0083\u0084\5\66\34\2\u0084")
        buf.write("\u0085\5\4\3\2\u0085\u008e\3\2\2\2\u0086\u0088\7\13\2")
        buf.write("\2\u0087\u0086\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087")
        buf.write("\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008c\3\2\2\2\u008b")
        buf.write("\u0089\3\2\2\2\u008c\u008e\5\66\34\2\u008d\u0080\3\2\2")
        buf.write("\2\u008d\u0089\3\2\2\2\u008e\5\3\2\2\2\u008f\u0090\7\60")
        buf.write("\2\2\u0090\u0095\5\b\5\2\u0091\u0092\5\60\31\2\u0092\u0093")
        buf.write("\5\b\5\2\u0093\u0095\3\2\2\2\u0094\u008f\3\2\2\2\u0094")
        buf.write("\u0091\3\2\2\2\u0095\7\3\2\2\2\u0096\u0097\7\b\2\2\u0097")
        buf.write("\u0098\5\n\6\2\u0098\u0099\7\t\2\2\u0099\t\3\2\2\2\u009a")
        buf.write("\u009b\5\34\17\2\u009b\u009c\7\n\2\2\u009c\u009d\5\n\6")
        buf.write("\2\u009d\u00a0\3\2\2\2\u009e\u00a0\5\34\17\2\u009f\u009a")
        buf.write("\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\13\3\2\2\2\u00a1\u00a2")
        buf.write("\5\6\4\2\u00a2\r\3\2\2\2\u00a3\u00a4\7\37\2\2\u00a4\17")
        buf.write("\3\2\2\2\u00a5\u00a6\7,\2\2\u00a6\21\3\2\2\2\u00a7\u00a8")
        buf.write("\t\2\2\2\u00a8\23\3\2\2\2\u00a9\u00aa\t\3\2\2\u00aa\25")
        buf.write("\3\2\2\2\u00ab\u00ac\t\4\2\2\u00ac\27\3\2\2\2\u00ad\u00ae")
        buf.write("\t\5\2\2\u00ae\31\3\2\2\2\u00af\u00b0\7*\2\2\u00b0\33")
        buf.write("\3\2\2\2\u00b1\u00b2\5\36\20\2\u00b2\35\3\2\2\2\u00b3")
        buf.write("\u00b4\5 \21\2\u00b4\u00b5\5\32\16\2\u00b5\u00b6\5 \21")
        buf.write("\2\u00b6\u00b9\3\2\2\2\u00b7\u00b9\5 \21\2\u00b8\u00b3")
        buf.write("\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\37\3\2\2\2\u00ba\u00bb")
        buf.write("\5\"\22\2\u00bb\u00bc\5\30\r\2\u00bc\u00bd\5\"\22\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00c0\5\"\22\2\u00bf\u00ba\3\2\2")
        buf.write("\2\u00bf\u00be\3\2\2\2\u00c0!\3\2\2\2\u00c1\u00c2\b\22")
        buf.write("\1\2\u00c2\u00c3\5$\23\2\u00c3\u00ca\3\2\2\2\u00c4\u00c5")
        buf.write("\f\4\2\2\u00c5\u00c6\5\26\f\2\u00c6\u00c7\5$\23\2\u00c7")
        buf.write("\u00c9\3\2\2\2\u00c8\u00c4\3\2\2\2\u00c9\u00cc\3\2\2\2")
        buf.write("\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb#\3\2\2")
        buf.write("\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\b\23\1\2\u00ce\u00cf")
        buf.write("\5&\24\2\u00cf\u00d6\3\2\2\2\u00d0\u00d1\f\4\2\2\u00d1")
        buf.write("\u00d2\5\24\13\2\u00d2\u00d3\5&\24\2\u00d3\u00d5\3\2\2")
        buf.write("\2\u00d4\u00d0\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7%\3\2\2\2\u00d8\u00d6")
        buf.write("\3\2\2\2\u00d9\u00da\b\24\1\2\u00da\u00db\5(\25\2\u00db")
        buf.write("\u00e2\3\2\2\2\u00dc\u00dd\f\4\2\2\u00dd\u00de\5\22\n")
        buf.write("\2\u00de\u00df\5(\25\2\u00df\u00e1\3\2\2\2\u00e0\u00dc")
        buf.write("\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\'\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5")
        buf.write("\u00e6\5\20\t\2\u00e6\u00e7\5(\25\2\u00e7\u00ea\3\2\2")
        buf.write("\2\u00e8\u00ea\5*\26\2\u00e9\u00e5\3\2\2\2\u00e9\u00e8")
        buf.write("\3\2\2\2\u00ea)\3\2\2\2\u00eb\u00ec\5\16\b\2\u00ec\u00ed")
        buf.write("\5*\26\2\u00ed\u00f0\3\2\2\2\u00ee\u00f0\5,\27\2\u00ef")
        buf.write("\u00eb\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0+\3\2\2\2\u00f1")
        buf.write("\u00f4\5\f\7\2\u00f2\u00f4\5.\30\2\u00f3\u00f1\3\2\2\2")
        buf.write("\u00f3\u00f2\3\2\2\2\u00f4-\3\2\2\2\u00f5\u0100\7\60\2")
        buf.write("\2\u00f6\u0100\7\61\2\2\u00f7\u0100\7/\2\2\u00f8\u0100")
        buf.write("\7\62\2\2\u00f9\u0100\5J&\2\u00fa\u0100\5\60\31\2\u00fb")
        buf.write("\u00fc\7\6\2\2\u00fc\u00fd\5\34\17\2\u00fd\u00fe\7\7\2")
        buf.write("\2\u00fe\u0100\3\2\2\2\u00ff\u00f5\3\2\2\2\u00ff\u00f6")
        buf.write("\3\2\2\2\u00ff\u00f7\3\2\2\2\u00ff\u00f8\3\2\2\2\u00ff")
        buf.write("\u00f9\3\2\2\2\u00ff\u00fa\3\2\2\2\u00ff\u00fb\3\2\2\2")
        buf.write("\u0100/\3\2\2\2\u0101\u0102\7\60\2\2\u0102\u0103\7\6\2")
        buf.write("\2\u0103\u0104\5r:\2\u0104\u0105\7\7\2\2\u0105\61\3\2")
        buf.write("\2\2\u0106\u0107\t\6\2\2\u0107\63\3\2\2\2\u0108\u010c")
        buf.write("\5\62\32\2\u0109\u010c\7\21\2\2\u010a\u010c\7\22\2\2\u010b")
        buf.write("\u0108\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2")
        buf.write("\u010c\65\3\2\2\2\u010d\u010f\58\35\2\u010e\u0110\7\13")
        buf.write("\2\2\u010f\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u010f")
        buf.write("\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0120\3\2\2\2\u0113")
        buf.write("\u0115\5B\"\2\u0114\u0116\7\13\2\2\u0115\u0114\3\2\2\2")
        buf.write("\u0116\u0117\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3")
        buf.write("\2\2\2\u0118\u0120\3\2\2\2\u0119\u011b\5N(\2\u011a\u011c")
        buf.write("\7\13\2\2\u011b\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d")
        buf.write("\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0120\3\2\2\2")
        buf.write("\u011f\u010d\3\2\2\2\u011f\u0113\3\2\2\2\u011f\u0119\3")
        buf.write("\2\2\2\u0120\67\3\2\2\2\u0121\u0125\5:\36\2\u0122\u0125")
        buf.write("\5<\37\2\u0123\u0125\5> \2\u0124\u0121\3\2\2\2\u0124\u0122")
        buf.write("\3\2\2\2\u0124\u0123\3\2\2\2\u01259\3\2\2\2\u0126\u0127")
        buf.write("\5\62\32\2\u0127\u0128\7\60\2\2\u0128\u0129\5@!\2\u0129")
        buf.write("\u012e\3\2\2\2\u012a\u012b\5\62\32\2\u012b\u012c\7\60")
        buf.write("\2\2\u012c\u012e\3\2\2\2\u012d\u0126\3\2\2\2\u012d\u012a")
        buf.write("\3\2\2\2\u012e;\3\2\2\2\u012f\u0130\7\22\2\2\u0130\u0131")
        buf.write("\7\60\2\2\u0131\u0135\5@!\2\u0132\u0133\7\22\2\2\u0133")
        buf.write("\u0135\7\60\2\2\u0134\u012f\3\2\2\2\u0134\u0132\3\2\2")
        buf.write("\2\u0135=\3\2\2\2\u0136\u0137\7\21\2\2\u0137\u0138\7\60")
        buf.write("\2\2\u0138\u0139\5@!\2\u0139?\3\2\2\2\u013a\u013b\7#\2")
        buf.write("\2\u013b\u013c\5\34\17\2\u013cA\3\2\2\2\u013d\u013e\5")
        buf.write("\62\32\2\u013e\u013f\5D#\2\u013f\u0140\5H%\2\u0140\u0145")
        buf.write("\3\2\2\2\u0141\u0142\5\62\32\2\u0142\u0143\5D#\2\u0143")
        buf.write("\u0145\3\2\2\2\u0144\u013d\3\2\2\2\u0144\u0141\3\2\2\2")
        buf.write("\u0145C\3\2\2\2\u0146\u0147\7\60\2\2\u0147\u0148\7\b\2")
        buf.write("\2\u0148\u0149\5F$\2\u0149\u014a\7\t\2\2\u014aE\3\2\2")
        buf.write("\2\u014b\u014c\7\61\2\2\u014c\u014d\7\n\2\2\u014d\u0150")
        buf.write("\5F$\2\u014e\u0150\7\61\2\2\u014f\u014b\3\2\2\2\u014f")
        buf.write("\u014e\3\2\2\2\u0150G\3\2\2\2\u0151\u0152\5@!\2\u0152")
        buf.write("I\3\2\2\2\u0153\u0154\7\b\2\2\u0154\u0155\5L\'\2\u0155")
        buf.write("\u0156\7\t\2\2\u0156K\3\2\2\2\u0157\u0158\5\34\17\2\u0158")
        buf.write("\u0159\7\n\2\2\u0159\u015a\5L\'\2\u015a\u015d\3\2\2\2")
        buf.write("\u015b\u015d\5\34\17\2\u015c\u0157\3\2\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015dM\3\2\2\2\u015e\u015f\7\23\2\2\u015f\u0160")
        buf.write("\7\60\2\2\u0160\u0161\7\6\2\2\u0161\u0162\5P)\2\u0162")
        buf.write("\u0166\7\7\2\2\u0163\u0165\7\13\2\2\u0164\u0163\3\2\2")
        buf.write("\2\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167")
        buf.write("\3\2\2\2\u0167\u0169\3\2\2\2\u0168\u0166\3\2\2\2\u0169")
        buf.write("\u016a\5V,\2\u016aO\3\2\2\2\u016b\u016c\5T+\2\u016c\u016d")
        buf.write("\5R*\2\u016d\u0170\3\2\2\2\u016e\u0170\3\2\2\2\u016f\u016b")
        buf.write("\3\2\2\2\u016f\u016e\3\2\2\2\u0170Q\3\2\2\2\u0171\u0172")
        buf.write("\7\n\2\2\u0172\u0173\5T+\2\u0173\u0174\5R*\2\u0174\u0177")
        buf.write("\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0171\3\2\2\2\u0176")
        buf.write("\u0175\3\2\2\2\u0177S\3\2\2\2\u0178\u0179\5\62\32\2\u0179")
        buf.write("\u017a\7\60\2\2\u017a\u017f\3\2\2\2\u017b\u017c\5\62\32")
        buf.write("\2\u017c\u017d\5D#\2\u017d\u017f\3\2\2\2\u017e\u0178\3")
        buf.write("\2\2\2\u017e\u017b\3\2\2\2\u017fU\3\2\2\2\u0180\u0184")
        buf.write("\5n8\2\u0181\u0184\5v<\2\u0182\u0184\3\2\2\2\u0183\u0180")
        buf.write("\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("W\3\2\2\2\u0185\u0187\58\35\2\u0186\u0188\7\13\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018a\u01b8\3\2\2\2\u018b\u018d\5")
        buf.write("B\"\2\u018c\u018e\7\13\2\2\u018d\u018c\3\2\2\2\u018e\u018f")
        buf.write("\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u01b8\3\2\2\2\u0191\u0193\5Z.\2\u0192\u0194\7\13\2\2")
        buf.write("\u0193\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0193\3")
        buf.write("\2\2\2\u0195\u0196\3\2\2\2\u0196\u01b8\3\2\2\2\u0197\u01b8")
        buf.write("\5d\63\2\u0198\u01b8\5h\65\2\u0199\u019b\5j\66\2\u019a")
        buf.write("\u019c\7\13\2\2\u019b\u019a\3\2\2\2\u019c\u019d\3\2\2")
        buf.write("\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01b8")
        buf.write("\3\2\2\2\u019f\u01a1\5l\67\2\u01a0\u01a2\7\13\2\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4\u01b8\3\2\2\2\u01a5\u01a7\5")
        buf.write("n8\2\u01a6\u01a8\7\13\2\2\u01a7\u01a6\3\2\2\2\u01a8\u01a9")
        buf.write("\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa")
        buf.write("\u01b8\3\2\2\2\u01ab\u01ad\5p9\2\u01ac\u01ae\7\13\2\2")
        buf.write("\u01ad\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b8\3\2\2\2\u01b1\u01b3")
        buf.write("\5v<\2\u01b2\u01b4\7\13\2\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write("\u01b5\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2")
        buf.write("\u01b6\u01b8\3\2\2\2\u01b7\u0185\3\2\2\2\u01b7\u018b\3")
        buf.write("\2\2\2\u01b7\u0191\3\2\2\2\u01b7\u0197\3\2\2\2\u01b7\u0198")
        buf.write("\3\2\2\2\u01b7\u0199\3\2\2\2\u01b7\u019f\3\2\2\2\u01b7")
        buf.write("\u01a5\3\2\2\2\u01b7\u01ab\3\2\2\2\u01b7\u01b1\3\2\2\2")
        buf.write("\u01b8Y\3\2\2\2\u01b9\u01ba\5\\/\2\u01ba\u01bb\5@!\2\u01bb")
        buf.write("[\3\2\2\2\u01bc\u01bf\7\60\2\2\u01bd\u01bf\5\6\4\2\u01be")
        buf.write("\u01bc\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf]\3\2\2\2\u01c0")
        buf.write("\u01c1\7\31\2\2\u01c1\u01c2\7\6\2\2\u01c2\u01c3\5\34\17")
        buf.write("\2\u01c3\u01c7\7\7\2\2\u01c4\u01c6\7\13\2\2\u01c5\u01c4")
        buf.write("\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7")
        buf.write("\u01c8\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01ca\u01cb\5X-\2\u01cb_\3\2\2\2\u01cc\u01cd\7\33\2\2")
        buf.write("\u01cd\u01ce\7\6\2\2\u01ce\u01cf\5\34\17\2\u01cf\u01d3")
        buf.write("\7\7\2\2\u01d0\u01d2\7\13\2\2\u01d1\u01d0\3\2\2\2\u01d2")
        buf.write("\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2")
        buf.write("\u01d4\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d7\5")
        buf.write("X-\2\u01d7a\3\2\2\2\u01d8\u01dc\7\32\2\2\u01d9\u01db\7")
        buf.write("\13\2\2\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2\2\u01dc")
        buf.write("\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2")
        buf.write("\u01de\u01dc\3\2\2\2\u01df\u01e2\5X-\2\u01e0\u01e2\3\2")
        buf.write("\2\2\u01e1\u01d8\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2c\3")
        buf.write("\2\2\2\u01e3\u01e7\5^\60\2\u01e4\u01e6\7\13\2\2\u01e5")
        buf.write("\u01e4\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2")
        buf.write("\u01e7\u01e8\3\2\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01e7\3")
        buf.write("\2\2\2\u01ea\u01eb\5f\64\2\u01eb\u01ec\5b\62\2\u01ece")
        buf.write("\3\2\2\2\u01ed\u01f1\5`\61\2\u01ee\u01f0\7\13\2\2\u01ef")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f3\3\2\2\2\u01f1\u01ef\3\2\2\2")
        buf.write("\u01f1\u01f2\3\2\2\2\u01f2\u01f4\3\2\2\2\u01f3\u01f1\3")
        buf.write("\2\2\2\u01f4\u01f5\5f\64\2\u01f5\u01f8\3\2\2\2\u01f6\u01f8")
        buf.write("\3\2\2\2\u01f7\u01ed\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8")
        buf.write("g\3\2\2\2\u01f9\u01fa\7\24\2\2\u01fa\u01fb\7\60\2\2\u01fb")
        buf.write("\u01fc\7\25\2\2\u01fc\u01fd\5\34\17\2\u01fd\u01fe\7\26")
        buf.write("\2\2\u01fe\u0202\5\34\17\2\u01ff\u0201\7\13\2\2\u0200")
        buf.write("\u01ff\3\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2")
        buf.write("\u0202\u0203\3\2\2\2\u0203\u0205\3\2\2\2\u0204\u0202\3")
        buf.write("\2\2\2\u0205\u0206\5X-\2\u0206i\3\2\2\2\u0207\u0208\7")
        buf.write("\27\2\2\u0208k\3\2\2\2\u0209\u020a\7\30\2\2\u020am\3\2")
        buf.write("\2\2\u020b\u020c\7\20\2\2\u020c\u020f\5\34\17\2\u020d")
        buf.write("\u020f\7\20\2\2\u020e\u020b\3\2\2\2\u020e\u020d\3\2\2")
        buf.write("\2\u020fo\3\2\2\2\u0210\u0211\7\60\2\2\u0211\u0212\7\6")
        buf.write("\2\2\u0212\u0213\5r:\2\u0213\u0214\7\7\2\2\u0214q\3\2")
        buf.write("\2\2\u0215\u0216\5\34\17\2\u0216\u0217\5t;\2\u0217\u021a")
        buf.write("\3\2\2\2\u0218\u021a\3\2\2\2\u0219\u0215\3\2\2\2\u0219")
        buf.write("\u0218\3\2\2\2\u021as\3\2\2\2\u021b\u021c\7\n\2\2\u021c")
        buf.write("\u021d\5\34\17\2\u021d\u021e\5t;\2\u021e\u0221\3\2\2\2")
        buf.write("\u021f\u0221\3\2\2\2\u0220\u021b\3\2\2\2\u0220\u021f\3")
        buf.write("\2\2\2\u0221u\3\2\2\2\u0222\u0224\7\34\2\2\u0223\u0225")
        buf.write("\7\13\2\2\u0224\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226")
        buf.write("\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0228\3\2\2\2")
        buf.write("\u0228\u0229\5x=\2\u0229\u022a\7\35\2\2\u022aw\3\2\2\2")
        buf.write("\u022b\u022c\5X-\2\u022c\u022d\5x=\2\u022d\u0230\3\2\2")
        buf.write("\2\u022e\u0230\3\2\2\2\u022f\u022b\3\2\2\2\u022f\u022e")
        buf.write("\3\2\2\2\u0230y\3\2\2\2\67\u0080\u0089\u008d\u0094\u009f")
        buf.write("\u00b8\u00bf\u00ca\u00d6\u00e2\u00e9\u00ef\u00f3\u00ff")
        buf.write("\u010b\u0111\u0117\u011d\u011f\u0124\u012d\u0134\u0144")
        buf.write("\u014f\u015c\u0166\u016f\u0176\u017e\u0183\u0189\u018f")
        buf.write("\u0195\u019d\u01a3\u01a9\u01af\u01b5\u01b7\u01be\u01c7")
        buf.write("\u01d3\u01dc\u01e1\u01e7\u01f1\u01f7\u0202\u020e\u0219")
        buf.write("\u0220\u0226\u022f")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "','", "<INVALID>", "'\\r'", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
                     "'break'", "'continue'", "'if'", "'else'", "'elif'", 
                     "'begin'", "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'<-'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'...'", "'=='", "'not'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "WS", "WS2", "SB_LEFTBRACKET", 
                      "SB_RIGHTBRACKET", "SB_LEFTSQUARE", "SB_RIGHTSQUARE", 
                      "SB_COMMA", "SB_NEWLINE", "SB_CR", "KW_NUMBER", "KW_BOOL", 
                      "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", 
                      "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", 
                      "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", 
                      "KW_END", "OP_PLUS", "OP_MINUS", "OP_MULT", "OP_DIV", 
                      "OP_MOD", "OP_ASSIGN", "OP_EQUAL_NUM", "OP_UNEQUAL", 
                      "OP_LESS", "OP_MORE", "OP_LESSOREQUAL", "OP_MOREOREQUAL", 
                      "OP_CONCAT", "OP_EQUAL_STR", "OP_NOT", "OP_AND", "OP_OR", 
                      "BOOL", "IDENTIFIER", "NUMBER", "STRING", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declarationLst = 1
    RULE_arrayElement = 2
    RULE_expr_element = 3
    RULE_op_index = 4
    RULE_op_unary_index = 5
    RULE_op_unary_sign = 6
    RULE_op_unary_logical = 7
    RULE_op_binary_multiplying = 8
    RULE_op_binary_adding = 9
    RULE_op_binary_logical = 10
    RULE_op_binary_relational = 11
    RULE_op_binary_string = 12
    RULE_expr = 13
    RULE_expr_string = 14
    RULE_expr_relational = 15
    RULE_expr_logical = 16
    RULE_expr_adding = 17
    RULE_expr_multiplying = 18
    RULE_expr_not = 19
    RULE_expr_sign = 20
    RULE_expr_index = 21
    RULE_operand = 22
    RULE_expr_func_call = 23
    RULE_kw_type_explicit = 24
    RULE_kw_type = 25
    RULE_stmt_declaration = 26
    RULE_stmt_var_declaration = 27
    RULE_stmt_var_declaration_explicit = 28
    RULE_stmt_var_declaration_dynamic = 29
    RULE_stmt_var_declaration_var = 30
    RULE_value_init = 31
    RULE_stmt_array_declaration = 32
    RULE_arrayId = 33
    RULE_arrayDim = 34
    RULE_array_init = 35
    RULE_arrayValue = 36
    RULE_exprLst = 37
    RULE_stmt_func_declaration = 38
    RULE_paramLst = 39
    RULE_paramLstTail = 40
    RULE_param = 41
    RULE_func_body = 42
    RULE_statement = 43
    RULE_stmt_assignment = 44
    RULE_assignment_lhs = 45
    RULE_if_statement = 46
    RULE_elif_statement = 47
    RULE_else_statement = 48
    RULE_stmt_if = 49
    RULE_elifLst = 50
    RULE_stmt_for = 51
    RULE_stmt_break = 52
    RULE_stmt_continue = 53
    RULE_stmt_return = 54
    RULE_stmt_func_call = 55
    RULE_argLst = 56
    RULE_argLstTail = 57
    RULE_stmt_block = 58
    RULE_statementLst = 59

    ruleNames =  [ "program", "declarationLst", "arrayElement", "expr_element", 
                   "op_index", "op_unary_index", "op_unary_sign", "op_unary_logical", 
                   "op_binary_multiplying", "op_binary_adding", "op_binary_logical", 
                   "op_binary_relational", "op_binary_string", "expr", "expr_string", 
                   "expr_relational", "expr_logical", "expr_adding", "expr_multiplying", 
                   "expr_not", "expr_sign", "expr_index", "operand", "expr_func_call", 
                   "kw_type_explicit", "kw_type", "stmt_declaration", "stmt_var_declaration", 
                   "stmt_var_declaration_explicit", "stmt_var_declaration_dynamic", 
                   "stmt_var_declaration_var", "value_init", "stmt_array_declaration", 
                   "arrayId", "arrayDim", "array_init", "arrayValue", "exprLst", 
                   "stmt_func_declaration", "paramLst", "paramLstTail", 
                   "param", "func_body", "statement", "stmt_assignment", 
                   "assignment_lhs", "if_statement", "elif_statement", "else_statement", 
                   "stmt_if", "elifLst", "stmt_for", "stmt_break", "stmt_continue", 
                   "stmt_return", "stmt_func_call", "argLst", "argLstTail", 
                   "stmt_block", "statementLst" ]

    EOF = Token.EOF
    COMMENT=1
    WS=2
    WS2=3
    SB_LEFTBRACKET=4
    SB_RIGHTBRACKET=5
    SB_LEFTSQUARE=6
    SB_RIGHTSQUARE=7
    SB_COMMA=8
    SB_NEWLINE=9
    SB_CR=10
    KW_NUMBER=11
    KW_BOOL=12
    KW_STRING=13
    KW_RETURN=14
    KW_VAR=15
    KW_DYNAMIC=16
    KW_FUNC=17
    KW_FOR=18
    KW_UNTIL=19
    KW_BY=20
    KW_BREAK=21
    KW_CONTINUE=22
    KW_IF=23
    KW_ELSE=24
    KW_ELIF=25
    KW_BEGIN=26
    KW_END=27
    OP_PLUS=28
    OP_MINUS=29
    OP_MULT=30
    OP_DIV=31
    OP_MOD=32
    OP_ASSIGN=33
    OP_EQUAL_NUM=34
    OP_UNEQUAL=35
    OP_LESS=36
    OP_MORE=37
    OP_LESSOREQUAL=38
    OP_MOREOREQUAL=39
    OP_CONCAT=40
    OP_EQUAL_STR=41
    OP_NOT=42
    OP_AND=43
    OP_OR=44
    BOOL=45
    IDENTIFIER=46
    NUMBER=47
    STRING=48
    ERROR_CHAR=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51

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

        def declarationLst(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationLstContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

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
            self.state = 120
            self.declarationLst()
            self.state = 121
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_declarationContext,0)


        def declarationLst(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationLstContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_declarationLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationLst" ):
                return visitor.visitDeclarationLst(self)
            else:
                return visitor.visitChildren(self)




    def declarationLst(self):

        localctx = ZCodeParser.DeclarationLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarationLst)
        self._la = 0 # Token type
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.SB_NEWLINE:
                    self.state = 123
                    self.match(ZCodeParser.SB_NEWLINE)
                    self.state = 128
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 129
                self.stmt_declaration()
                self.state = 130
                self.declarationLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.SB_NEWLINE:
                    self.state = 132
                    self.match(ZCodeParser.SB_NEWLINE)
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 138
                self.stmt_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expr_element(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_elementContext,0)


        def expr_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayElement" ):
                return visitor.visitArrayElement(self)
            else:
                return visitor.visitChildren(self)




    def arrayElement(self):

        localctx = ZCodeParser.ArrayElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arrayElement)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 142
                self.expr_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.expr_func_call()
                self.state = 144
                self.expr_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_LEFTSQUARE(self):
            return self.getToken(ZCodeParser.SB_LEFTSQUARE, 0)

        def op_index(self):
            return self.getTypedRuleContext(ZCodeParser.Op_indexContext,0)


        def SB_RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.SB_RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_element" ):
                return visitor.visitExpr_element(self)
            else:
                return visitor.visitChildren(self)




    def expr_element(self):

        localctx = ZCodeParser.Expr_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 149
            self.op_index()
            self.state = 150
            self.match(ZCodeParser.SB_RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def op_index(self):
            return self.getTypedRuleContext(ZCodeParser.Op_indexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_op_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_index" ):
                return visitor.visitOp_index(self)
            else:
                return visitor.visitChildren(self)




    def op_index(self):

        localctx = ZCodeParser.Op_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_op_index)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.expr()
                self.state = 153
                self.match(ZCodeParser.SB_COMMA)
                self.state = 154
                self.op_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_unary_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayElement(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayElementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_op_unary_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_unary_index" ):
                return visitor.visitOp_unary_index(self)
            else:
                return visitor.visitChildren(self)




    def op_unary_index(self):

        localctx = ZCodeParser.Op_unary_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_op_unary_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.arrayElement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_unary_signContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MINUS(self):
            return self.getToken(ZCodeParser.OP_MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_unary_sign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_unary_sign" ):
                return visitor.visitOp_unary_sign(self)
            else:
                return visitor.visitChildren(self)




    def op_unary_sign(self):

        localctx = ZCodeParser.Op_unary_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_op_unary_sign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ZCodeParser.OP_MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_unary_logicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_NOT(self):
            return self.getToken(ZCodeParser.OP_NOT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_unary_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_unary_logical" ):
                return visitor.visitOp_unary_logical(self)
            else:
                return visitor.visitChildren(self)




    def op_unary_logical(self):

        localctx = ZCodeParser.Op_unary_logicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_op_unary_logical)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(ZCodeParser.OP_NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_binary_multiplyingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MULT(self):
            return self.getToken(ZCodeParser.OP_MULT, 0)

        def OP_DIV(self):
            return self.getToken(ZCodeParser.OP_DIV, 0)

        def OP_MOD(self):
            return self.getToken(ZCodeParser.OP_MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_multiplying

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_binary_multiplying" ):
                return visitor.visitOp_binary_multiplying(self)
            else:
                return visitor.visitChildren(self)




    def op_binary_multiplying(self):

        localctx = ZCodeParser.Op_binary_multiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_op_binary_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.OP_MULT) | (1 << ZCodeParser.OP_DIV) | (1 << ZCodeParser.OP_MOD))) != 0)):
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


    class Op_binary_addingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_PLUS(self):
            return self.getToken(ZCodeParser.OP_PLUS, 0)

        def OP_MINUS(self):
            return self.getToken(ZCodeParser.OP_MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_binary_adding" ):
                return visitor.visitOp_binary_adding(self)
            else:
                return visitor.visitChildren(self)




    def op_binary_adding(self):

        localctx = ZCodeParser.Op_binary_addingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_op_binary_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.OP_PLUS or _la==ZCodeParser.OP_MINUS):
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


    class Op_binary_logicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_AND(self):
            return self.getToken(ZCodeParser.OP_AND, 0)

        def OP_OR(self):
            return self.getToken(ZCodeParser.OP_OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_binary_logical" ):
                return visitor.visitOp_binary_logical(self)
            else:
                return visitor.visitChildren(self)




    def op_binary_logical(self):

        localctx = ZCodeParser.Op_binary_logicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_op_binary_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.OP_AND or _la==ZCodeParser.OP_OR):
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


    class Op_binary_relationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_EQUAL_NUM(self):
            return self.getToken(ZCodeParser.OP_EQUAL_NUM, 0)

        def OP_EQUAL_STR(self):
            return self.getToken(ZCodeParser.OP_EQUAL_STR, 0)

        def OP_UNEQUAL(self):
            return self.getToken(ZCodeParser.OP_UNEQUAL, 0)

        def OP_LESS(self):
            return self.getToken(ZCodeParser.OP_LESS, 0)

        def OP_MORE(self):
            return self.getToken(ZCodeParser.OP_MORE, 0)

        def OP_LESSOREQUAL(self):
            return self.getToken(ZCodeParser.OP_LESSOREQUAL, 0)

        def OP_MOREOREQUAL(self):
            return self.getToken(ZCodeParser.OP_MOREOREQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_binary_relational" ):
                return visitor.visitOp_binary_relational(self)
            else:
                return visitor.visitChildren(self)




    def op_binary_relational(self):

        localctx = ZCodeParser.Op_binary_relationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_op_binary_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.OP_EQUAL_NUM) | (1 << ZCodeParser.OP_UNEQUAL) | (1 << ZCodeParser.OP_LESS) | (1 << ZCodeParser.OP_MORE) | (1 << ZCodeParser.OP_LESSOREQUAL) | (1 << ZCodeParser.OP_MOREOREQUAL) | (1 << ZCodeParser.OP_EQUAL_STR))) != 0)):
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


    class Op_binary_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_CONCAT(self):
            return self.getToken(ZCodeParser.OP_CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_binary_string" ):
                return visitor.visitOp_binary_string(self)
            else:
                return visitor.visitChildren(self)




    def op_binary_string(self):

        localctx = ZCodeParser.Op_binary_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_op_binary_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(ZCodeParser.OP_CONCAT)
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

        def expr_string(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_stringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.expr_string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_relationalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,i)


        def op_binary_string(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_stringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_string" ):
                return visitor.visitExpr_string(self)
            else:
                return visitor.visitChildren(self)




    def expr_string(self):

        localctx = ZCodeParser.Expr_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr_string)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.expr_relational()
                self.state = 178
                self.op_binary_string()
                self.state = 179
                self.expr_relational()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.expr_relational()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_relationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_logical(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_logicalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,i)


        def op_binary_relational(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_relationalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_relational" ):
                return visitor.visitExpr_relational(self)
            else:
                return visitor.visitChildren(self)




    def expr_relational(self):

        localctx = ZCodeParser.Expr_relationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr_relational)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.expr_logical(0)
                self.state = 185
                self.op_binary_relational()
                self.state = 186
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.expr_logical(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_logicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_adding(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_addingContext,0)


        def expr_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,0)


        def op_binary_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_logicalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_logical" ):
                return visitor.visitExpr_logical(self)
            else:
                return visitor.visitChildren(self)



    def expr_logical(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_logicalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr_logical, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.expr_adding(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_logicalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logical)
                    self.state = 194
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 195
                    self.op_binary_logical()
                    self.state = 196
                    self.expr_adding(0) 
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_addingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_multiplying(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_multiplyingContext,0)


        def expr_adding(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_addingContext,0)


        def op_binary_adding(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_addingContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_adding" ):
                return visitor.visitExpr_adding(self)
            else:
                return visitor.visitChildren(self)



    def expr_adding(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_addingContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr_adding, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.expr_multiplying(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_addingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_adding)
                    self.state = 206
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 207
                    self.op_binary_adding()
                    self.state = 208
                    self.expr_multiplying(0) 
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_multiplyingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_not(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_notContext,0)


        def expr_multiplying(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_multiplyingContext,0)


        def op_binary_multiplying(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_multiplyingContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_multiplying

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_multiplying" ):
                return visitor.visitExpr_multiplying(self)
            else:
                return visitor.visitChildren(self)



    def expr_multiplying(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_multiplyingContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr_multiplying, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.expr_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_multiplyingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_multiplying)
                    self.state = 218
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 219
                    self.op_binary_multiplying()
                    self.state = 220
                    self.expr_not() 
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op_unary_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Op_unary_logicalContext,0)


        def expr_not(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_notContext,0)


        def expr_sign(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_signContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_not

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_not" ):
                return visitor.visitExpr_not(self)
            else:
                return visitor.visitChildren(self)




    def expr_not(self):

        localctx = ZCodeParser.Expr_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr_not)
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.op_unary_logical()
                self.state = 228
                self.expr_not()
                pass
            elif token in [ZCodeParser.SB_LEFTBRACKET, ZCodeParser.SB_LEFTSQUARE, ZCodeParser.OP_MINUS, ZCodeParser.BOOL, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.expr_sign()
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


    class Expr_signContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op_unary_sign(self):
            return self.getTypedRuleContext(ZCodeParser.Op_unary_signContext,0)


        def expr_sign(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_signContext,0)


        def expr_index(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_indexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_sign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_sign" ):
                return visitor.visitExpr_sign(self)
            else:
                return visitor.visitChildren(self)




    def expr_sign(self):

        localctx = ZCodeParser.Expr_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr_sign)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.op_unary_sign()
                self.state = 234
                self.expr_sign()
                pass
            elif token in [ZCodeParser.SB_LEFTBRACKET, ZCodeParser.SB_LEFTSQUARE, ZCodeParser.BOOL, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.expr_index()
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


    class Expr_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op_unary_index(self):
            return self.getTypedRuleContext(ZCodeParser.Op_unary_indexContext,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_index" ):
                return visitor.visitExpr_index(self)
            else:
                return visitor.visitChildren(self)




    def expr_index(self):

        localctx = ZCodeParser.Expr_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr_index)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.op_unary_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.operand()
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def arrayValue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayValueContext,0)


        def expr_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_func_callContext,0)


        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_operand)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 247
                self.arrayValue()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 248
                self.expr_func_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 249
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 250
                self.expr()
                self.state = 251
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def argLst(self):
            return self.getTypedRuleContext(ZCodeParser.ArgLstContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_func_call" ):
                return visitor.visitExpr_func_call(self)
            else:
                return visitor.visitChildren(self)




    def expr_func_call(self):

        localctx = ZCodeParser.Expr_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 256
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 257
            self.argLst()
            self.state = 258
            self.match(ZCodeParser.SB_RIGHTBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kw_type_explicitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_NUMBER(self):
            return self.getToken(ZCodeParser.KW_NUMBER, 0)

        def KW_BOOL(self):
            return self.getToken(ZCodeParser.KW_BOOL, 0)

        def KW_STRING(self):
            return self.getToken(ZCodeParser.KW_STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_kw_type_explicit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKw_type_explicit" ):
                return visitor.visitKw_type_explicit(self)
            else:
                return visitor.visitChildren(self)




    def kw_type_explicit(self):

        localctx = ZCodeParser.Kw_type_explicitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_kw_type_explicit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING))) != 0)):
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


    class Kw_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_type_explicitContext,0)


        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def KW_DYNAMIC(self):
            return self.getToken(ZCodeParser.KW_DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_kw_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKw_type" ):
                return visitor.visitKw_type(self)
            else:
                return visitor.visitChildren(self)




    def kw_type(self):

        localctx = ZCodeParser.Kw_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_kw_type)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.kw_type_explicit()
                pass
            elif token in [ZCodeParser.KW_VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(ZCodeParser.KW_VAR)
                pass
            elif token in [ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
                self.match(ZCodeParser.KW_DYNAMIC)
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


    class Stmt_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declarationContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def stmt_array_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_array_declarationContext,0)


        def stmt_func_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_declaration" ):
                return visitor.visitStmt_declaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_declaration(self):

        localctx = ZCodeParser.Stmt_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt_declaration)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.stmt_var_declaration()
                self.state = 269 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 268
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 271 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.stmt_array_declaration()
                self.state = 275 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 274
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 277 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.stmt_func_declaration()
                self.state = 281 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 280
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 283 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_declaration_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declaration_explicitContext,0)


        def stmt_var_declaration_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declaration_dynamicContext,0)


        def stmt_var_declaration_var(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declaration_varContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_declaration" ):
                return visitor.visitStmt_var_declaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_var_declaration(self):

        localctx = ZCodeParser.Stmt_var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt_var_declaration)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.stmt_var_declaration_explicit()
                pass
            elif token in [ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.stmt_var_declaration_dynamic()
                pass
            elif token in [ZCodeParser.KW_VAR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 289
                self.stmt_var_declaration_var()
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


    class Stmt_var_declaration_explicitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_type_explicitContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration_explicit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_declaration_explicit" ):
                return visitor.visitStmt_var_declaration_explicit(self)
            else:
                return visitor.visitChildren(self)




    def stmt_var_declaration_explicit(self):

        localctx = ZCodeParser.Stmt_var_declaration_explicitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt_var_declaration_explicit)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.kw_type_explicit()
                self.state = 293
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 294
                self.value_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.kw_type_explicit()
                self.state = 297
                self.match(ZCodeParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_declaration_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DYNAMIC(self):
            return self.getToken(ZCodeParser.KW_DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration_dynamic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_declaration_dynamic" ):
                return visitor.visitStmt_var_declaration_dynamic(self)
            else:
                return visitor.visitChildren(self)




    def stmt_var_declaration_dynamic(self):

        localctx = ZCodeParser.Stmt_var_declaration_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt_var_declaration_dynamic)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 302
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 303
                self.value_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 305
                self.match(ZCodeParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_declaration_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_declaration_var" ):
                return visitor.visitStmt_var_declaration_var(self)
            else:
                return visitor.visitChildren(self)




    def stmt_var_declaration_var(self):

        localctx = ZCodeParser.Stmt_var_declaration_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stmt_var_declaration_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(ZCodeParser.KW_VAR)
            self.state = 309
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 310
            self.value_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ASSIGN(self):
            return self.getToken(ZCodeParser.OP_ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_value_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_init" ):
                return visitor.visitValue_init(self)
            else:
                return visitor.visitChildren(self)




    def value_init(self):

        localctx = ZCodeParser.Value_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 313
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_array_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_type_explicitContext,0)


        def arrayId(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayIdContext,0)


        def array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_array_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_array_declaration" ):
                return visitor.visitStmt_array_declaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_array_declaration(self):

        localctx = ZCodeParser.Stmt_array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_stmt_array_declaration)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.kw_type_explicit()
                self.state = 316
                self.arrayId()
                self.state = 317
                self.array_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.kw_type_explicit()
                self.state = 320
                self.arrayId()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def SB_LEFTSQUARE(self):
            return self.getToken(ZCodeParser.SB_LEFTSQUARE, 0)

        def arrayDim(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDimContext,0)


        def SB_RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.SB_RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayId

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayId" ):
                return visitor.visitArrayId(self)
            else:
                return visitor.visitChildren(self)




    def arrayId(self):

        localctx = ZCodeParser.ArrayIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arrayId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 325
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 326
            self.arrayDim()
            self.state = 327
            self.match(ZCodeParser.SB_RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def arrayDim(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDimContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayDim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDim" ):
                return visitor.visitArrayDim(self)
            else:
                return visitor.visitChildren(self)




    def arrayDim(self):

        localctx = ZCodeParser.ArrayDimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_arrayDim)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.match(ZCodeParser.NUMBER)
                self.state = 330
                self.match(ZCodeParser.SB_COMMA)
                self.state = 331
                self.arrayDim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.match(ZCodeParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_init" ):
                return visitor.visitArray_init(self)
            else:
                return visitor.visitChildren(self)




    def array_init(self):

        localctx = ZCodeParser.Array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_array_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.value_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_LEFTSQUARE(self):
            return self.getToken(ZCodeParser.SB_LEFTSQUARE, 0)

        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def SB_RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.SB_RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayValue" ):
                return visitor.visitArrayValue(self)
            else:
                return visitor.visitChildren(self)




    def arrayValue(self):

        localctx = ZCodeParser.ArrayValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arrayValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 338
            self.exprLst()
            self.state = 339
            self.match(ZCodeParser.SB_RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLst" ):
                return visitor.visitExprLst(self)
            else:
                return visitor.visitChildren(self)




    def exprLst(self):

        localctx = ZCodeParser.ExprLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exprLst)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.expr()
                self.state = 342
                self.match(ZCodeParser.SB_COMMA)
                self.state = 343
                self.exprLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_func_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNC(self):
            return self.getToken(ZCodeParser.KW_FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def paramLst(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def func_body(self):
            return self.getTypedRuleContext(ZCodeParser.Func_bodyContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_func_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func_declaration" ):
                return visitor.visitStmt_func_declaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_func_declaration(self):

        localctx = ZCodeParser.Stmt_func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_stmt_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(ZCodeParser.KW_FUNC)
            self.state = 349
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 350
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 351
            self.paramLst()
            self.state = 352
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 356
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 353
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 358
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 359
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def paramLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamLst" ):
                return visitor.visitParamLst(self)
            else:
                return visitor.visitChildren(self)




    def paramLst(self):

        localctx = ZCodeParser.ParamLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_paramLst)
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.param()
                self.state = 362
                self.paramLstTail()
                pass
            elif token in [ZCodeParser.SB_RIGHTBRACKET]:
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


    class ParamLstTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def paramLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramLstTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamLstTail" ):
                return visitor.visitParamLstTail(self)
            else:
                return visitor.visitChildren(self)




    def paramLstTail(self):

        localctx = ZCodeParser.ParamLstTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_paramLstTail)
        try:
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(ZCodeParser.SB_COMMA)
                self.state = 368
                self.param()
                self.state = 369
                self.paramLstTail()
                pass
            elif token in [ZCodeParser.SB_RIGHTBRACKET]:
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


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_type_explicitContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arrayId(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayIdContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_param)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.kw_type_explicit()
                self.state = 375
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.kw_type_explicit()
                self.state = 378
                self.arrayId()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_return(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_returnContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = ZCodeParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_func_body)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.stmt_return()
                pass
            elif token in [ZCodeParser.KW_BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.stmt_block()
                pass
            elif token in [ZCodeParser.SB_NEWLINE]:
                self.enterOuterAlt(localctx, 3)

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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declarationContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def stmt_array_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_array_declarationContext,0)


        def stmt_assignment(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_assignmentContext,0)


        def stmt_if(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_ifContext,0)


        def stmt_for(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_forContext,0)


        def stmt_break(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_breakContext,0)


        def stmt_continue(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_continueContext,0)


        def stmt_return(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_returnContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_statement)
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.stmt_var_declaration()
                self.state = 389 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 388
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 391 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.stmt_array_declaration()
                self.state = 395 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 394
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 397 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.stmt_assignment()
                self.state = 401 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 400
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 403 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 405
                self.stmt_if()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 406
                self.stmt_for()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 407
                self.stmt_break()
                self.state = 409 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 408
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 411 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 413
                self.stmt_continue()
                self.state = 415 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 414
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 417 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 419
                self.stmt_return()
                self.state = 421 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 420
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 423 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 425
                self.stmt_func_call()
                self.state = 427 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 426
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 429 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 431
                self.stmt_block()
                self.state = 433 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 432
                        self.match(ZCodeParser.SB_NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 435 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_lhs(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_lhsContext,0)


        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_assignment" ):
                return visitor.visitStmt_assignment(self)
            else:
                return visitor.visitChildren(self)




    def stmt_assignment(self):

        localctx = ZCodeParser.Stmt_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_stmt_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.assignment_lhs()
            self.state = 440
            self.value_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arrayElement(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayElementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_lhs" ):
                return visitor.visitAssignment_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assignment_lhs(self):

        localctx = ZCodeParser.Assignment_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_assignment_lhs)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.arrayElement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IF(self):
            return self.getToken(ZCodeParser.KW_IF, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(ZCodeParser.KW_IF)
            self.state = 447
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 448
            self.expr()
            self.state = 449
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.SB_NEWLINE:
                self.state = 450
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 455
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 456
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELIF(self):
            return self.getToken(ZCodeParser.KW_ELIF, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_elif_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(ZCodeParser.KW_ELIF)
            self.state = 459
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 460
            self.expr()
            self.state = 461
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.SB_NEWLINE:
                self.state = 462
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 468
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELSE(self):
            return self.getToken(ZCodeParser.KW_ELSE, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.match(ZCodeParser.KW_ELSE)
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.SB_NEWLINE:
                    self.state = 471
                    self.match(ZCodeParser.SB_NEWLINE)
                    self.state = 476
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 477
                self.statement()
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


    class Stmt_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def elifLst(self):
            return self.getTypedRuleContext(ZCodeParser.ElifLstContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_if" ):
                return visitor.visitStmt_if(self)
            else:
                return visitor.visitChildren(self)




    def stmt_if(self):

        localctx = ZCodeParser.Stmt_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.if_statement()
            self.state = 485
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 482
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 487
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 488
            self.elifLst()
            self.state = 489
            self.else_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statementContext,0)


        def elifLst(self):
            return self.getTypedRuleContext(ZCodeParser.ElifLstContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elifLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifLst" ):
                return visitor.visitElifLst(self)
            else:
                return visitor.visitChildren(self)




    def elifLst(self):

        localctx = ZCodeParser.ElifLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_elifLst)
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.elif_statement()
                self.state = 495
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 492
                        self.match(ZCodeParser.SB_NEWLINE) 
                    self.state = 497
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

                self.state = 498
                self.elifLst()
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


    class Stmt_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FOR(self):
            return self.getToken(ZCodeParser.KW_FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def KW_UNTIL(self):
            return self.getToken(ZCodeParser.KW_UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def KW_BY(self):
            return self.getToken(ZCodeParser.KW_BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_for" ):
                return visitor.visitStmt_for(self)
            else:
                return visitor.visitChildren(self)




    def stmt_for(self):

        localctx = ZCodeParser.Stmt_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_stmt_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(ZCodeParser.KW_FOR)
            self.state = 504
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 505
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 506
            self.expr()
            self.state = 507
            self.match(ZCodeParser.KW_BY)
            self.state = 508
            self.expr()
            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.SB_NEWLINE:
                self.state = 509
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 515
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_breakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BREAK(self):
            return self.getToken(ZCodeParser.KW_BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_break

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_break" ):
                return visitor.visitStmt_break(self)
            else:
                return visitor.visitChildren(self)




    def stmt_break(self):

        localctx = ZCodeParser.Stmt_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(ZCodeParser.KW_BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_continueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CONTINUE(self):
            return self.getToken(ZCodeParser.KW_CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_continue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_continue" ):
                return visitor.visitStmt_continue(self)
            else:
                return visitor.visitChildren(self)




    def stmt_continue(self):

        localctx = ZCodeParser.Stmt_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(ZCodeParser.KW_CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_RETURN(self):
            return self.getToken(ZCodeParser.KW_RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_return" ):
                return visitor.visitStmt_return(self)
            else:
                return visitor.visitChildren(self)




    def stmt_return(self):

        localctx = ZCodeParser.Stmt_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_stmt_return)
        try:
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.match(ZCodeParser.KW_RETURN)
                self.state = 522
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 523
                self.match(ZCodeParser.KW_RETURN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def argLst(self):
            return self.getTypedRuleContext(ZCodeParser.ArgLstContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func_call" ):
                return visitor.visitStmt_func_call(self)
            else:
                return visitor.visitChildren(self)




    def stmt_func_call(self):

        localctx = ZCodeParser.Stmt_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_stmt_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 527
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 528
            self.argLst()
            self.state = 529
            self.match(ZCodeParser.SB_RIGHTBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def argLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ArgLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgLst" ):
                return visitor.visitArgLst(self)
            else:
                return visitor.visitChildren(self)




    def argLst(self):

        localctx = ZCodeParser.ArgLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_argLst)
        try:
            self.state = 535
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_LEFTBRACKET, ZCodeParser.SB_LEFTSQUARE, ZCodeParser.OP_MINUS, ZCodeParser.OP_NOT, ZCodeParser.BOOL, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.expr()
                self.state = 532
                self.argLstTail()
                pass
            elif token in [ZCodeParser.SB_RIGHTBRACKET]:
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


    class ArgLstTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def argLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ArgLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argLstTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgLstTail" ):
                return visitor.visitArgLstTail(self)
            else:
                return visitor.visitChildren(self)




    def argLstTail(self):

        localctx = ZCodeParser.ArgLstTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_argLstTail)
        try:
            self.state = 542
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.match(ZCodeParser.SB_COMMA)
                self.state = 538
                self.expr()
                self.state = 539
                self.argLstTail()
                pass
            elif token in [ZCodeParser.SB_RIGHTBRACKET]:
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


    class Stmt_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BEGIN(self):
            return self.getToken(ZCodeParser.KW_BEGIN, 0)

        def statementLst(self):
            return self.getTypedRuleContext(ZCodeParser.StatementLstContext,0)


        def KW_END(self):
            return self.getToken(ZCodeParser.KW_END, 0)

        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = ZCodeParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_stmt_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 546 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 545
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 548 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.SB_NEWLINE):
                    break

            self.state = 550
            self.statementLst()
            self.state = 551
            self.match(ZCodeParser.KW_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statementLst(self):
            return self.getTypedRuleContext(ZCodeParser.StatementLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statementLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementLst" ):
                return visitor.visitStatementLst(self)
            else:
                return visitor.visitChildren(self)




    def statementLst(self):

        localctx = ZCodeParser.StatementLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_statementLst)
        try:
            self.state = 557
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING, ZCodeParser.KW_RETURN, ZCodeParser.KW_VAR, ZCodeParser.KW_DYNAMIC, ZCodeParser.KW_FOR, ZCodeParser.KW_BREAK, ZCodeParser.KW_CONTINUE, ZCodeParser.KW_IF, ZCodeParser.KW_BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                self.statement()
                self.state = 554
                self.statementLst()
                pass
            elif token in [ZCodeParser.KW_END]:
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expr_logical_sempred
        self._predicates[17] = self.expr_adding_sempred
        self._predicates[18] = self.expr_multiplying_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_logical_sempred(self, localctx:Expr_logicalContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_adding_sempred(self, localctx:Expr_addingContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_multiplying_sempred(self, localctx:Expr_multiplyingContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




