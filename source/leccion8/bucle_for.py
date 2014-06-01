# -*- coding: utf8 -*-

"""
    Ejemplo de uso de bucle For

"""

print "\nItera una lista de animales"
print "===========================\n"

# Midiendo cadenas de texto
lista_animales = ['gato', 'ventana', 'defenestrado']

for animal in lista_animales:
    print "El animal es:", animal, ", la cantidad de letras de la posicion son:", len(animal)

# Si se necesita iterar sobre una secuencia de números. 
# Genera una lista conteniendo progresiones aritméticos
print "\nRango de 15 numeros:", range(15)

print "\nItera una cadena con rango dinamico"
print "===================================\n"

frases = ['Mary', 'tenia', 'un', 'corderito']
for palabra in range(len(frases)):
    print "La palabra es:", frases[palabra], "su posicion en la frase es:", palabra

#####################################################

print "\nItera una tupla de parametros"
print "=============================\n"

conexion_bd = "127.0.0.1","root","123456","nomina"
for parametro in conexion_bd:
    print parametro

#####################################################

print "\nItera un diccionario datos basicos"
print "==================================\n"

datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"14522590",
    "fecha_nacimiento":"03121980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Complicado"
}

dato = datos_basicos.keys()
valor = datos_basicos.values()
cantidad_datos = datos_basicos.items()

for dato, valor in cantidad_datos:
    print dato + ": " + valor