# -*- coding: utf8 -*-

"""
    Ejemplo de uso de bucle For
"""

print "\nItera una lista de animales"
print "===========================\n"

# Definiendo cadenas de texto
lista_animales = ['gato', 'ventana', 'defenestrado']

for animal in lista_animales:
    print "El animal es:", animal, ", la cantidad de letras de la posición son:", len(animal)

# Si se necesita iterar sobre una secuencia de números. 
# Genera una lista conteniendo progresiones aritméticos
print "\nRango de 15 números:", range(15)

print "\nItera una cadena con rango dinámico"
print "===================================\n"

frases = ['Mary', 'tenia', 'un', 'corderito']
for palabra in range(len(frases)):
    print "La palabra es:", frases[palabra], "su posición en la frase es:", palabra

#####################################################

print "\nItera una tupla de parámetros"
print "=============================\n"

conexion_bd = "127.0.0.1","root","123456","nomina"
for parametro in conexion_bd:
    print parametro

#####################################################

print "\nItera un diccionario datos básicos"
print "==================================\n"

datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Complicado"
}
dato = datos_basicos.keys()
valor = datos_basicos.values()
cantidad_datos = datos_basicos.items()

for dato, valor in cantidad_datos:
    print dato + ": " + valor
