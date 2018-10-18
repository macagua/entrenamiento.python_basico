# -*- coding: utf8 -*-

"""
    Operadores lógicos
"""

a = 10
b = 20

print "el valor de la variable 'a' es:", a
print "el valor de la variable 'b' es:", b

# Operador and
if ( a and b ):
   print "Operador and | a y b son VERDADERO"
else:
   print "Operador and | O bien la variable 'a' no es VERDADERO o la variable 'b' no es VERDADERO"

# Operador or
if ( a or b ):
   print "Operador or | O bien la variable 'a' es VERDADERA o la variable 'b' es VERDADERA o ambas variables son VERDADERA"
else:
   print "Operador or | Ni la variable 'a' es VERDADERA ni la variable 'b' es VERDADERA"

# Operador not
if not( a and b ):
   print "Operador not | Ni la variable 'a' NO es VERDADERA o la variable 'b' NO es VERDADERA"
else:
   print "Operador not | las variables 'a' y 'b' son VERDADERAS"
