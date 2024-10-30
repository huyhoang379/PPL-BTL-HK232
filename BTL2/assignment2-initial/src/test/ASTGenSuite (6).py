import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def testcase0(self):
        input = """## hello world
var str <- "Hello world!"
"""
        expect = '''Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 300))
        except:
            print(f"fail test case: 0. This test case is: ## hello world")
    def testcase1(self):
        input = """##single declaration
number a 
"""
        expect = '''Program([VarDecl(Id(a), NumberType, None, None)])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 301))
        except:
            print(f"fail test case: 1. This test case is: ##single declaration")
    def testcase2(self):
        input = """## array declaration check
func foo(number a) return a+1
number a[2,3] <- [[1+2,3,"abc",foo(4)],[true,false,true]]
"""
        expect = '''Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(3.0), StringLit(abc), CallExpr(Id(foo), [NumLit(4.0)])), ArrayLit(BooleanLit(True), BooleanLit(False), BooleanLit(True))))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 302))
        except:
            print(f"fail test case: 2. This test case is: ## array declaration check")
    def testcase3(self):
        input = """ ##mergesort with zcode
func merge(number arr[100], number left, number mid, number right)
begin
    number i
    number j
    number k
    number n1 <- mid - left + 1
    number n2 <- right - mid
    number L[100]
    number R[100]

    for i until i < n1 by 1
        L[i] <- arr[left + i]

    for j until j < n2 by 1
        R[j] <- arr[mid + 1 + j]

    i <- 0
    j <- 0
    k <- left

    for k until k <= right by 1
    begin
        if ((i < n1) and (j >= n2) or (L[i] <= R[j]))
        begin
            arr[k] <- L[i]
            i <- i + 1
        end
        else begin
            arr[k] <- R[j]
            j <- j + 1
        end
    end
end

func mergeSort(number arr[100], number left, number right)
begin
    if (left < right)
    begin
        number mid <- (left + right) / 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        merge(arr, left, mid, right)
    end
end
"""
        expect = '''Program([FuncDecl(Id(merge), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(mid), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, None), VarDecl(Id(j), NumberType, None, None), VarDecl(Id(k), NumberType, None, None), VarDecl(Id(n1), NumberType, None, BinaryOp(+, BinaryOp(-, Id(mid), Id(left)), NumLit(1.0))), VarDecl(Id(n2), NumberType, None, BinaryOp(-, Id(right), Id(mid))), VarDecl(Id(L), ArrayType([100.0], NumberType), None, None), VarDecl(Id(R), ArrayType([100.0], NumberType), None, None), For(Id(i), BinaryOp(<, Id(i), Id(n1)), NumLit(1.0), AssignStmt(ArrayCell(Id(L), [Id(i)]), ArrayCell(Id(arr), [BinaryOp(+, Id(left), Id(i))]))), For(Id(j), BinaryOp(<, Id(j), Id(n2)), NumLit(1.0), AssignStmt(ArrayCell(Id(R), [Id(j)]), ArrayCell(Id(arr), [BinaryOp(+, BinaryOp(+, Id(mid), NumLit(1.0)), Id(j))]))), AssignStmt(Id(i), NumLit(0.0)), AssignStmt(Id(j), NumLit(0.0)), AssignStmt(Id(k), Id(left)), For(Id(k), BinaryOp(<=, Id(k), Id(right)), NumLit(1.0), Block([If((BinaryOp(or, BinaryOp(and, BinaryOp(<, Id(i), Id(n1)), BinaryOp(>=, Id(j), Id(n2))), BinaryOp(<=, ArrayCell(Id(L), [Id(i)]), ArrayCell(Id(R), [Id(j)]))), Block([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(L), [Id(i)])), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))])), [], Block([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(R), [Id(j)])), AssignStmt(Id(j), BinaryOp(+, Id(j), NumLit(1.0)))]))]))])), FuncDecl(Id(mergeSort), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([If((BinaryOp(<, Id(left), Id(right)), Block([VarDecl(Id(mid), NumberType, None, BinaryOp(/, BinaryOp(+, Id(left), Id(right)), NumLit(2.0))), CallStmt(Id(mergeSort), [Id(arr), Id(left), Id(mid)]), CallStmt(Id(mergeSort), [Id(arr), BinaryOp(+, Id(mid), NumLit(1.0)), Id(right)]), CallStmt(Id(merge), [Id(arr), Id(left), Id(mid), Id(right)])])), [], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 303))
        except:
            print(f"fail test case: 3. This test case is: ##mergesort with zcode")
    def testcase4(self):
        input = """##if else check
func main()
begin
bool a<-true
if (a) b<-a+1
else if (not a) b<-a+2
else b<-a+3
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), BoolType, None, BooleanLit(True)), If((Id(a), AssignStmt(Id(b), BinaryOp(+, Id(a), NumLit(1.0)))), [], If((UnaryOp(not, Id(a)), AssignStmt(Id(b), BinaryOp(+, Id(a), NumLit(2.0)))), [], AssignStmt(Id(b), BinaryOp(+, Id(a), NumLit(3.0)))))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 304))
        except:
            print(f"fail test case: 4. This test case is: ##if else check")
    def testcase5(self):
        input = """##if else check 
func main() begin 
number today <- getToday()
number day <- getDay()
if (today=2) writeString("Hom nay phai di hoc")
elif (today = 3) 
    if (day=1) writeString("hom nay duoc nghi hoc")
    elif (day=25) writeString("hom nay lam kiem tra")
    else writeString("hom nay di hoc bth")
elif (today=4) writeString("Hom nay di hoc buoi sang")
else writeString("Hom nay duoc nghi hoc")
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(today), NumberType, None, CallExpr(Id(getToday), [])), VarDecl(Id(day), NumberType, None, CallExpr(Id(getDay), [])), If((BinaryOp(=, Id(today), NumLit(2.0)), CallStmt(Id(writeString), [StringLit(Hom nay phai di hoc)])), [(BinaryOp(=, Id(today), NumLit(3.0)), If((BinaryOp(=, Id(day), NumLit(1.0)), CallStmt(Id(writeString), [StringLit(hom nay duoc nghi hoc)])), [(BinaryOp(=, Id(day), NumLit(25.0)), CallStmt(Id(writeString), [StringLit(hom nay lam kiem tra)]))], CallStmt(Id(writeString), [StringLit(hom nay di hoc bth)]))), (BinaryOp(=, Id(today), NumLit(4.0)), CallStmt(Id(writeString), [StringLit(Hom nay di hoc buoi sang)]))], CallStmt(Id(writeString), [StringLit(Hom nay duoc nghi hoc)]))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 305))
        except:
            print(f"fail test case: 5. This test case is: ##if else check ")
    def testcase6(self):
        input = """##for check
func main()
begin
    string words[4] <- ["apple", "banana", "cherry", "date"]
    dynamic i<-0
    for  i until i > size(words) - 1 by 1
        writeString(words[i])
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(words), ArrayType([4.0], StringType), None, ArrayLit(StringLit(apple), StringLit(banana), StringLit(cherry), StringLit(date))), VarDecl(Id(i), None, dynamic, NumLit(0.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(-, CallExpr(Id(size), [Id(words)]), NumLit(1.0))), NumLit(1.0), CallStmt(Id(writeString), [ArrayCell(Id(words), [Id(i)])]))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 306))
        except:
            print(f"fail test case: 6. This test case is: ##for check")
    def testcase7(self):
        input = """## sum of array
func sum(number a[100], number length)
begin
    var i <- 0
    var sum <- 0
    for i until i >= length by 1
        sum <- sum + a[i]
    return sum
end

