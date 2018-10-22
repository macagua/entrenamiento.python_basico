# -*- coding: utf8 -*-

"""
   La lista son variables que almacenan arrays, internamente 
   cada posición puede ser un tipo de datos distinto.
"""

# Colección ordenada / arreglos o vectores
l = [2, "tres", True, ["uno", 10]]
print l

# Acceder a un elemento especifico
l2 = l[1]
print l2

# Acceder a un elemento a una lista anidada
l3 = l[3][0]
print l3

# Establecer nuevo valor de un elemento de lista
l[1] = 4
print l
l[1] = "tres"

# Obtener un rango de elemento especifico
l3 = l[0:3]
print l3

# Obtener un rango con saltos de elementos específicos
l4 = l[0:3:2]
print l4

l5 = l[1::2]
print l5
