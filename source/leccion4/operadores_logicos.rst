.. -*- coding: utf-8 -*-


.. _python_operadores_logicos:

Operadores de lógicos
---------------------

Estos son los distintos tipos de operadores con los que puede trabajar
con valores booleanos, los llamados operadores lógicos o condicionales:

+----------------+--------------------+------------------------+
| **Operador**   | **Descripción**    | **Ejemplo**            |
+----------------+--------------------+------------------------+
|                |                    | ::                     |
|                |                    |                        |
| and            | ¿se cumple a y b?  |     >>> True and False |
|                |                    |     False              |
+----------------+--------------------+------------------------+
|                |                    | ::                     |
|                |                    |                        |
| or             | ¿se cumple a o b?  |     >>> True or False  |
|                |                    |     True               |
+----------------+--------------------+------------------------+
|                |                    | ::                     |
|                |                    |                        |
| not            | No a               |     >>> not True       |
|                |                    |     False              |
+----------------+--------------------+------------------------+


Ejemplo de operadores de lógicos
................................

A continuación, se presentan algunos ejemplos de su uso:

**Definir variables usadas en los siguientes ejemplos**:

.. literalinclude:: ../../recursos/leccion4/operadores_logicos.py
    :linenos:
    :language: python
    :lines: 7


**Ejemplo de operador lógico and**:

.. literalinclude:: ../../recursos/leccion4/operadores_logicos.py
    :linenos:
    :language: python
    :lines: 16-20


**Ejemplo de operador lógico or**:

.. literalinclude:: ../../recursos/leccion4/operadores_logicos.py
    :linenos:
    :language: python
    :lines: 25-31


**Ejemplo de operador lógico not**:

.. literalinclude:: ../../recursos/leccion4/operadores_logicos.py
    :linenos:
    :language: python
    :lines: 36-40


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion4/operadores_logicos.py>`.


.. tip::
    Para ejecutar el código :file:`operadores_logicos.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando: ::

        python operadores_logicos.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion4>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
