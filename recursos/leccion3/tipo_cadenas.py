# -*- coding: utf8 -*-

"""
    Una cadena de caracteres, no es más que varios caracteres 
    encerrado entre comillas simples ('cadena') o dobles ("cadena").
"""

# Comillas simples
cadenaa = 'Texto entre comillas simples'
print cadenaa
print type(cadenaa)

# Comillas dobles
cadenab = "Texto entre comillas dobles"
print cadenab
print type(cadenab)

# Cadena con código escapes
cadenaesc = 'Texto entre \n\tcomillas simples'
print cadenaesc
print type(cadenaesc)

# Cadena varias lineas
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

# Repetición de cadena
cadrep = "Cadena" * 3
print cadrep
print type(cadrep)

# Concatenación de cadena
nombre = "Leonardo"
apellido = "Caballero"
nombre_completo = nombre + " " + apellido
print nombre_completo
print type(nombre_completo)

# tamaño de cadena
print "Tamaño de cadena '", nombre_completo, "' es:", len(nombre_completo)

# acceder a rango de cadena
print nombre_completo[3:13]
