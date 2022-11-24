.. -*- coding: utf-8 -*-


.. _python_opers_pertenencia:

Operadores de pertenencia
-------------------------

Estos son los distintos tipos de operadores de pertenencia con los que puede evaluar
si se encuentra un objeto en una determinada colección:


.. _python_opers_in:

Operador in
...........

El operador ``in``, significa, para cualquier colección del valor del lado izquierdo
contenga el valor del lado derecho:

.. code-block:: pycon

    >>> b = [1, 2, 3]
    >>> 2 in b
    True
    >>> 5 in b
    False

En el ejemplo anterior, si ``b`` es una :ref:`lista <python_list>`, este prueba que ``2`` y ``5`` sean
elementos de la :ref:`lista <python_list>` ``b``.


.. _python_opers_notin:

Operador not in
................

El operador ``not in``, el contrario de operador :ref:`in <python_opers_in>`, devuelve
``True`` cuando un elemento no está en una secuencia.

.. code-block:: pycon

    >>> b = [1, 2, 3]
    >>> 4 not in b
    True
    >>> 1 not in b
    False

En el ejemplo anterior, si ``b`` es una :ref:`lista <python_list>`, este prueba que ``4`` y ``1`` sean
elementos de la :ref:`lista <python_list>` ``b``.


Ejemplos
........

A continuación, se presentan algunos ejemplos de su uso:

**Definir variables usadas en los siguientes ejemplos**:

.. literalinclude:: ../../recursos/leccion4/operadores_pertenencia.py
    :language: python
    :linenos:
    :lines: 3-11


**Operador de pertenencia in**:

.. literalinclude:: ../../recursos/leccion4/operadores_pertenencia.py
    :language: python
    :linenos:
    :lines: 15-32


**Operador de pertenencia not in**:

.. literalinclude:: ../../recursos/leccion4/operadores_pertenencia.py
    :language: python
    :linenos:
    :lines: 35-52


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion4/operadores_pertenencia.py>`.


.. tip::
    Para ejecutar el código :file:`operadores_pertenencia.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    .. code-block:: console

        $ python operadores_pertenencia.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion4>`
    del entrenamiento para ampliar su conocimiento en esta temática.