func main() begin
    writeNumber(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    writeNumber(sum([2, 0, 2, 4], 4))
end
"""
        expect = '''Program([FuncDecl(Id(sum), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(sum), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), AssignStmt(Id(sum), BinaryOp(+, Id(sum), ArrayCell(Id(a), [Id(i)])))), Return(Id(sum))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0), NumLit(6.0), NumLit(7.0), NumLit(8.0), NumLit(9.0), NumLit(10.0)), NumLit(10.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(sum), [ArrayLit(NumLit(2.0), NumLit(0.0), NumLit(2.0), NumLit(4.0)), NumLit(4.0)])])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 307))
        except:
            print(f"fail test case: 7. This test case is: ## sum of array")
    def testcase8(self):
        input = """## print array iteratively
func printArr(number a[100], number length)
begin
    var i <- 0
    for i until i >= length by 1 begin
        writeNumber(a[i])
        writeString(" ")
    end
    writeString("\\n")
end
"""
        expect = '''Program([FuncDecl(Id(printArr), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), Block([CallStmt(Id(writeNumber), [ArrayCell(Id(a), [Id(i)])]), CallStmt(Id(writeString), [StringLit( )])])), CallStmt(Id(writeString), [StringLit(\\n)])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 308))
        except:
            print(f"fail test case: 8. This test case is: ## print array iteratively")
    def testcase9(self):
        input = """## print array recursively
func printArr(number a[100], number length)
begin
    if (length < 0)
        return
    printArr(a, length - 1)
    writeNumber(a[length - 1])
    writeString(" ")
end
"""
        expect = '''Program([FuncDecl(Id(printArr), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([If((BinaryOp(<, Id(length), NumLit(0.0)), Return()), [], None), CallStmt(Id(printArr), [Id(a), BinaryOp(-, Id(length), NumLit(1.0))]), CallStmt(Id(writeNumber), [ArrayCell(Id(a), [BinaryOp(-, Id(length), NumLit(1.0))])]), CallStmt(Id(writeString), [StringLit( )])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 309))
        except:
            print(f"fail test case: 9. This test case is: ## print array recursively")
    def testcase10(self):
        input = """## find max in array
func max(number a[100], number length)
begin
    if (length <= 0)
        return -1e9 ## Represent negative infinity
    var max <- a[0]
    var i <- 0
    for i until i >= length by 1
        if (a[i] > max) max <- a[i]
    return max
end
"""
        expect = '''Program([FuncDecl(Id(max), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([If((BinaryOp(<=, Id(length), NumLit(0.0)), Return(UnaryOp(-, NumLit(1000000000.0)))), [], None), VarDecl(Id(max), None, var, ArrayCell(Id(a), [NumLit(0.0)])), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), If((BinaryOp(>, ArrayCell(Id(a), [Id(i)]), Id(max)), AssignStmt(Id(max), ArrayCell(Id(a), [Id(i)]))), [], None)), Return(Id(max))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 310))
        except:
            print(f"fail test case: 10. This test case is: ## find max in array")
    def testcase11(self):
        input = """## find minimum in array 
func min(number a[100], number length)
begin
    if (length <= 0)
        return 1E+9 ## Represent possitive infinity
    var min <- a[0]
    var i <- 0
    for i until i >= length by 1
        if (a[i] < min) min <- a[i]
    return min
end
"""
        expect = '''Program([FuncDecl(Id(min), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([If((BinaryOp(<=, Id(length), NumLit(0.0)), Return(NumLit(1000000000.0))), [], None), VarDecl(Id(min), None, var, ArrayCell(Id(a), [NumLit(0.0)])), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), If((BinaryOp(<, ArrayCell(Id(a), [Id(i)]), Id(min)), AssignStmt(Id(min), ArrayCell(Id(a), [Id(i)]))), [], None)), Return(Id(min))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 311))
        except:
            print(f"fail test case: 11. This test case is: ## find minimum in array ")
    def testcase12(self):
        input = """## convert decimal to binary
func round(number n)

func dec_to_bin(number n) begin
    if (n < 0) return "not implemented"
    if (n = 0) return "0"
    
    var res <- ""
    var i <- 0
    for i until n <= 0 by 0 begin
        if (n % 2 == 0) res <- "0" ... res
        else res <- "1" ... res
        n <- round(n/2)
    end
    
    return res
end

func round(number n) return n - n % 1

func main() begin
    writeNumber(dec_to_bin(10))
    writeNumber(dec_to_bin(100))
    writeNumber(dec_to_bin(1000))
end
"""
        expect = '''Program([FuncDecl(Id(round), [VarDecl(Id(n), NumberType, None, None)], None), FuncDecl(Id(dec_to_bin), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(<, Id(n), NumLit(0.0)), Return(StringLit(not implemented))), [], None), If((BinaryOp(=, Id(n), NumLit(0.0)), Return(StringLit(0))), [], None), VarDecl(Id(res), None, var, StringLit()), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(n), NumLit(0.0)), NumLit(0.0), Block([If((BinaryOp(==, BinaryOp(%, Id(n), NumLit(2.0)), NumLit(0.0)), AssignStmt(Id(res), BinaryOp(..., StringLit(0), Id(res)))), [], AssignStmt(Id(res), BinaryOp(..., StringLit(1), Id(res)))), AssignStmt(Id(n), CallExpr(Id(round), [BinaryOp(/, Id(n), NumLit(2.0))]))])), Return(Id(res))])), FuncDecl(Id(round), [VarDecl(Id(n), NumberType, None, None)], Return(BinaryOp(-, Id(n), BinaryOp(%, Id(n), NumLit(1.0))))), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(dec_to_bin), [NumLit(10.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(dec_to_bin), [NumLit(100.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(dec_to_bin), [NumLit(1000.0)])])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 312))
        except:
            print(f"fail test case: 12. This test case is: ## convert decimal to binary")
    def testcase13(self):
        input = """## find GCD 
func gcd(number a, number b)
begin
    if (b = 0) return a
    return gcd(b, a % b)
end

func main() begin
    writeNumber(gcd(6, 9))
    writeNumber(gcd(24, 16))
    writeNumber(gcd(1, 7))
end
"""
        expect = '''Program([FuncDecl(Id(gcd), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(=, Id(b), NumLit(0.0)), Return(Id(a))), [], None), Return(CallExpr(Id(gcd), [Id(b), BinaryOp(%, Id(a), Id(b))]))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(gcd), [NumLit(6.0), NumLit(9.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(gcd), [NumLit(24.0), NumLit(16.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(gcd), [NumLit(1.0), NumLit(7.0)])])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 313))
        except:
            print(f"fail test case: 13. This test case is: ## find GCD ")
    def testcase14(self):
        input = """##palindrome string 
func isPalindrome(string s[100], number left, number right)
begin
    ## Because ZCode string cannot be indexed, cut, etc...
    ## We assume that s is an array of 1-length strings, aka characters
    ## And we will check whether characters from left to right (inclusively) can make a palindrome string
    
    if (left > right + 1) return false
    if ((left = right) or (left = right + 1)) return true
    return (s[left] == s[right]) and isPalindrome(s, left + 1, right - 1)
end

func main()
begin
    isPalindrome(["m", "o", "m"], 0, 2)
    isPalindrome(["d", "o", "g", "e", "e", "s", "e", "s", "e", "e", "g", "o", "d"], 0, 12)
end
"""
        expect = '''Program([FuncDecl(Id(isPalindrome), [VarDecl(Id(s), ArrayType([100.0], StringType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([If((BinaryOp(>, Id(left), BinaryOp(+, Id(right), NumLit(1.0))), Return(BooleanLit(False))), [], None), If((BinaryOp(or, BinaryOp(=, Id(left), Id(right)), BinaryOp(=, Id(left), BinaryOp(+, Id(right), NumLit(1.0)))), Return(BooleanLit(True))), [], None), Return(BinaryOp(and, BinaryOp(==, ArrayCell(Id(s), [Id(left)]), ArrayCell(Id(s), [Id(right)])), CallExpr(Id(isPalindrome), [Id(s), BinaryOp(+, Id(left), NumLit(1.0)), BinaryOp(-, Id(right), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(isPalindrome), [ArrayLit(StringLit(m), StringLit(o), StringLit(m)), NumLit(0.0), NumLit(2.0)]), CallStmt(Id(isPalindrome), [ArrayLit(StringLit(d), StringLit(o), StringLit(g), StringLit(e), StringLit(e), StringLit(s), StringLit(e), StringLit(s), StringLit(e), StringLit(e), StringLit(g), StringLit(o), StringLit(d)), NumLit(0.0), NumLit(12.0)])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 314))
        except:
            print(f"fail test case: 14. This test case is: ##palindrome string ")
    def testcase15(self):
        input = """## fibonanci
number res[100]

func fib(number n)
begin
    if (res[n] != -1) return res[n]
    res[n] <- fib(n - 1) + fib(n - 2)
    return res[n]
end

func main() begin
    res[0] <- 0
    res[1] <- 1
    
    var i <- 2
    for i until i = 100 by 1 res[i] <- -1
    
    writeNumber(fib(5))
    writeNumber(fib(10))
    writeNumber(fib(50))
end
"""
        expect = '''Program([VarDecl(Id(res), ArrayType([100.0], NumberType), None, None), FuncDecl(Id(fib), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(!=, ArrayCell(Id(res), [Id(n)]), UnaryOp(-, NumLit(1.0))), Return(ArrayCell(Id(res), [Id(n)]))), [], None), AssignStmt(ArrayCell(Id(res), [Id(n)]), BinaryOp(+, CallExpr(Id(fib), [BinaryOp(-, Id(n), NumLit(1.0))]), CallExpr(Id(fib), [BinaryOp(-, Id(n), NumLit(2.0))]))), Return(ArrayCell(Id(res), [Id(n)]))])), FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(res), [NumLit(0.0)]), NumLit(0.0)), AssignStmt(ArrayCell(Id(res), [NumLit(1.0)]), NumLit(1.0)), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), AssignStmt(ArrayCell(Id(res), [Id(i)]), UnaryOp(-, NumLit(1.0)))), CallStmt(Id(writeNumber), [CallExpr(Id(fib), [NumLit(5.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(fib), [NumLit(10.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(fib), [NumLit(50.0)])])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 315))
        except:
            print(f"fail test case: 15. This test case is: ## fibonanci")
    def testcase16(self):
        input = r"""## check nested if with for loop
number LOOP_COUNT <- 0
func toAsciiCode(string s)
begin 
string ascii[96] <- [" ","!","'"","#","$","%","&","\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~",""]
number i<-0
for i until s == ascii[i] by 1
    i<-i+1
return i+32
end

func doNoThing(number n) return n
func main() begin
    number i<-0
    if (toAsciiCode("a") % 3 = 0)
        if (toAssciiCode("b") = doNoThing(toAsciiCode("b")/3)*3)
            for i until i<=doNoThing(3) by 1 LOOP_COUNT<- LOOP_COUNT ----1
        elif (toAsciiCode("c")=i) 
            if (i*i*i%128 = toAsciiCode("H"))
            for i until i<=doNoThing(100) by 1 
                if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                else for i until i<=doNoThing(100) by 1 
                    if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                    else i<-1--i 
end
"""
        expect = r'''Program([VarDecl(Id(LOOP_COUNT), NumberType, None, NumLit(0.0)), FuncDecl(Id(toAsciiCode), [VarDecl(Id(s), StringType, None, None)], Block([VarDecl(Id(ascii), ArrayType([96.0], StringType), None, ArrayLit(StringLit( ), StringLit(!), StringLit('"), StringLit(#), StringLit($), StringLit(%), StringLit(&), StringLit(\'), StringLit((), StringLit()), StringLit(*), StringLit(+), StringLit(,), StringLit(-), StringLit(.), StringLit(/), StringLit(0), StringLit(1), StringLit(2), StringLit(3), StringLit(4), StringLit(5), StringLit(6), StringLit(7), StringLit(8), StringLit(9), StringLit(:), StringLit(;), StringLit(<), StringLit(=), StringLit(>), StringLit(?), StringLit(@), StringLit(A), StringLit(B), StringLit(C), StringLit(D), StringLit(E), StringLit(F), StringLit(G), StringLit(H), StringLit(I), StringLit(J), StringLit(K), StringLit(L), StringLit(M), StringLit(N), StringLit(O), StringLit(P), StringLit(Q), StringLit(R), StringLit(S), StringLit(T), StringLit(U), StringLit(V), StringLit(W), StringLit(X), StringLit(Y), StringLit(Z), StringLit([), StringLit(\\), StringLit(]), StringLit(^), StringLit(_), StringLit(`), StringLit(a), StringLit(b), StringLit(c), StringLit(d), StringLit(e), StringLit(f), StringLit(g), StringLit(h), StringLit(i), StringLit(j), StringLit(k), StringLit(l), StringLit(m), StringLit(n), StringLit(o), StringLit(p), StringLit(q), StringLit(r), StringLit(s), StringLit(t), StringLit(u), StringLit(v), StringLit(w), StringLit(x), StringLit(y), StringLit(z), StringLit({), StringLit(|), StringLit(}), StringLit(~), StringLit())), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(==, Id(s), ArrayCell(Id(ascii), [Id(i)])), NumLit(1.0), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))), Return(BinaryOp(+, Id(i), NumLit(32.0)))])), FuncDecl(Id(doNoThing), [VarDecl(Id(n), NumberType, None, None)], Return(Id(n))), FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), If((BinaryOp(=, BinaryOp(%, CallExpr(Id(toAsciiCode), [StringLit(a)]), NumLit(3.0)), NumLit(0.0)), If((BinaryOp(=, CallExpr(Id(toAssciiCode), [StringLit(b)]), BinaryOp(*, CallExpr(Id(doNoThing), [BinaryOp(/, CallExpr(Id(toAsciiCode), [StringLit(b)]), NumLit(3.0))]), NumLit(3.0))), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(3.0)])), NumLit(1.0), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, Id(LOOP_COUNT), UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0)))))))), [(BinaryOp(=, CallExpr(Id(toAsciiCode), [StringLit(c)]), Id(i)), If((BinaryOp(=, BinaryOp(%, BinaryOp(*, BinaryOp(*, Id(i), Id(i)), Id(i)), NumLit(128.0)), CallExpr(Id(toAsciiCode), [StringLit(H)])), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], AssignStmt(Id(i), BinaryOp(-, NumLit(1.0), UnaryOp(-, Id(i))))))))), [], None))], None)), [], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 316))
        except:
            print(f"fail test case: 16. This test case is: ## check nested if with for loop")
    def testcase17(self):
        input = r"""## check nested if with for loop
number LOOP_COUNT <- 0
func toAsciiCode(string s)
begin 
string ascii[96] <- [" ","!","'"","#","$","%","&","\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~",""]
number i<-0
for i until s == ascii[i] by 1
    i<-i+1
return i+32
end

func doNoThing(number n) return n
func main() begin
    number i<-0
    if (toAsciiCode("a") % 3 = 0)
        if (toAssciiCode("b") = doNoThing(toAsciiCode("b")/3)*3)
            for i until i<=doNoThing(3) by 1 LOOP_COUNT<- LOOP_COUNT ----1
        elif (toAsciiCode("c")=i) 
            if (i*i*i%128 = toAsciiCode("H"))
            for i until i<=doNoThing(100) by 1 
                if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                else for i until i<=doNoThing(100) by 1 
                    if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                    else i<-1--i 
            elif (false) i<-toAsciiCode("1")
            else i<-0
        elif (true) i<-1
end
"""
        expect = r'''Program([VarDecl(Id(LOOP_COUNT), NumberType, None, NumLit(0.0)), FuncDecl(Id(toAsciiCode), [VarDecl(Id(s), StringType, None, None)], Block([VarDecl(Id(ascii), ArrayType([96.0], StringType), None, ArrayLit(StringLit( ), StringLit(!), StringLit('"), StringLit(#), StringLit($), StringLit(%), StringLit(&), StringLit(\'), StringLit((), StringLit()), StringLit(*), StringLit(+), StringLit(,), StringLit(-), StringLit(.), StringLit(/), StringLit(0), StringLit(1), StringLit(2), StringLit(3), StringLit(4), StringLit(5), StringLit(6), StringLit(7), StringLit(8), StringLit(9), StringLit(:), StringLit(;), StringLit(<), StringLit(=), StringLit(>), StringLit(?), StringLit(@), StringLit(A), StringLit(B), StringLit(C), StringLit(D), StringLit(E), StringLit(F), StringLit(G), StringLit(H), StringLit(I), StringLit(J), StringLit(K), StringLit(L), StringLit(M), StringLit(N), StringLit(O), StringLit(P), StringLit(Q), StringLit(R), StringLit(S), StringLit(T), StringLit(U), StringLit(V), StringLit(W), StringLit(X), StringLit(Y), StringLit(Z), StringLit([), StringLit(\\), StringLit(]), StringLit(^), StringLit(_), StringLit(`), StringLit(a), StringLit(b), StringLit(c), StringLit(d), StringLit(e), StringLit(f), StringLit(g), StringLit(h), StringLit(i), StringLit(j), StringLit(k), StringLit(l), StringLit(m), StringLit(n), StringLit(o), StringLit(p), StringLit(q), StringLit(r), StringLit(s), StringLit(t), StringLit(u), StringLit(v), StringLit(w), StringLit(x), StringLit(y), StringLit(z), StringLit({), StringLit(|), StringLit(}), StringLit(~), StringLit())), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(==, Id(s), ArrayCell(Id(ascii), [Id(i)])), NumLit(1.0), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))), Return(BinaryOp(+, Id(i), NumLit(32.0)))])), FuncDecl(Id(doNoThing), [VarDecl(Id(n), NumberType, None, None)], Return(Id(n))), FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), If((BinaryOp(=, BinaryOp(%, CallExpr(Id(toAsciiCode), [StringLit(a)]), NumLit(3.0)), NumLit(0.0)), If((BinaryOp(=, CallExpr(Id(toAssciiCode), [StringLit(b)]), BinaryOp(*, CallExpr(Id(doNoThing), [BinaryOp(/, CallExpr(Id(toAsciiCode), [StringLit(b)]), NumLit(3.0))]), NumLit(3.0))), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(3.0)])), NumLit(1.0), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, Id(LOOP_COUNT), UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0)))))))), [(BinaryOp(=, CallExpr(Id(toAsciiCode), [StringLit(c)]), Id(i)), If((BinaryOp(=, BinaryOp(%, BinaryOp(*, BinaryOp(*, Id(i), Id(i)), Id(i)), NumLit(128.0)), CallExpr(Id(toAsciiCode), [StringLit(H)])), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], AssignStmt(Id(i), BinaryOp(-, NumLit(1.0), UnaryOp(-, Id(i))))))))), [(BooleanLit(False), AssignStmt(Id(i), CallExpr(Id(toAsciiCode), [StringLit(1)])))], AssignStmt(Id(i), NumLit(0.0)))), (BooleanLit(True), AssignStmt(Id(i), NumLit(1.0)))], None)), [], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 317))
        except:
            print(f"fail test case: 17. This test case is: ## check nested if with for loop")
    def testcase18(self):
        input = """## this check break statement
func main() begin 
var i<-0
for i until i=1 by 1
    if (i=0) break 
end 
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(1.0)), NumLit(1.0), If((BinaryOp(=, Id(i), NumLit(0.0)), Break), [], None))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 318))
        except:
            print(f"fail test case: 18. This test case is: ## this check break statement")
    def testcase19(self):
        input = """## this check continue statement 
func main() begin 
var i<-0
for i until i=10 by 1
    begin 
        var j<--0.87e-4
        i <- i*j
        continue
    end
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), Block([VarDecl(Id(j), None, var, UnaryOp(-, NumLit(8.7e-05))), AssignStmt(Id(i), BinaryOp(*, Id(i), Id(j))), Continue]))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 319))
        except:
            print(f"fail test case: 19. This test case is: ## this check continue statement ")
    def testcase20(self):
        input = """## check return statement
