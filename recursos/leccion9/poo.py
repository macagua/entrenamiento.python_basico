class Persona:
    """Clase que representa una Persona"""

    cedula = "V-26938401"
    nombre = "Leonardo"
    apellido = "Caballero"
    sexo = "M"

    def hablar(self, mensaje):
        """Mostrar mensaje de saludo de Persona"""
        return mensaje


macagua = Persona
print("El objeto de la clase {}, {}.".format(macagua.__name__, macagua.__doc__))
print("Hola, mucho gusto, mi nombre es '{} {}', \nmi cédula de identidad es '{}', y mi sexo es '{}'.".format(
    macagua.nombre,
    macagua.apellido,
    macagua.cedula,
    macagua.sexo)
)
