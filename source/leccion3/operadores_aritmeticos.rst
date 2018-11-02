.. -*- coding: utf-8 -*-


.. _python_operadores_aritmeticos:

Operadores aritméticos
----------------------

Los valores numéricos son además el resultado de una serie de operadores 
aritméticos y matemáticos:

+----------------+-------------------+---------------------------+
| **Operador**   | **Descripción**   | **Ejemplo**               |
+----------------+-------------------+---------------------------+
|                |                   | ::                        |
|                |                   |                           |
| \+             | Suma              |     >>> 3 + 2             |
|                |                   |     5                     |
+----------------+-------------------+---------------------------+
|                |                   | ::                        |
|                |                   |                           |
| \-             | Resta             |     >>> 4 - 7             |
|                |                   |     -3                    |
+----------------+-------------------+---------------------------+
|                |                   | ::                        |
|                |                   |                           |
| \-             | Negación          |     >>> -7                |
|                |                   |     -7                    |
+----------------+-------------------+---------------------------+
|                |                   | ::                        |
|                |                   |                           |
| \*             | Multiplicación    |     >>> 2 * 6             |
|                |                   |     12                    |
+----------------+-------------------+---------------------------+
|                |                   | ::                        |
|                |                   |                           |
| \*\*           | Exponente         |     >>> 2 ** 6            |
|                |                   |     64                    |
+----------------+-------------------+---------------------------+
|                |                   | ::                        |
|                |                   |                           |
| /              | División          |     >>> 3.5 / 2           |
|                |                   |     1.75                  |
+----------------+-------------------+---------------------------+
|                |                   | ::                        |
|                |                   |                           |
| //             | División entera   |     >>> 3.5 // 2          |
|                |                   |     1.0                   |
+----------------+-------------------+---------------------------+
|                |                   | ::                        |
|                |                   |                           |
| %              | Módulo            |     >>> 7 % 2             |
|                |                   |     1                     |
+----------------+-------------------+---------------------------+


**Operador división**

El operador *división* el resultado que se devuelve es un número real. 


**Operador división entera**

El operador *división entera* el resultado que se devuelve es solo la 
parte entera.

No obstante hay que tener en cuenta que si utilizamos dos operandos
enteros, Python determinará que quiere que la variable resultado
también sea un entero, por lo que el resultado de, por ejemplo, 
``3 / 2`` y ``3 // 2`` sería el mismo: ``1``.

Si quisiéramos obtener los decimales necesitaríamos que al menos uno de
los operandos fuera un número real, bien indicando los decimales:

::

    r = 3.0 / 2

O bien utilizando la función :ref:`float <python_funcion_float>` para 
convertir a entero coma flotante o real:

::

    r = float(3) / 2

Esto es así porque cuando se mezclan tipos de números, Python convierte
todos los operandos al tipo más complejo de entre los tipos de los
operandos.


**Operador módulo**

El operador *módulo* no hace otra cosa que devolvernos el resto de la
división entre los dos operandos. En el ejemplo, ``7 / 2`` sería ``3``, 
con ``1`` de resto, luego el *módulo* es ``1``.


.. _python_operadores_aritmeticos_precedencia:

Orden de precedencia
....................

El orden de precedencia de ejecución de los operadores aritméticos es:

#. Exponente: ``**``

#. Negación: ``-``

#. Multiplicación, División, División entera, Módulo: ``*``, ``/``, ``//``, ``%``

#. Suma, Resta: ``+``, ``-``

Eso quiere decir que se debe usar así:

::

    >>> 2**1/12
    0.16666666666666666
    >>> 

Más igualmente usted puede omitir este orden de precedencia de ejecución de los operadores 
aritméticos usando paréntesis ``()``  anidados entre cada nivel calculo, por ejemplo:

::

    >>> 2**(1/12)
    1.0594630943592953
    >>> 


Ejemplo de operadores numéricos
...............................

A continuación, se presentan algunos ejemplos de su uso:

**Ejemplo de definir variables numéricas**

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 7


**Ejemplo de operador aritmético Suma**, Añade valores a cada lado del operador.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 10


**Ejemplo de operador aritmético Resta**, Resta el operando de la derecha del 
operador del lado izquierdo.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 13


**Ejemplo de operador aritmético Multiplicación**, Multiplica los valores de 
ambos lados del operador.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 16


**Ejemplo de operador aritmético Exponente, Realiza el cálculo exponencial** 
(potencia) de los operadores.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 19


**Ejemplo de operador aritmético División**.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 22


**Ejemplo de operador aritmético División entera**.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 25


**Ejemplo de operador aritmético Cociente de una división**, la división de 
operandos que el resultado es el cociente en el cual se eliminan los dígitos 
después del punto decimal.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 29


**Ejemplo de operador aritmético Módulo**, el cual divide el operando de la 
izquierda por el operador del lado derecho y devuelve el resto.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 33


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/operadores_numericos.py>`.


.. tip::
    Para ejecutar el código :file:`operadores_numericos.py`, abra una 
    consola de comando, acceda al dirfectorio donde se encuentra el mismo, 
    y ejecute el siguiente comando: ::

        python2 operadores_asignaciones.py


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
