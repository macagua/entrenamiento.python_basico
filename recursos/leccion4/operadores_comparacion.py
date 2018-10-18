# -*- coding: utf8 -*-

"""
    Operadores de comparación
"""

a = 21
b = 10
c = 5;
d = 20;

print "el valor de la variable 'a' es:", a
print "el valor de la variable 'b' es:", b
print "el valor de la variable 'c' es:", c
print "el valor de la variable 'd' es:", d

# Igual
if ( a == b ):
   print "Comparación == | la variable 'a' es igual a la variable 'b'"
else:
   print "Comparación == | la variable 'a' no es igual a la variable 'b'"

# Distinto
if ( a != b ):
   print "Comparación != | la variable 'a' no es igual a la variable 'b'"
else:
   print "Comparación != | la variable 'a' es igual a la variable 'b'"

# Diferente
if ( a <> b ):
   print "Comparación <> | la variable 'a' no es igual a la variable 'b'"
else:
   print "Comparación <> | la variable 'a' es igual a la variable 'b'"

# Menor que
if ( a < b ):
   print "Comparación < | la variable 'a' es menor que la variable 'b'"
else:
   print "Comparación < | la variable 'a' no es menor que la variable 'b'"

# Mayor que
if ( a > b ):
   print "Comparación > | la variable 'a' es mayor que la variable 'b'"
else:
   print "Comparación > | la variable 'a' no es mayor que la variable 'b'"

# Menor o igual que
if ( c <= d ):
   print "Comparación <= | la variable 'c' es menor o igual a la variable 'd'"
else:
   print "Comparación <= | la variable 'c' es ni menor de ni igual a la variable 'd'"

# Mayor o igual que
if ( d >= c ):
   print "Comparación >= | la variable 'd' es o bien mayor que o igual a la variable 'c'"
else:
   print "Comparación >= | la variable 'd' es ni mayor que ni igual a la variable 'c'"
