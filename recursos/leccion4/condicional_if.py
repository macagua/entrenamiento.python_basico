# -*- coding: utf8 -*-

"""Ejemplo de uso del condicional 'if' usando operadores relacionales"""

dato1, dato2, dato3, dato4 = 21, 10, 5, 20;

print "Valor de variable 'dato1':", dato1
print "Valor de variable 'dato2':", dato2
print "Valor de variable 'dato3':", dato3
print "Valor de variable 'dato4':", dato4

# Igual
if (dato1 == dato2):
   print "Variable 'dato1' es igual a la variable 'dato2'."
else:
   print "Variable 'dato1' no es igual a la variable 'dato2'."

# Distinto
if (dato1 != dato2):
   print "Variable 'dato1' es distinto a la variable 'dato2'."
else:
   print "Variable 'dato1' no es distinto a la variable 'dato2'."

# Diferente
if (dato1 <> dato2):
   print "Variable 'dato1' es diferente a la variable 'dato2'."
else:
   print "Variable 'dato1' no es diferente a la variable 'dato2'."

# Menor que
if (dato1 < dato2):
   print "Variable 'dato1' es menor que la variable 'dato2'."
else:
   print "Variable 'dato1' no es menor que la variable 'dato2'."

# Mayor que
if (dato1 > dato2):
   print "Variable 'dato1' es mayor que la variable 'dato2'."
else:
   print "Variable 'dato1' no es mayor que la variable 'dato2'."

# Menor o igual que
if (dato3 <= dato4):
   print "Variable 'dato3' es menor o igual que la variable 'dato4'."
else:
   print "Variable 'dato3' no es menor o igual que la variable 'dato4'."

# Mayor o igual que
if (dato4 >= dato3):
   print "Variable 'dato4' es mayor o igual que la variable 'dato3'."
else:
   print "Variable 'dato4' no es mayor o igual que a la variable 'dato3'."


# Ejemplo de condicional if / elif / else completo
numero = int(raw_input("\nIngresa un número entero, por favor: "))

if numero < 0:
    numero = 0
    print 'El número ingresado es negativo cambiado a cero.\n'
elif numero == 0:
    print 'El número ingresado es 0.\n'
elif numero == 1:
    print 'El número ingresado es 1.\n'
else:
    print 'El número ingresado es mayor que uno.\n'
