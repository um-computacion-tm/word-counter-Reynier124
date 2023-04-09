import unittest

def contar_palabras(oracion): 
    cantidad = len(oracion.split(" "))
    palabras = {oracion : cantidad}
    return palabras

if __name__ == "__main__":
    unittest.main()