# -*- coding: utf8 -*-

"""Ilustración de ingreso interactivo en Python.

Simula a sala de chat del servicio LatinChat.com.

Validando datos de entradas numérico y tipo cadena.

E interactuá con el usuario y en base a condicionales 
muestra un mensaje.

"""

print "\nSimulando a LatinChat"
print "====================="

print "\nSala de Chat > De 30 a 40 años"
print "------------------------------\n"

print 'Ana: ¿Cómo se llama usted?: ' 
nombre = raw_input('Yo: ')
print 'Ana: Hola', nombre, ', encantada de conocerte :3'

print 'Ana: ¿Que edad tiene usted?: '
edad = input('Yo: ')
print 'Usted tiene', edad, ', y yo ya no digo mi edad xD'

print 'Ana: ¿Tiene WebCam?, ingrese "si" o "no", por favor!: '
tiene_WebCam = raw_input('Yo: ')

if tiene_WebCam in ('s', 'S', 'si', 'Si', 'SI'):
	print "Ponga la WebCam para verle :-D"
elif tiene_WebCam in ('n', 'no', 'No', 'NO'):
	print "Lastima por usted :'( Adiós"