func foo() return 1
func main() begin 
    return 0
end
"""
        expect = '''Program([FuncDecl(Id(foo), [], Return(NumLit(1.0))), FuncDecl(Id(main), [], Block([Return(NumLit(0.0))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 320))
        except:
            print(f"fail test case: 20. This test case is: ## check return statement")
    def testcase21(self):
        input = """## complex expresion and sin function
func integral(number a, number b,number c) return c*b-c*a 
func sin(number x,bool degree, number exactrate) begin 
    var pi <- 3.141592653589793238462643383279502884197
    if (degree) x<- x*pi/180
    x<- x%(2*pi)
    number pow <- x 
    dynamic i<-1
    dynamic fact <- 1
    dynamic res <- 2*x
    for i until i=exactrate by 2
    begin
        res <- res - pow/fact 
        pow <- pow * x * X
        fact <- fact*i*(i-1)
    end
    return res
end
func main() begin 
    var n1 <- 1
    var n2 <- 2
    var n3 <- 3
    var n4 <- 4
    var b1 <- true 
    var b2 <- fasle 
    var b3 <- not true 
    var b4 <- true or false 
    dynamic res 
    res <- ( integral((n1*2 + 2*n1*n2 - n3*-n4)*n1%n2/n3+n4--n1*sin(3.14,false,701)) > sin(n1*n2-n3%n4,n1=n2*3-n4+sin(n1,n2>n3,701*n2%1),701) ) or (not b1 and b2 and not b3 or b4) and (b1 and not b4 or b3 and not b2)
end
"""
        expect = '''Program([FuncDecl(Id(integral), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None), VarDecl(Id(c), NumberType, None, None)], Return(BinaryOp(-, BinaryOp(*, Id(c), Id(b)), BinaryOp(*, Id(c), Id(a))))), FuncDecl(Id(sin), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(degree), BoolType, None, None), VarDecl(Id(exactrate), NumberType, None, None)], Block([VarDecl(Id(pi), None, var, NumLit(3.141592653589793)), If((Id(degree), AssignStmt(Id(x), BinaryOp(/, BinaryOp(*, Id(x), Id(pi)), NumLit(180.0)))), [], None), AssignStmt(Id(x), BinaryOp(%, Id(x), BinaryOp(*, NumLit(2.0), Id(pi)))), VarDecl(Id(pow), NumberType, None, Id(x)), VarDecl(Id(i), None, dynamic, NumLit(1.0)), VarDecl(Id(fact), None, dynamic, NumLit(1.0)), VarDecl(Id(res), None, dynamic, BinaryOp(*, NumLit(2.0), Id(x))), For(Id(i), BinaryOp(=, Id(i), Id(exactrate)), NumLit(2.0), Block([AssignStmt(Id(res), BinaryOp(-, Id(res), BinaryOp(/, Id(pow), Id(fact)))), AssignStmt(Id(pow), BinaryOp(*, BinaryOp(*, Id(pow), Id(x)), Id(X))), AssignStmt(Id(fact), BinaryOp(*, BinaryOp(*, Id(fact), Id(i)), BinaryOp(-, Id(i), NumLit(1.0))))])), Return(Id(res))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n1), None, var, NumLit(1.0)), VarDecl(Id(n2), None, var, NumLit(2.0)), VarDecl(Id(n3), None, var, NumLit(3.0)), VarDecl(Id(n4), None, var, NumLit(4.0)), VarDecl(Id(b1), None, var, BooleanLit(True)), VarDecl(Id(b2), None, var, Id(fasle)), VarDecl(Id(b3), None, var, UnaryOp(not, BooleanLit(True))), VarDecl(Id(b4), None, var, BinaryOp(or, BooleanLit(True), BooleanLit(False))), VarDecl(Id(res), None, dynamic, None), AssignStmt(Id(res), BinaryOp(and, BinaryOp(or, BinaryOp(>, CallExpr(Id(integral), [BinaryOp(-, BinaryOp(+, BinaryOp(/, BinaryOp(%, BinaryOp(*, BinaryOp(-, BinaryOp(+, BinaryOp(*, Id(n1), NumLit(2.0)), BinaryOp(*, BinaryOp(*, NumLit(2.0), Id(n1)), Id(n2))), BinaryOp(*, Id(n3), UnaryOp(-, Id(n4)))), Id(n1)), Id(n2)), Id(n3)), Id(n4)), BinaryOp(*, UnaryOp(-, Id(n1)), CallExpr(Id(sin), [NumLit(3.14), BooleanLit(False), NumLit(701.0)])))]), CallExpr(Id(sin), [BinaryOp(-, BinaryOp(*, Id(n1), Id(n2)), BinaryOp(%, Id(n3), Id(n4))), BinaryOp(=, Id(n1), BinaryOp(+, BinaryOp(-, BinaryOp(*, Id(n2), NumLit(3.0)), Id(n4)), CallExpr(Id(sin), [Id(n1), BinaryOp(>, Id(n2), Id(n3)), BinaryOp(%, BinaryOp(*, NumLit(701.0), Id(n2)), NumLit(1.0))]))), NumLit(701.0)])), BinaryOp(or, BinaryOp(and, BinaryOp(and, UnaryOp(not, Id(b1)), Id(b2)), UnaryOp(not, Id(b3))), Id(b4))), BinaryOp(and, BinaryOp(or, BinaryOp(and, Id(b1), UnaryOp(not, Id(b4))), Id(b3)), UnaryOp(not, Id(b2)))))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 321))
        except:
            print(f"fail test case: 21. This test case is: ## complex expresion and sin function")
    def testcase22(self):
        input = """## check prime
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
        expect = '''Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), If((CallExpr(Id(isPrime), [Id(x)]), CallStmt(Id(printString), [StringLit(Yes)])), [], CallStmt(Id(printString), [StringLit(No)]))])), FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), Return(BooleanLit(True)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), BinaryOp(+, NumLit(1.0), NumLit(1.0)), VarDecl(Id(c), None, var, NumLit(1.0)))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 322))
        except:
            print(f"fail test case: 22. This test case is: ## check prime")
    def testcase23(self):
        input = """## looping test
func test_looping(string a[1, 2], number __[0], bool cc_c)
begin
    if (a > b)
        for a until a + 1 by b + 1 if (a > b)
                if (a > b) number c
                elif (a > b) number c
                elif (a > b) number c
                else number c
            else
                break
    else
        for a until a > b by a * b / c
            for a until ssss[1, 2] by foo("hey", true, false, 1.e-3)
                if (a > b) number c
                else number c
end
"""
        expect = '''Program([FuncDecl(Id(test_looping), [VarDecl(Id(a), ArrayType([1.0, 2.0], StringType), None, None), VarDecl(Id(__), ArrayType([0.0], NumberType), None, None), VarDecl(Id(cc_c), BoolType, None, None)], Block([If((BinaryOp(>, Id(a), Id(b)), For(Id(a), BinaryOp(+, Id(a), NumLit(1.0)), BinaryOp(+, Id(b), NumLit(1.0)), If((BinaryOp(>, Id(a), Id(b)), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [(BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), (BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None))], VarDecl(Id(c), NumberType, None, None))), [], Break))), [], For(Id(a), BinaryOp(>, Id(a), Id(b)), BinaryOp(/, BinaryOp(*, Id(a), Id(b)), Id(c)), For(Id(a), ArrayCell(Id(ssss), [NumLit(1.0), NumLit(2.0)]), CallExpr(Id(foo), [StringLit(hey), BooleanLit(True), BooleanLit(False), NumLit(0.001)]), If((BinaryOp(>, Id(a), Id(b)), VarDecl(Id(c), NumberType, None, None)), [], VarDecl(Id(c), NumberType, None, None)))))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 323))
        except:
            print(f"fail test case: 23. This test case is: ## looping test")
    def testcase24(self):
        input = """## BFS with Zcode 
number QUEUE[100] <- [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
number HEAD <- 0
number TAIL <- 0
func push(number item) begin 
    QUEUE[TAIL] <- item 
    TAIL <- (TAIL + 1)%100
end 
func pop() begin 
    number item <- QUEUE[HEAD]
    HEAD <- (HEAD + 1)%100
    return item
end
func main() begin
bool graph[10,10] 
var i<-0
for i until i=10 by 1
begin
    var j<-0
    for j until j=10 by 1
        dynamic num <- readNumber()
        if (num=1) graph[i,j] <- true
        else graph[i,j] <- false 
end
dynamic start <- readNumber()
dynamic des <- readNumber()
bool visit[10]
i<-0
for i until i=10 by 1 visit[i] <- false
push(start)
for i until (HEAD = TAIL) by 0
begin
var top <- pop()
visit[top] <- true 
if (top = des) break 
i<-0 
for i until i=10 by 1
    if (not visit[i]) push(i)
end
end
"""
        expect = '''Program([VarDecl(Id(QUEUE), ArrayType([100.0], NumberType), None, ArrayLit(NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0))), VarDecl(Id(HEAD), NumberType, None, NumLit(0.0)), VarDecl(Id(TAIL), NumberType, None, NumLit(0.0)), FuncDecl(Id(push), [VarDecl(Id(item), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(QUEUE), [Id(TAIL)]), Id(item)), AssignStmt(Id(TAIL), BinaryOp(%, BinaryOp(+, Id(TAIL), NumLit(1.0)), NumLit(100.0)))])), FuncDecl(Id(pop), [], Block([VarDecl(Id(item), NumberType, None, ArrayCell(Id(QUEUE), [Id(HEAD)])), AssignStmt(Id(HEAD), BinaryOp(%, BinaryOp(+, Id(HEAD), NumLit(1.0)), NumLit(100.0))), Return(Id(item))])), FuncDecl(Id(main), [], Block([VarDecl(Id(graph), ArrayType([10.0, 10.0], BoolType), None, None), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), Block([VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(j), BinaryOp(=, Id(j), NumLit(10.0)), NumLit(1.0), VarDecl(Id(num), None, dynamic, CallExpr(Id(readNumber), []))), If((BinaryOp(=, Id(num), NumLit(1.0)), AssignStmt(ArrayCell(Id(graph), [Id(i), Id(j)]), BooleanLit(True))), [], AssignStmt(ArrayCell(Id(graph), [Id(i), Id(j)]), BooleanLit(False)))])), VarDecl(Id(start), None, dynamic, CallExpr(Id(readNumber), [])), VarDecl(Id(des), None, dynamic, CallExpr(Id(readNumber), [])), VarDecl(Id(visit), ArrayType([10.0], BoolType), None, None), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), AssignStmt(ArrayCell(Id(visit), [Id(i)]), BooleanLit(False))), CallStmt(Id(push), [Id(start)]), For(Id(i), BinaryOp(=, Id(HEAD), Id(TAIL)), NumLit(0.0), Block([VarDecl(Id(top), None, var, CallExpr(Id(pop), [])), AssignStmt(ArrayCell(Id(visit), [Id(top)]), BooleanLit(True)), If((BinaryOp(=, Id(top), Id(des)), Break), [], None), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), If((UnaryOp(not, ArrayCell(Id(visit), [Id(i)])), CallStmt(Id(push), [Id(i)])), [], None))]))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 324))
        except:
            print(f"fail test case: 24. This test case is: ## BFS with Zcode ")
    def testcase25(self):
        input = """##check declaration 
number a[4,2,3] 
number b[3,2,1] <- [1]
"""
        expect = '''Program([VarDecl(Id(a), ArrayType([4.0, 2.0, 3.0], NumberType), None, None), VarDecl(Id(b), ArrayType([3.0, 2.0, 1.0], NumberType), None, ArrayLit(NumLit(1.0)))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 325))
        except:
            print(f"fail test case: 25. This test case is: ##check declaration ")
    def testcase26(self):
        input = r"""## expresion with concat string 
func main() begin
bool a <- foo((x < -2) or (("a'""..."a\'") == "a'"a\'"))[3,2]
end
"""
        expect = r'''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), BoolType, None, ArrayCell(CallExpr(Id(foo), [BinaryOp(or, BinaryOp(<, Id(x), UnaryOp(-, NumLit(2.0))), BinaryOp(==, BinaryOp(..., StringLit(a'"), StringLit(a\')), StringLit(a'"a\')))]), [NumLit(3.0), NumLit(2.0)]))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 326))
        except:
            print(f"fail test case: 26. This test case is: ## expresion with concat string ")
    def testcase27(self):
        input = """##for in for
func main()
begin
var i<-0
var j<-0
var k<-0
number x<-readNumber()
for i until i<x/2 by 1 
for j until j<x/2 by 1 
for k until k<x/2 by 1 
x <- x + 1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), VarDecl(Id(k), None, var, NumLit(0.0)), VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), For(Id(i), BinaryOp(<, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), For(Id(j), BinaryOp(<, Id(j), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), For(Id(k), BinaryOp(<, Id(k), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), AssignStmt(Id(x), BinaryOp(+, Id(x), NumLit(1.0))))))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 327))
        except:
            print(f"fail test case: 27. This test case is: ##for in for")
    def testcase28(self):
        input = """## expresion in array lit 
func foo(number a) begin
if ((a=1) or (a=0)) return 1
return a*foo(a)
end

number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(foo(3))]]

func main()
begin
number a<- arr[foo(1),foo(3)%3]
return
end
"""
        expect = '''Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(=, Id(a), NumLit(1.0)), BinaryOp(=, Id(a), NumLit(0.0))), Return(NumLit(1.0))), [], None), Return(BinaryOp(*, Id(a), CallExpr(Id(foo), [Id(a)])))])), VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(*, NumLit(5.0), NumLit(6.0)), BinaryOp(%, NumLit(7.0), NumLit(2.0)), BinaryOp(*, UnaryOp(-, NumLit(3.13e-06)), CallExpr(Id(foo), [CallExpr(Id(foo), [NumLit(3.0)])]))))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, ArrayCell(Id(arr), [CallExpr(Id(foo), [NumLit(1.0)]), BinaryOp(%, CallExpr(Id(foo), [NumLit(3.0)]), NumLit(3.0))])), Return()]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 328))
        except:
            print(f"fail test case: 28. This test case is: ## expresion in array lit ")
    def testcase29(self):
        input = """## testcase 49 in TheHieu's parser test 
func main()
begin
number _ <- readNumber()
number __<- readNumber()
for _ until _*_ = _+_*_-2*_ by _+_
if (_) 
for _ until _/(_*_)%_ < _/(_*_+_) by _/_
if (_*_<_+_) begin
end
elif (__<_) if ((__+_/__ = _%__) and (__*_< -1)) for _ until _/(_*_)%_ < _/(_*_+_) by _/_ if (true) break 
else continue
else break
elif (true) continue
else break
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(_), NumberType, None, CallExpr(Id(readNumber), [])), VarDecl(Id(__), NumberType, None, CallExpr(Id(readNumber), [])), For(Id(_), BinaryOp(=, BinaryOp(*, Id(_), Id(_)), BinaryOp(-, BinaryOp(+, Id(_), BinaryOp(*, Id(_), Id(_))), BinaryOp(*, NumLit(2.0), Id(_)))), BinaryOp(+, Id(_), Id(_)), If((Id(_), For(Id(_), BinaryOp(<, BinaryOp(%, BinaryOp(/, Id(_), BinaryOp(*, Id(_), Id(_))), Id(_)), BinaryOp(/, Id(_), BinaryOp(+, BinaryOp(*, Id(_), Id(_)), Id(_)))), BinaryOp(/, Id(_), Id(_)), If((BinaryOp(<, BinaryOp(*, Id(_), Id(_)), BinaryOp(+, Id(_), Id(_))), Block([])), [(BinaryOp(<, Id(__), Id(_)), If((BinaryOp(and, BinaryOp(=, BinaryOp(+, Id(__), BinaryOp(/, Id(_), Id(__))), BinaryOp(%, Id(_), Id(__))), BinaryOp(<, BinaryOp(*, Id(__), Id(_)), UnaryOp(-, NumLit(1.0)))), For(Id(_), BinaryOp(<, BinaryOp(%, BinaryOp(/, Id(_), BinaryOp(*, Id(_), Id(_))), Id(_)), BinaryOp(/, Id(_), BinaryOp(+, BinaryOp(*, Id(_), Id(_)), Id(_)))), BinaryOp(/, Id(_), Id(_)), If((BooleanLit(True), Break), [], Continue))), [], Break)), (BooleanLit(True), Continue)], Break))), [], None))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 329))
        except:
            print(f"fail test case: 29. This test case is: ## testcase 49 in TheHieu's parser test ")
    def testcase30(self):
        input = """## complex bool expresion 
