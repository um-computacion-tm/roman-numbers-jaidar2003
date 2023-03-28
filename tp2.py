import unittest

def roman_to_decimal(roman):
    if roman == 'I':
        return 1
    
class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal('I')
        self.assertEqual(resultado, 1)
if __name__ == '__main__':
    unittest.main()

