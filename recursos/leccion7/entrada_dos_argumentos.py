# -*- coding: utf8 -*-

import sys

# Comprobación de seguridad, ejecutar sólo si se reciben 2 
# argumentos realemente
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print texto
else:
    print "ERROR: Introdujo uno (1) o más de dos (2) argumentos"
    print "SOLUCIÓN: Introduce los argumentos correctamente"
    print 'Ejemplo: entrada_dos_argumentos.py "Texto" 5'
