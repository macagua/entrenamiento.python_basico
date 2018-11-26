.. -*- coding: utf-8 -*-


.. _python_condicional_if:

Condicional if
--------------

La sentencia condicional ``if`` se usa para tomar decisiones, este evaluá
básicamente una operación lógica, es decir una expresión que de
como resultado verdadero o false (``True`` o ``False``), y ejecuta
la pieza de código siguiente siempre y cuando el resultado sea verdadero.

Ejemplo de condicionales if
...........................

A continuación, se presenta un ejemplo del uso de condicionales ``if``:


**Definir variables usadas en los siguientes ejemplos**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :linenos:
    :language: python
    :lines: 7


**Ejemplo de operador de comparación Igual**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :linenos:
    :language: python
    :lines: 15-18


**Ejemplo de operador de comparación Distinto**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :linenos:
    :language: python
    :lines: 21-24


**Ejemplo de operador de comparación Diferente**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :linenos:
    :language: python
    :lines: 27-30


**Ejemplo de operador de comparación Menor que**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :linenos:
    :language: python
    :lines: 33-36


**Ejemplo de operador de comparación Mayor que**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :linenos:
    :language: python
    :lines: 39-42


**Ejemplo de operador de comparación Menor o igual que**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :linenos:
    :language: python
    :lines: 45-48


**Ejemplo de operador de comparación Mayor o igual que**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :linenos:
    :language: python
    :lines: 51-54


**Ejemplo de condicional if / elif / else completo**:

.. literalinclude:: ../../recursos/leccion4/condicional_if.py
    :linenos:
    :language: python
    :lines: 58-68

En el ejemplo anterior usa dos funciones integradas en el interprete Python:

- La función :ref:`int() <python_funcion_int>` que convierte el valor ingresado 
  a numero entero.

- La función :ref:`raw_input() <python_funcion_raw_input>` lee el valor ingresado 
  por la entrada estándar.

El valor es ingresado en la variable ``numero`` comprobará en el sentencia condicional 
``if``, si la comprobación devuelve ``False`` intentará con el siguiente bloque condicional 
``elif``, si la comprobación devuelve ``False`` nuevamente intentará con el siguiente 
bloque condicional ``elif`` si de nuevo la comprobación devuelve ``False`` por ultimo 
intentará con el siguiente bloque condicional ``else`` la cual se ejecutara sin comprobación.

- ``if CONDICION``, significa, **Si** se cumple la 
  :ref:`expresión condicional <python_expresiones_condicional>` se ejecuta el bloque de 
  sentencias seguidas.

- ``elif CONDICION``, significa, **De lo contrario Si** se cumple la 
  :ref:`expresión condicional <python_expresiones_condicional>` se ejecuta el bloque de 
  sentencias seguidas.

- ``else``, significa, **De lo contrario** se cumple sin evaluar ninguna 
  :ref:`expresión condicional <python_expresiones_condicional>` y ejecuta el bloque de 
  sentencias seguidas.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion4/condicional_if.py>`.


.. tip::
    Para ejecutar el código :file:`condicional_if.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando: ::

        python condicional_if.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion4>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
