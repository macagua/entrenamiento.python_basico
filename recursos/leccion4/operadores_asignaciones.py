# -*- coding: utf8 -*-

"""
    Operadores de asignaciones
"""

a = 21
b = 10
c = 0

print "el valor de la variable 'a' es:", a
print "el valor de la variable 'b' es:", b

c = a + b
print "Operador + | El valor de la variable 'c' es ", c

c += a
print "Operador += | El valor de la variable 'c' es ", c 

c *= a
print "Operador *= | El valor de la variable 'c' es ", c 

c /= a 
print "Operador /= | El valor de la variable 'c' es ", c 

c = 2
c %= a
print "Operador %= | El valor de la variable 'c' es ", c

c **= a
print "Operador **= | El valor de la variable 'c' es ", c

c //= a
print "Operador //= | El valor de la variable 'c' es ", c
