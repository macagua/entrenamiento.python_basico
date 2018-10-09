# -*- coding: utf8 -*-

"""
    El diccionario, que define una relación 
    uno a uno entre claves y valores.
"""

datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"14522590",
    "fecha_nacimiento":"03121980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Complicado"
}

print "\nDetalle del diccionario"
print "=======================\n"

print "\nClaves del diccionario:", datos_basicos.keys()
print "\nValores del diccionario:", datos_basicos.values()
print "\nElementos del diccionario:", datos_basicos.items()


# Ejemplo practico de los diccionarios
print "\nInscripcion de Curso"
print "===================="

print "\nDatos de participante"
print "---------------------"

print "Cedula de identidad:", datos_basicos['cedula']
print "Nombre completo: " + datos_basicos['nombres'] + " " + datos_basicos['apellidos']