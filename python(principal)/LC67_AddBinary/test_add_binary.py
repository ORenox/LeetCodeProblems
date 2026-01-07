import unittest

from LC67_AddBinary import Solution

class TestAddBinary(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_addBinary_case1(self):
       self.assertEqual(self.solution.addBinary("11", "1"), "100")
       self.assertEqual(self.solution.addBinary("1010", "1011"), "10101")

    def test_addBinary_case2(self):
        a = "1010"
        b = "1011"
        expected = "10101"
        result = self.solution.addBinary(a, b)
        self.assertEqual(result, expected)

    def test_addBinary_case3(self):
        a = "0"
        b = "0"
        expected = "0"
        result = self.solution.addBinary(a, b)
        self.assertEqual(result, expected)

    def test_addBinary_case4(self):
        a = "1111"
        b = "1111"
        expected = "11110"
        result = self.solution.addBinary(a, b)
        self.assertEqual(result, expected)
if __name__ == "__main__":
    unittest.main()


#python -m unittest test.py