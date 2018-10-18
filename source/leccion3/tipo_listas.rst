.. -*- coding: utf-8 -*-


.. _python_listas:

Tipos de listas
---------------

La lista en Python son variables que almacenan ``arrays``, 
internamente cada posición puede ser un tipo de datos distinto.

En Python tiene varios tipos de datos *compuestos*, usados para agrupar otros
valores.  El más versátil es la *lista*, la cual puede ser escrita como una
lista de valores separados por coma (ítems) entre corchetes.  No es necesario
que los ítems de una lista tengan todos el mismo tipo. ::

   >>> a = ['pan', 'huevos', 100, 1234]
   >>> a
   ['pan', 'huevos', 100, 1234]


Ejemplo de listas
.................

A continuación, se presentan algunos ejemplos de su uso:

**Ejemplo de establecer una colección ordenada/arreglos o vectores**

.. literalinclude:: ../../recursos/leccion3/tipo_listas.py
    :linenos:
    :language: python
    :lines: 9-10


**Ejemplo de acceder a un elemento especifico de una lista**

.. literalinclude:: ../../recursos/leccion3/tipo_listas.py
    :linenos:
    :language: python
    :lines: 13-14


**Ejemplo de acceder a un elemento a una lista anidada**

.. literalinclude:: ../../recursos/leccion3/tipo_listas.py
    :linenos:
    :language: python
    :lines: 17-18


**Ejemplo de establecer nuevo valor de un elemento de lista**

.. literalinclude:: ../../recursos/leccion3/tipo_listas.py
    :linenos:
    :language: python
    :lines: 21-23


**Ejemplo de obtener un rango de elemento especifico**

.. literalinclude:: ../../recursos/leccion3/tipo_listas.py
    :linenos:
    :language: python
    :lines: 26-27


**Ejemplos de obtener un rango con saltos de elementos específicos**

.. literalinclude:: ../../recursos/leccion3/tipo_listas.py
    :linenos:
    :language: python
    :lines: 30-34

**Ejemplo de iterar sobre cualquier secuencia**

Usted puede iterar sobre cualquier secuencia (cadena de texto, lista, 
claves en un diccionario, lineas en un archivo, ...):

*Ejemplo de iterar sobre una cadena de texto*

::

    >>> vocales = 'aeiou'

    >>> for letra in 'hermosa':
    ...     if letra in vocales:
    ...         print letra,
    e o a

*Ejemplo de iterar sobre una lista*

::

    >>> mensaje = "Hola, como estas tu?"
    >>> mensaje.split() # retorna una lista
    ['Hola,', 'como', 'estas', 'tu?']
    >>> for palabra in mensaje.split():
    ...     print palabra
    ...
    Hola,
    como
    estas
    tu?

*Ejemplo de iterar sobre dos o más secuencias*

Para iterar sobre dos o más secuencias al mismo tiempo, los valores pueden 
emparejarse con la función ``zip()``.

>>> preguntas = ['nombre', 'objetivo', 'sistema operativo']
>>> respuestas = ['Leonardo', 'aprender Python', 'Linux']
>>> for pregunta, respuesta in zip(preguntas, respuestas):
...     print '¿Cual es tu {0}?, la respuesta es: {1}.'.format(pregunta, respuesta)
... 
¿Cual es tu nombre?, la respuesta es: Leonardo.
¿Cual es tu objetivo?, la respuesta es: aprender Python.
¿Cual es tu sistema operativo?, la respuesta es: Linux.
>>> 

Referencia
..........

- `Iterate over any sequence - Scipy lecture notes`_.


.. _`Iterate over any sequence - Scipy lecture notes`: https://www.pybonacci.org/scipy-lecture-notes-ES/intro/language/control_flow.html#iterate-over-any-sequence
