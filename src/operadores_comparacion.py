# -*- coding: utf8 -*-

"""
    Operadores de comparacion
"""

a = 21
b = 10

print "el valor de la variable 'a' es:", a
print "el valor de la variable 'b' es:", b

if ( a == b ):
   print "Comparacion == | a es igual a b"
else:
   print "Comparacion == | a no es igual a b"

if ( a != b ):
   print "Comparacion != | a no es igual a b"
else:
   print "Comparacion != | a es igual a b"

if ( a <> b ):
   print "Comparacion <> | a no es igual a b"
else:
   print "Comparacion <> | a es igual a b"

if ( a < b ):
   print "Comparacion < | a es menor que b" 
else:
   print "Comparacion < | a no es menor que b"

if ( a > b ):
   print "Comparacion > | a es mayor que b"
else:
   print "Comparacion > | a no es mayor que b"

c = 5;
d = 20;

print "el valor de la variable 'c' es:", c
print "el valor de la variable 'd' es:", d

if ( c <= d ):
   print "Comparacion <= | la variable 'c' es menor o igual a la variable 'd'"
else:
   print "Comparacion <= | la variable 'c' es ni menor de ni igual a la variable 'd'"

if ( d >= c ):
   print "Comparacion >= | la variable 'd' es o bien mayor que o igual a la variable 'c'"
else:
   print "Comparacion >= | la variable 'd' es ni mayor que ni igual a la variable 'c'"