# -*- coding: utf8 -*-

# Comillas simples
cadenaa = 'Texto entre comillas simples'
print cadenaa
print type(cadenaa)

# Comillas dobles
cadenab = "Texto entre comillas dobles"
print cadenab
print type(cadenab)

# Cadena con codigo escapes
cadenaesc = 'Texto entre \n\tcomillas simples'
print cadenaesc
print type(cadenaesc)

# Cadena multilinea
cadenac = """Texto linea 1
linea 2
linea 3
linea 4
.
.
.
.
.
linea N
"""
print cadenac
print type(cadenac)

# Repeticion de cadena
cadrep = "Cadena" * 3
print cadrep
print type(cadrep)

# Concatenacion de cadena
nombre = "Leonardo"
apellido = "Caballero"
nombre_completo = nombre + " " + apellido
print nombre_completo
print type(nombre_completo)

print "Tamano de cadena '", nombre_completo, "' es:", len(nombre_completo)

# acceder a rango de la cadena
print nombre_completo[3:13]
