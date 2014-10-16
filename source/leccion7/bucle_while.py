# -*- coding: utf8 -*-

"""
    Ejemplo de uso de bucle While
"""

print "\nWhile controlado con Conteo"
print "===========================\n"

print "Un ejemplo es un sumador numérico hasta 10, \ncomo se muestra a continuación:\n"

suma = -1
while suma < 10:
    suma = suma + 1
print "La suma es " + str(suma)

print "\nWhile controlado con Evento"
print "===========================\n"

print "Un ejemplo es calcular el promedio de grado, \ncomo se muestra a continuación:\n"

promedio = 0.0
total = 0
contar = 0

print "Introduzca valor numerico de un grado (-1 para salir): "
grado = int(raw_input())	
while grado != -1:
    total = total + grado
    contar = contar + 1
    print "Introduzca valor numerico de un grado (-1 para salir): "
    grado = int(raw_input())
promedio = total / contar
print "Promedio de grado: " + str(promedio)



print "\nWhile con sentencia break"
print "=========================\n"

variable = 10
while variable > 0:
    print 'Actual valor de variable:', variable
    variable = variable -1
    if variable == 5:
        break

print "\nWhile con sentencia continue"
print "============================\n"

variable = 10
while variable > 0:              
   variable = variable -1
   if variable == 5:
      continue
   print 'Actual valor de variable:', variable
