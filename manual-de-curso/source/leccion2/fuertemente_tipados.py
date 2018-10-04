# -*- coding: utf8 -*-

""" 
    El fuertemente tipado significa que el tipo de valor no 
    cambia repentinamente. Una cadena que contiene solo dígitos 
    no se convierte mágicamente en un número. Cada cambio de tipo 
    requiere una conversión explícita.

    >>> valor1 = 2
    >>> valor2 = "5"
    >>> total = valor1 + valor2
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>> total = valor1 + int(valor2)
    >>> print "El total es: " + str(total)
    7
"""

valor1 = 2 # "valor1" guarda un valor entero
valor2 = "5" # "valor1" guarda un valor cadena
total = valor1 + int(valor2) # se usa el metodo int() para convertir a entero
print "El total es: " + str(total) # se usa el metodo str() para convertir a cadena
