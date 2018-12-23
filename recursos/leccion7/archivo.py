# -*- coding: utf8 -*-

"""
   Manipula un archivo con permisos de escritura y 
   lectura, ademas de interactuar de el mismo
"""

import os

print "\nCrear un archivo"
print "================"

NOMBRE_ARCHIVO = 'datos.txt'

archivo = open(NOMBRE_ARCHIVO, 'w') # abre el archivo datos.txt
archivo.write('Este es una prueba \ny otra prueba.')
archivo.close()

if NOMBRE_ARCHIVO in os.listdir("."):
    print "\nArchivo creado en la ruta: \n\n\t{0}/{1}".format(
        os.getcwd(), NOMBRE_ARCHIVO)
else:
    print "El archivo no fue creado!!!\n"


print "\n\nLeer un archivo"
print "===============\n"

archivo = open(NOMBRE_ARCHIVO, 'r')
contenido = archivo.read()
print contenido
archivo.close()


print "\n\nIterar sobre un archivo"
print "=======================\n"

archivo = open(NOMBRE_ARCHIVO, 'r')
for linea in archivo:
    print linea
print "\n"
archivo.close()


print "\nEliminar un archivo"
print "==================="

os.remove(os.getcwd()+"/"+NOMBRE_ARCHIVO)
print "\nEliminado archivo desde la ruta: \n\n\t{0}/{1}".format(
    os.getcwd(), NOMBRE_ARCHIVO)
