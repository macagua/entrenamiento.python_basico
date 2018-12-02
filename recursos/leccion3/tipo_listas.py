# -*- coding: utf8 -*-

"""
    La lista son variables que almacenan arrays, internamente 
    cada posición puede ser un tipo de datos distinto.
"""

# Colección ordenada / arreglos o vectores
lista = [2, "tres", True, ["uno", 10]]
print lista

# Acceder a un elemento especifico
l2 = lista[1]
print l2

# Acceder a un elemento a una lista anidada
l3 = lista[3][0]
print l3

# Establecer nuevo valor de un elemento de lista
lista[1] = 4
print lista
lista[1] = "tres"

# Obtener un rango de elemento especifico
l3 = lista[0:3]
print l3

# Obtener un rango con saltos de elementos específicos
l4 = lista[0:3:2]
print l4
l5 = lista[1::2]
print l5
