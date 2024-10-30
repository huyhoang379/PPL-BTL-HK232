import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_00(self):
        input = """ true """
        expect = "true,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,100))
    
    def test_01(self):
        input = """ false """
        expect = "false,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,101))
        
    def test_02(self):
        input = """ number """
        expect = "number,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,102))
        
    def test_03(self):
        input = """ bool """
        expect = "bool,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,103))
        
    def test_04(self):
        input = """ string """
        expect = "string,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,104))
        
    def test_05(self):
        input = """ return """
        expect = "return,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,105))
        
    def test_06(self):
        input = """ var """
        expect = "var,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,106))
        
    def test_07(self):
        input = """ dynamic """
        expect = "dynamic,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,107))
        
    def test_08(self):
        input = """ func """
        expect = "func,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,108))
        
    def test_09(self):
        input = """ until """
        expect = "until,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,109))
        
    def test_010(self):
        input = """ by """
        expect = "by,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,110))
        
    def test_11(self):
        input = """ break """
        expect = "break,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,111))
        
    def test_12(self):
        input = """ continue """
        expect = "continue,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))
        
    def test_13(self):
        input = """ if """
        expect = "if,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,113))
        
    def test_14(self):
        input = """ else """
        expect = "else,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,114))
        
    def test_15(self):
        input = """ elif """
        expect = "elif,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,115))
    
    def test_16(self):
        input = """ begin """
        expect = "begin,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,116))
        
    def test_17(self):
        input = """ end """
        expect = "end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,117))
        
    def test_18(self):
        input = """ not """
        expect = "not,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,118))
        
    def test_19(self):
        input = """ and """
        expect = "and,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,119))
        
    def test_20(self):
        input = """ or """
        expect = "or,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,120))
        
    def test_21(self):
        input = """ + """
        expect = "+,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,121))
        
    def test_22(self):
        input = """ - """
        expect = "-,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,122))
        
    def test_23(self):
        input = """ * """
        expect = "*,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,123))
        
    def test_24(self):
        input = """ / """
        expect = "/,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,124))
        
    def test_25(self):
        input = """ % """
        expect = "%,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,125))
    
    def test_26(self):
        input = """ = """
        expect = "=,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,126))
        
    def test_27(self):
        input = """ <- """
        expect = "<-,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,127))
        
    def test_28(self):
        input = """ != """
        expect = "!=,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,128))
        
    def test_29(self):
        input = """ < """
        expect = "<,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,129))
        
    def test_30(self):
        input = """ <= """
        expect = "<=,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,130))
        
    def test_31(self):
        input = """ > """
        expect = ">,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,131))
        
    def test_32(self):
        input = """ >= """
        expect = ">=,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,132))
        
    def test_33(self):
        input = """ ... """
        expect = "...,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,133))
        
    def test_34(self):
        input = """ == """
        expect = "==,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,134))
        
    def test_35(self):
        input = """ ( """
        expect = "(,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,135))
        
    def test_36(self):
        input = """ ) """
        expect = "),<EOF>"
        self.assertTrue(TestLexer.test(input,expect,136))
        
    def test_37(self):
        input = """ () """
        expect = "(,),<EOF>"
        self.assertTrue(TestLexer.test(input,expect,137))
        
    def test_38(self):
        input = """ [ """
        expect = "[,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,138))
        
    def test_39(self):
        input = """ [] """
        expect = "[,],<EOF>"
        self.assertTrue(TestLexer.test(input,expect,139))
        
    def test_40(self):
        input = """ \n """
        expect = "\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,140))
        
    def test_41(self):
        input = """ , """
        expect = ",,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,141))
    
    def test_42(self):
        input = """ 0 """
        expect = "0,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,142))
        
    def test_43(self):
        input = """ 199 """
        expect = "199,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,143))
        
    def test_44(self):
        input = """ 12. """
        expect = "12.,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,144))
        
    def test_45(self):
        input = """ 12.3 """
        expect = "12.3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,145))
        
    def test_46(self):
        input = """ 12.3e3 """
        expect = "12.3e3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,146))
        
    def test_47(self):
        input = """ 12e3 """
        expect = "12e3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,147))
        
    def test_48(self):
        input = """ 12.3e-30 """
        expect = "12.3e-30,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,148))
        
    def test_49(self):
        input = """ "This is a string containing tab \\t" """
        expect = "This is a string containing tab \\t,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,149))
        
    def test_50(self):
        input = """ "He asked me: '\"Where is John?'\"" """
        expect = "He asked me: '\"Where is John?'\",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,150))
        
    def test_51(self):
        input = "abc\t"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,151))
        
    def test_52(self):
        input = "1234567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,152))
        
    def test_53(self):
        input = "1234.567"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,153))
        
    def test_54(self):
        input = """func main() return 1
        """
        expect = "func,main,(,),return,1,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,154))
        
    def test_55(self):
        input = """func main() begin
        end
        """
        expect = "func,main,(,),begin,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,155))
        
    def test_56(self):
        input =""" true false number bool string
        return var dynamic func
        for until by break continue
        if else elif begin end
        not and or """
        expect = "true,false,number,bool,string,\n,return,var,dynamic,func,\n,for,until,by,break,continue,\n,if,else,elif,begin,end,\n,not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,156))
        
    def test_57(self):
        input = """ + - * / %
        not and or = <-
        != < <= > >=
        ... == """
        expect = "+,-,*,/,%,\n,not,and,or,=,<-,\n,!=,<,<=,>,>=,\n,...,==,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,157))
        
    def test_58(self):
        input = """ ## This is a single comment.
        a <- 5 """
        expect = "\n,a,<-,5,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,158))
        
    def test_59(self):
        input = """   """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,159))
        
    def test_60(self):
        input = """ \t """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,160))
        
    def test_61(self):
        input = """ \b """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,161))
        
    def test_62(self):
        input = """ \f """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,162))
        
    def test_63(self):
        input = """ ( ) [ ] , \n"""
        expect = "(,),[,],,,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,163))
        
    def test_64(self):
        input = """ "Hello \\ \" """
        expect = "Illegal Escape In String: Hello \\ "
        self.assertTrue(TestLexer.test(input,expect,164))
        
    def test_65(self):
        input = """ "This is test \\t" """
        expect = "This is test \\t,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,165))
        
    def test_66(self):
        input = """ "He asked me: '\" """
        expect = "Unclosed String: He asked me: '\" "
        self.assertTrue(TestLexer.test(input,expect,166))
        
    def test_67(self):
        input = """ .01 """
        expect = "Error Token ."
        self.assertTrue(TestLexer.test(input,expect,167))
        
    def test_68(self):
        input = """ "" """
        expect = ",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,168))
        
    def test_69(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,169))
        
    def test_70(self):
        input = "abc a12"
        expect = "abc,a12,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,170))
        
    def test_71(self):
        input = "abc A12"
        expect = "abc,A12,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,171))
        
    def test_72(self):
        input = "abc?svn"
        expect = "abc,Error Token ?"
        self.assertTrue(TestLexer.test(input,expect,172))
        
    def test_73(self):
        input = "0a12"
        expect = "0,a12,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,173))
        
    def test_74(self):
        input = "1.0"
        expect = "1.0,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,174))
        
    def test_75(self):
        input = "1e-12"
        expect = "1e-12,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,175))
        
    def test_76(self):
        input = "1.0e-12"
        expect = "1.0e-12,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,176))
        
    def test_77(self):
        input = "0.001"
        expect = "0.001,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,177))
        
    def test_78(self):
        input = "'0.01'"
        expect = "Error Token '"
        self.assertTrue(TestLexer.test(input,expect,178))
        
    def test_79(self):
        input = "1.0e"
        expect = "1.0,e,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,179))
        
    def test_80(self):
        input = "0e123"
        expect = "0e123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,180))
        
    def test_81(self):
        input = ".e123"
        expect = "Error Token ."
        self.assertTrue(TestLexer.test(input,expect,181))
        
    def test_82(self):
        input = "e123"
        expect = "e123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,182))
        
    def test_83(self):
        input = """ "' \\b \\f \\r \\n \\t \\\\ Huy \\b \\f \\r \\n \\t \\\\ Hoang \\b \\f \\r \\n \\t \\\\" """
        expect = "' \\b \\f \\r \\n \\t \\\\ Huy \\b \\f \\r \\n \\t \\\\ Hoang \\b \\f \\r \\n \\t \\\\,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,183))
        
    def test_84(self):
        input = "B _ b bz BZ bZ _b b_ b1 _1 B1"
        expect = "B,_,b,bz,BZ,bZ,_b,b_,b1,_1,B1,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,184))
        
    def test_85(self):
        input = "0 -0 999 000 123. 45. 6. 78.9 78.9e9 12.3e-45 6.e7 8.e-90 26e+3 20e-03 24e+02 20e-03"
        expect = "0,-,0,999,000,123.,45.,6.,78.9,78.9e9,12.3e-45,6.e7,8.e-90,26e+3,20e-03,24e+02,20e-03,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,185))
        
    def test_86(self):
        input = "h#"
        expect = "h,Error Token #"
        self.assertTrue(TestLexer.test(input,expect,186))
        
    def test_87(self):
        input = "h##1"
        expect = "h,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,187))
        
    def test_88(self):
        input = "####"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,188))
        
    def test_89(self):
        input = "## Huy Hoang"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,189))
        
    def test_90(self):
        input = ";"
        expect = "Error Token ;"
        self.assertTrue(TestLexer.test(input,expect,190))
        
    def test_91(self):
        input = "{"
        expect = "Error Token {"
        self.assertTrue(TestLexer.test(input,expect,191))
        
    def test_92(self):
        input = """ "Hoang \\" """
        expect = "Illegal Escape In String: Hoang \\\""
        self.assertTrue(TestLexer.test(input,expect,192))
        
    def test_93(self):
        input = """ "Hoang \t \n" """
        expect = "Unclosed String: Hoang 	 "
        self.assertTrue(TestLexer.test(input,expect,193))
        
    def test_94(self):
        input = """ "Hoang \\" """
        expect = "Illegal Escape In String: Hoang \\\""
        self.assertTrue(TestLexer.test(input,expect,194))
        
    def test_95(self):
        input = """ "Hoang 
        " """
        expect = "Unclosed String: Hoang "
        self.assertTrue(TestLexer.test(input,expect,195))
        
    def test_96(self):
        input = """ "Hoang \\\'" " """
        expect = "Hoang \\',Unclosed String:  "
        self.assertTrue(TestLexer.test(input,expect,196))
        
    def test_97(self):
        input = """ "Hoang \'" " """
        expect = "Hoang '\" ,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,197))
        
    def test_98(self):
        input = """ "Hoang '\\ """
        expect = "Illegal Escape In String: Hoang '\\ "
        self.assertTrue(TestLexer.test(input,expect,198))
        
    def test_99(self):
        input = """ "Hoang \\\n """
        expect = "Illegal Escape In String: Hoang \\\n"
        self.assertTrue(TestLexer.test(input,expect,199))
        
#     def test_100(self):
#         input = """
#             func main() begin
#         bool _b[1] <- [true]
#         number a[2,2] <- [[1,2],[3,4]]
#         a[1,1] <- a[1,2]
# end
#         """
#         expect = "Illegal Escape In String: Hoang \\\n"
#         self.assertTrue(TestLexer.test(input,expect,0))