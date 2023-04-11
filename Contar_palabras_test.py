import unittest
from Contar_palabras import contar_palabras  
    
class TestContarPalabras(unittest.TestCase):
    def test_hola(self):
        resultado = contar_palabras('hola')
        self.assertEqual(resultado, {'hola' : 1})
    def test_2(self):
        resultado = contar_palabras('Hola mundo')
        self.assertEqual(resultado, {'hola' : 1, 'mundo': 1})
    def test_3(self):
        resultado = contar_palabras('Yo soy tú y tú eres yo')
        self.assertEqual(resultado, {'yo': 2, 'soy': 1, 'tú': 2, 'y': 1, 'eres': 1})