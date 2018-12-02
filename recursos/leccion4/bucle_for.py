# -*- coding: utf8 -*-

"""Ejemplo de uso de bucle 'for'"""

# Bucle 'for' con estructura 'lista'
print "\nBucle 'for' con estructura 'lista'"
print "==================================\n"

print "Ejemplo: Itera una lista de animales\n"

# Definir lista
animales = ['gato', 'perro', 'serpiente']
for animal in animales:
    print "El animal es: {0}, tamaño de palabra es: {1}".format(
        animal, len(animal))


# Si se necesita iterar sobre una secuencia de números. 
# Generar una lista conteniendo progresiones aritméticos
print "\nFunción range()"
print "===============\n"

print "Rango de 15 números:", range(15)


# Bucle 'for' con estructura 'lista' y función range()
print "\nBucle 'for' con rango dinámico y función range()"
print "================================================\n"

print "Ejemplo: Itera un cadena de caracteres con rango dinámico\n"

oracion = 'Mary entiende muy bien Python'
frases = oracion.split() # convierte a una lista cada palabra
print "La oración analizada es:", oracion, ".\n"
for palabra in range(len(frases)):
    print "La palabra es: {0} su posición en la frase es: {1}".format(
        frases[palabra], palabra)


# Bucle 'for' con estructura 'ẗupla'
print "\nBucle 'for' con estructura 'ẗupla'"
print "==================================\n"

print "Ejemplo: Itera una tupla de parámetros\n"

conexion_bd = "127.0.0.1","root","123456","nomina"
for parametro in conexion_bd:
    print parametro


# Bucle 'for' con estructura 'diccionario'
print "\nBucle 'for' con estructura 'diccionario'"
print "========================================\n"

print "Ejemplo: Itera un diccionario de datos básicos\n"

datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}
clave = datos_basicos.keys()
valor = datos_basicos.values()
cantidad_datos = datos_basicos.items()

for clave, valor in cantidad_datos:
    print clave + ": " + valor


# Bucle 'for' con sentencia 'else'
print "\nBucle 'for' con sentencia 'else'"
print "================================\n"

print "Ejemplo: Itera un tupla con datos de conexión a base de datos\n"

db_connection = "127.0.0.1","5432","root","nomina"
for parametro in db_connection:
    print parametro
else:
    print """El comando PostgreSQL es: 
$ psql -h {server} -p {port} -U {user} -d {db_name}""".format(
        server=db_connection[0], port=db_connection[1], 
        user=db_connection[2], db_name=db_connection[3])
