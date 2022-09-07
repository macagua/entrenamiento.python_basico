class VenezolanoError(Exception):
    """ Clase base para expresiones Venezolanas. """
    def __init__(self, evaluar):
        self.evaluar = evaluar


class ConoDeLaMadreError(VenezolanoError):
    """ Clase base para la expresión Venezolana central Coño de la madre - CDLM. """
    def __init__(self, expresion):
        self.expresion = expresion
    def __str__(self):
        return "\nCoño de la madre, {0}!!!".format(str(self.expresion))


class MaduroError(ConoDeLaMadreError):
    """ Excepción lanzada por errores para la expresión CDLM Maduro. """
    def __init__(self, sentimiento):
        self.sentimiento = sentimiento
    def __str__(self):
        return "\nCoño de la madre, {0}!!!".format(str(self.sentimiento))


class CaraETablaError(ConoDeLaMadreError):
    """ Excepción lanzada por errores para la excepción Cara e' Tabla. """
    def __init__(self, expresion):
        self.expresion = expresion
    def __str__(self):
        return "\n¡Que Cara e' tabla es {0}!".format(str(self.expresion))


class HijuEPutaError(VenezolanoError):
    """ Excepción lanzada por errores para expresiones Venezolanas Andinas. """
    def __str__(self):
        if self.evaluar < 14:
            return "Uish, si que hijue puta, hace frio!!!\n"
        else:
            return "¡No, esta sereno!\n"


class PuesError(VenezolanoError):
    """ Excepción lanzada por errores para expresiones Venezolanas Llaneras. """
    def __str__(self):
        if self.evaluar:
            return "Pues compae!!!\n"
        else:
            return "Pues no compae!!!\n"


class MaracuchoError(VenezolanoError):
    """ Clase base para expresiones Marachuchas. """
    def __str__(self):
        print("\n¿Eres de Maracaibo?")
        if self.evaluar:
            return "Claro primo, cuando voy pa' Maracaibo y empiezo a pasar el puente..."
        else:
            return "No primo, yo soy Zuliano, de Cabimas!!!"


class VergaError(MaracuchoError):
    """ Clase base para expresiones del verbo Vergación. """
    def __str__(self):
        if self.evaluar != 150:
            return "\n¡Vergación de error primo, lo fregaste, con el valor {0}.".format(self.evaluar)
        else:
            return "\n¡Verga primo, es: {0}".format(self.evaluar)