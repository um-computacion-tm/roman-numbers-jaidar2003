import unittest

def conversion_entero_romano(entero):
    numeros = [1000, 900, 400, 100, 90, 50, 40, 20, 9, 5, 4, 1]
    numerales = ['M', 'CM', 'CD', 'C', 'XC', 'L', 'XL','XX', 'IX', 'V', 'IV', 'I']

    numeral = ''
    i=0

    while entero > 0:
        for _ in range(entero // numeros[i]):
            numeral += numerales[i]  
            entero -= numeros [i]
        i += 1
    return numeral
#aaaaa

print(conversion_entero_romano(29))

class TestEnteroARomano(unittest.TestCase):
    def test_uno(self):
        resultado = conversion_entero_romano(1)
        self.assertEqual(resultado, 'I')

class TestEnteroARomano(unittest.TestCase):
    def test_dos(self):
        resultado = conversion_entero_romano(23)
        self.assertEqual(resultado, 'XXIII')

class TestEnteroARomano(unittest.TestCase):
    def test_dos(self):
        resultado = conversion_entero_romano(29)
        self.assertEqual(resultado, 'XXIX')

class TestEnteroARomano(unittest.TestCase):
    def test_tres(self):
        resultado = conversion_entero_romano(1001)
        self.assertEqual(resultado, 'MI')

class TestEnteroARomano(unittest.TestCase):
    def test_cuatro(self):
        resultado = conversion_entero_romano(453)
        self.assertEqual(resultado, 'CDLIII')

class TestEnteroARomano(unittest.TestCase):
    def test_cinco(self):
        resultado = conversion_entero_romano(3999)
        self.assertEqual(resultado, 'MMMCMXCIX')

if __name__ == '__main__':
    unittest.main()

