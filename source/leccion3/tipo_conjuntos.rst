.. -*- coding: utf-8 -*-


.. _python_set:

Tipo conjuntos
--------------

Un conjunto, es una colección no ordenada y sin elementos repetidos. Los usos básicos 
de éstos incluyen verificación de pertenencia y eliminación de entradas duplicadas.

+---------------+-----------+-------------------------+-------------------------------------+
| **Clase**     | **Tipo**  | **Notas**               | **Ejemplo**                         |
+---------------+-----------+-------------------------+-------------------------------------+
| ``set``       | Conjuntos | Mutable, sin orden, no  | ``set([4.0, 'Carro', True])``       |
|               |           | contiene duplicados.    |                                     |
+---------------+-----------+-------------------------+-------------------------------------+
| ``frozenset`` | Conjuntos | Inmutable, sin orden,   | ``frozenset([4.0, 'Carro', True])`` |
|               |           | no contiene duplicados. |                                     |
+---------------+-----------+-------------------------+-------------------------------------+

.. note::

	- **Mutable:** su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.

	- **Inmutable:** su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.


----


Convertir a conjuntos
.....................

Para convertir a *tipos conjuntos* debe usar las funciones :ref:`set() <python_fun_set>` 
y :ref:`frozenset() <python_fun_frozenset>`, las cuales 
:ref:`están integradas <python_fun_builtins>` en el interprete Python.

.. tip:: 
    Para más información consulte las funciones integradas para 
    :ref:`operaciones de secuencias <python_fun_builtins_secuencias>`.


Ejemplo de conjuntos set
........................

A continuación, se presentan un ejemplo de conjuntos ``set``:

.. literalinclude:: ../../recursos/leccion3/tipo_conjuntos.py
    :language: python
    :lines: 9-38

----

Ejemplo de conjuntos frozenset
..............................

A continuación, se presentan un ejemplo de conjuntos ``frozenset``:

::

	>>> inmutable = frozenset([1, 2, 3, 2, 1, 4, 5, 3])
	>>> print inmutable, type(inmutable)
	frozenset([1, 2, 3, 4, 5]) <type 'frozenset'>

Los elementos de un set son únicos (sin repeticiones dentro del ``set``), y deben 
ser objetos inmutables: números, cadenas de caracteres, tuplas y sets inmutables, 
pero no listas ni sets mutables.


----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los **conjuntos set** 
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

::

    >>> help(set)

Usted puede consultar toda la documentación disponible sobre los **conjuntos frozenset** 
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

::

    >>> help(frozenset)

Para salir de esa ayuda presione la tecla ``q``.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_conjuntos.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_conjuntos.py`, abra una consola de comando, 
    acceda al directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    ::

        python tipo_conjuntos.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