func main() 
begin
dynamic a
a <- ((A or B and C + 3*2%4/3)<=(not(-1+foo(x+y*(z-1)))))...(x!=y)
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, dynamic, None), AssignStmt(Id(a), BinaryOp(..., BinaryOp(<=, BinaryOp(and, BinaryOp(or, Id(A), Id(B)), BinaryOp(+, Id(C), BinaryOp(/, BinaryOp(%, BinaryOp(*, NumLit(3.0), NumLit(2.0)), NumLit(4.0)), NumLit(3.0)))), UnaryOp(not, BinaryOp(+, UnaryOp(-, NumLit(1.0)), CallExpr(Id(foo), [BinaryOp(+, Id(x), BinaryOp(*, Id(y), BinaryOp(-, Id(z), NumLit(1.0))))])))), BinaryOp(!=, Id(x), Id(y))))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 330))
        except:
            print(f"fail test case: 30. This test case is: ## complex bool expresion ")
    def testcase31(self):
        input = """## example code in assignment specification page 8
func foo(number a[5], string b)
begin
var i <- 0
for i until i >= 5 by 1
begin
a[i] <- i * i + 5
end
return -1
end
"""
        expect = '''Program([FuncDecl(Id(foo), [VarDecl(Id(a), ArrayType([5.0], NumberType), None, None), VarDecl(Id(b), StringType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), NumLit(5.0)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(a), [Id(i)]), BinaryOp(+, BinaryOp(*, Id(i), Id(i)), NumLit(5.0)))])), Return(UnaryOp(-, NumLit(1.0)))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 331))
        except:
            print(f"fail test case: 31. This test case is: ## example code in assignment specification page 8")
    def testcase32(self):
        input = """## block in block 
func main ()
begin
begin
begin
end
end
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([Block([Block([])])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 332))
        except:
            print(f"fail test case: 32. This test case is: ## block in block ")
    def testcase33(self):
        input = """## nested if to check ambigous. in this testcase, i use tab for for the match if 
func main() begin 
number a<- readNumber()
if (a>0) 
    if (a%2 = 0) 
        begin
        end
    else if (a<50) return
        elif (a<100) return
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, CallExpr(Id(readNumber), [])), If((BinaryOp(>, Id(a), NumLit(0.0)), If((BinaryOp(=, BinaryOp(%, Id(a), NumLit(2.0)), NumLit(0.0)), Block([])), [], If((BinaryOp(<, Id(a), NumLit(50.0)), Return()), [(BinaryOp(<, Id(a), NumLit(100.0)), Return())], None))), [], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 333))
        except:
            print(f"fail test case: 33. This test case is: ## nested if to check ambigous. in this testcase, i use tab for for the match if ")
    def testcase34(self):
        input = """## nested if to check ambigous. in this testcase, i use tab for for the match if 
func main() begin 
number a<- readNumber()
if (a<0) 
    if (-a%2 = 0) 
        begin
        end
    else if (a<50) return
        elif (a<100) return
        else return 
elif (a>10) 
    begin 
    end 
else return
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, CallExpr(Id(readNumber), [])), If((BinaryOp(<, Id(a), NumLit(0.0)), If((BinaryOp(=, BinaryOp(%, UnaryOp(-, Id(a)), NumLit(2.0)), NumLit(0.0)), Block([])), [], If((BinaryOp(<, Id(a), NumLit(50.0)), Return()), [(BinaryOp(<, Id(a), NumLit(100.0)), Return())], Return()))), [(BinaryOp(>, Id(a), NumLit(10.0)), Block([]))], Return())]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 334))
        except:
            print(f"fail test case: 34. This test case is: ## nested if to check ambigous. in this testcase, i use tab for for the match if ")
    def testcase35(self):
        input = """##check function return an array 
func returnArray() 
    return [[1,2,3,4],[2,3],2]
func main() begin 
    dynamic a <- returnArray()[0,1]
end
"""
        expect = '''Program([FuncDecl(Id(returnArray), [], Return(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(2.0), NumLit(3.0)), NumLit(2.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, dynamic, ArrayCell(CallExpr(Id(returnArray), []), [NumLit(0.0), NumLit(1.0)]))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 335))
        except:
            print(f"fail test case: 35. This test case is: ##check function return an array ")
    def testcase36(self):
        input = """## Bubble Sort Algorithm
func main()
begin
    number arr[5] <- [5, 1, 4, 2, 8] ## declaring and initializing an array of numbers
    var n <- 5 ## number of elements in the array
    dynamic i 
    dynamic j ## loop variables
    dynamic temp ## temporary variable for swapping
    i<-0
    for i until i > n-1 by 1
    begin
        j<-0
        for j  until j > n-i-2 by 1
        begin
            if (arr[j] > arr[j+1])
            begin
                ## Swap arr[j] and arr[j+1]
                temp <- arr[j]
                arr[j] <- arr[j+1]
                arr[j+1] <- temp
            end
        end
    end
    
    ## After sorting, print the sorted array
    writeString("Sorted Array: ")
    i<-0
    for i until i > n-1 by 1
    begin
        writeNumber(arr[i])
    end
    return
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(5.0), NumLit(1.0), NumLit(4.0), NumLit(2.0), NumLit(8.0))), VarDecl(Id(n), None, var, NumLit(5.0)), VarDecl(Id(i), None, dynamic, None), VarDecl(Id(j), None, dynamic, None), VarDecl(Id(temp), None, dynamic, None), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(-, Id(n), NumLit(1.0))), NumLit(1.0), Block([AssignStmt(Id(j), NumLit(0.0)), For(Id(j), BinaryOp(>, Id(j), BinaryOp(-, BinaryOp(-, Id(n), Id(i)), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(>, ArrayCell(Id(arr), [Id(j)]), ArrayCell(Id(arr), [BinaryOp(+, Id(j), NumLit(1.0))])), Block([AssignStmt(Id(temp), ArrayCell(Id(arr), [Id(j)])), AssignStmt(ArrayCell(Id(arr), [Id(j)]), ArrayCell(Id(arr), [BinaryOp(+, Id(j), NumLit(1.0))])), AssignStmt(ArrayCell(Id(arr), [BinaryOp(+, Id(j), NumLit(1.0))]), Id(temp))])), [], None)]))])), CallStmt(Id(writeString), [StringLit(Sorted Array: )]), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(-, Id(n), NumLit(1.0))), NumLit(1.0), Block([CallStmt(Id(writeNumber), [ArrayCell(Id(arr), [Id(i)])])])), Return()]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 336))
        except:
            print(f"fail test case: 36. This test case is: ## Bubble Sort Algorithm")
    def testcase37(self):
        input = """## function without implementation
func main()
func a(number b)
func c(number g[10],string s[10], bool bo[10])
"""
        expect = '''Program([FuncDecl(Id(main), [], None), FuncDecl(Id(a), [VarDecl(Id(b), NumberType, None, None)], None), FuncDecl(Id(c), [VarDecl(Id(g), ArrayType([10.0], NumberType), None, None), VarDecl(Id(s), ArrayType([10.0], StringType), None, None), VarDecl(Id(bo), ArrayType([10.0], BoolType), None, None)], None)])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 337))
        except:
            print(f"fail test case: 37. This test case is: ## function without implementation")
    def testcase38(self):
        input = """## array with float number 
number arr[3.14,1e9,1.]
"""
        expect = '''Program([VarDecl(Id(arr), ArrayType([3.14, 1000000000.0, 1.0], NumberType), None, None)])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 338))
        except:
            print(f"fail test case: 38. This test case is: ## array with float number ")
    def testcase39(self):
        input = """## if check again :)))
func main() begin 
if (true) 
    if (true) 
        begin
        end
    elif (false)
        begin
        end
end 
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((BooleanLit(True), If((BooleanLit(True), Block([])), [(BooleanLit(False), Block([]))], None)), [], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 339))
        except:
            print(f"fail test case: 39. This test case is: ## if check again :)))")
    def testcase40(self):
        input = """## complex expression 
string s <- "hallo"
dynamic a<- (("abc"...s) == "aa") or false and true or not (2+3*sin(x)%pi/(3%2)/-4>5) or (1=2)
"""
        expect = '''Program([VarDecl(Id(s), StringType, None, StringLit(hallo)), VarDecl(Id(a), None, dynamic, BinaryOp(or, BinaryOp(or, BinaryOp(and, BinaryOp(or, BinaryOp(==, BinaryOp(..., StringLit(abc), Id(s)), StringLit(aa)), BooleanLit(False)), BooleanLit(True)), UnaryOp(not, BinaryOp(>, BinaryOp(+, NumLit(2.0), BinaryOp(/, BinaryOp(/, BinaryOp(%, BinaryOp(*, NumLit(3.0), CallExpr(Id(sin), [Id(x)])), Id(pi)), BinaryOp(%, NumLit(3.0), NumLit(2.0))), UnaryOp(-, NumLit(4.0)))), NumLit(5.0)))), BinaryOp(=, NumLit(1.0), NumLit(2.0))))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 340))
        except:
            print(f"fail test case: 40. This test case is: ## complex expression ")
    def testcase41(self):
        input = """## complex expresion
string text <- "world"
dynamic result <- (length(text) > 3) and (substring(text, 0, 3) == "wor") or (false and not(true)) or (cos(2*pi) = 1)
"""
        expect = '''Program([VarDecl(Id(text), StringType, None, StringLit(world)), VarDecl(Id(result), None, dynamic, BinaryOp(or, BinaryOp(or, BinaryOp(and, BinaryOp(>, CallExpr(Id(length), [Id(text)]), NumLit(3.0)), BinaryOp(==, CallExpr(Id(substring), [Id(text), NumLit(0.0), NumLit(3.0)]), StringLit(wor))), BinaryOp(and, BooleanLit(False), UnaryOp(not, BooleanLit(True)))), BinaryOp(=, CallExpr(Id(cos), [BinaryOp(*, NumLit(2.0), Id(pi))]), NumLit(1.0))))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 341))
        except:
            print(f"fail test case: 41. This test case is: ## complex expresion")
    def testcase42(self):
        input = """## simple expresion 
string s <- "abc"..."abc"
"""
        expect = '''Program([VarDecl(Id(s), StringType, None, BinaryOp(..., StringLit(abc), StringLit(abc)))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 342))
        except:
            print(f"fail test case: 42. This test case is: ## simple expresion ")
    def testcase43(self):
        input = """## simple expresion 
bool s <- ("abc"..."abc") == "abcabc"
"""
        expect = '''Program([VarDecl(Id(s), BoolType, None, BinaryOp(==, BinaryOp(..., StringLit(abc), StringLit(abc)), StringLit(abcabc)))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 343))
        except:
            print(f"fail test case: 43. This test case is: ## simple expresion ")
    def testcase44(self):
        input = """## simple expresion
func inc(number x) return x+1
number a <-  inc(inc(inc(inc(3))))
"""
        expect = '''Program([FuncDecl(Id(inc), [VarDecl(Id(x), NumberType, None, None)], Return(BinaryOp(+, Id(x), NumLit(1.0)))), VarDecl(Id(a), NumberType, None, CallExpr(Id(inc), [CallExpr(Id(inc), [CallExpr(Id(inc), [CallExpr(Id(inc), [NumLit(3.0)])])])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 344))
        except:
            print(f"fail test case: 44. This test case is: ## simple expresion")
    def testcase45(self):
        input = """## simple expresion 
func xor(bool a, bool b) return (a and not b) or (not a and b)
bool a<- xor(true,false) or xor(false,true) or not (xor(true,true))
"""
        expect = '''Program([FuncDecl(Id(xor), [VarDecl(Id(a), BoolType, None, None), VarDecl(Id(b), BoolType, None, None)], Return(BinaryOp(or, BinaryOp(and, Id(a), UnaryOp(not, Id(b))), BinaryOp(and, UnaryOp(not, Id(a)), Id(b))))), VarDecl(Id(a), BoolType, None, BinaryOp(or, BinaryOp(or, CallExpr(Id(xor), [BooleanLit(True), BooleanLit(False)]), CallExpr(Id(xor), [BooleanLit(False), BooleanLit(True)])), UnaryOp(not, CallExpr(Id(xor), [BooleanLit(True), BooleanLit(True)]))))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 345))
        except:
            print(f"fail test case: 45. This test case is: ## simple expresion ")
    def testcase46(self):
        input = """## just stupid testcase with all kinds of operation
dynamic a<- x...b==c or d + e / f + not - i[4]
"""
        expect = '''Program([VarDecl(Id(a), None, dynamic, BinaryOp(..., Id(x), BinaryOp(==, Id(b), BinaryOp(or, Id(c), BinaryOp(+, BinaryOp(+, Id(d), BinaryOp(/, Id(e), Id(f))), UnaryOp(not, UnaryOp(-, ArrayCell(Id(i), [NumLit(4.0)]))))))))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 346))
        except:
            print(f"fail test case: 46. This test case is: ## just stupid testcase with all kinds of operation")
    def testcase47(self):
        input = r"""## Tower of Hanoi 
func print(string src, string dst, string aux)

func tower_of_hanoi(number n, string src, string dst, string aux)
begin
    if (n = 1) print(src, dst)
    else begin
        tower_of_hanoi(n - 1, src, aux, dst)
        tower_of_hanoi(1, src, dst, aux)
        tower_of_hanoi(n - 1, aux, dst, src)
    end
end

func print(string src, string dst) begin
    output <- "Move 1 disk from tower "
    output <- output ... src
    output <- output ... " to tower "
    output <- output ... des
    output <- output ... "\n"
    writeString(output)
end
"""
        expect = r'''Program([FuncDecl(Id(print), [VarDecl(Id(src), StringType, None, None), VarDecl(Id(dst), StringType, None, None), VarDecl(Id(aux), StringType, None, None)], None), FuncDecl(Id(tower_of_hanoi), [VarDecl(Id(n), NumberType, None, None), VarDecl(Id(src), StringType, None, None), VarDecl(Id(dst), StringType, None, None), VarDecl(Id(aux), StringType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(1.0)), CallStmt(Id(print), [Id(src), Id(dst)])), [], Block([CallStmt(Id(tower_of_hanoi), [BinaryOp(-, Id(n), NumLit(1.0)), Id(src), Id(aux), Id(dst)]), CallStmt(Id(tower_of_hanoi), [NumLit(1.0), Id(src), Id(dst), Id(aux)]), CallStmt(Id(tower_of_hanoi), [BinaryOp(-, Id(n), NumLit(1.0)), Id(aux), Id(dst), Id(src)])]))])), FuncDecl(Id(print), [VarDecl(Id(src), StringType, None, None), VarDecl(Id(dst), StringType, None, None)], Block([AssignStmt(Id(output), StringLit(Move 1 disk from tower )), AssignStmt(Id(output), BinaryOp(..., Id(output), Id(src))), AssignStmt(Id(output), BinaryOp(..., Id(output), StringLit( to tower ))), AssignStmt(Id(output), BinaryOp(..., Id(output), Id(des))), AssignStmt(Id(output), BinaryOp(..., Id(output), StringLit(\n))), CallStmt(Id(writeString), [Id(output)])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 347))
        except:
            print(f"fail test case: 47. This test case is: ## Tower of Hanoi ")
    def testcase48(self):
        input = """## n-queens with zcode
func printSolution(number board[100, 100], number n)
begin
    var i <- 0
    var j <- 0
	for i until i >= n by 1 begin
		for j until j >= n by 1
            if (board[i, j]) writeString("Q ")
		    else writeString(". ")
		printf("\\n")
	end
end

func isSafe(number board[100, 100], number n, number row, number col) begin
	var i <- 0
    var j <- 0
	for i until i >= col by 1
		if (board[row, i])
			return false
    
    i <- row
    j <- col
	for i until ((i < 0) or (j < 0)) by -1 begin
		if (board[i, j])
			return false
        j <- j - 1
    end
    
    i <- row
    j <- col
	for i until ((i >= n) or (j < 0)) by 1 begin
		if (board[i, j])
			return false
        j <- j - 1
    end
	
    return true
end

func solverec(number board[100, 100], number col, number n) begin
    if (col >= n) return true
    
    var i <- 0
    for i until i >= n by 1 begin
		if (isSafe(board, n, i, col)) begin
			board[i, col] <- 1
			if (solverec(board, col + 1, n)) return true
			board[i, col] <- 0
		end
	end
	
    return false
end

func solve(number n)
begin
    number board[100, 100]
    var i <- 0
    var j <- 0
    for i until i >= n by 1
        for j until j >= n by 1
            board[i, j] <- 0
    
    if (not solverec(board, 0, n)) writeString("No solution")
    else printSolution(board, n)
end
"""
        expect = '''Program([FuncDecl(Id(printSolution), [VarDecl(Id(board), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), Block([For(Id(j), BinaryOp(>=, Id(j), Id(n)), NumLit(1.0), If((ArrayCell(Id(board), [Id(i), Id(j)]), CallStmt(Id(writeString), [StringLit(Q )])), [], CallStmt(Id(writeString), [StringLit(. )]))), CallStmt(Id(printf), [StringLit(\\n)])]))])), FuncDecl(Id(isSafe), [VarDecl(Id(board), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(row), NumberType, None, None), VarDecl(Id(col), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(col)), NumLit(1.0), If((ArrayCell(Id(board), [Id(row), Id(i)]), Return(BooleanLit(False))), [], None)), AssignStmt(Id(i), Id(row)), AssignStmt(Id(j), Id(col)), For(Id(i), BinaryOp(or, BinaryOp(<, Id(i), NumLit(0.0)), BinaryOp(<, Id(j), NumLit(0.0))), UnaryOp(-, NumLit(1.0)), Block([If((ArrayCell(Id(board), [Id(i), Id(j)]), Return(BooleanLit(False))), [], None), AssignStmt(Id(j), BinaryOp(-, Id(j), NumLit(1.0)))])), AssignStmt(Id(i), Id(row)), AssignStmt(Id(j), Id(col)), For(Id(i), BinaryOp(or, BinaryOp(>=, Id(i), Id(n)), BinaryOp(<, Id(j), NumLit(0.0))), NumLit(1.0), Block([If((ArrayCell(Id(board), [Id(i), Id(j)]), Return(BooleanLit(False))), [], None), AssignStmt(Id(j), BinaryOp(-, Id(j), NumLit(1.0)))])), Return(BooleanLit(True))])), FuncDecl(Id(solverec), [VarDecl(Id(board), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(col), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(>=, Id(col), Id(n)), Return(BooleanLit(True))), [], None), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), Block([If((CallExpr(Id(isSafe), [Id(board), Id(n), Id(i), Id(col)]), Block([AssignStmt(ArrayCell(Id(board), [Id(i), Id(col)]), NumLit(1.0)), If((CallExpr(Id(solverec), [Id(board), BinaryOp(+, Id(col), NumLit(1.0)), Id(n)]), Return(BooleanLit(True))), [], None), AssignStmt(ArrayCell(Id(board), [Id(i), Id(col)]), NumLit(0.0))])), [], None)])), Return(BooleanLit(False))])), FuncDecl(Id(solve), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(board), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), For(Id(j), BinaryOp(>=, Id(j), Id(n)), NumLit(1.0), AssignStmt(ArrayCell(Id(board), [Id(i), Id(j)]), NumLit(0.0)))), If((UnaryOp(not, CallExpr(Id(solverec), [Id(board), NumLit(0.0), Id(n)])), CallStmt(Id(writeString), [StringLit(No solution)])), [], CallStmt(Id(printSolution), [Id(board), Id(n)]))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 348))
        except:
            print(f"fail test case: 48. This test case is: ## n-queens with zcode")
    def testcase49(self):
        input = """## fibonanci recursively
func fibo(number x) begin 
    if (x=0) return 1
    if (x=1) return 2
    return fibo(x-1)+fibo(x-2)
end
func main() begin 
    writeNumber(fibo(3))
end
"""
        expect = '''Program([FuncDecl(Id(fibo), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(=, Id(x), NumLit(0.0)), Return(NumLit(1.0))), [], None), If((BinaryOp(=, Id(x), NumLit(1.0)), Return(NumLit(2.0))), [], None), Return(BinaryOp(+, CallExpr(Id(fibo), [BinaryOp(-, Id(x), NumLit(1.0))]), CallExpr(Id(fibo), [BinaryOp(-, Id(x), NumLit(2.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(fibo), [NumLit(3.0)])])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 349))
        except:
            print(f"fail test case: 49. This test case is: ## fibonanci recursively")
    def testcase50(self):
        input = """## assignment check 
func main() begin 
    number a[4,6,7,8]
    a[3,2,1,ahahaha(4)] <- 1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(ArrayCell(Id(a), [NumLit(3.0), NumLit(2.0), NumLit(1.0), CallExpr(Id(ahahaha), [NumLit(4.0)])]), NumLit(1.0))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 350))
        except:
            print(f"fail test case: 50. This test case is: ## assignment check ")
    def testcase51(self):
        input = """## assignment check 
func main() begin 
    number a[4,6,7,8]
    a <- [1,2,3]
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(Id(a), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 351))
        except:
            print(f"fail test case: 51. This test case is: ## assignment check ")
    def testcase52(self):
        input = """## assignment check 
func main() begin 
    number a[4,6,7,8]
    a[3,true,1,ahahaha(4)] <- 1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(ArrayCell(Id(a), [NumLit(3.0), BooleanLit(True), NumLit(1.0), CallExpr(Id(ahahaha), [NumLit(4.0)])]), NumLit(1.0))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 352))
        except:
            print(f"fail test case: 52. This test case is: ## assignment check ")
    def testcase53(self):
        input = """##declaration check 
number a<-2
"""
        expect = '''Program([VarDecl(Id(a), NumberType, None, NumLit(2.0))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 353))
        except:
            print(f"fail test case: 53. This test case is: ##declaration check ")
    def testcase54(self):
        input = """##declaration check 
string a
"""
        expect = '''Program([VarDecl(Id(a), StringType, None, None)])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 354))
        except:
            print(f"fail test case: 54. This test case is: ##declaration check ")
    def testcase55(self):
        input = """##declaration check 
string a<-2
"""
        expect = '''Program([VarDecl(Id(a), StringType, None, NumLit(2.0))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 355))
        except:
            print(f"fail test case: 55. This test case is: ##declaration check ")
    def testcase56(self):
        input = """##declaration check 
bool a<-2
"""
        expect = '''Program([VarDecl(Id(a), BoolType, None, NumLit(2.0))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 356))
        except:
            print(f"fail test case: 56. This test case is: ##declaration check ")
    def testcase57(self):
        input = """##declaration check 
var a<-2
"""
        expect = '''Program([VarDecl(Id(a), None, var, NumLit(2.0))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 357))
        except:
            print(f"fail test case: 57. This test case is: ##declaration check ")
    def testcase58(self):
        input = """##declaration check 
dynamic a
"""
        expect = '''Program([VarDecl(Id(a), None, dynamic, None)])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 358))
        except:
            print(f"fail test case: 58. This test case is: ##declaration check ")
    def testcase59(self):
        input = """## array is a expression too
func main()
begin
number b<-1
var a<- --------[1,2]*----------------b
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), NumberType, None, NumLit(1.0)), VarDecl(Id(a), None, var, BinaryOp(*, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, ArrayLit(NumLit(1.0), NumLit(2.0)))))))))), UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, Id(b)))))))))))))))))))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 359))
        except:
            print(f"fail test case: 59. This test case is: ## array is a expression too")
    def testcase60(self):
        input = """## a lot of minus 
func main()
begin
number b<-1
var a<- --------1*----------------b
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(b), NumberType, None, NumLit(1.0)), VarDecl(Id(a), None, var, BinaryOp(*, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0))))))))), UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, Id(b)))))))))))))))))))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 360))
        except:
            print(f"fail test case: 60. This test case is: ## a lot of minus ")
    def testcase61(self):
        input = """## only function call
