# -*- coding: utf8 -*-

"""
    Ejemplo de uso de sentencia conficional if
"""

numero = int(raw_input("Ingresa un entero, por favor: "))

if numero < 0:
    numero = 0
    print 'Numero negativo cambiado a cero'
elif numero == 0:
    print 'Numero es Cero'
elif numero == 1:
    print 'Numero Simple'
else:
    print 'Mayor que uno'
