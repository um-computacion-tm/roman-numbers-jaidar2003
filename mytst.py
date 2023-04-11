import unittest
from contador1 import contar_palabras
class TestContarPalabras(unittest.TestCase):
    
    def test_contar_palabras(self):
        frase = "Hola mundo hola Python "
        resultado = contar_palabras(frase)
        self.assertEqual(resultado["Hola"], 1)
        self.assertEqual(resultado["mundo"], 1)
        self.assertEqual(resultado["hola"], 1)
        self.assertEqual(resultado["Python"], 1)
      #aidar     
if __name__ == '_main_':
    unittest.main()