func main() begin 
doNoThing()
hello("TheHieu")
testcase(h[14,2])
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([CallStmt(Id(doNoThing), []), CallStmt(Id(hello), [StringLit(TheHieu)]), CallStmt(Id(testcase), [ArrayCell(Id(h), [NumLit(14.0), NumLit(2.0)])])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 361))
        except:
            print(f"fail test case: 61. This test case is: ## only function call")
    def testcase62(self):
        input = """## check numlit 
var a<- 1.e91
number b<- -3.255e-4
"""
        expect = '''Program([VarDecl(Id(a), None, var, NumLit(1e+91)), VarDecl(Id(b), NumberType, None, UnaryOp(-, NumLit(0.0003255)))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 362))
        except:
            print(f"fail test case: 62. This test case is: ## check numlit ")
    def testcase63(self):
        input = """## this code with alot of newline


func main()


begin 
if (a=2) 



a<-2


end 

"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((BinaryOp(=, Id(a), NumLit(2.0)), AssignStmt(Id(a), NumLit(2.0))), [], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 363))
        except:
            print(f"fail test case: 63. This test case is: ## this code with alot of newline")
    def testcase64(self):
        input = """## if if else else 
func main() begin 
bool a<-true 
bool b<-false 
if (not a) 
    if (b) writeString("b is correct")
    else writeString("b is not correct")
else writeString("a is correct")
return
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), BoolType, None, BooleanLit(True)), VarDecl(Id(b), BoolType, None, BooleanLit(False)), If((UnaryOp(not, Id(a)), If((Id(b), CallStmt(Id(writeString), [StringLit(b is correct)])), [], CallStmt(Id(writeString), [StringLit(b is not correct)]))), [], CallStmt(Id(writeString), [StringLit(a is correct)])), Return()]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 364))
        except:
            print(f"fail test case: 64. This test case is: ## if if else else ")
    def testcase65(self):
        input = """## if elif if elif elif else 
func main()
begin 
if(1) return 
elif (2) 
    if (3) return 
    elif (4) return 
    elif (5) return 
    else return
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), Return()), [(NumLit(2.0), If((NumLit(3.0), Return()), [(NumLit(4.0), Return()), (NumLit(5.0), Return())], Return()))], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 365))
        except:
            print(f"fail test case: 65. This test case is: ## if elif if elif elif else ")
    def testcase66(self):
        input = """##BST with Zcode 
func initTree(number tree[100,3]) begin 
    var i<-0 
    for i until i=100 by 1
        begin 
            tree[i,0] <- -1
            tree[i,1] <- -1
            tree[i,2] <- -1
        end
end

func appendNode(number val,number head,number tree[100,3],bool freeNode[100])
begin 
number node <- 0 
for node until node=100 by 1
    if (freeNode[node]) break 
freeNode[node] <- false 
tree[node,0] <- val 
if (head = -1) return node 
var i <- 0 
number currNode <- 0
for i until i=100 by 1 
begin 
if (tree[node,0] < tree[currNode,0])
    begin 
        if (tree[currNode,1]!=-1) currNode <- tree[currNode,1]
        else tree[currNode,1] <- node 
    end
else begin
    if (tree[currNode,2]!=-1) currNode <- tree[currNode,2]
    else tree[currNode,2] <- node
end
end 
return head
end 

func main() begin 
number tree[100,3]
bool freeNode[100]
number head <- -1
initTree(tree)
var i<-0 
for i until i=100 by 1
    freeNode[i] <- true
i<-0 
for i until i=100 by 1
    begin 
        number val <- readNumber()
        head <- appendNode(val,head,tree, freeNode)
    end
end
"""
        expect = '''Program([FuncDecl(Id(initTree), [VarDecl(Id(tree), ArrayType([100.0, 3.0], NumberType), None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(tree), [Id(i), NumLit(0.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(ArrayCell(Id(tree), [Id(i), NumLit(1.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(ArrayCell(Id(tree), [Id(i), NumLit(2.0)]), UnaryOp(-, NumLit(1.0)))]))])), FuncDecl(Id(appendNode), [VarDecl(Id(val), NumberType, None, None), VarDecl(Id(head), NumberType, None, None), VarDecl(Id(tree), ArrayType([100.0, 3.0], NumberType), None, None), VarDecl(Id(freeNode), ArrayType([100.0], BoolType), None, None)], Block([VarDecl(Id(node), NumberType, None, NumLit(0.0)), For(Id(node), BinaryOp(=, Id(node), NumLit(100.0)), NumLit(1.0), If((ArrayCell(Id(freeNode), [Id(node)]), Break), [], None)), AssignStmt(ArrayCell(Id(freeNode), [Id(node)]), BooleanLit(False)), AssignStmt(ArrayCell(Id(tree), [Id(node), NumLit(0.0)]), Id(val)), If((BinaryOp(=, Id(head), UnaryOp(-, NumLit(1.0))), Return(Id(node))), [], None), VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(currNode), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), Block([If((BinaryOp(<, ArrayCell(Id(tree), [Id(node), NumLit(0.0)]), ArrayCell(Id(tree), [Id(currNode), NumLit(0.0)])), Block([If((BinaryOp(!=, ArrayCell(Id(tree), [Id(currNode), NumLit(1.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(Id(currNode), ArrayCell(Id(tree), [Id(currNode), NumLit(1.0)]))), [], AssignStmt(ArrayCell(Id(tree), [Id(currNode), NumLit(1.0)]), Id(node)))])), [], Block([If((BinaryOp(!=, ArrayCell(Id(tree), [Id(currNode), NumLit(2.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(Id(currNode), ArrayCell(Id(tree), [Id(currNode), NumLit(2.0)]))), [], AssignStmt(ArrayCell(Id(tree), [Id(currNode), NumLit(2.0)]), Id(node)))]))])), Return(Id(head))])), FuncDecl(Id(main), [], Block([VarDecl(Id(tree), ArrayType([100.0, 3.0], NumberType), None, None), VarDecl(Id(freeNode), ArrayType([100.0], BoolType), None, None), VarDecl(Id(head), NumberType, None, UnaryOp(-, NumLit(1.0))), CallStmt(Id(initTree), [Id(tree)]), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), AssignStmt(ArrayCell(Id(freeNode), [Id(i)]), BooleanLit(True))), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), Block([VarDecl(Id(val), NumberType, None, CallExpr(Id(readNumber), [])), AssignStmt(Id(head), CallExpr(Id(appendNode), [Id(val), Id(head), Id(tree), Id(freeNode)]))]))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 366))
        except:
            print(f"fail test case: 66. This test case is: ##BST with Zcode ")
    def testcase67(self):
        input = """## count the number of digits of a number 
func main() begin 
var num <- readNumber() 
number count <- 1 
number core <- 10 
for core until false by 0
    if (num < core) break
    else core <- 10*core
    count<-count+1
writeNumber(num)
writeString(" has ")
writeNumber(count) 
writeString(" digits.")
end 
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(num), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(count), NumberType, None, NumLit(1.0)), VarDecl(Id(core), NumberType, None, NumLit(10.0)), For(Id(core), BooleanLit(False), NumLit(0.0), If((BinaryOp(<, Id(num), Id(core)), Break), [], AssignStmt(Id(core), BinaryOp(*, NumLit(10.0), Id(core))))), AssignStmt(Id(count), BinaryOp(+, Id(count), NumLit(1.0))), CallStmt(Id(writeNumber), [Id(num)]), CallStmt(Id(writeString), [StringLit( has )]), CallStmt(Id(writeNumber), [Id(count)]), CallStmt(Id(writeString), [StringLit( digits.)])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 367))
        except:
            print(f"fail test case: 67. This test case is: ## count the number of digits of a number ")
    def testcase68(self):
        input = """##declare in statement without block
func main() 
begin 
    if (1) number a[3,2] <- [[1,2],[3,4],[5,6]]
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), VarDecl(Id(a), ArrayType([3.0, 2.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(5.0), NumLit(6.0))))), [], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 368))
        except:
            print(f"fail test case: 68. This test case is: ##declare in statement without block")
    def testcase69(self):
        input = """##declare in statement without block
func main() 
begin 
    for i until i!=0 by 1 dynamic i
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(!=, Id(i), NumLit(0.0)), NumLit(1.0), VarDecl(Id(i), None, dynamic, None))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 369))
        except:
            print(f"fail test case: 69. This test case is: ##declare in statement without block")
    def testcase70(self):
        input = """##declare in statement without block
func main() 
begin 
    if (1) string s <- "kkk"
    elif (2) string s <- "TheHieu"
    else bool b <- false
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), VarDecl(Id(s), StringType, None, StringLit(kkk))), [(NumLit(2.0), VarDecl(Id(s), StringType, None, StringLit(TheHieu)))], VarDecl(Id(b), BoolType, None, BooleanLit(False)))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 370))
        except:
            print(f"fail test case: 70. This test case is: ##declare in statement without block")
    def testcase71(self):
        input = """##declare in statement without block
func main() 
begin 
    if (1) string a[3,2] <- [[1,2],[3,4],[5,6]]
    else number b[4,4,4]
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), VarDecl(Id(a), ArrayType([3.0, 2.0], StringType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(5.0), NumLit(6.0))))), [], VarDecl(Id(b), ArrayType([4.0, 4.0, 4.0], NumberType), None, None))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 371))
        except:
            print(f"fail test case: 71. This test case is: ##declare in statement without block")
    def testcase72(self):
        input = """## use identifier nearly the same with key words
