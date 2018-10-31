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
        """ Devuelve una cadena representativa de Persona """
        return "%s: %s %s, %s." % (
            str(self.cedula), self.nombre,
            self.apellido, self.sexo
        )

    def hablar(self, mensaje):
        """ Mostrar mensaje de saludo de Persona """
        return mensaje

    def getSexo(self, sexo):
        """ Mostrar el genero de la Persona """
        genero = ('Masculino','Femenino')
        if sexo == "M":
            return genero[0]
        elif sexo == "F":
            return genero[1]
        else:
            return "Genero desconocido"


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

# Dos instancias de Objeto Persona
persona1 = Persona("V-13458796", "Leonardo", "Caballero", "M")
persona2 = Persona("V-23569874", "Ana", "Poleo", "F")
persona1.hablar("Hola Mundo")
print persona1
print persona1.nombre, persona1.apellido, persona1.getSexo(persona1.sexo)

print persona1.hablar("Hola, Soy una Persona") +", me llamo '"+ \
persona1.nombre +" "+ persona1.apellido +"' y mi cédula de identidad es '"+  \
persona1.cedula +"'."

print "\n" + str(persona2)
print "Nombre: {0} {1}, sexo: {2}.".format(
    persona2.nombre, persona2.apellido, persona2.getSexo(persona2.__getattribute__('sexo')))

print persona2.hablar("Hola, Soy una Persona") +", me llamo '"+ \
persona2.__getattribute__('nombre') +" "+ \
persona2.__getattribute__('apellido') +"' y mi cédula de identidad es '"+  \
persona1.__getattribute__('cedula') +"'."

# Una instancia de Objeto Supervisor
supervisor1 = Supervisor("V-16987456", "Pedro", "Perez", "No se", "El chivo")
print "\n" + str(supervisor1)
print "El permiso es: {0}.".format(supervisor1.permisos)
print "Las tareas son: {0}.".format(supervisor1.consulta_tareas())
# Método heredado de la clase Persona
print "El sexo es: {0}.".format(
    supervisor1.getSexo(supervisor1.sexo))

# Mostrar los atributos y métodos propios de la clase Supervisor 
# y los heredados de la clase Persona
print supervisor1.hablar("Hola, Soy el supervisor") +", me llamo "+ \
supervisor1.nombre +", mi cargo es '"+ \
supervisor1.permisos +"' y mi sexo es '"+  \
supervisor1.getSexo(supervisor1.sexo) +"'."
