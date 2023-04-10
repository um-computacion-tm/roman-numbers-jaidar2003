import unittest

from decimal2 import decimal_a_romano
from romano import romano_a_decimal

class TestConversor(unittest.TestCase):
    def test_decimal_a_romano(self):
        self.assertEqual(decimal_a_romano(1), "I")
        self.assertEqual(decimal_a_romano(9), "IX")
        self.assertEqual(decimal_a_romano(1066), "MLXVI")
        self.assertEqual(decimal_a_romano(1989), "MCMLXXXIX")
        self.assertEqual(decimal_a_romano(3999), "MMMCMXCIX")
        
    def test_romano_a_decimal(self):
        self.assertEqual(romano_a_decimal("I"), 1)
        self.assertEqual(romano_a_decimal("IX"), 9)
        self.assertEqual(romano_a_decimal("MLXVI"), 1066)
        self.assertEqual(romano_a_decimal("MCMLXXXIX"), 1989)
        self.assertEqual(romano_a_decimal("MMMCMXCIX"), 3999)

if __name__ == "_main_":
    unittest.main()

#test1