func main()
begin 
    dynamic for_ 
    var var_  <- for_ 
    if(var_) for_<-1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(for_), None, dynamic, None), VarDecl(Id(var_), None, var, Id(for_)), If((Id(var_), AssignStmt(Id(for_), NumLit(1.0))), [], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 372))
        except:
            print(f"fail test case: 72. This test case is: ## use identifier nearly the same with key words")
    def testcase73(self):
        input = """## use identifier nearly the same with key words
func main()
begin 
    dynamic for_ 
    var var_  <- for_ 
    if_ (var_)
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(for_), None, dynamic, None), VarDecl(Id(var_), None, var, Id(for_)), CallStmt(Id(if_), [Id(var_)])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 373))
        except:
            print(f"fail test case: 73. This test case is: ## use identifier nearly the same with key words")
    def testcase74(self):
        input = """## string using ## 
func main()
begin 
    string s<-"this test case is to check if it is work normally if ## in the string"
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(s), StringType, None, StringLit(this test case is to check if it is work normally if ## in the string))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 374))
        except:
            print(f"fail test case: 74. This test case is: ## string using ## ")
    def testcase75(self):
        input = """## exmaple of block in Zcode specification page 12
func main() begin
number r
number s
r <- 2.0
number a[5]
number b[5]
s <- r * r * 3.14
a[0] <- s
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(r), NumberType, None, None), VarDecl(Id(s), NumberType, None, None), AssignStmt(Id(r), NumLit(2.0)), VarDecl(Id(a), ArrayType([5.0], NumberType), None, None), VarDecl(Id(b), ArrayType([5.0], NumberType), None, None), AssignStmt(Id(s), BinaryOp(*, BinaryOp(*, Id(r), Id(r)), NumLit(3.14))), AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), Id(s))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 375))
        except:
            print(f"fail test case: 75. This test case is: ## exmaple of block in Zcode specification page 12")
    def testcase76(self):
        input = """## testcase in forum by me. Link: https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=4591
func main() begin
if (1)
	if (2)
		b()
	elif (3)
		if (4)
			c()
		elif (5)
			d()
		else e()
	elif(6)
		f()
	else g()
elif (7) h()
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), If((NumLit(2.0), CallStmt(Id(b), [])), [(NumLit(3.0), If((NumLit(4.0), CallStmt(Id(c), [])), [(NumLit(5.0), CallStmt(Id(d), []))], CallStmt(Id(e), []))), (NumLit(6.0), CallStmt(Id(f), []))], CallStmt(Id(g), []))), [(NumLit(7.0), CallStmt(Id(h), []))], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 376))
        except:
            print(f"fail test case: 76. This test case is: ## testcase in forum by me. Link: https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=4591")
    def testcase77(self):
        input = """## testcase in forum by me. Link: https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=4591
func main() begin
var i<-0 
if (1) 
	for i until i=10 by 1
		if (2) return
		elif (3) return
		else  return
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), If((NumLit(1.0), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), If((NumLit(2.0), Return()), [(NumLit(3.0), Return())], Return()))), [], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 377))
        except:
            print(f"fail test case: 77. This test case is: ## testcase in forum by me. Link: https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=4591")
    def testcase78(self):
        input = r"""## check nested if with for loop
