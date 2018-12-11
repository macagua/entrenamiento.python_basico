.. -*- coding: utf-8 -*-


.. _python_opers_logicos:

Operadores lógicos
------------------

Estos son los distintos tipos de operadores con los que puede trabajar con valores 
booleanos, los llamados operadores lógicos o condicionales:


.. _python_opers_logi_and:

Operador and
............

El operador ``and`` evalúa si el valor del lado izquierdo y el lado derecho *se cumple*.

::

    >>> True and False
    False


.. _python_opers_logi_or:

Operador or
............

El operador ``or`` evalúa si el valor del lado izquierdo o el lado derecho *se cumple*.

::

    >>> True or False
    True


.. _python_opers_logi_not:

Operador not
............

El operador ``not`` devuelve el valor *opuesto* la valor booleano.

::

    >>> not True
    False

Si la expresión es ``True`` el valor devuelto es ``False``, de lo contrario si la 
expresión es ``False`` el valor devuelto es ``True``.

::

    >>> not False
    True


.. _python_opers_logi_ejs:

Ejemplos
........

A continuación, se presentan algunos ejemplos de su uso:

**Definir variables usadas en los siguientes ejemplos**:

.. literalinclude:: ../../recursos/leccion4/operadores_logicos.py
    :linenos:
    :language: python
    :lines: 5


**Ejemplo de operador lógico and**:

.. literalinclude:: ../../recursos/leccion4/operadores_logicos.py
    :linenos:
    :language: python
    :lines: 14-18


**Ejemplo de operador lógico or**:

.. literalinclude:: ../../recursos/leccion4/operadores_logicos.py
    :linenos:
    :language: python
    :lines: 23-29


**Ejemplo de operador lógico not**:

.. literalinclude:: ../../recursos/leccion4/operadores_logicos.py
    :linenos:
    :language: python
    :lines: 34-38


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion4/operadores_logicos.py>`.


.. tip::
    Para ejecutar el código :file:`operadores_logicos.py`, abra una consola de comando, 
    acceda al directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    ::

        python operadores_logicos.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion4>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
