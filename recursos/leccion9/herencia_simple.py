# -*- coding: utf8 -*-

from clases import Persona, Supervisor

# Dos instancias de Objeto Persona
persona1 = Persona("V-13458796", "Leonardo", "Caballero", "M")
persona2 = Persona("V-23569874", "Ana", "Poleo", "F")

print persona1.__doc__[25:34]
print len(persona1.__doc__[25:34]) * "="

print "\n" + str(persona1) + "\n"

print "- Cedula de identidad: {0}.".format(persona1.cedula)
print "- Nombre completo: {0} {1}.".format(persona1.nombre,
    persona1.apellido)
print "- Genero: {0}.".format(persona1.getGenero(persona1.sexo))
print "- {0} {1} dijo: {2}".format(persona1.nombre, 
    persona1.apellido, persona1.hablar("Hola Ana :-*"))

print persona1.hablar("\nHola, Soy una Persona") +", me llamo '"+ \
persona1.nombre +" "+ persona1.apellido +"', con cédula '"+  \
persona1.cedula +"'."

print "\nOtra " + persona1.__doc__[25:34]
print (len(persona1.__doc__[25:34])+5) * "-"

print "\n" + str(persona2) + "\n"

print "- Cedula de identidad: {0}.".format(persona2.cedula)
print "- Nombre completo: {0} {1}.".format(persona2.nombre,
    persona2.apellido)
print "- Genero: {0}.".format(persona2.getGenero(persona2.__getattribute__('sexo')))
print "- {0} {1} dijo: {2}".format(persona2.nombre, persona2.apellido, persona2.hablar("Hola Leonardo ^_^"))

print persona2.hablar("\nHola, Soy otra Persona") +", me llamo '"+ \
persona2.__getattribute__('nombre') +" "+ \
persona2.__getattribute__('apellido') +"', con cédula '"+  \
persona2.__getattribute__('cedula') +"'."

# Una instancia de Objeto Supervisor
supervisor1 = Supervisor("V-16987456", "Jen", "Paz", "D", "Chivo")

print "\n" + supervisor1.__doc__[26:37]
print len(supervisor1.__doc__[26:37]) * "="

print "\n" + str(supervisor1) + "\n"

# Atributo(s) y Método(s) heredado de la clase Persona
print "- Cedula de identidad: {0}.".format(supervisor1.cedula)
print "- Nombre completo: {0} {1}.".format(
	supervisor1.nombre, supervisor1.apellido)
print "- Genero: {0}.".format(
	supervisor1.getGenero(supervisor1.sexo))
print "- {0} {1} dijo: {2}".format(
	supervisor1.nombre, supervisor1.apellido, 
	supervisor1.hablar("A trabajar Leonardo!!!".upper()))

# Atributo(s) y Método(s) heredado de la clase Supervisor
print "- Rol: {0}.".format(supervisor1.rol)
print "- N. Tareas: {0}.".format(supervisor1.consulta_tareas())

# Mostrar los atributos y métodos propios de la clase Supervisor 
# y los heredados de la clase Persona
print """\nHola, Soy el {0} {1} {2}, mi cédula es '{3}', 
mi genero '{4}', con el rol '{5}' y mis tareas
asignadas '{6}'.""".format(
    supervisor1.__doc__[26:37].lower(),
    supervisor1.nombre, supervisor1.apellido, supervisor1.cedula, 
    supervisor1.getGenero(supervisor1.sexo), supervisor1.rol,
    supervisor1.consulta_tareas())
