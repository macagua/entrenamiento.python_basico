# -*- coding: utf8 -*-

# Importar el modulo llamado "funciones"
import funciones

print "Importo el modulo '{0}'\n".format(
    funciones.__file__.replace(
    	funciones.__file__, "funciones.pyc"))

print "Función '{0}' del módulo '{1}' se llamo mostrando:".format(
    funciones.mensaje.__name__,
    funciones.__file__.replace(
    	funciones.__file__, "funciones.pyc"))

# Usted puede llamar una función definida dentro del módulo
funciones.mensaje("Python")
