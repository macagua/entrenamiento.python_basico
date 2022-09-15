.. -*- coding: utf-8 -*-


.. _python_opers:

Operadores
----------

A continuación, se ofrecen una referencia corta de los diversos *operadores* en Python:


Operadores de asignaciones
..........................

Una corta referencia de los *operadores de asignación* se ofrece a continuación:

+--------------+-----------------------------------+---------------------+
| **Operador** | **Descripción**                   | **Ejemplo**         |
+--------------+-----------------------------------+---------------------+
|              |                                   | ::                  |
|              |                                   |                     |
| ``=``        | asigna valor a una variable       |     >>> r = 5       |
|              |                                   |     >>> r1 = r      |
+--------------+-----------------------------------+---------------------+
|              |                                   |  ::                 |
|              |                                   |                     |
| ``+=``       | suma el valor a la variable       |     >>> r = 5       |
|              |                                   |     >>> r += 10; r  |
|              |                                   |     15              |
+--------------+-----------------------------------+---------------------+
|              |                                   |  ::                 |
|              |                                   |                     |
| ``-=``       | resta el valor a la variable      |     >>> r = 5       |
|              |                                   |     >>> r -= 10; r  |
|              |                                   |     -5              |
+--------------+-----------------------------------+---------------------+
|              |                                   | ::                  |
|              |                                   |                     |
| ``*=``       | multiplica el valor a la variable |     >>> r = 5       |
|              |                                   |     >>> r *= 10; r  |
|              |                                   |     50              |
+--------------+-----------------------------------+---------------------+
|              |                                   | ::                  |
|              |                                   |                     |
| ``/=``       | divide el valor a la variable     |     >>> r = 5       |
|              |                                   |     >>> r /= 10; r  |
|              |                                   |     0               |
+--------------+-----------------------------------+---------------------+
|              |                                   | ::                  |
|              |                                   |                     |
| ``**=``      | calcula el exponente del valor    |     >>> r = 5       |
|              | de la variable                    |     >>> r **= 10; r |
|              |                                   |     9765625         |
+--------------+-----------------------------------+---------------------+
|              |                                   | ::                  |
|              |                                   |                     |
| ``//=``      | calcula la división entera del    |     >>> r = 5       |
|              | valor de la variable              |     >>> r //= 10; r |
|              |                                   |     0               |
+--------------+-----------------------------------+---------------------+
|              |                                   | ::                  |
|              |                                   |                     |
| ``%=``       | devuelve el resto de la división  |     >>> r = 5       |
|              | del valor de la variable          |     >>> r %= 10; r  |
|              |                                   |     5               |
+--------------+-----------------------------------+---------------------+

.. seealso::
    Usted puede consultar para más información la explicación de cada uno de los
    :ref:`operadores de asignaciones <python_opers_asignaciones>`.


Operadores aritméticos
......................

Una corta referencia de los *operadores aritméticos* se ofrece a continuación:

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


.. seealso::
    Usted puede consultar para más información la explicación de cada uno de los
    :ref:`operadores aritméticos <python_opers_aritmeticos>`.


Operadores relacionales
.......................

Una corta referencia de los *operadores relacionales* se ofrece a continuación:

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

.. seealso::
    Usted puede consultar para más información la explicación de cada uno de los
    :ref:`operadores relacionales <python_opers_relacionales>`.


Operadores lógicos
..................

Una corta referencia de los *operadores lógicos* se ofrece a continuación:

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
| not            | No al valor        |     >>> not True       |
|                |                    |     False              |
+----------------+--------------------+------------------------+

.. seealso::
    Usted puede consultar para más información la explicación de cada uno de los
    :ref:`operadores lógicos <python_opers_logicos>`.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
