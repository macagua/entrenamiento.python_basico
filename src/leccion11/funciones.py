# -*- coding: utf8 -*-

"""
    Funciones en Python
"""

# escribe la sucesión Fibonacci hasta n
def imprime_fibonacci(n):
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b

# devuelve la sucesión Fibonacci hasta n
def devuelve_fibonacci(n): 
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a + b
    return resultado

print "La sucesión Fibonacci hasta 10 es:", imprime_fibonacci(10)

print "La sucesión Fibonacci hasta 50 es:", devuelve_fibonacci(50)