.. -*- coding: utf-8 -*-

Sentencias IF
===================================

La sentencia ``If`` se usa para tomar decisiones, este evalua
basicamente una operación logica, es decir una expresión que de
como resultado verdadero o false (``True`` o ``False``), y ejecuta
la pieza de codigo siguiente siempre y cuando el resultado sea verdadero.

Ejemplo de Sentencias IF
........................

.. literalinclude:: condicional_if.py
    :linenos:
    :language: python

Operadores de Asignaciones
--------------------------

Los operadores de asignación se utilizan para basicamente asignar un
valor a una variable, así como cuando utilizamos el “=”.

Los operadores de asignación son ``=,+=,-=,\*=,/=,\*\*=,//=``, a
continuación algunos ejemplos.

-  ``=`` , igual a, es el mas simple de todos y asigna a la variable del
   lado izquierdo cualquier variable o resultado del lado derecho.

-  ``+=`` , suma a la variable del lado izquierdo el valor del lado derecho.
    ej.  si  “a” es igual a 5 y a+=10, entonces “a” sera igual a 15

-  ``-=`` , resta a la variable del lado izquierdo el valor del lado derecho.
    ej.  si  “a” es igual a 5 y a-=10, entonces “a” sera igual a -5

-  ``\*=``, multiplica  a la variable del lado izquierdo el valor del lado derecho.
    ej.  si  “a” es igual a 5 y a\*=10, entonces “a” sera igual a 50

Espero que hasta el momento hayas podido encontrar este tutorial de
ayuda, espero tus comentarios.

Ejemplo de Operadores de Asignaciones
.....................................

.. literalinclude:: operadores_asignaciones.py
    :linenos:
    :language: python

Operadores de Comparación 
-------------------------

Los valores booleanos son además el resultado de expresiones que
utilizan operadores relacionales (comparaciones entre valores):

+----------------+------------------------------+---------------------------+
| **Operador**   | **Descripción**              | **Ejemplo**               |
+----------------+------------------------------+---------------------------+
| ==             | ¿son iguales a y b?          | r = 5 == 3 # r es False   |
+----------------+------------------------------+---------------------------+
| !=             | ¿son distintos a y b?        | r = 5 != 3 # r es True    |
+----------------+------------------------------+---------------------------+
| <              | ¿es a menor que b?           | r = 5 < 3 # r es False    |
+----------------+------------------------------+---------------------------+
| >              | ¿es a mayor que b?           | r = 5 > 3 # r es True     |
+----------------+------------------------------+---------------------------+
| <=             | ¿es a menor o igual que b?   | r = 5 <= 5 # r es True    |
+----------------+------------------------------+---------------------------+
| >=             | ¿es a mayor o igual que b?   | r = 5 >= 3 # r es True    |
+----------------+------------------------------+---------------------------+

Ejemplo Operadores de Comparación
.................................

.. literalinclude:: operadores_comparacion.py
    :linenos:
    :language: python

Operadores de Lógicos
---------------------

Estos son los distintos tipos de operadores con los que podemos trabajar
con valores booleanos, los llamados operadores lógicos o condicionales:

+----------------+---------------------+-----------------------------------+
| **Operador**   | **Descripción**     | **Ejemplo**                       |
+----------------+---------------------+-----------------------------------+
| and            | ¿se cumple a y b?   | r = True and False # r es False   |
+----------------+---------------------+-----------------------------------+
| or             | ¿se cumple a o b?   | r = True or False # r es True     |
+----------------+---------------------+-----------------------------------+
| not            | No a                | r = not True # r es False         |
+----------------+---------------------+-----------------------------------+

Ejemplo de Operadores de Lógicos
................................

.. literalinclude:: operadores_logicos.py
    :linenos:
    :language: python

Vídeo tutorial
--------------

- `Tutorial Python 10 - Sentencias condicionales`_.

Referencia
----------

- `Sentencias IF`_.

- `Condicionales if y else en Python`_.

- `Python - Tipos básicos`_.

- `Operadores basicos de Python`_.
 
.. _Sentencias IF: http://docs.python.org.ar/tutorial/2/controlflow.html#la-sentencia-if
.. _Tutorial Python 10 - Sentencias condicionales: https://www.youtube.com/watch?v=hLqKvB7tGWk
.. _Python - Tipos básicos: http://mundogeek.net/archivos/2008/01/17/python-tipos-basicos/
.. _Operadores basicos de Python: http://codigoprogramacion.com/cursos/tutoriales-python/operadores-basicos-de-python.html
.. _Condicionales if y else en Python: http://codigoprogramacion.com/cursos/tutoriales-python/condicionales-if-y-else-en-python.html
