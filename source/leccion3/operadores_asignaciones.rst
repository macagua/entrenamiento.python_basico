.. -*- coding: utf-8 -*-


.. _python_operadores_asignaciones:

Operadores de asignaciones
--------------------------

Los operadores de asignación se utilizan para 


Existe en Python todo un grupo de operadores los cuales le permiten básicamente asignar 
un valor a una variable, usando el operador "``=``". Con estos operadores pueden aplicar 
la técnica denominada :ref:`asignación aumentada <python_asignacion_aumentada>`.

A continuación, se describen de los operadores de asignación:

+--------------+-----------------------------------+---------------------+-----------+
| **Operador** | **Descripción**                   | **Ejemplo**         | **Notas** |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   | ::                  |           |
|              |                                   |                     |           |
| ``=``        | asigna valor a una variable       |     >>> r = 5       | [1]       |
|              |                                   |     >>> r1 = r      |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   |  ::                 |           |
|              |                                   |                     |           |
| ``+=``       | suma el valor a la variable       |     >>> r = 5       | [2]       |
|              |                                   |     >>> r += 10; r  |           |
|              |                                   |     15              |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   |  ::                 |           |
|              |                                   |                     |           |
| ``-=``       | resta el valor a la variable      |     >>> r = 5       | [3]       |
|              |                                   |     >>> r -= 10; r  |           |
|              |                                   |     -5              |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   | ::                  |           |
|              |                                   |                     |           |
| ``*=``       | multiplica el valor a la variable |     >>> r = 5       | [4]       |
|              |                                   |     >>> r *= 10; r  |           |
|              |                                   |     50              |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   | ::                  |           |
|              |                                   |                     |           |
| ``/=``       | divide el valor a la variable     |     >>> r = 5       | [5]       |
|              |                                   |     >>> r /= 10; r  |           |
|              |                                   |     0               |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   | ::                  |           |
|              |                                   |                     |           |
| ``**=``      | calcula el exponente del valor    |     >>> r = 5       | [6]       |
|              | de la variable                    |     >>> r **= 10; r |           |
|              |                                   |     9765625         |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   | ::                  |           |
|              |                                   |                     |           |
| ``//=``      | calcula la división entera del    |     >>> r = 5       | [7]       |
|              | valor de la variable              |     >>> r //= 10; r |           |
|              |                                   |     0               |           |
+--------------+-----------------------------------+---------------------+-----------+
|              |                                   | ::                  |           |
|              |                                   |                     |           |
| ``%=``       | devuelve el resto de la división  |     >>> r = 5       | [8]       |
|              | del valor de la variable          |     >>> r %= 10; r  |           |
|              |                                   |     5               |           |
+--------------+-----------------------------------+---------------------+-----------+


**Operador Igual** [1]

El operador *igual a*, (``=``), es el más simple de todos y asigna a la variable 
del lado izquierdo cualquier variable o resultado del lado derecho.


**Operador Suma** [2]

El operador ``+=`` suma a la variable del lado izquierdo el valor del lado derecho.

	::

		>>> r = 5; r += 10; r
		15

En el ejemplo anterior si la variable "``r``" es igual a ``5`` y ``r += 10``, entonces 
la variable "``r``" sera igual a ``15``. Su equivalente seria el siguiente:

	::

		>>> r = 5; r = r + 10; r
		15


**Operador Resta** [3]

El operador ``-=`` resta a la variable del lado izquierdo el valor del lado derecho.

	::

		>>> r = 5; r -= 10; r
		-5

En el ejemplo anterior si la variable "``r``" es igual a ``5`` y ``r -= 10``, entonces 
la variable "``r``" sera igual a ``-5``. Su equivalente seria el siguiente:

	::

		>>> r = 5; r = r - 10; r
		-5


**Operador Multiplicación** [4]

El operador ``*=`` multiplica a la variable del lado izquierdo el valor del lado derecho.

	::

		>>> r = 5; r *= 10; r
		50

En el ejemplo anterior si la variable "``r``" es igual a ``5`` y ``r *= 10``, entonces 
la variable "``r``" sera igual a ``50``. Su equivalente seria el siguiente:

	::

		>>> r = 5; r = r * 10; r
		50


**Operador División** [5]

El operador ``/=`` divide a la variable del lado izquierdo el valor del lado derecho.

	::

		>>> r = 5; r /= 10; r
		0

En el ejemplo anterior si la variable "``r``" es igual a ``5`` y ``r /= 10``, entonces 
la variable "``r``" sera igual a ``0``. Su equivalente seria el siguiente:

	::

		>>> r = 5; r = r / 10; r
		0


**Operador Exponente** [6]

El operador ``**=`` calcula el exponente a la variable del lado izquierdo el valor del 
lado derecho.

	::

		>>> r = 5; r **= 10; r
		9765625

En el ejemplo anterior si la variable "``r``" es igual a ``5`` y ``r **= 10``, entonces 
la variable "``r``" sera igual a ``9765625``. Su equivalente seria el siguiente:

	::

		>>> r = 5; r = r ** 10; r
		9765625


**Operador División entera** [7]

El operador ``//=`` calcula la división entera a la variable del lado izquierdo el valor 
del lado derecho.

	::

		>>> r = 5; r //= 10; r
		0

En el ejemplo anterior si la variable "``r``" es igual a ``5`` y ``r //= 10``, entonces 
la variable "``r``" sera igual a ``0``. Su equivalente seria el siguiente:

	::

		>>> r = 5; r = r // 10; r
		0

**Operador Módulo**  [8]

El operador ``%=`` devuelve el resto de la división a la variable del lado izquierdo el 
valor del lado derecho.

	::

		>>> r = 5; r %= 10; r
		5

En el ejemplo anterior si la variable "``r``" es igual a ``5`` y ``r %= 10``, entonces 
la variable "``r``" sera igual a ``5``. Su equivalente seria el siguiente:

	::

		>>> r = 5; r = r % 10; r
		5


.. _python_asignacion_aumentada:

Asignación aumentada
....................

Es frecuente que una variable tenga que ser redefinida en función de sí misma. En vez de escribir:

::

	>>> contador = contador + 1

Se puede abreviar a su equivalente:

::

	>>> contador += 1

Que no sólo es más corto de escribir, sino también más eficiente.


.. _python_operadores_asignaciones_ejemplo:

Ejemplo de operadores de asignaciones
.....................................

A continuación, se presentan algunos ejemplos de su uso:

.. literalinclude:: ../../recursos/leccion3/operadores_asignaciones.py
    :linenos:
    :language: python
    :lines: 7-32


.. important::
	Usted puede descargar el código usado en esta sección haciendo clic 
	:download:`aquí <../../recursos/leccion3/operadores_asignaciones.py>`.


.. tip::
	Para ejecutar el código :file:`operadores_asignaciones.py`, abra una 
	consola de comando, acceda al directorio donde se encuentra el mismo, 
	y ejecute el siguiente comando: ::

		python2 operadores_asignaciones.py
