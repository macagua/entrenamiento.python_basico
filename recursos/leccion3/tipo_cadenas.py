# -*- coding: utf8 -*-

"""
    Una cadena de caracteres, no es más que varios caracteres 
    encerrado entre comillas simples ('cadena') o dobles ("cadena").
"""

# Comillas simples
cadena1 = 'Texto entre comillas simples'
print cadena1
print type(cadena1)

# Comillas dobles
cadena2 = "Texto entre comillas dobles"
print cadena2
print type(cadena2)

# Cadena con código escapes
cadena3 = 'Texto entre \n\tcomillas simples'
print cadena3
print type(cadena3)

# Cadena varias lineas
cadena4 = """Texto linea 1
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
print cadena4
print type(cadena4)

# Repetición de cadena
cadena5 = "Cadena" * 3
print cadena5
print type(cadena5)

# Concatenación de cadena
nombre = "Leonardo"
apellido = "Caballero"
nombre_completo = nombre + " " + apellido
print nombre_completo, type(nombre_completo)

# tamaño de cadena
print "Tamaño de cadena '", nombre_completo, "' es:", len(nombre_completo)

# acceder a rango de cadena
print "Acceso a rango de cadena: '", nombre_completo[3:13]

# formato de impresión de cadena
print "Tamaño de cadena '{nombre_completo}' es: {tamano} ".format(
	nombre_completo=nombre_completo, tamano=len(nombre_completo))
