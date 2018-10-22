# -*- coding: utf8 -*-

"""
    Operadores de comparación
"""

dato1 = 21
dato2 = 10
dato3 = 5;
dato4 = 20;

print "Valor de variable 'dato1':", dato1
print "Valor de variable 'dato2':", dato2
print "Valor de variable 'dato3':", dato3
print "Valor de variable 'dato4':", dato4

# Igual
if ( dato1 == dato2 ):
   print "Variable 'dato1' es igual a la variable 'dato2', (operador ==)"
else:
   print "Variable 'dato1' no es igual a la variable 'dato2', (operador ==)"

# Distinto
if ( dato1 != dato2 ):
   print "Variable 'dato1' es distinto a la variable 'dato2', (operador !=)"
else:
   print "Variable 'dato1' no es distinto a la variable 'dato2', (operador !=)"

# Diferente
if ( dato1 <> dato2 ):
   print "Variable 'dato1' es diferente a la variable 'dato2', (operador )"
else:
   print "Variable 'dato1' no es diferente a la variable 'dato2', (operador )"

# Menor que
if ( dato1 < dato2 ):
   print "Variable 'dato1' es menor que la variable 'dato2', (operador <)"
else:
   print "Variable 'dato1' no es menor que la variable 'dato2', (operador <)"

# Mayor que
if ( dato1 > dato2 ):
   print "Variable 'dato1' es mayor que la variable 'dato2', (operador >)"
else:
   print "Variable 'dato1' no es mayor que la variable 'dato2', (operador >)"

# Menor o igual que
if ( dato3 <= dato4 ):
   print "Variable 'dato3' es menor o igual que la variable 'dato4', (operador <=)"
else:
   print "Variable 'dato3' no es menor o igual que la variable 'dato4', (operador <=)"

# Mayor o igual que
if ( dato4 >= dato3 ):
   print "Variable 'dato4' es mayor o igual que la variable 'dato3', (operador >=)"
else:
   print "Variable 'dato4' no es mayor o igual que a la variable 'dato3', (operador >=)"
