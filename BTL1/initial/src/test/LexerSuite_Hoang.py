import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # def test_simple_string(self):
    #     """test simple string"""
    #     self.assertTrue(TestLexer.test("'Yanxi Palace - 2018'","'Yanxi Palace - 2018',<EOF>",101))

    # def test_complex_string(self):
    #     """test complex string"""
    #     self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))
    
    def test_1(self):
        input = """ "Vo \\n" """
        expect = "Vo \\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,101))
        
    def test_3(self):
        input = "abc\t"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,103))
        
    def test_4(self):
        input = "1234567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,104))
        
    def test_5(self):
        input = "1234.567"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,105))
        
    def test_6(self):
        input = """ "He asked me: '\"Where is John?'\"" """
        expect = "He asked me: '\"Where is John?'\",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,106))
        
    def test_7(self):
        input = """ "Hello \\ \" """
        expect = "Illegal Escape In String: Hello \\ "
        self.assertTrue(TestLexer.test(input,expect,107))
        
    def test_8(self):
        input = """ "This is test \\t" """
        expect = "This is test \\t,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,108))
        
    def test_9(self):
        input = """ "He asked me: '\" """
        expect = "Unclosed String: He asked me: '\" "
        self.assertTrue(TestLexer.test(input,expect,109))
        
    def test_KeyWord_Operators_Separators(self):
        """test KeyWord Op# https://www.facebook.com/groups/211867931379013
# https://www.facebook.com/groups/211867931379013
# https://www.facebook.com/groups/211867931379013
# https://www.facebook.com/groups/211867931379013   erators Separators"""
        
        ##^ test KeyWord
        input = "true false number bool string return var dynamic func for until by break continue if else elif begin end not and or"
        expect = "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,101))
        
        ##^ test Operators
        input = "+-*/%= <- != < <= > >= ... =="
        expect = "+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,102))

        
    def test_Identifiers(self):
        """test Identifiers"""
        ##^ test true ID
        self.assertTrue(TestLexer.test("A _ a az AZ aZ _a a_ a1 _1 A1", "A,_,a,az,AZ,aZ,_a,a_,a1,_1,A1,<EOF>", 106))     

        ##^ test false ID
        self.assertTrue(TestLexer.test("1Tienc", "1,Tienc,<EOF>", 107))
        self.assertTrue(TestLexer.test("11Tienc", "11,Tienc,<EOF>", 108))
        
    def test_Literal(self):
        """test Identifiers"""   
        
        ##^ test NUMBER_LIT    
        input = "0 -0 199 001 012. 12. 0. 12.3 12.3e3 12.3e-30 2.e3 0.e-30 31e+3 31e-3 0e+3 0e-3"
        expect = "0,-,0,199,001,012.,12.,0.,12.3,12.3e3,12.3e-30,2.e3,0.e-30,31e+3,31e-3,0e+3,0e-3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,109))
        ##^ fail NUMBER_LIT
        self.assertTrue(TestLexer.test(".12e-3","Error Token .",110))
        self.assertTrue(TestLexer.test("12.2h-3","12.2,h,-,3,<EOF>",111))
        
        ##^ test STRING_LIT 
        input = """ "Vo  Tien" """ # kiểm tra bình thường
        expect = "Vo  Tien,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))
        self.assertTrue(TestLexer.test(""" "" """,",<EOF>",113)) # chuỗi rỗng
        
        ##^ kiểm tra các kí tự cho phép
        input = """ "' \\b \\f \\r \\n \\t \\\\ Vo \\b \\f \\r \\n \\t \\\\  Tien \\b \\f \\r \\n \\t \\\\" """
        expect = "' \\b \\f \\r \\n \\t \\\\ Vo \\b \\f \\r \\n \\t \\\\  Tien \\b \\f \\r \\n \\t \\\\,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,114))
        self.assertTrue(TestLexer.test(""" "'"Vo '" Tien '' '"" ""","'\"Vo '\" Tien '' '\",<EOF>",115))
        
        ##^ kiểm tra lỗi Unclosed String
        self.assertTrue(TestLexer.test(""" "Vo \n" """, "Unclosed String: Vo ", 116))
        self.assertTrue(TestLexer.test(""" "Vo \n Tien" """, "Unclosed String: Vo ", 117))
        self.assertTrue(TestLexer.test(""" "Vo  """, "Unclosed String: Vo  ", 118))
        self.assertTrue(TestLexer.test(""" "Vo \\n \n """, "Unclosed String: Vo \\n ", 119))
        self.assertTrue(TestLexer.test(""" "Vo ' \\n \\b """, "Unclosed String: Vo ' \\n \\b ", 120))
        
        ##^ kiểm tra lỗi Illegal Escape
        self.assertTrue(TestLexer.test(""" "Tien ' \\1  """, "Illegal Escape In String: Tien ' \\1", 123))
        self.assertTrue(TestLexer.test(""" "Tien \\2 \\n \n """, "Illegal Escape In String: Tien \\2", 124))
        self.assertTrue(TestLexer.test(""" "Tien \\e \\n \\r """, "Illegal Escape In String: Tien \\e", 125))        

    
    def test_Comments_newline(self):
        """test Comments và newline""" 
        self.assertTrue(TestLexer.test("## Vo tien","<EOF>",130))    
        self.assertTrue(TestLexer.test("###","<EOF>",131)) 
        self.assertTrue(TestLexer.test("a##1","a,<EOF>",132)) 
        self.assertTrue(TestLexer.test("a#","a,Error Token #",133))    
        # self.assertTrue(TestLexer.test("a\n##1\nb","a,\n,\n,b,<EOF>",134))  
        # self.assertTrue(TestLexer.test("a\n\n\n#","a,\n,\n,\n,Error Token #",135))
#         input = """a
#                     ## comment
#                 """
#         expect = """a,
# ,
# ,<EOF>"""
#         self.assertTrue(TestLexer.test(input,expect,136))   


    def test_complex(self): # test case 140 ->
                
        input = "."
        expect = "Error Token ."
        self.assertTrue(TestLexer.test(input,expect,140))
        
        input = ";"
        expect = "Error Token ;"
        self.assertTrue(TestLexer.test(input,expect,141))
        
        input = "{"
        expect = "Error Token {"
        self.assertTrue(TestLexer.test(input,expect,142))       
        
        self.assertTrue(TestLexer.test("+1-2","+,1,-,2,<EOF>",143)) 
        self.assertTrue(TestLexer.test(""" "Tien \t \n" """, "Unclosed String: Tien 	 ", 144))
        self.assertTrue(TestLexer.test(""" "Tien \\" """, "Illegal Escape In String: Tien \\\"", 145))
        self.assertTrue(TestLexer.test(""" "Tien \\\n """, "Illegal Escape In String: Tien \\\n", 146))
        self.assertTrue(TestLexer.test(""" "Tien '\\ """, "Illegal Escape In String: Tien '\\ ", 147))
        self.assertTrue(TestLexer.test(""" "Tien \'" " """, "Tien '\" ,<EOF>", 148))
        self.assertTrue(TestLexer.test(""" "Tien \\\'" " """, "Tien \\',Unclosed String:  ", 149))
        self.assertTrue(TestLexer.test(""" "Tien 
                                       " """, "Unclosed String: Tien ", 150))