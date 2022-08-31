.. -*- coding: utf-8 -*-


.. _python_opers_relacionales:

Operadores relacionales
-----------------------

Los valores booleanos son además el resultado de expresiones que utilizan operadores 
relacionales (comparaciones entre valores):


.. _python_opers_rela_igual:

Operador ==
...........

El operador ``==`` evalúa que los valores sean *iguales* para varios tipos de datos.

::

    >>> 5 == 3
    False
    >>> 5 == 5
    True
    >>> "Plone" == 5
    False
    >>> "Plone" == "Plone"
    True
    >>> type("Plone") == str
    True


.. _python_opers_rela_dist:

Operador !=
...........

El operador ``!=`` evalúa si los valores son *distintos*.

::

    >>> 5 != 3
    True
    >>> "Plone" != 5
    True
    >>> "Plone" != False
    True


.. _python_opers_rela_menor:

Operador <
..........

El operador ``<`` evalúa si el valor del lado izquierdo es *menor que* el valor del 
lado derecho.

::

    >>> 5 < 3
    False


.. _python_opers_rela_mayor:

Operador >
..........

El operador ``>`` evalúa si el valor del lado izquierdo es *mayor que* el valor del 
lado derecho.

::

    >>> 5 > 3
    True


.. _python_opers_rela_menigu:

Operador <=
...........

El operador ``<=`` evalúa si el valor del lado izquierdo es *menor o igual que* el 
valor del lado derecho.

::

    >>> 5 <= 3
    False


.. _python_opers_rela_mayigu:

Operador >=
...........

El operador ``>=`` evalúa si el valor del lado izquierdo es *mayor o igual que* el 
valor del lado derecho.

::

    >>> 5 >= 3
    True


.. _python_opers_rela_ejs:

Ejemplos
........

A continuación, se presentan algunos ejemplos de su uso:

**Ejemplo de definir variables de tipo numéricas, cadenas y listas**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :language: python
    :lines: 3-5


**Ejemplo de operador relacional Igual**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :language: python
    :lines: 8-9


**Ejemplo de operador relacional Diferente**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :language: python
    :lines: 18-19


**Ejemplo de operador relacional Menor que**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :language: python
    :lines: 25-26


**Ejemplo de operador relacional Mayor que**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :language: python
    :lines: 29-30


**Ejemplo de operador relacional Menor o igual que**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :language: python
    :lines: 33-34


**Ejemplo de operador relacional Mayor o igual que**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :language: python
    :lines: 37-38


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/operadores_relacionales.py>`.


.. tip::
    Para ejecutar el código :file:`operadores_relacionales.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando:

    ::

        python operadores_relacionales.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
