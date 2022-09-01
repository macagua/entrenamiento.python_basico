.. -*- coding: utf-8 -*-


.. _python_fun_recursivas:

Funciones recursivas
--------------------

Las funciones recursivas son funciones que se llaman a sí mismas durante su propia 
ejecución. Ellas funcionan de forma similar a las iteraciones, pero debe encargarse 
de planificar el momento en que dejan de llamarse a sí mismas o tendrá una función 
recursiva infinita.

Estas funciones se estilan utilizar para dividir una tarea en sub-tareas más simples 
de forma que sea más fácil abordar el problema y solucionarlo.

Función recursiva sin retorno
.............................

Un ejemplo de una función recursiva sin retorno, es el ejemplo de cuenta regresiva 
hasta cero a partir de un número:

::

    >>> def cuenta_regresiva(numero):
    ...     numero -= 1
    ...     if numero > 0:
    ...         print(numero)
    ...         cuenta_regresiva(numero)
    ...     else:
    ...         print("Boooooooom!")
    ...     print("Fin de la función", numero)
    ... 
    >>> cuenta_regresiva(5)
    4
    3
    2
    1
    Boooooooom!
    Fin de la función 0
    Fin de la función 1
    Fin de la función 2
    Fin de la función 3
    Fin de la función 4

Función recursiva con retorno
.............................

Un ejemplo de una función recursiva con retorno, es el ejemplo del calculo del 
factorial de un número corresponde al producto de todos los números desde 1 hasta 
el propio número. Es el ejemplo con retorno más utilizado para mostrar la utilidad 
de este tipo de funciones:

::

    >>> def factorial(numero):
    ...     print("Valor inicial ->",numero)
    ...     if numero > 1:
    ...         numero = numero * factorial(numero -1)
    ...     print("valor final ->",numero)
    ...     return numero
    ... 
    >>> print(factorial(5))
    Valor inicial -> 5
    Valor inicial -> 4
    Valor inicial -> 3
    Valor inicial -> 2
    Valor inicial -> 1
    valor final -> 1
    valor final -> 2
    valor final -> 6
    valor final -> 24
    valor final -> 120
    120

.. todo::
    TODO terminar de escribir la sección Funciones recursivas.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion5>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
