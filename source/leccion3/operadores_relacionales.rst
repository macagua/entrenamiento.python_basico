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
    :lines: 7-9


**Ejemplo de operador relacional Igual**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 12-19


**Ejemplo de operador relacional Diferente**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 22-26


**Ejemplo de operador relacional Menor que**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 29-30


**Ejemplo de operador relacional Mayor que**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 33-34


**Ejemplo de operador relacional Menor o igual que**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 37-38


**Ejemplo de operador relacional Mayor o igual que**

.. literalinclude:: ../../recursos/leccion3/operadores_relacionales.py
    :linenos:
    :language: python
    :lines: 41-42


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
