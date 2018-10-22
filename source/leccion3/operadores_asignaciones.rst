.. -*- coding: utf-8 -*-


.. _python_operadores_asignaciones:

Operadores de asignaciones
--------------------------

Los operadores de asignación se utilizan para básicamente asignar un
valor a una variable, así como cuando utilizamos el "=".

A continuación, se descriptiven de los operadores de asignación:

+--------------+-----------------------------------+---------------------+-----------+
| **Operador** | **Descripción**                   | **Ejemplo**         | **Notas** |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   | ::                  |           |
|              |                                   |                     |           |
| ``=``        | asigna valor a una variable       |     >>> a = 5       | [1]       |
|              |                                   |     >>> b = a       |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   |  ::                 |           |
|              |                                   |                     |           |
| ``+=``       | suma el valor a la variable       |     >>> a = 5; a    | [2]       |
|              |                                   |      5              |           |
|              |                                   |      >>> a += 10; a |           |
|              |                                   |      15             |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   |  ::                 |           |
|              |                                   |                     |           |
| ``-=``       | resta el valor a la variable      |     >>> a = 5; a    | [3]       |
|              |                                   |      5              |           |
|              |                                   |      >>> a -= 10; a |           |
|              |                                   |      -5             |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   | ::                  |           |
|              |                                   |                     |           |
| ``*=``       | multiplica el valor a la variable |     >>> a = 5; a    | [4]       |
|              |                                   |     5               |           |
|              |                                   |     >>> a *= 10; a  |           |
|              |                                   |     50              |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   | ::                  |           |
|              |                                   |                     |           |
| ``/=``       | divide el valor a la variable     |     >>> a = 5; a    | [5]       |
|              |                                   |     5               |           |
|              |                                   |     >>> a /= 10; a  |           |
|              |                                   |     0               |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   | ::                  |           |
|              |                                   |                     |           |
| ``**=``      | .. todo::                         |     >>> a = 5; a    | [6]       |
|              |    Explicar esta descripción      |     5               |           |
|              |                                   |     >>> a **= 10; a |           |
|              |                                   |     9765625         |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   | ::                  |           |
|              |                                   |                     |           |
| ``//=``      | .. todo::                         |     >>> a = 5; a    | [7]       |
|              |    Explicar esta descripción      |     5               |           |
|              |                                   |     >>> a //= 10; a |           |
|              |                                   |     0               |           |
+--------------+-----------------------------------+---------------------+-----------+


.. note::

	Nota [1]
		El operador *igual a*, (``=``) , es el más simple de todos y asigna a la variable del
		lado izquierdo cualquier variable o resultado del lado derecho.

	Nota [2]
		El operador ``+=`` , suma a la variable del lado izquierdo el valor del lado derecho.
		ej.  si la variable "``a``" es igual a ``5`` y ``a+=10``, entonces la variable "``a``" sera igual a ``15``.

	Nota [3]
		El operador ``-=`` , resta a la variable del lado izquierdo el valor del lado derecho.
		ej.  si la variable "``a``" es igual a ``5`` y ``a-=10``, entonces la variable "``a``" sera igual a ``-5``.

	Nota [4]
		El operador ``*=``, multiplica  a la variable del lado izquierdo el valor del lado derecho.
		ej.  si la variable "``a``" es igual a ``5`` y ``a*=10``, entonces la variable "``a``" sera igual a ``50``.

	Nota [5]
		El operador ``/=``, 

		.. todo::  Escribir esta nota.

	Nota [6]
		El operador ``**=``, 

		.. todo::  Escribir esta nota.

	Nota [7]
		El operador ``//=``, 

		.. todo::  Escribir esta nota.


Ejemplo de operadores de asignaciones
.....................................

A continuación, se presentan algunos ejemplos de su uso:

.. literalinclude:: ../../recursos/leccion3/operadores_asignaciones.py
    :linenos:
    :language: python
    :lines: 7-32
