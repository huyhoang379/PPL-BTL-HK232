import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func checkNumberSign(number num)
            begin
                if (num > 0)
                    return "Positive"
                elif (num < 0)
                    return "Negative"
                else
                    return "Zero"
            end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
