"""Módulo de clases comunes"""


class Persona:
    """Clase que representa una Persona"""

    def __init__(self, cedula, nombre, apellido, sexo):
        """Constructor de clase Persona"""
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def __str__(self):
        """Devuelve una cadena representativa de Persona"""
        doc = self.__doc__[25:34] if self.__doc__ else "Persona"
        return f"{doc}: {str(self.cedula)}, {self.nombre} {self.apellido}, {self.getGenero(self.sexo)}."

    def hablar(self, mensaje):
        """Mostrar mensaje de saludo de Persona"""
        return mensaje

    def getGenero(self, sexo):
        """Mostrar el genero de la Persona"""
        genero = ("Masculino", "Femenino")
        if sexo == "M":
            return genero[0]
        elif sexo == "F":
            return genero[1]
        else:
            return "Desconocido"


class Supervisor(Persona):
    """Clase que representa a un Supervisor"""

    def __init__(self, cedula, nombre, apellido, sexo, rol):
        """Constructor de clase Supervisor"""

        # Invoca al constructor de clase Persona
        Persona.__init__(self, cedula, nombre, apellido, sexo)

        # Nuevos atributos
        self.rol = rol
        self.tareas = ["10", "11", "12", "13"]

    def __str__(self):
        """Devuelve una cadena representativa al Supervisor"""
        doc = self.__doc__[26:37] if self.__doc__ else "Supervisor"
        return f"{doc}: {self.nombre} {self.apellido}, rol: '{self.rol}', sus tareas: {self.consulta_tareas()}."

    def consulta_tareas(self):
        """Mostrar las tareas del Supervisor"""
        return ", ".join(self.tareas)


class Destreza:
    """Clase la cual representa la Destreza de la Persona"""

    def __init__(self, area, herramienta, experiencia):
        """Constructor de clase Destreza"""
        self.area = area
        self.herramienta = herramienta
        self.experiencia = experiencia

    def __str__(self):
        """Devuelve una cadena representativa de la Destreza"""
        return """Destreza en el área {} con la herramienta {},
        tiene {} años de experiencia.""".format(
            str(self.area),
            self.experiencia,
            self.herramienta,
        )


class JefeCuadrilla(Supervisor, Destreza):
    """Clase la cual representa al Jefe de Cuadrilla"""

    def __init__(
        self,
        cedula,
        nombre,
        apellido,
        sexo,
        rol,
        area,
        herramienta,
        experiencia,
        cuadrilla,
    ):
        """Constructor de clase Jefe de Cuadrilla"""

        # Invoca al constructor de clase Supervisor
        Supervisor.__init__(self, cedula, nombre, apellido, sexo, rol)
        # Invoca al constructor de clase Destreza
        Destreza.__init__(self, area, herramienta, experiencia)

        # Nuevos atributos
        self.cuadrilla = cuadrilla

    def __str__(self):
        """Devuelve cadena representativa al Jefe de Cuadrilla"""
        doc = self.__doc__[28:46] if self.__doc__ else "JefeCuadrilla"
        return f"{doc}: {self.nombre} {self.apellido}, rol '{self.rol}', tareas {self.consulta_tareas()}, cuadrilla: {self.cuadrilla}" 


class Obrero(Persona, Destreza):
    """Clase la cual representa al personal Obrero"""

    def __init__(
        self, cedula, nombre, apellido, sexo, area, herramienta, experiencia, patriota
    ):
        """Constructor de clase Obrero"""

        # Invoca al constructor de clase Persona
        Persona.__init__(self, cedula, nombre, apellido, sexo)
        # Invoca al constructor de clase Destreza
        Destreza.__init__(self, area, herramienta, experiencia)

        # Nuevos atributos
        self.patriota = patriota

    def __str__(self):
        """Devuelve una cadena representativa de un Obrero"""
        doc = self.__doc__[37:44] if self.__doc__ else "Obrero"
        return f"{doc}: {self.nombre} {self.apellido}, es {self.obtener_patriotismo(self.patriota)}."

    def obtener_patriotismo(self, patriota):
        """Mostrar el patriotismo de un Obrero"""
        patriotismo = ("RODILLA EN TIERRA", "APATRIDA")
        if patriota == True:
            return patriotismo[0]
        elif patriota == False:
            return patriotismo[1]
        else:
            return "NINI"
