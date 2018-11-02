# -*- coding: utf8 -*-

"""
   Ejemplo de la manipulación de archivos con la escritura, 
   lectura y iteración de los mismos
"""

import os

print "\nCrear un archivo"
print "================"

NOMBRE_ARCHIVO = 'datos.txt'

f = open(NOMBRE_ARCHIVO, 'w') # abre el archivo datos.txt
f.write('Este es una prueba \ny otra prueba.')
f.close()

if NOMBRE_ARCHIVO in os.listdir("."):
    print "\nArchivo creado con éxito en la ruta: \n\n" + "\t"+ os.getcwd() + "/" + NOMBRE_ARCHIVO
else:
    print "El archivo no fue creado!!!\n"


print "\n\nLeer un archivo"
print "===============\n"

f = open(NOMBRE_ARCHIVO, 'r')
s = f.read()
print s
f.close()


print "\n\nIterar sobre un archivo"
print "=======================\n"

f = open(NOMBRE_ARCHIVO, 'r')
for line in f:
    print line
print "\n"
f.close()
