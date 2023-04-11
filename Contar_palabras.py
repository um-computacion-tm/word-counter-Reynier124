import unittest

def contar_palabras(oracion): 
    resultado = {}
    for word in oracion.split(' '):
        if word in resultado:
            resultado[word.lower()] += 1
        else:
            resultado[word.lower()] = 1
    return resultado
        

if __name__ == "__main__":
    unittest.main()