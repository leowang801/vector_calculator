from cmath import sqrt
import unittest
from vector_functions import *


#Vectors for testing:
a = [3, 4, 12]
b = [5, 11, 14]
c = [-3, -6, 4]
d = [2, -1, -11]
e = [2.3, 4.5, -3.7]
f = [8.6, 2.3, 5.3]

class TestMagnitude(unittest.TestCase):
    def test_all_positive(self):
        self.assertEqual(magnitude([3, 4]), 5, "Should be 5")
        self.assertEqual(magnitude([3, 1, 1, 6, 7, 2]), 10, "Should be 10")


    def test_negative(self):
        self.assertEqual(magnitude([-12, -5]), 13, "Should be 13")
        self.assertEqual(magnitude([-8, 4, -6, 2, 1]), 11, "Should be 11")
    
    def test_to_ten_decimal_places(self):
        self.assertAlmostEqual(magnitude([4/5, 6/5]), sqrt(36 + 16)/5, 10)
        self.assertAlmostEqual(magnitude([-3/5, 6/5, -8/3]), sqrt(9/25 + 36/25 + 64/9), 10)

class TestDotProd(unittest.TestCase):
    def test_dot_positive(self):
        self.assertEqual(dot_prod(a, b), 15 + 44 + 12 * 14)
    
    def test_dot_negative(self):
        self.assertEqual(dot_prod(c, d), -3 * 2 + -6 * -1 + -11 * 4)



if __name__ == '__main__':
    unittest.main()