# -*- coding: utf8 -*-

"""Ilustración de ingreso interactivo en Python.

Simula a sala de chat del servicio LatinChat.com.

Validando datos de entradas numérico y tipo cadena.

E interactuá con el usuario y en base a condicionales 
muestra un mensaje.

"""

print "\nSimulando a LatinChat"
print "====================="

print "\nLatinChat > De 20 a 30 años"
print "---------------------------\n"

print 'Pepe: ' 
nombre = raw_input('¿Cómo te llamás?: ')
print 'Pepe: Hola', nombre, ', encantado de conocerte :3'

print 'Pepe: '
edad = input('¿Cual es tu edad?: ')
print 'Tu tienes', edad, 'y yo no tengo soy un programa xD'

print 'Pepe: '
tiene_WebCam = raw_input('¿Tienes WebCam?, ingrese "si" o "no", por favor!: ')

if tiene_WebCam in ('s', 'S', 'si', 'Si', 'SI'):
	print "Pon la WebCam para verte :-D"
elif tiene_WebCam in ('n', 'no', 'No', 'NO'):
	print "Lastima por ti :'( Adiós"
