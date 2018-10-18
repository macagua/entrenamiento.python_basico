.. -*- coding: utf-8 -*-


.. _python_operadores_aritmeticos:

Operadores aritméticos
----------------------

Los valores numéricos son además el resultado de  una serie
de operadores aritméticos y matemáticos:

+----------------+-------------------+---------------------------+
| **Operador**   | **Descripción**   | **Ejemplo**               |
+----------------+-------------------+---------------------------+
| \+             | Suma              | r = 3 + 2 # r es 5        |
+----------------+-------------------+---------------------------+
| \-             | Resta             | r = 4 – 7 # r es -3       |
+----------------+-------------------+---------------------------+
| \-             | Negación          | r = -7 # r es -7          |
+----------------+-------------------+---------------------------+
| \*             | Multiplicación    | r = 2 \* 6 # r es 12      |
+----------------+-------------------+---------------------------+
| \*\*           | Exponente         | r = 2 \*\* 6 # r es 64    |
+----------------+-------------------+---------------------------+
| /              | División          | r = 3.5 / 2 # r es 1.75   |
+----------------+-------------------+---------------------------+
| //             | División entera   | r = 3.5 // 2 # r es 1.0   |
+----------------+-------------------+---------------------------+
| %              | Módulo            | r = 7 % 2 # r es 1        |
+----------------+-------------------+---------------------------+

Puede que tengáis dudas sobre cómo funciona el operador de módulo, y
cuál es la diferencia entre división y división entera.

El operador de módulo no hace otra cosa que devolvernos el resto de la
división entre los dos operandos. En el ejemplo, 7 / 2 sería 3, con 1 de
resto, luego el módulo es 1.

La diferencia entre división y división entera no es otra que la que
indica su nombre. En la división el resultado que se devuelve es un
número real, mientras que en la división entera el resultado que se
devuelve es solo la parte entera.

No obstante hay que tener en cuenta que si utilizamos dos operandos
enteros, Python determinará que queremos que la variable resultado
también sea un entero, por lo que el resultado de, por ejemplo, 3 / 2 y
3 // 2 sería el mismo: 1.

Si quisiéramos obtener los decimales necesitaríamos que al menos uno de
los operandos fuera un número real, bien indicando los decimales

::

    r = 3.0 / 2

o bien utilizando la función ``float`` (no es necesario que sepas lo que
significa el término función, ni que recuerdes esta forma, lo veremos un
poco más adelante):

::

    r = float(3) / 2

Esto es así porque cuando se mezclan tipos de números, Python convierte
todos los operandos al tipo más complejo de entre los tipos de los
operandos.

Ejemplo de operadores numéricos
...............................

A continuación, se presentan algunos ejemplos de su uso:

**Ejemplo de definir variables numéricas**

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 7-10


**Ejemplo de operador aritmético Suma**, Añade valores a cada lado del operador.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 13-13


**Ejemplo de operador aritmético Resta**, Resta el operando de la derecha del 
operador del lado izquierdo.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 16-16


**Ejemplo de operador aritmético Multiplicación**, Multiplica los valores de 
ambos lados del operador.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 19-19


**Ejemplo de operador aritmético Exponente, Realiza el cálculo exponencial** 
(potencia) de los operadores.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 22-22


**Ejemplo de operador aritmético División**.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 25-25


**Ejemplo de operador aritmético División entera**.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 28-28


**Ejemplo de operador aritmético Cociente de una división**, la división de 
operandos que el resultado es el cociente en el cual se eliminan los dígitos 
después del punto decimal.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 32-32


**Ejemplo de operador aritmético Modulo**, el cual divide el operando de la 
izquierda por el operador del lado derecho y devuelve el resto.

.. literalinclude:: ../../recursos/leccion3/operadores_numericos.py
    :linenos:
    :language: python
    :lines: 36-36

