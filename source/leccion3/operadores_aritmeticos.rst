.. -*- coding: utf-8 -*-


.. _python_opers_aritmeticos:

Operadores aritméticos
----------------------

Los valores numéricos son además el resultado de una serie de operadores aritméticos
y matemáticos:


.. _python_opers_arit_suma:

Operador Suma
.............

El operador ``+`` suma los valores de tipo de datos numéricos.

.. code-block:: pycon

    >>> 3 + 2
    5


.. _python_opers_arit_resta:

Operador Resta
..............

El operador ``-`` resta los valores de tipo de datos numéricos.

.. code-block:: pycon

    >>> 4 - 7
    -3


.. _python_opers_arit_nega:

Operador Negación
.................

El operador ``-`` asigna un valor negativo a un tipo de datos numéricos.

.. code-block:: pycon

    >>> -7
    -7


.. _python_opers_arit_multi:

Operador Multiplicación
.......................

El operador ``*`` multiplica los valores de tipo de datos numéricos.

.. code-block:: pycon

    >>> 2 * 6
    12


.. _python_opers_arit_expo:

Operador Exponente
..................

El operador ``**`` calcula el exponente entre valores de tipo de datos numéricos.

.. code-block:: pycon

    >>> 2**6
    64


.. _python_opers_arit_div:

Operador división
.................

El operador *división* el resultado que se devuelve es un número real.

.. code-block:: pycon

    >>> 3.5 / 2
    1.75


.. _python_opers_arit_divent:

Operador división entera
........................

El operador *división entera* el resultado que se devuelve es solo la parte entera.

.. code-block:: pycon

    >>> 3.5 // 22
    1.0

No obstante hay que tener en cuenta que si utilizamos dos operandos enteros, Python
determinará que quiere que la variable resultado también sea un entero, por lo que
el resultado de, por ejemplo, ``3 / 2`` y ``3 // 2`` sería el mismo: ``1``.

Si quisiéramos obtener los decimales necesitaríamos que al menos uno de los operandos
fuera un número real, bien indicando los decimales:

.. code-block:: pycon

    r = 3.0 / 2

O bien utilizando la función :ref:`float() <python_fun_float>` para convertir a
entero coma flotante o real:

.. code-block:: pycon

    r = float(3) / 2

Esto es así porque cuando se mezclan tipos de :ref:`números <python_int>`, Python convierte todos los
operandos al tipo más complejo de entre los tipos de los operandos.


.. _python_opers_arit_mod:

Operador Módulo
...............

El operador *módulo* no hace otra cosa que devolver el resto de la división entre
los dos operandos. En el ejemplo, ``7 / 2`` sería ``3``, con ``1`` de resto, luego
el *módulo* es ``1``.

.. code-block:: pycon

    >>> 7 % 2
    1


.. _python_opers_aritmeticos_precedencia:

Orden de precedencia
....................

El orden de precedencia de ejecución de los operadores aritméticos es:

#. Exponente: ``**``

#. Negación: ``-``

#. Multiplicación, División, División entera, Módulo: ``*``, ``/``, ``//``, ``%``

#. Suma, Resta: ``+``, ``-``

Eso quiere decir que se debe usar así:

.. code-block:: pycon

    >>> 2**1 / 12
    0.16666666666666666
    >>>

Más igualmente usted puede omitir este orden de precedencia de ejecución de los
operadores aritméticos usando paréntesis ``()``  anidados entre cada nivel calculo,
por ejemplo:

.. code-block:: pycon

    >>> 2 ** (1 / 12)
    1.0594630943592953
    >>>


.. _python_opers_arit_ejs:

Ejemplos
........

A continuación, se presentan algunos ejemplos de su uso:

**Definir variables numéricas**

.. literalinclude:: ../../recursos/leccion3/operadores_aritmeticos.py
    :language: python
    :linenos:
    :lines: 3


**Operador aritmético Suma**, Añade valores a cada lado del operador.

.. literalinclude:: ../../recursos/leccion3/operadores_aritmeticos.py
    :language: python
    :linenos:
    :lines: 6


**Operador aritmético Resta**, Resta el operando de la derecha del operador
del lado izquierdo.

.. literalinclude:: ../../recursos/leccion3/operadores_aritmeticos.py
    :language: python
    :linenos:
    :lines: 9


**Operador aritmético Multiplicación**, Multiplica los valores de
ambos lados del operador.

.. literalinclude:: ../../recursos/leccion3/operadores_aritmeticos.py
    :language: python
    :linenos:
    :lines: 12


**Operador aritmético Exponente, Realiza el cálculo exponencial**
(potencia) de los operadores.

.. literalinclude:: ../../recursos/leccion3/operadores_aritmeticos.py
    :language: python
    :linenos:
    :lines: 15


**Operador aritmético División**.

.. literalinclude:: ../../recursos/leccion3/operadores_aritmeticos.py
    :language: python
    :linenos:
    :lines: 18


**Operador aritmético División entera**.

.. literalinclude:: ../../recursos/leccion3/operadores_aritmeticos.py
    :language: python
    :linenos:
    :lines: 21


**Operador aritmético Cociente de una división**, la división de operandos
que el resultado es el cociente en el cual se eliminan los dígitos después del punto
decimal.

.. literalinclude:: ../../recursos/leccion3/operadores_aritmeticos.py
    :language: python
    :linenos:
    :lines: 25


**Operador aritmético Módulo**, el cual divide el operando de la izquierda
por el operador del lado derecho y devuelve el resto.

.. literalinclude:: ../../recursos/leccion3/operadores_aritmeticos.py
    :language: python
    :linenos:
    :lines: 29

----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion3/operadores_aritmeticos.py>`.


.. tip::
    Para ejecutar el código :file:`operadores_aritmeticos.py`, abra una
    consola de comando, acceda al directorio donde se encuentra el mismo,
    y ejecute el siguiente comando:

    .. code-block:: console

        $ python operadores_aritmeticos.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
