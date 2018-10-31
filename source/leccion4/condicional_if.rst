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

.. seealso::

    .. figure:: https://img.youtube.com/vi/hLqKvB7tGWk/0.jpg
        :align: center
        :width: 60%

        Vídeo `Tutorial Python 10 - Sentencias condicionales`_, cortesía de `CodigoFacilito.com`_.

    .. todo:: Cambiar la URL de imagen de previsuaalación del video, de forma local.

    **Otros recursos**
      - `Python - Tipos básicos`_.

      - `Operadores básicos de Python`_.


Referencias
...........

- `Sentencias IF`_.

- `Condicionales if y else en Python`_.

.. _`Python - Tipos básicos`: http://mundogeek.net/archivos/2008/01/17/python-tipos-basicos/
.. _`Operadores básicos de Python`: http://codigoprogramacion.com/cursos/tutoriales-python/operadores-basicos-de-python.html
.. _`Tutorial Python 10 - Sentencias condicionales`: https://www.youtube.com/watch?v=hLqKvB7tGWk
.. _`CodigoFacilito.com`: https://www.codigofacilito.com/
.. _`Sentencias IF`: http://docs.python.org.ar/tutorial/2/controlflow.html#la-sentencia-if
.. _`Condicionales if y else en Python`: http://codigoprogramacion.com/cursos/tutoriales-python/condicionales-if-y-else-en-python.html
