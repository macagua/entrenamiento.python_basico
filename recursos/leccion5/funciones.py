# -*- coding: utf8 -*-

"""
    Funciones en Python
"""

def iva():
    ''' funcion basica de Python '''
    iva = 12
    costo = input('¿Cual es el monto a calcular?: ')
    calculo = costo * iva / 100
    print calculo

def suma(numero1,numero2):
    print numero1 + numero2

def imprime_fibonacci(n):
    ''' escribe la sucesión Fibonacci hasta n '''
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b

def devuelve_fibonacci(n): 
    ''' devuelve la sucesión Fibonacci hasta n '''
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a + b
    return resultado

print "El calculo de IVA es :", iva()

print "La suma de dos numeros es:", suma(13,37)

print "El calculo de IVA es :", iva(10)

print "La sucesión Fibonacci hasta 10 es:", imprime_fibonacci(10)

print "La sucesión Fibonacci hasta 50 es:", devuelve_fibonacci(50)