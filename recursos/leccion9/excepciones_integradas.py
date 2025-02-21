import os.path
import sys


RUTA_BASE = os.path.dirname(__file__)
RUTA_ARCHIVO = os.path.join(RUTA_BASE, "numeros.txt")
linea1, linea2 = 1, 3

archivo = open(RUTA_ARCHIVO, "w")
archivo.write("1\n2\n")
archivo.close()

total = 0
try:
    archivo = open(RUTA_ARCHIVO)
    cadenas = archivo.readline()
    linea1 += int(cadenas.strip())
    cadenas = archivo.readline()
    linea2 += int(cadenas.strip())
    total = linea1 + linea2
    archivo.close()
except OSError as err:
    print(f"Error E/S ({err.errno}): {err.strerror}")
except ValueError:
    print("No pude convertir el dato a un entero.")
except:
    print(f"Error inesperado: {sys.exc_info()[0]}")
    raise

print(f"El total es: {total}")
