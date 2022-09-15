from clases import Destreza, JefeCuadrilla, Obrero


# Una instancia de Objeto JefeCuadrilla
jefe_cuadrilla1 = JefeCuadrilla(
    "V-16987456",
    "Mario",
    "Paz",
    "M",
    "Derecho a todo",
    "Proyectos",
    "Pala",
    25,
    "Asfaltado",
)
jefe_cuadrilla1.tareas = ["14", "15", "16"]

print(jefe_cuadrilla1.__doc__[28:46])
print(len(jefe_cuadrilla1.__doc__[28:46]) * "=")

print("\n" + str(jefe_cuadrilla1) + "\n")

# Atributo(s) y Método(s) heredado de la clase Persona
print(f"- Cedula de identidad: {jefe_cuadrilla1.cedula}.")
print(f"- Nombre completo: {jefe_cuadrilla1.nombre} {jefe_cuadrilla1.apellido}.")
print(f"- Genero: {jefe_cuadrilla1.getGenero(jefe_cuadrilla1.sexo)}.")
print(
    "- {} {} dijo: {}".format(
        jefe_cuadrilla1.nombre,
        jefe_cuadrilla1.apellido,
        jefe_cuadrilla1.hablar("Hola Pedro :-)"),
    )
)

# Atributo(s) y Método(s) heredado de la clase Supervisor
print(f"- Rol: {jefe_cuadrilla1.rol}.")
print(f"- N. Tareas: {jefe_cuadrilla1.consulta_tareas()}.")

# Atributo(s) y Método(s) heredado de la clase Destreza
print(f"- Área de conocimiento: {jefe_cuadrilla1.area}.")
print(f"- Herramienta con más destreza: {jefe_cuadrilla1.herramienta}.")
print(f"- Años de experiencia: {jefe_cuadrilla1.experiencia}.")

# Atributo(s) y Método(s) heredado de la clase JefeCuadrilla
print(f"- Nombre de cuadrilla: {jefe_cuadrilla1.cuadrilla}.")

# Mostrar los atributos y métodos propios de la clase JefeCuadrilla
# y los heredados de la clase Persona y Supervisor.
print(
    """\nHola, Soy {}, me llamo {}.
mi rol es '{}', mi genero es '{}' y
estoy la cuadrilla '{}'.""".format(
        jefe_cuadrilla1.__doc__[28:46].lower(),
        (jefe_cuadrilla1.nombre + " " + jefe_cuadrilla1.apellido),
        jefe_cuadrilla1.rol,
        jefe_cuadrilla1.getGenero(jefe_cuadrilla1.sexo),
        jefe_cuadrilla1.cuadrilla,
    )
)


obrero1 = Obrero(
    "E-1456893", "Nicolás", "Maduro", "Pato", "Chófer", "Autobús", 23, True
)

print("\n" + obrero1.__doc__[37:44])
print(len(obrero1.__doc__[37:44]) * "=")

print("\n" + str(obrero1) + "\n")

# Atributo(s) y Método(s) heredado de la clase Persona
print(f"- Cedula de identidad: {obrero1.cedula}.")
print(f"- Nombre completo: {obrero1.nombre} {obrero1.apellido}.")
print(f"- Genero: {obrero1.getGenero(obrero1.sexo)}.")
print(
    "- {} {} dijo: {}".format(
        obrero1.nombre, obrero1.apellido, obrero1.hablar("Hola Cilita ;-)")
    )
)

# Atributo(s) y Método(s) heredado de la clase Destreza
print(f"- Área de conocimiento: {obrero1.area}.")
print(f"- Herramienta con más destreza: {obrero1.herramienta}.")
print(f"- Años de experiencia: {obrero1.experiencia}.")

# Atributo(s) y Método(s) heredado de la clase Obrero
print(f"- Patriotismo: {obrero1.getPatriotismo(obrero1.patriota)}.")

# Mostrar los atributos y métodos propios de la clase Obrero
# y los heredados de la clase Persona y Destreza.
print(
    """\nHola, Soy {}, me llamo {}.
mi sexo es '{}', mi área de conocimiento es '{}'
usando la herramienta '{}' tengo '{}' años de experiencia,
ademas soy un '{}'.""".format(
        obrero1.__doc__[37:44].lower(),
        (obrero1.nombre + " " + obrero1.apellido),
        obrero1.getGenero(obrero1.sexo),
        obrero1.area,
        obrero1.herramienta,
        obrero1.experiencia,
        obrero1.getPatriotismo(obrero1.patriota),
    )
)
