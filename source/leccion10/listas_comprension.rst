.. -*- coding: utf-8 -*-


.. _python_listas_comprension:

Listas de comprensión
---------------------

La listas de comprensión, del inglés *list comprehensions*, es una funcionalidad 
que le permite crear listas avanzadas en una misma línea de código. 

La forma general de la definición de una lista por comprensión es: 

::

    [expresion for item in iterable]

Opcionalmente, se puede incluir un condicional en la expresión: 

::

    [expresion for item in iterable if condicion]

``expresion`` puede ser cualquier expresión computable en Python, generalmente 
involucrando un ``item`` del iterable llamado ``iterable`` puede ser cualquier 
objeto iterable, como una secuencia (:ref:`lista <python_list>` o 
:ref:`cadena de caracteres <python_str>`), la función la función 
:ref:`range() <python_fun_range>`, etc.

La salida siempre es un tipo de :ref:`lista <python_list>` Python.


Ejemplo 1
.........

Si requiere crear una lista de 4 elementos y cada elemento calcularle la potencia 
de 2, usando el método tradicional, eso seria así:

::

    >>> lista = []
    >>> for i in range(4):
    ...     lista.append(i**2)
    ... 
    >>> print lista
    [0, 1, 4, 9]

Entonces el ejemplo anterior usando listas de comprensión, eso seria así:

::

    >>> [i**2 for i in range(4)]
    [0, 1, 4, 9]


Ejemplo 2
.........

A continuación se crear una lista con las letras de una palabra, usando el método 
tradicional, eso seria así:

::

    >>> lista = []
    >>> for letra in 'casa':
    ...     lista.append(letra)
    ... 
    >>> print lista
    ['c', 'a', 's', 'a']


Entonces el ejemplo anterior usando listas de comprensión, eso seria así:

::

    >>> lista = [letra for letra in 'casa']
    >>> print lista
    ['c', 'a', 's', 'a']

Como puede detallar en el ejemplo anterior, gracias a la listas de comprensión 
usted puede indicar directamente cada elemento que va a formar la lista, en este 
caso cada letra, a la vez que definimos el :ref:`bucle for <python_bucle_for>`, 
entonces la lista está formada por cada letra que recorremos en el bucle ``for``.


Ejemplo 3
.........

A continuación se crear una lista con las potencias de 2 de los primeros 10 
números, usando el método tradicional, eso seria así:

::

    >>> lista = []
    >>> for numero in range(0,11):
    ...     lista.append(numero**2)
    ... 
    >>> print lista
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Entonces el ejemplo anterior usando listas de comprensión, eso seria así:

::

    >>> lista = [numero**2 for numero in range(0,11)]
    >>> print lista
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

De este código anterior usted puede aprender que es posible modificar al vuelo 
los elementos los cuales van a formar la lista.


Ejemplo 4
.........

A continuación se crear una lista con los todos los múltiples de 2 entre 0 y 10, 
usando el método tradicional, eso seria así:

::

    >>> lista = []
    >>> for numero in range(0,11):
    ...     lista.append(numero**2)
    ... 
    >>> print lista
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


También, si añade al código anterior, los números del 0 al 10 cuando su módulo de 
2 sea 0 usando el método tradicional, eso seria así:

::

    >>> lista = []
    >>> for numero in range(0,11):
    ...     if numero % 2 == 0:
    ...         lista.append(numero)
    ... 
    >>> print lista
    [0, 2, 4, 6, 8, 10]

Entonces el ejemplo anterior donde crear una lista con los todos los múltiples de 
2 entre 0 y 10, usando listas de comprensión, eso seria así:

::

    >>> lista = [numero for numero in range(0,11) if numero % 2 == 0 ]
    >>> print lista
    [0, 2, 4, 6, 8, 10]

Para el ejemplo anterior donde crear una lista con los todos los múltiples de 2 
entre 0 y 10 cuando su módulo de 2 sea 0, usando listas de comprensión, eso seria 
así:

::

    >>> [numero for numero in range(0,11) if numero % 2 == 0 ] 
    [0, 2, 4, 6, 8, 10]

En este caso puede observar que incluso puede marcar una condición justo al final 
para añadir o no el elemento en la lista.


Ejemplo 5
.........

A continuación se crear una lista de pares a partir de otra lista creada con las 
potencias de 2 de los primeros 10 números, usando el método tradicional, eso seria 
así:

::

    >>> lista = []
    >>> for numero in range(0,11):
    ...     lista.append(numero**2)
    ... 
    >>> pares = []
    >>> for numero in lista:
    ...     if numero % 2 == 0:
    ...         pares.append(numero)
    ... 
    >>> print pares
    [0, 4, 16, 36, 64, 100]

Entonces el ejemplo anterior usando listas de comprensión, eso seria así:

::

    >>> lista = [numero for numero in 
    ...             [numero**2 for numero in range(0,11)] 
    ...                 if numero % 2 == 0]
    >>> print lista
    [0, 4, 16, 36, 64, 100]

Crear listas a partir de listas anidadas le permite llevar la listas de comprensión 
al siguiente nivel y además no hay un límite.


Usando Listas de comprensión con Archivos
.........................................

.. todo::
    TODO escribir esta sección.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion10>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
