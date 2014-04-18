# -*- coding: utf8 -*-

"""
    módulo de Sucesión de números Fibonacci
    Mas informacion en http://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci
"""

a, b = 0, 1
while b < 100:
    print b,
    a, b = b, a + b