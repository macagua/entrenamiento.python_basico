.. -*- coding: utf-8 -*-


.. _python_conjuntos:

Tipo conjuntos
--------------

Un conjunto, es una colección no ordenada y sin elementos repetidos. 
Los usos básicos de éstos incluyen verificación de pertenencia y 
eliminación de entradas duplicadas.

+---------------+-----------+----------------------------------------------+----------------------------------+
| **Tipo**      | **Clase** | **Notas**                                    | **Ejemplo**                      |
+---------------+-----------+----------------------------------------------+----------------------------------+
| ``set``       | Conjunto  | Mutable, sin orden, no contiene duplicados   | set([4.0, 'Carro', True])        |
+---------------+-----------+----------------------------------------------+----------------------------------+
| ``frozenset`` | Conjunto  | Inmutable, sin orden, no contiene duplicados | frozenset([4.0, 'Carro', True])  |
+---------------+-----------+----------------------------------------------+----------------------------------+

.. note::

	- **Mutable:** si su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.

	- **Inmutable:** si su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.


Ejemplo de conjuntos set
........................

A continuación, se presentan un ejemplo de conjuntos ``set``:

.. literalinclude:: ../../recursos/leccion3/tipo_conjuntos.py
    :linenos:
    :language: python
    :lines: 9-42

----

Ejemplo de conjuntos frozenset
..............................

A continuación, se presentan un ejemplo de conjuntos ``frozenset``:

::

	>>> a = frozenset([1, 2, 3, 2, 1, 4, 5, 3])
	>>> a
	frozenset([1, 2, 3, 4, 5])
	>>> print a, type(a)
	frozenset([1, 2, 3, 4, 5]) <type 'frozenset'>
	>>> 

Los elementos de un set son únicos (sin repeticiones dentro del ``set``), y 
deben ser objetos inmutables: números, cadenas de caracteres, tuplas y sets 
inmutables, pero no listas ni sets mutables.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_conjuntos.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_conjuntos.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando: ::

        python2 tipo_conjuntos.py

----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los 
**conjuntos set** desde la :ref:`consola interactiva <python_interactivo>` 
de la siguiente forma:

::

    >>> help(set)

Usted puede consultar toda la documentación disponible sobre los 
**conjuntos frozenset** desde la :ref:`consola interactiva <python_interactivo>` 
de la siguiente forma:

::

    >>> help(frozenset)

Para salir de esa ayuda presione la tecla ``q``.
