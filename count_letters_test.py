import unittest

def count_letters(word):
    resultado = {}
    for letter in word:
        resultado[letter] = 1
    return resultado


class TestCountLetters(unittest.TestCase):
    def test_simple(self):
        resultado = count_letters('a')
        self.assertEqual(resultado, {'a' : 1})
    def test_complex(self):
        resultado = count_letters('hola')
        self.assertEqual(resultado, {'h' : 1, 'o' :1, 'l' : 1, 'a' : 1})

if __name__ == '__main__':
    unittest.main()