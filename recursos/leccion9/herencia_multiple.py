# -*- coding: utf8 -*-

from clases import Destreza, JefeCuadrilla, Obrero

# Una instancia de Objeto JefeCuadrilla
jefe_cuadrilla1 = JefeCuadrilla("V-16987456", "Mario", "Paz", 
    "M", "Derecho a todo", "Proyectos", "Pala", 25, "Asfaltado")
jefe_cuadrilla1.tareas = ['14','15','16']

print(jefe_cuadrilla1.__doc__[28:46])
print(len(jefe_cuadrilla1.__doc__[28:46]) * "=")

print("\n" + str(jefe_cuadrilla1) + "\n")

# Atributo(s) y Método(s) heredado de la clase Persona
print("- Cedula de identidad: {0}.".format(jefe_cuadrilla1.cedula))
print("- Nombre completo: {0} {1}.".format(jefe_cuadrilla1.nombre,
    jefe_cuadrilla1.apellido))
print("- Genero: {0}.".format(jefe_cuadrilla1.getGenero(jefe_cuadrilla1.sexo)))
print("- {0} {1} dijo: {2}".format(jefe_cuadrilla1.nombre, 
    jefe_cuadrilla1.apellido, jefe_cuadrilla1.hablar("Hola Pedro :-)")))

# Atributo(s) y Método(s) heredado de la clase Supervisor
print("- Rol: {0}.".format(jefe_cuadrilla1.rol))
print("- N. Tareas: {0}.".format(jefe_cuadrilla1.consulta_tareas()))

# Atributo(s) y Método(s) heredado de la clase Destreza
print("- Área de conocimiento: {0}.".format(jefe_cuadrilla1.area))
print("- Herramienta con más destreza: {0}.".format(jefe_cuadrilla1.herramienta))
print("- Años de experiencia: {0}.".format(jefe_cuadrilla1.experiencia))

# Atributo(s) y Método(s) heredado de la clase JefeCuadrilla
print("- Nombre de cuadrilla: {0}.".format(jefe_cuadrilla1.cuadrilla))

# Mostrar los atributos y métodos propios de la clase JefeCuadrilla 
# y los heredados de la clase Persona y Supervisor.
print("""\nHola, Soy {0}, me llamo {1}.
mi rol es '{2}', mi genero es '{3}' y 
estoy la cuadrilla '{4}'.""".format(
    jefe_cuadrilla1.__doc__[28:46].lower(),
    (jefe_cuadrilla1.nombre +" "+ jefe_cuadrilla1.apellido), 
    jefe_cuadrilla1.rol,
    jefe_cuadrilla1.getGenero(jefe_cuadrilla1.sexo),
    jefe_cuadrilla1.cuadrilla))


obrero1 = Obrero("E-1456893", "Nicolás", "Maduro", "Pato", 
    "Chófer", "Autobús", 23, True)

print("\n" + obrero1.__doc__[37:44])
print(len(obrero1.__doc__[37:44]) * "=")

print("\n" + str(obrero1) + "\n")

# Atributo(s) y Método(s) heredado de la clase Persona
print("- Cedula de identidad: {0}.".format(obrero1.cedula))
print("- Nombre completo: {0} {1}.".format(obrero1.nombre,
    obrero1.apellido))
print("- Genero: {0}.".format(obrero1.getGenero(obrero1.sexo)))
print("- {0} {1} dijo: {2}".format(obrero1.nombre, 
    obrero1.apellido, obrero1.hablar("Hola Cilita ;-)")))

# Atributo(s) y Método(s) heredado de la clase Destreza
print("- Área de conocimiento: {0}.".format(obrero1.area))
print("- Herramienta con más destreza: {0}.".format(obrero1.herramienta))
print("- Años de experiencia: {0}.".format(obrero1.experiencia))

# Atributo(s) y Método(s) heredado de la clase Obrero
print("- Patriotismo: {0}.".format(
    obrero1.getPatriotismo(obrero1.patriota)))

# Mostrar los atributos y métodos propios de la clase Obrero 
# y los heredados de la clase Persona y Destreza.
print("""\nHola, Soy {0}, me llamo {1}.
mi sexo es '{2}', mi área de conocimiento es '{3}' 
usando la herramienta '{4}' tengo '{5}' años de experiencia,
ademas soy un '{6}'.""".format(
    obrero1.__doc__[37:44].lower(),
    (obrero1.nombre +" "+ obrero1.apellido), 
    obrero1.getGenero(obrero1.sexo), obrero1.area, 
    obrero1.herramienta, obrero1.experiencia,
    obrero1.getPatriotismo(obrero1.patriota)))
