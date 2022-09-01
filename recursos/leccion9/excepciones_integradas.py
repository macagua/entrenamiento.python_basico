# -*- coding: utf8 -*-

import os.path
import sys

RUTA_BASE = os.path.dirname(__file__)
RUTA_ARCHIVO = os.path.join(RUTA_BASE, 'numeros.txt')
linea1, linea2 = 1, 3

archivo = open(RUTA_ARCHIVO, 'w')
archivo.write("1\n2\n")
archivo.close()

try:
    archivo = open(RUTA_ARCHIVO, 'r')
    cadenas = archivo.readline()
    linea1 += int(cadenas.strip())
    cadenas = archivo.readline()
    linea2 += int(cadenas.strip())
    total = linea1 + linea2
    archivo.close()
except IOError as err:
    print("Error E/S ({0}): {1}".format(err.errno, err.strerror))
except ValueError:
    print("No pude convertir el dato a un entero.")
except:
    print("Error inesperado:", sys.exc_info()[0])
    raise

print("El total es:", total)
