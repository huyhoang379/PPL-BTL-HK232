import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
        
    def test_2(self):
        """Simple program: int main() {} """
        input = """func main() begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_a(self):
        """test"""
        input = """
            var VoTien <- true and "true" or 1 
            var VoTien <- 1 and 2 and 3 or 4 or 4
            var VoTien <- 1 + 2 - 2 + 3 and 3
            var VoTien <- 1 / 2 * 3 % 4
            var VoTien <- 1 / 2 / 2 * 3 % 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200)) 

    def test_declared(self): # test case 201 -> 220
        """declared"""    
        
        #! biến
        input = """ 
            number VoTien
            
            ## VO Tien
            number VoTien <- 0
            bool a[122,15]
            bool a[122,15] <- 1 + 1 / 2 * 3
            string b[3]
            ## 12 
            
            string b[3] <- 2 ... " tring"
            var i <- 0
            dynamic i
            dynamic i <- 0
            ## VO Tien
             
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))   
        
        # input = """ 
        #     var VoTien
        # """
        # expect = "Error on line 2 col 22: \r\n"
        # self.assertTrue(TestParser.test(input, expect, 202))   
        
        input = """ 
            dynamic VoTien[5] <- 3
        """
        expect = "Error on line 2 col 26: ["
        self.assertTrue(TestParser.test(input, expect, 203))         

        input = """ 
            bool a["string"]
            bool a[[1,2]]
            bool a[1+1]
        """
        expect = "Error on line 2 col 19: string"
        self.assertTrue(TestParser.test(input, expect, 204))   
        
        input = """ 
            bool a[1,]
        """
        expect = "Error on line 2 col 21: ]"
        self.assertTrue(TestParser.test(input, expect, 205)) 

        input = """ 
            var a[1]
        """
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 206))  
        
         
        
        #! hàm và declaration_statement
        input = """ 
            func main()
            func main(number f1)
            func main(number a[5],bool x[5,2,3], bool a[5,2,3], string b, bool c)
            func main(number num1, number num2)
                var VoTien <- 1
            func main(number f1 <- c)
        """
        expect = "Error on line 7 col 32: <-"
        self.assertTrue(TestParser.test(input, expect, 207))       
        
        input = """ 
            func main()
            ## VO Tien
            func main() func main(dynamic a) ## VO Tien
        """
        expect = "Error on line 4 col 24: func"
        self.assertTrue(TestParser.test(input, expect, 208))  

        input = """ 
            func main(var a)
        """
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input, expect, 209))                 

        #! lỗi comment và newline
        input = """ 
            ##12
            ##12
            
            func main(number a) var c <- 1
        """
        expect = "Error on line 5 col 32: var"
        self.assertTrue(TestParser.test(input, expect, 210))   
        
        input = """ 
            func main(string a) 
                begin 
                    break ## 12
                end
            func main(dynamic a) 
        """
        expect = "Error on line 6 col 22: dynamic"
        self.assertTrue(TestParser.test(input, expect, 211))    

        input = """ 
            func main(number a[1,2,3]) ##12
                break
        """
        expect = "Error on line 3 col 16: break"
        self.assertTrue(TestParser.test(input, expect, 212))    
        
        input = """
            ##12
            func main(number a) 
                ##12
                
                begin 
                    break
                end
                
                ##12
                ##12
            func main(number a)
            ##12        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))                  

        input = """ 
            ## 12
            
            var a <- 1 ## 12
            ## 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))   
        
        input = """var a <- 1"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 215))  

        input = """func main(number a) """
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 216))  
                                   
    def test_Expression(self):
        """Expression"""
        #! nối chuỗi không có tính kết hợp
        input = """ var VoTien <- "Vo" ... "Tien" 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
        
        input = """ var VoTien <- "Vo" ... 1 ... "Tien" 
        """
        expect = "Error on line 1 col 26: ..."
        self.assertTrue(TestParser.test(input, expect, 212))
        
        #! so sánh không có tính kết hợp
        input = """ 
            var VoTien <- true > "true" 
            var VoTien <- true >= "true"
            var VoTien <- true = "true"
            var VoTien <- true == "true"
            var VoTien <- true < "true"
            var VoTien <- true <= "true"
            var VoTien <- true >= "true" ... 1 > 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
        
        input = """ var VoTien <- true > x >= z 
        """
        expect = "Error on line 1 col 24: >="
        self.assertTrue(TestParser.test(input, expect, 214))
        
        #! cộng trừ nhân chia và and/or ....
        input = """ 
            var VoTien <- true and "true" or 1 
            var VoTien <- 1 and 2 and 3 or 4 or 4
            var VoTien <- 1 + 2 - 2 + 3 and 3
            var VoTien <- 1 / 2 * 3 % 4
            var VoTien <- 1 / 2 / 2 * 3 % 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        
        input = """var VoTien <- true >= "true" and 1 > 2
        """
        expect = "Error on line 1 col 35: >"
        self.assertTrue(TestParser.test(input, expect, 216)) 
        
        #! toán tử not và sign   
        input = """ 
            var VoTien <- -1 * not 1
            var VoTien <- not not not----C
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217)) 
        
        input = """var VoTien <- - not 1
        """
        expect = "Error on line 1 col 16: not"
        self.assertTrue(TestParser.test(input, expect, 218)) 
        
        #! toán tử array
        input = """ 
            var VoTien <- a[1] + 1
            var VoTien <- array[1,1+2][1][2,3]
            var VoTien <- array[1,(1)...2,array[ar[(1*2) and 1]],array[2]]
            var VoTien <- a[1] + fun()[1,fun()] 
            var VoTien <- 1[1]
        """
        expect = "Error on line 3 col 38: ["
        self.assertTrue(TestParser.test(input, expect, 219))
        
        input = """var VoTien <- a[]
        """
        expect = "Error on line 1 col 16: ]"
        self.assertTrue(TestParser.test(input, expect, 220)) 
        
        #! hàm 
        input = """ 
            var VoTien <- a()
            var VoTien <- a(1,2)
            var VoTien <- a(x,array[2])[2]
            var VoTien <- a(z,k[3] ... 2)[1,2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))    
        
        input = """var VoTien <- a()()
        """
        expect = "Error on line 1 col 17: ("
        self.assertTrue(TestParser.test(input, expect, 222))  
        
        #! tổng hợp

        # input = """ 
        #     var VoTien <- a() + ++1 / 2 *3 <= 3 ... "v" >= 2
        #     var VoTien <- a(1,2)[1,2,3 ... 2] + false + true
        #     var VoTien <- a(z,k[2,3,"2"] ... 2)[true]
        #     var VoTien <- (a ... 3) ... b and (a >= b) < b[1, b[1]]
        #     var VoTien <-  ["tr", 2, 3, 4, 5] + [[1, 2 + 2 * 2 / 3, 3], [4, 5, 6]]
        #     var VoTien <- a(x,array[2])[2,3+2,true,false]
        # """
        # expect = "successful"
        # self.assertTrue(TestParser.test(input, expect, 223))  

        input = """var VoTien <- a[1]()
        """
        expect = "Error on line 1 col 18: ("
        self.assertTrue(TestParser.test(input, expect, 224))         
        
    def test_Statements(self): # test 230 -> ...
        """Statements"""
        
        #! test assignment_statement
        input = """
        ## comment
        func main()

            ## comment
            begin
            aPI <- 3.14
            end
            ## comment
            
        ## comment
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        
        input = """
        func main() begin 
        end
        func main() 
            begin 
                ## comment0
            end
        func main()
            ## comment1
            begin
                ## comment2
                
                ## comment3
                VoTien <- 1 + 2 + fun()
                VoTien[1+a] <- 1
                
                ## comment4
                VoTien[3+4,2,4] <- 1
                
                ## comment5
            end
            ## comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231)) 
        
        input = """
        func main()
            begin
            aPI + 1 <- 3.14
            end
        """
        expect = "Error on line 4 col 16: +"
        self.assertTrue(TestParser.test(input, expect, 232))
        
        input = """
        func main()
            begin
            aPI()<- 3.14
            end
        """
        expect = "Error on line 4 col 17: <-"
        self.assertTrue(TestParser.test(input, expect, 233))
        
        input = """
        func main()
            begin
            (aPI)[2]<- 3.14
            end
        """
        expect = "Error on line 4 col 12: ("
        self.assertTrue(TestParser.test(input, expect, 234))
                
        #! test if_statement 
        input = """
        func main()
            begin   
                if(1+1) api <- 1
                ## comment0
                
                if(1+1) 
                    ## comment1
                    
                    api <- 1
                    ## comment2
                else api <- 1
                ## comment3
                
                if (1) api <- 1
                elif (1 ... 2)
                    ## comment1
                    
                    api <- 1
                    ## comment2
                elif (1) api <- 1
                
                if (1) api <- 1
                elif (1 ... 2) api <- 1
                elif (1) api <- 1
                else api <- 1   
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))  
        
        input = """
        func main()
            begin   
                if (api <- 1)
            end
        """
        expect = "Error on line 4 col 24: <-"
        self.assertTrue(TestParser.test(input, expect, 236))        
        
        #! test for break Continue
        input = """
        func main()
            begin
            for i until i >= 10 by 1 + 1
                ## comment
                
                a <- 1
            ## comment
            end
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))    
        
        input = """
        func main()
            begin
            for i[1] until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 238))    

        input = """
        func main()
            begin
            for i+1 until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 17: +"
        self.assertTrue(TestParser.test(input, expect, 239)) 
        
        input = """
        func main()
        begin 
            break
            continue
            for i until i >= 10 by 1 + 1 ... 3 / 2
                begin
                    break
                    continue
                end
                
            for i until i >= 10 by 1 print(1)
            for i until i >= 10 by 1 
                print(1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))  
        
        input = """
        func main()
            begin
            for i until i >= 10 by 1 + 1
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input, expect, 241))  
        
        
        #! return  call_statement
        input = """
        func main()
            return 1 + 1
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

        input = """
        func main()
            begin
            main()
            end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
        
        # input = """
        # func main()
        # begin 
        #     return ([1,2,3]) + 1
        #     return main()
        #     main(1,2)
        #     fun()
        #     main([1,2,3], 1+2, a, c ... e)
        # end
        # """
        # expect = "successful"
        # self.assertTrue(TestParser.test(input, expect, 244))  
        
        input = """
        func main()
            return func()
        """
        expect = "Error on line 3 col 19: func"
        self.assertTrue(TestParser.test(input, expect, 245))      
        
        input = """
        func main()
            return break
        """
        expect = "Error on line 3 col 19: break"
        self.assertTrue(TestParser.test(input, expect, 246)) 
        
        #! return  block
        input = """
        func main()
            begin
                begin
                    begin
                        x <- 1
                    end
                    
                    begin
                        return true
                    end
                    
                    return false
                end
                
                begin
                end
                return true
            end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
     
    def test_NewLine(self): # test 250 -> ...
        """new line"""
        input = """var aPI <- 3.14"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 250))          
  
    def test_Source_Code(self): # test 270 -> ...
        """Source_Code"""
        input = """
        func areDivisors(number num1, number num2)
            return (num1 % num2 = 0 ... num2 % num1 = 0)
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) printString("Yes")
                else printString("No")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))   
        
        
        input = """
            func isPrime(number x)
            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end
            func isPrime(number x)
            begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
            if (x % i = 0) return false
            end
            return true
            
            
            for i until i > x / 2 by 1 + 1 var c <- 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))