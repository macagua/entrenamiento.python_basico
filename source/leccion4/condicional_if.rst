.. -*- coding: utf-8 -*-


.. _python_condi_if:

Condicional if
--------------

La sentencia condicional ``if`` se usa para tomar decisiones, este evaluá básicamente 
una operación lógica, es decir una expresión que de como resultado ``True`` o ``False``, 
y ejecuta la pieza de código siguiente siempre y cuando el resultado sea verdadero.

A continuación un de estructura condicional ``if``/``elif``/``else`` completo:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :language: python
    :lines: 48-58

En el ejemplo anterior usa dos funciones integradas en el interprete Python:

- La función :ref:`int() <python_fun_int>` que convierte el valor ingresado a número 
  entero.

- La función :ref:`raw_input() <python_fun_raw_input>` lee el valor ingresado por la 
  entrada estándar.

El valor es ingresado en la variable ``numero`` comprobará en el sentencia condicional 
``if``, si la comprobación devuelve ``False`` intentará con el siguiente bloque 
condicional ``elif``, si la comprobación devuelve ``False`` nuevamente intentará con el 
siguiente bloque condicional ``elif`` si de nuevo la comprobación devuelve ``False`` por 
ultimo intentará con el siguiente bloque condicional ``else`` la cual se ejecutara sin 
comprobación.


.. _python_sent_if:

Sentencia if
............

La sentencia ``if EXPRESION``, significa, **Si** se cumple la 
:ref:`expresión condicional <python_expresiones_condicional>` se ejecuta el bloque de 
sentencias seguidas.


.. _python_sent_elif:

Sentencia elif
..............

La sentencia ``elif EXPRESION``, significa, **De lo contrario Si** se cumple la 
:ref:`expresión condicional <python_expresiones_condicional>` se ejecuta el bloque de 
sentencias seguidas.


.. _python_sent_else:

Sentencia else
..............

La sentencia ``else``, significa, **De lo contrario** se cumple sin evaluar ninguna 
:ref:`expresión condicional <python_expresiones_condicional>` y ejecuta el bloque de 
sentencias seguidas.


.. _python_opers_is:

Operador is
...........

El operador ``is``, significa, que prueba identidad: ambos lados de la expresión 
condicional debe ser el mismo objecto:

::

    >>> 1 is 1.
    False
    >>> a, b = 1, 1
    >>> a is b
    True


.. _python_opers_in:

Operador in
...........

El operador ``in``, significa, para cualquier colección del valor del lado izquierdo 
contenga el valor del lado derecho:

::

    >>> b = [1, 2, 3]
    >>> 2 in b
    True
    >>> 5 in b
    False

En el ejemplo anterior, si ``b`` es una lista, este prueba que ``2`` y ``5`` sean 
elementos de la lista ``b``.


.. _python_opers_notin:

Operador not in
................

El operador ``not in``, el contrario de operador :ref:`in <python_opers_in>`, devuelve 
``True`` cuando un elemento no está en una secuencia.

::

    >>> b = [1, 2, 3]
    >>> 4 not in b
    True
    >>> 1 not in b
    False

En el ejemplo anterior, si ``b`` es una lista, este prueba que ``4`` y ``1`` sean 
elementos de la lista ``b``.


.. _python_expresiones_condicional:

Expresiones condicional
.......................

Estos son los distintos tipos de expresiones condicionales:


Expresión if
~~~~~~~~~~~~

La expresión de la sentencia ``if`` se evaluá a ``False`` cuando se cumple las 
siguientes expresiones están presente:

- Cualquier numero igual a cero (0, 0.0, 0+0j).

- Un contenedor vació (:ref:`lista <python_list>`, :ref:`tupla <python_tuple>`, 
  :ref:`conjunto <python_set>`, :ref:`diccionario <python_dict>`). 

- ``False``, ``None``.

De lo contrario evaluá a ``True`` cuando se cumple la siguiente expresión esta presente:

- cualquier cosa de lo contrario.

::

    if EXPRESION:
        pass


Expresión ==
~~~~~~~~~~~~

Esta expresión usa el operador :ref:`== <python_opers_rela_igual>` para validar la misma.


Expresión is
~~~~~~~~~~~~

Esta expresión usa el operador :ref:`is <python_opers_is>` para validar la misma.


Expresión in
~~~~~~~~~~~~

Esta expresión usa el operador :ref:`in <python_opers_in>` para validar la misma.


Ejemplos
........

A continuación, se presenta un ejemplo del uso de condicionales ``if``:


**Definir variables usadas en los siguientes ejemplos**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :language: python
    :lines: 3


**Ejemplo de operador de comparación Igual**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :language: python
    :lines: 11-14


**Ejemplo de operador de comparación Distinto**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :language: python
    :lines: 17-20


**Ejemplo de operador de comparación Diferente**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :language: python
    :lines: 17-20


**Ejemplo de operador de comparación Menor que**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :language: python
    :lines: 23-26


**Ejemplo de operador de comparación Mayor que**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :language: python
    :lines: 29-32


**Ejemplo de operador de comparación Menor o igual que**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :language: python
    :lines: 35-38


**Ejemplo de operador de comparación Mayor o igual que**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :language: python
    :lines: 41-44


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion4/condicional_if.py>`.


.. tip::
    Para ejecutar el código :file:`condicional_if.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando:

    ::

        python condicional_if.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion4>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
