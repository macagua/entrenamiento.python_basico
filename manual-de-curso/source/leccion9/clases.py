# -*- coding: utf8 -*-

class Persona(object):
    """ Clase que representa una persona. """

    def __init__(self, cedula, nombre, apellido, sexo):
        """ Constructor de clase Persona """
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def __str__(self):
        """ Devuelve una cadena representativa al Persona """
        return "%s: %s %s, %s." % (
            str(self.cedula), self.nombre,
            self.apellido, self.sexo
        )

    def hablar(self, mensaje):
        """ Mostrar mensaje de saludo de Persona """
        print mensaje

class Supervisor(Persona):
    """ Clase que representa a un Supervisor """

    def __init__(self, cedula, nombre, apellido, sexo, permisos):
        """ Constructor de clase Supervisor """

        # Invoca al constructor de clase Persona
        Persona.__init__(self, cedula, nombre, apellido, sexo)

        # Nuevos atributos
        self.permisos = permisos
        self.tareas = ['10','11','12','13']

    def __str__(self):
        """ Devuelve una cadena representativa al Supervisor """
        return "%s %s, rol(es) '%s', sus tareas: %s." % (
            self.nombre, self.apellido, self.permisos, self.consulta_tareas()
        )

    def consulta_tareas(self):
        """ Mostrar las tareas del Supervisor """
        return ', '.join(self.tareas)

# Instancia de Objeto Persona
persona1 = Persona("V-13458796", "Leonardo", "Caballero", "M")
persona2 = Persona("V-23569874", "Ana", "Poleo", "F")
persona1.hablar("Hola Mundo")
print persona1.nombre, persona1.apellido
print "{0} {1}.".format(persona2.nombre, persona2.apellido)

# Instancia de Objeto Supervisor
supervisor1 = Supervisor("V-16987456", "Pedro", "Perez", "No se", "El chivo")
print supervisor1
print "El permiso es: {0}.".format(supervisor1.permisos)
print "Las tareas son: {0}.".format(supervisor1.consulta_tareas())

