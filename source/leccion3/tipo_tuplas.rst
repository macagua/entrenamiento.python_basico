.. -*- coding: utf-8 -*-


.. _python_tuplas:

Tipo tuplas
-----------

La tupla es una lista inmutable. Esta no puede modificarse de ningún 
modo después de su creación.

Ejemplo de tuplas
.................

A continuación, se presentan algunos ejemplos de su uso:

**Ejemplo simple de tupla**

.. literalinclude:: ../../recursos/leccion3/tipo_tuplas.py
    :language: python
    :lines: 9-9


**Ejemplo de tuplas anidadas**

.. literalinclude:: ../../recursos/leccion3/tipo_tuplas.py
    :language: python
    :lines: 12-12


**Operación asignar de valores de una tupla en variables**

.. literalinclude:: ../../recursos/leccion3/tipo_tuplas.py
    :language: python
    :lines: 15-15


**Cuidar seguimiento del número de la numeración**

Una tarea común es iterar sobre una secuencia mientras cuidas 
el seguimiento de la numeración de un elemento.

Podría usar un bucle ``while`` con un contador o un bucle ``for`` 
usando la función :ref:`range <python_funcion_range>` y la función 
:ref:`len <python_funcion_len>`:

::

	>>> words = ('cool', 'powerful', 'readable')
	>>> for i in range(0, len(words)):
	...     print i, words[i]
	0 cool
	1 powerful
	2 readable

Pero, Python provee la palabra reservada ``enumerate`` para esto:

.. literalinclude:: ../../recursos/leccion3/tipo_tuplas.py
    :language: python
    :lines: 43-44


**Caso real de conexión a BD**

A continuación, un ejemplo más apegado a la realidad que busca 
establecer una conexión a una BD:

.. literalinclude:: ../../recursos/leccion3/tipo_tuplas.py
    :language: python
    :lines: 18-38


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_tuplas.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_tuplas.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando: ::

        python tipo_tuplas.py

----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre las **tuplas** 
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

::

    >>> help(tuple)


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
