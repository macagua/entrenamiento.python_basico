.. -*- coding: utf-8 -*-


.. _python_opers_asignaciones:

Operadores de asignaciones
--------------------------

Los operadores de asignación se utilizan para 


Existe en Python todo un grupo de operadores los cuales le permiten básicamente asignar 
un valor a una variable, usando el operador "``=``". Con estos operadores pueden aplicar 
la técnica denominada :ref:`asignación aumentada <python_asignacion_aumentada>`.


.. _python_opers_asig_igual:

Operador =
..........

El operador *igual a*, (``=``), es el más simple de todos y asigna a la variable del 
lado izquierdo cualquier variable o resultado del lado derecho.


.. _python_opers_asig_suma:

Operador +=
...........

El operador ``+=`` suma a la variable del lado izquierdo el valor del lado derecho.

::

    >>> r = 5; r += 10; r
    15

En el ejemplo anterior si la variable "``r``" es igual a ``5`` y ``r += 10``, entonces 
la variable "``r``" sera igual a ``15``. Su equivalente seria el siguiente:

::

    >>> r = 5; r = r + 10; r
    15


.. _python_opers_asig_resta:

Operador -=
...........

El operador ``-=`` resta a la variable del lado izquierdo el valor del lado derecho.

::

    >>> r = 5; r -= 10; r
    -5

En el ejemplo anterior si la variable "``r``" es igual a ``5`` y ``r -= 10``, entonces 
la variable "``r``" sera igual a ``-5``. Su equivalente seria el siguiente:

::

    >>> r = 5; r = r - 10; r
    -5


.. _python_opers_asig_multi:

Operador \*=
............

El operador ``*=`` multiplica a la variable del lado izquierdo el valor del lado derecho.

::

    >>> r = 5; r *= 10; r
    50

En el ejemplo anterior si la variable "``r``" es igual a ``5`` y ``r *= 10``, entonces 
la variable "``r``" sera igual a ``50``. Su equivalente seria el siguiente:

::

    >>> r = 5; r = r * 10; r
    50


.. _python_opers_asig_div:

Operador /=
...........

El operador ``/=`` divide a la variable del lado izquierdo el valor del lado derecho.

::

    >>> r = 5; r /= 10; r
    0

En el ejemplo anterior si la variable "``r``" es igual a ``5`` y ``r /= 10``, entonces 
la variable "``r``" sera igual a ``0``. Su equivalente seria el siguiente:

::

    >>> r = 5; r = r / 10; r
    0


.. _python_opers_asig_expo:

Operador \**=
.............

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


.. _python_opers_asig_divent:

Operador //=
............

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


.. _python_opers_asig_mod:

Operador %=
...........

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

Es frecuente que una variable tenga que ser definida de nuevo en función de sí misma. 
Normalmente usted escribir la siguiente sintaxis:

::

    >>> contador = contador + 1

El código anterior, se puede abreviar a su equivalente, usando la asignación aumentada, 
de la siguiente manera:

::

    >>> contador += 1

El código anterior, no sólo es más corto de escribir, sino también más eficiente en 
tiempo de ejecución.


.. _python_opers_asig_ejs:

Ejemplos
........

A continuación, se presentan algunos ejemplos de su uso:

.. literalinclude:: ../../recursos/leccion3/operadores_asignaciones.py
    :language: python
    :lines: 3-28

----

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/operadores_asignaciones.py>`.


.. tip::
    Para ejecutar el código :file:`operadores_asignaciones.py`, abra una consola de 
    comando, acceda al directorio donde se encuentra el mismo, y ejecute el siguiente 
    comando: 

    ::

        python operadores_asignaciones.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html
