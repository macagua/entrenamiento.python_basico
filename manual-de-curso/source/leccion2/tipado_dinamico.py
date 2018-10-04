# -*- coding: utf8 -*-

"""
    El tipado dinámico significa que los objetos en tiempo de 
    ejecución (valores) tienen un tipo, a diferencia del tipado 
    estático donde las variables tienen un tipo.

    >>> variable = 11
    >>> print variable, type(variable)
    11 <type 'int'>
    >>> variable = "activo"
    >>> print (variable), type(variable)
    activo <type 'str'>
"""

variable = 11 # "variable" guarda un valor entero
print variable, type(variable)
variable = "activo" # "variable" guarda un valor cadena
print (variable), type(variable)
