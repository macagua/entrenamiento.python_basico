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
print(f"El objeto de la clase {macagua.__name__}, {macagua.__doc__}.")
print(f"Hola, mucho gusto, mi nombre es '{macagua.nombre} {macagua.apellido}', \nmi cédula de identidad es '{macagua.cedula}', y mi sexo es '{macagua.sexo}'.")
