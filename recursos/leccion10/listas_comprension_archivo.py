"""Programa para leer y escribir un archivo de texto con listas de compresión"""

import os

NOMBRE_ARCHIVO = "listas_comprension_archivo.txt"
DIR_ARCHIVO = os.path.dirname(os.path.abspath(__file__)) + os.sep
ARCHIVO = DIR_ARCHIVO + NOMBRE_ARCHIVO


with open(ARCHIVO, "r") as f:
    # Lee todas las líneas del archivo y las almacena en una lista
    lineas = f.readlines()

# Crea una nueva lista con las líneas modificadas con la las letras a mayúsculas
nuevas_lineas = [linea.upper() for linea in lineas]

with open(ARCHIVO, "w") as f:
    # Escribe las nuevas líneas en el archivo, separadas por saltos de línea
    f.write("\n".join(nuevas_lineas))

f.close()
