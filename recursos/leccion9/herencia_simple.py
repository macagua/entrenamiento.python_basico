from clases import Persona, Supervisor

# Dos instancias de Objeto Persona
persona1 = Persona("V-26938401", "Leonardo", "Caballero", "M")
persona2 = Persona("V-23569874", "Ana", "Poleo", "F")

print(persona1.__doc__[25:34])
print(len(persona1.__doc__[25:34]) * "=")

print("\n" + str(persona1) + "\n")

print(f"- Cédula de identidad: {persona1.cedula}.")
print(f"- Nombre completo: {persona1.nombre} {persona1.apellido}.")
print(f"- Genero: {persona1.obtener_genero(persona1.sexo)}.")
print(
    "- {} {} dijo: {}".format(
        persona1.nombre, persona1.apellido, persona1.hablar("Hola Ana :-*")
    )
)

print(
    persona1.hablar("\nHola, Soy una Persona")
    + ", me llamo '"
    + persona1.nombre
    + " "
    + persona1.apellido
    + "', con cédula '"
    + persona1.cedula
    + "'."
)

print("\nOtra " + persona1.__doc__[25:34])
print((len(persona1.__doc__[25:34]) + 5) * "-")

print("\n" + str(persona2) + "\n")

print(f"- Cédula de identidad: {persona2.cedula}.")
print(f"- Nombre completo: {persona2.nombre} {persona2.apellido}.")
print(
    "- Genero: {}.".format(persona2.obtener_genero(persona2.__getattribute__("sexo")))
)
print(
    "- {} {} dijo: {}".format(
        persona2.nombre, persona2.apellido, persona2.hablar("Hola Leonardo ^_^")
    )
)

print(
    persona2.hablar("\nHola, Soy otra Persona")
    + ", me llamo '"
    + persona2.__getattribute__("nombre")
    + " "
    + persona2.__getattribute__("apellido")
    + "', con cédula '"
    + persona2.__getattribute__("cedula")
    + "'."
)

# Una instancia de Objeto Supervisor
supervisor1 = Supervisor("V-16987456", "Jen", "Paz", "D", "Chivo")

print("\n" + supervisor1.__doc__[26:37])
print(len(supervisor1.__doc__[26:37]) * "=")

print("\n" + str(supervisor1) + "\n")

# Atributo(s) y Método(s) heredado de la clase Persona
print(f"- Cédula de identidad: {supervisor1.cedula}.")
print(f"- Nombre completo: {supervisor1.nombre} {supervisor1.apellido}.")
print(f"- Genero: {supervisor1.obtener_genero(supervisor1.sexo)}.")
print(
    "- {} {} dijo: {}".format(
        supervisor1.nombre,
        supervisor1.apellido,
        supervisor1.hablar("A trabajar Leonardo!!!".upper()),
    )
)

# Atributo(s) y Método(s) heredado de la clase Supervisor
print(f"- Rol: {supervisor1.rol}.")
print(f"- N. Tareas: {supervisor1.consulta_tareas()}.")

# Mostrar los atributos y métodos propios de la clase Supervisor
# y los heredados de la clase Persona
print(
    """\nHola, Soy el {} {} {}, mi cédula es '{}',
mi genero '{}', con el rol '{}' y mis tareas
asignadas '{}'.""".format(
        supervisor1.__doc__[26:37].lower(),
        supervisor1.nombre,
        supervisor1.apellido,
        supervisor1.cedula,
        supervisor1.obtener_genero(supervisor1.sexo),
        supervisor1.rol,
        supervisor1.consulta_tareas(),
    )
)
