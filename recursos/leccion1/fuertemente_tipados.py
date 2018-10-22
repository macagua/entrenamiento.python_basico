# -*- coding: utf8 -*-

""" 
    El fuertemente tipado significa que el tipo de valor no 
    cambia repentinamente. Un string que contiene solo dígitos 
    no se convierte mágicamente en un número. Cada cambio de tipo 
    requiere una conversión explícita.

    >>> valor1, valor2 = 2, "5"
    >>> total = valor1 + valor2
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>> total = valor1 + int(valor2)
    >>> print "El total es: " + str(total)
    7
"""

# varible "valor1" es integer, varible "valor2" es string
valor1, valor2 = 2, "5"
# el metodo int() es para convertir a integer
total = valor1 + int(valor2)
# el metodo str() es para convertir a string
print "El total es: " + str(total)
