import unittest
from Contar_palabras import contar_palabras  
    
class TestContarPalabras(unittest.TestCase):
    def test_hola(self):
        resultado = contar_palabras('hola')
        self.assertEqual(resultado, {'hola' : 1})
    def test_2(self):
        resultado = contar_palabras('Hola mundo')
        self.assertEqual(resultado, {'Hola mundo' : 2})
    def test_3(self):
        resultado = contar_palabras('Goku le gana')
        self.assertEqual(resultado, {'Goku le gana' : 3})
    def test_4(self):
        resultado = contar_palabras('Sistema de representación recursada')
        self.assertEqual(resultado, {'Sistema de representación recursada' : 4})
    def test_5(self):
        resultado = contar_palabras('Yo soy tú y tú eres yo')
        self.assertEqual(resultado, {'Yo soy tú y tú eres yo' : 7})
    def test_6(self):
        resultado = contar_palabras('Ayer fui yo, ahora eres tú')
        self.assertEqual(resultado, {'Ayer fui yo, ahora eres tú' : 6})
    def test_7(self):
        resultado = contar_palabras('Me gusta el helado de jamón y queso')
        self.assertEqual(resultado, {'Me gusta el helado de jamón y queso' : 8})
    def test_8(self):
        resultado = contar_palabras('El planeta tierra es grande, pero jupiter lo es más')
        self.assertEqual(resultado, {'El planeta tierra es grande, pero jupiter lo es más' : 10})
    def test_9(self):
        resultado = contar_palabras('Tecnologia, ciencia y sociedad la mejor materia de ingenieria')
        self.assertEqual(resultado, {'Tecnologia, ciencia y sociedad la mejor materia de ingenieria' : 9})
    def test_10(self):
        resultado = contar_palabras('Voy a visitar a la morgue al terminar la facultad')
        self.assertEqual(resultado, {'Voy a visitar a la morgue al terminar la facultad' : 10})