number LOOP_COUNT <- 0
func toAsciiCode(string s)
begin 
string ascii[96] <- [" ","!","'"","#","$","%","&","\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~",""]
number i<-0
for i until s == ascii[i] by 1
    i<-i+1
return i+32
end

func doNoThing(number n) return n
func main() begin
    number i<-0
    if (toAsciiCode("g") % 3 = 0)
        if (toAssciiCode("b") = doNoThing(toAsciiCode("b")/3)*3)
            for i until i<=doNoThing(3) by 1 LOOP_COUNT<- LOOP_COUNT ----1
        elif (toAsciiCode("b")=i) 
            if (i*i*i%128 = toAsciiCode("H"))
            for i until i<=doNoThing(100) by 1 
                if (true and true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                else for i until i<=doNoThing(100) by 1 
                    if (true) LOOP_COUNT <- LOOP_COUNT + 1 - 2 * 0
                    else i<-1--i 
end
"""
        expect = r'''Program([VarDecl(Id(LOOP_COUNT), NumberType, None, NumLit(0.0)), FuncDecl(Id(toAsciiCode), [VarDecl(Id(s), StringType, None, None)], Block([VarDecl(Id(ascii), ArrayType([96.0], StringType), None, ArrayLit(StringLit( ), StringLit(!), StringLit('"), StringLit(#), StringLit($), StringLit(%), StringLit(&), StringLit(\'), StringLit((), StringLit()), StringLit(*), StringLit(+), StringLit(,), StringLit(-), StringLit(.), StringLit(/), StringLit(0), StringLit(1), StringLit(2), StringLit(3), StringLit(4), StringLit(5), StringLit(6), StringLit(7), StringLit(8), StringLit(9), StringLit(:), StringLit(;), StringLit(<), StringLit(=), StringLit(>), StringLit(?), StringLit(@), StringLit(A), StringLit(B), StringLit(C), StringLit(D), StringLit(E), StringLit(F), StringLit(G), StringLit(H), StringLit(I), StringLit(J), StringLit(K), StringLit(L), StringLit(M), StringLit(N), StringLit(O), StringLit(P), StringLit(Q), StringLit(R), StringLit(S), StringLit(T), StringLit(U), StringLit(V), StringLit(W), StringLit(X), StringLit(Y), StringLit(Z), StringLit([), StringLit(\\), StringLit(]), StringLit(^), StringLit(_), StringLit(`), StringLit(a), StringLit(b), StringLit(c), StringLit(d), StringLit(e), StringLit(f), StringLit(g), StringLit(h), StringLit(i), StringLit(j), StringLit(k), StringLit(l), StringLit(m), StringLit(n), StringLit(o), StringLit(p), StringLit(q), StringLit(r), StringLit(s), StringLit(t), StringLit(u), StringLit(v), StringLit(w), StringLit(x), StringLit(y), StringLit(z), StringLit({), StringLit(|), StringLit(}), StringLit(~), StringLit())), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(==, Id(s), ArrayCell(Id(ascii), [Id(i)])), NumLit(1.0), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))), Return(BinaryOp(+, Id(i), NumLit(32.0)))])), FuncDecl(Id(doNoThing), [VarDecl(Id(n), NumberType, None, None)], Return(Id(n))), FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), If((BinaryOp(=, BinaryOp(%, CallExpr(Id(toAsciiCode), [StringLit(g)]), NumLit(3.0)), NumLit(0.0)), If((BinaryOp(=, CallExpr(Id(toAssciiCode), [StringLit(b)]), BinaryOp(*, CallExpr(Id(doNoThing), [BinaryOp(/, CallExpr(Id(toAsciiCode), [StringLit(b)]), NumLit(3.0))]), NumLit(3.0))), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(3.0)])), NumLit(1.0), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, Id(LOOP_COUNT), UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0)))))))), [(BinaryOp(=, CallExpr(Id(toAsciiCode), [StringLit(b)]), Id(i)), If((BinaryOp(=, BinaryOp(%, BinaryOp(*, BinaryOp(*, Id(i), Id(i)), Id(i)), NumLit(128.0)), CallExpr(Id(toAsciiCode), [StringLit(H)])), For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BinaryOp(and, BooleanLit(True), BooleanLit(True)), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], For(Id(i), BinaryOp(<=, Id(i), CallExpr(Id(doNoThing), [NumLit(100.0)])), NumLit(1.0), If((BooleanLit(True), AssignStmt(Id(LOOP_COUNT), BinaryOp(-, BinaryOp(+, Id(LOOP_COUNT), NumLit(1.0)), BinaryOp(*, NumLit(2.0), NumLit(0.0))))), [], AssignStmt(Id(i), BinaryOp(-, NumLit(1.0), UnaryOp(-, Id(i))))))))), [], None))], None)), [], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 378))
        except:
            print(f"fail test case: 78. This test case is: ## check nested if with for loop")
    def testcase79(self):
        input = r"""## print function 
func print(string src, string dst) begin
    output <- "Move 1 disk from tower "
    output <- output ... src
    output <- output ... " to tower "
    output <- output ... des
    output <- output ... "\n"
    writeString(output)
end
"""
        expect = r'''Program([FuncDecl(Id(print), [VarDecl(Id(src), StringType, None, None), VarDecl(Id(dst), StringType, None, None)], Block([AssignStmt(Id(output), StringLit(Move 1 disk from tower )), AssignStmt(Id(output), BinaryOp(..., Id(output), Id(src))), AssignStmt(Id(output), BinaryOp(..., Id(output), StringLit( to tower ))), AssignStmt(Id(output), BinaryOp(..., Id(output), Id(des))), AssignStmt(Id(output), BinaryOp(..., Id(output), StringLit(\n))), CallStmt(Id(writeString), [Id(output)])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 379))
        except:
            print(f"fail test case: 79. This test case is: ## print function ")
    def testcase80(self):
        input = """## only function call
func main() begin 
doNoThing()
hello("HelloTheHieu")
testcase(h[14,2])
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([CallStmt(Id(doNoThing), []), CallStmt(Id(hello), [StringLit(HelloTheHieu)]), CallStmt(Id(testcase), [ArrayCell(Id(h), [NumLit(14.0), NumLit(2.0)])])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 380))
        except:
            print(f"fail test case: 80. This test case is: ## only function call")
    def testcase81(self):
        input = """## expresion in array lit 
func foo(number a) begin
if ((a=1) or (a=0)) return 1
return a*foo(a)+3
end

number arr[2,3] <- [[1,2,3],[5*6,7%2,-3.13E-6*foo(4)*foo(foo(3))]]
"""
        expect = '''Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(=, Id(a), NumLit(1.0)), BinaryOp(=, Id(a), NumLit(0.0))), Return(NumLit(1.0))), [], None), Return(BinaryOp(+, BinaryOp(*, Id(a), CallExpr(Id(foo), [Id(a)])), NumLit(3.0)))])), VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(*, NumLit(5.0), NumLit(6.0)), BinaryOp(%, NumLit(7.0), NumLit(2.0)), BinaryOp(*, BinaryOp(*, UnaryOp(-, NumLit(3.13e-06)), CallExpr(Id(foo), [NumLit(4.0)])), CallExpr(Id(foo), [CallExpr(Id(foo), [NumLit(3.0)])])))))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 381))
        except:
            print(f"fail test case: 81. This test case is: ## expresion in array lit ")
    def testcase82(self):
        input = """## hello world
var str <- "Hello world!"
"""
        expect = '''Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 382))
        except:
            print(f"fail test case: 82. This test case is: ## hello world")
    def testcase83(self):
        input = """##single declaration
number a 
"""
        expect = '''Program([VarDecl(Id(a), NumberType, None, None)])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 383))
        except:
            print(f"fail test case: 83. This test case is: ##single declaration")
    def testcase84(self):
        input = """## array declaration check
func foo(number a) return a+1
number a[2,3] <- [[1+2,3,"abc",foo(4)],[true,false,true]]
"""
        expect = '''Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(3.0), StringLit(abc), CallExpr(Id(foo), [NumLit(4.0)])), ArrayLit(BooleanLit(True), BooleanLit(False), BooleanLit(True))))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 384))
        except:
            print(f"fail test case: 84. This test case is: ## array declaration check")
    def testcase85(self):
        input = """ ##mergesort with zcode
func merge(number arr[100], number left, number mid, number right)
begin
    number i
    number j
    number k
    number n1 <- mid - left + 1
    number n2 <- right - mid
    number L[100]
    number R[100]

    for i until i < n1 by 1
        L[i] <- arr[left + i]

    for j until j < n2 by 1
        R[j] <- arr[mid + 1 + j]

    i <- 0
    j <- 0
    k <- left

    for k until k <= right by 1
    begin
        if ((i < n1) and (j >= n2) or (L[i] <= R[j]))
        begin
            arr[k] <- L[i]
            i <- i + 1
        end
        else begin
            arr[k] <- R[j]
            j <- j + 1
        end
    end
end

func mergeSort(number arr[100], number left, number right)
begin
    if (left < right)
    begin
        number mid <- (left + right) / 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        merge(arr, left, mid, right)
    end
end
"""
        expect = '''Program([FuncDecl(Id(merge), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(mid), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, None), VarDecl(Id(j), NumberType, None, None), VarDecl(Id(k), NumberType, None, None), VarDecl(Id(n1), NumberType, None, BinaryOp(+, BinaryOp(-, Id(mid), Id(left)), NumLit(1.0))), VarDecl(Id(n2), NumberType, None, BinaryOp(-, Id(right), Id(mid))), VarDecl(Id(L), ArrayType([100.0], NumberType), None, None), VarDecl(Id(R), ArrayType([100.0], NumberType), None, None), For(Id(i), BinaryOp(<, Id(i), Id(n1)), NumLit(1.0), AssignStmt(ArrayCell(Id(L), [Id(i)]), ArrayCell(Id(arr), [BinaryOp(+, Id(left), Id(i))]))), For(Id(j), BinaryOp(<, Id(j), Id(n2)), NumLit(1.0), AssignStmt(ArrayCell(Id(R), [Id(j)]), ArrayCell(Id(arr), [BinaryOp(+, BinaryOp(+, Id(mid), NumLit(1.0)), Id(j))]))), AssignStmt(Id(i), NumLit(0.0)), AssignStmt(Id(j), NumLit(0.0)), AssignStmt(Id(k), Id(left)), For(Id(k), BinaryOp(<=, Id(k), Id(right)), NumLit(1.0), Block([If((BinaryOp(or, BinaryOp(and, BinaryOp(<, Id(i), Id(n1)), BinaryOp(>=, Id(j), Id(n2))), BinaryOp(<=, ArrayCell(Id(L), [Id(i)]), ArrayCell(Id(R), [Id(j)]))), Block([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(L), [Id(i)])), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))])), [], Block([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(R), [Id(j)])), AssignStmt(Id(j), BinaryOp(+, Id(j), NumLit(1.0)))]))]))])), FuncDecl(Id(mergeSort), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([If((BinaryOp(<, Id(left), Id(right)), Block([VarDecl(Id(mid), NumberType, None, BinaryOp(/, BinaryOp(+, Id(left), Id(right)), NumLit(2.0))), CallStmt(Id(mergeSort), [Id(arr), Id(left), Id(mid)]), CallStmt(Id(mergeSort), [Id(arr), BinaryOp(+, Id(mid), NumLit(1.0)), Id(right)]), CallStmt(Id(merge), [Id(arr), Id(left), Id(mid), Id(right)])])), [], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 385))
        except:
            print(f"fail test case: 85. This test case is: ##mergesort with zcode")
    def testcase86(self):
        input = """##if else check
func main()
begin
bool a<-true
if (a) b<-a+1
else if (not a) b<-a+2
else b<-a+3
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), BoolType, None, BooleanLit(True)), If((Id(a), AssignStmt(Id(b), BinaryOp(+, Id(a), NumLit(1.0)))), [], If((UnaryOp(not, Id(a)), AssignStmt(Id(b), BinaryOp(+, Id(a), NumLit(2.0)))), [], AssignStmt(Id(b), BinaryOp(+, Id(a), NumLit(3.0)))))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 386))
        except:
            print(f"fail test case: 86. This test case is: ##if else check")
    def testcase87(self):
        input = """##if else check 
func main() begin 
number today <- getToday()
number day <- getDay()
if (today=2) writeString("Hom nay phai di hoc")
elif (today = 3) 
if (day=1) writeString("hom nay duoc nghi hoc")
elif (day=25) writeString("hom nay lam kiem tra")
else writeString("hom nay di hoc bth")
elif (today=4) writeString("Hom nay di hoc buoi sang")
else writeString("Hom nay duoc nghi hoc")
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(today), NumberType, None, CallExpr(Id(getToday), [])), VarDecl(Id(day), NumberType, None, CallExpr(Id(getDay), [])), If((BinaryOp(=, Id(today), NumLit(2.0)), CallStmt(Id(writeString), [StringLit(Hom nay phai di hoc)])), [(BinaryOp(=, Id(today), NumLit(3.0)), If((BinaryOp(=, Id(day), NumLit(1.0)), CallStmt(Id(writeString), [StringLit(hom nay duoc nghi hoc)])), [(BinaryOp(=, Id(day), NumLit(25.0)), CallStmt(Id(writeString), [StringLit(hom nay lam kiem tra)]))], CallStmt(Id(writeString), [StringLit(hom nay di hoc bth)]))), (BinaryOp(=, Id(today), NumLit(4.0)), CallStmt(Id(writeString), [StringLit(Hom nay di hoc buoi sang)]))], CallStmt(Id(writeString), [StringLit(Hom nay duoc nghi hoc)]))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 387))
        except:
            print(f"fail test case: 87. This test case is: ##if else check ")
    def testcase88(self):
        input = """## use identifier nearly the same with key words
func main()
begin 
    dynamic for1 
    var var1  <- for_ 
    if(var_) for_<-1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(for1), None, dynamic, None), VarDecl(Id(var1), None, var, Id(for_)), If((Id(var_), AssignStmt(Id(for_), NumLit(1.0))), [], None)]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 388))
        except:
            print(f"fail test case: 88. This test case is: ## use identifier nearly the same with key words")
    def testcase89(self):
        input = """## use identifier nearly the same with key words
func main()
begin 
    dynamic for_ 
    var var_  <- for_ 
    if__(var_)
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(for_), None, dynamic, None), VarDecl(Id(var_), None, var, Id(for_)), CallStmt(Id(if__), [Id(var_)])]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 389))
        except:
            print(f"fail test case: 89. This test case is: ## use identifier nearly the same with key words")
    def testcase90(self):
        input = """## assignment check 
func main() begin 
    number a[4,6,7,8]
    a[3,2,1,ahahaha(4)] <- 1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(ArrayCell(Id(a), [NumLit(3.0), NumLit(2.0), NumLit(1.0), CallExpr(Id(ahahaha), [NumLit(4.0)])]), NumLit(1.0))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 390))
        except:
            print(f"fail test case: 90. This test case is: ## assignment check ")
    def testcase91(self):
        input = """## assignment check 
func main() begin 
    number a[4,6,7,8]
    a <- [1,2,3]
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(Id(a), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 391))
        except:
            print(f"fail test case: 91. This test case is: ## assignment check ")
    def testcase92(self):
        input = """## assignment check 
func main() begin 
    number a[4,6,7,8]
    a[3,true,1,ahahaha(4)] <- 1
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(ArrayCell(Id(a), [NumLit(3.0), BooleanLit(True), NumLit(1.0), CallExpr(Id(ahahaha), [NumLit(4.0)])]), NumLit(1.0))]))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 392))
        except:
            print(f"fail test case: 92. This test case is: ## assignment check ")
    def testcase93(self):
        input = """##declaration check 
number a<-2
"""
        expect = '''Program([VarDecl(Id(a), NumberType, None, NumLit(2.0))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 393))
        except:
            print(f"fail test case: 93. This test case is: ##declaration check ")
    def testcase94(self):
        input = """##declaration check 
string a
"""
        expect = '''Program([VarDecl(Id(a), StringType, None, None)])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 394))
        except:
            print(f"fail test case: 94. This test case is: ##declaration check ")
    def testcase95(self):
        input = """##declaration check 
string a<-2
"""
        expect = '''Program([VarDecl(Id(a), StringType, None, NumLit(2.0))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 395))
        except:
            print(f"fail test case: 95. This test case is: ##declaration check ")
    def testcase96(self):
        input = """##declaration check 
bool a<-2
"""
        expect = '''Program([VarDecl(Id(a), BoolType, None, NumLit(2.0))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 396))
        except:
            print(f"fail test case: 96. This test case is: ##declaration check ")
    def testcase97(self):
        input = """##declaration check 
var a<-2
"""
        expect = '''Program([VarDecl(Id(a), None, var, NumLit(2.0))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 397))
        except:
            print(f"fail test case: 97. This test case is: ##declaration check ")
    def testcase98(self):
        input = """##declaration check 
dynamic a
"""
        expect = '''Program([VarDecl(Id(a), None, dynamic, None)])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 398))
        except:
            print(f"fail test case: 98. This test case is: ##declaration check ")
    def testcase99(self):
        input = """##declaration check 
dynamic abc <-2
"""
        expect = '''Program([VarDecl(Id(abc), None, dynamic, NumLit(2.0))])'''
        try:
            self.assertTrue(TestAST.test(input, expect, 399))
        except:
            print(f"fail test case: 99. This test case is: ##declaration check ")