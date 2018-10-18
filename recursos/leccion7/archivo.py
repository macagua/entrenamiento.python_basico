# -*- coding: utf8 -*-

"""
   Ejemplo de la manipulación de archivos con la escritura, 
   lectura y iteración de los mismos
"""

import os

print "\nCrear un archivo"
print "================"

nombre_archivo = 'archivo.txt'

f = open(nombre_archivo, 'w') # abre el archivo archivo.txt
f.write('Este es una prueba \ny otra prueba.')
f.close()

if nombre_archivo in os.listdir("."):
    print "\nEl archivo se creo exitosamente en la siguiente ruta: \n\n" + "\t"+ os.getcwd() + "/" + nombre_archivo
else:
    print "El archivo no se creo exitosamente\n"


print "\n\nLeer un archivo"
print "===============\n"

f = open(nombre_archivo, 'r')
s = f.read()
print s
f.close()


print "\n\nIterar sobre un archivo"
print "=======================\n"

f = open(nombre_archivo, 'r')
for line in f:
    print line
print "\n"
f.close()
