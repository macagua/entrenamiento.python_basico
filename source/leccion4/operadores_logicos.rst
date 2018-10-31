.. -*- coding: utf-8 -*-


.. _python_operadores_logicos:

Operadores de lógicos
---------------------

Estos son los distintos tipos de operadores con los que podemos trabajar
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
    :lines: 16-19


**Ejemplo de operador lógico or**:

.. literalinclude:: ../../recursos/leccion4/operadores_logicos.py
    :linenos:
    :language: python
    :lines: 24-27


**Ejemplo de operador lógico not**:

.. literalinclude:: ../../recursos/leccion4/operadores_logicos.py
    :linenos:
    :language: python
    :lines: 32-35


.. seealso:: 

    .. figure:: https://img.youtube.com/vi/ZrxcqbFYjiw/0.jpg
        :align: center
        :width: 60%

        Vídeo `Tutorial Python 5 - Booleanos, operadores lógicos y cadenas`_, 
        cortesía de `CodigoFacilito.com`_.

    .. todo:: Cambiar la URL de imagen de previsualización del video, de forma local.

.. _`Tutorial Python 5 - Booleanos, operadores lógicos y cadenas`: https://www.youtube.com/watch?v=ZrxcqbFYjiw
.. _`CodigoFacilito.com`: https://www.codigofacilito.com/
