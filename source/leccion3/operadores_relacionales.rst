.. -*- coding: utf-8 -*-


.. _python_operadores_relacionales:

Operadores relacionales
-----------------------

Los valores booleanos son además el resultado de expresiones que
utilizan operadores relacionales (comparaciones entre valores):

+----------------+----------------------------+------------------+
| **Operador**   | **Descripción**            | **Ejemplo**      |
+----------------+----------------------------+------------------+
|                |                            | ::               |
|                |                            |                  |
| ==             | ¿son iguales a y b?        |     >>> 5 == 3   |
|                |                            |     False        |
+----------------+----------------------------+------------------+
|                |                            | ::               |
|                |                            |                  |
| !=             | ¿son distintos a y b?      |     >>> 5 != 3   |
|                |                            |     True         |
+----------------+----------------------------+------------------+
|                |                            | ::               |
|                |                            |                  |
| <              | ¿es a menor que b?         |     >>> 5 < 3    |
|                |                            |     False        |
+----------------+----------------------------+------------------+
|                |                            | ::               |
|                |                            |                  |
| >              | ¿es a mayor que b?         |     >>> 5 > 3    |
|                |                            |     True         |
+----------------+----------------------------+------------------+
|                |                            | ::               |
|                |                            |                  |
| <=             | ¿es a menor o igual que b? |     >>> 5 <= 5   |
|                |                            |     True         |
+----------------+----------------------------+------------------+
|                |                            | ::               |
|                |                            |                  |
| >=             | ¿es a mayor o igual que b? |     >>> 5 >= 3   |
|                |                            |     True         |
+----------------+----------------------------+------------------+


Ejemplo de operadores relacionales
..................................

A continuación, se presentan algunos ejemplos de su uso:

**Ejemplo de definir variables numéricas**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 4-6


**Ejemplo de operador relacional Igual**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 9-16


**Ejemplo de operador relacional Diferente**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 19-23


**Ejemplo de operador relacional Menor que**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 26-27


**Ejemplo de operador relacional Mayor que**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 30-31


**Ejemplo de operador relacional Menor o igual que**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 34-35


**Ejemplo de operador relacional Mayor o igual que**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 38-39


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

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
