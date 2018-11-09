# -*- coding: utf8 -*-

from excepciones_propias import *


# Excepción ConoDeLaMadreError
try:
    raise ConoDeLaMadreError("No joda")
except ConoDeLaMadreError as cdlm:
    print type(cdlm)            # la instancia de excepción
    print "\t" + cdlm.__doc__   # __doc__ permite imprimir la docstring de la Excepción
    print "{0} \n".format(cdlm) # __str__ permite imprimir args directamente


# Excepción MaduroError
try:
    raise MaduroError("Maldito Maduro")
except MaduroError as m:
    print type(m)          # la instancia de excepción
    print "\t" + m.__doc__ # __doc__ permite imprimir la docstring de la Excepción
    print m                # __str__ permite imprimir args directamente
    print u'Un sentimiento nacional es:', m.sentimiento, "\n"


# Excepción CaraETablaError
try:
    raise CaraETablaError("Ramos Allud")
except CaraETablaError as carae:
    print type(carae)            # la instancia de excepción
    print "\t" + carae.__doc__   # __doc__ permite imprimir la docstring de la Excepción
    print "{0} \n".format(carae) # __str__ permite imprimir args directamente


# Excepción HijuEPutaError
try:
    raise HijuEPutaError(13)
except HijuEPutaError as hijue:
    print type(hijue)          # la instancia de excepción
    print "\t" + hijue.__doc__ # __doc__ permite imprimir la docstring de la Excepción
    print '\n¿Hace pacheco?'
    print hijue                # __str__ permite imprimir args directamente


# Excepción PuesError
try:
    raise PuesError("pollo" in ["carne", "leche", "huevos", "pan"])
except PuesError as pues:
    print type(pues)          # la instancia de excepción
    print "\t" + pues.__doc__ # __doc__ permite imprimir la docstring de la Excepción
    print '\n¿Es cierto?'
    print pues                # __str__ permite imprimir args directamente


# Excepción MaracuchoError
try:
    raise MaracuchoError("maracucho" in ["guaro", "gocho", "maracucho", "oriental", "caraqueño"])
except MaracuchoError as mcho:
    print type(mcho)            # la instancia de excepción
    print "\t" + mcho.__doc__   # __doc__ permite imprimir la docstring de la Excepción
    print "{0} \n".format(mcho) # __str__ permite imprimir args directamente


# Excepción VergaError
try:
    raise VergaError(120)
except VergaError as verga:
    print type(verga)            # la instancia de excepción
    print "\t" + verga.__doc__   # __doc__ permite imprimir la docstring de la Excepción
    print "{0} \n".format(verga) # __str__ permite imprimir args directamente
