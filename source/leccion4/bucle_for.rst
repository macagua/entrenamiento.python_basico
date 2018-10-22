.. -*- coding: utf-8 -*-


.. _python_bucle_for:

Bucle for
----------

La sentencia ``for`` en Python difiere un poco de lo que uno puede estar
acostumbrado en lenguajes como C o Pascal.  En lugar de siempre iterar sobre
una progresión aritmética de números (como en Pascal) o darle al usuario la
posibilidad de definir tanto el paso de la iteración como la condición de fin
(como en C), la sentencia `for` de Python itera sobre los ítems de
cualquier secuencia (una lista o una cadenas de caracteres), en el orden que aparecen
en la secuencia.


Tipos de Bucle 'for'
.....................

A continuación, se presentan algunos ejemplos del uso del bucle ``for``:


Bucle 'for' con Listas
~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``for`` con tipos de 
estructuras de datos :ref:`Listas <python_listas>`:

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 7-14


Bucle 'for' con Listas y función 'range'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``for`` con tipos de 
estructuras de datos :ref:`Listas <python_listas>` con la función ``range``:

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 18-25

Si se necesita iterar sobre una secuencia de números. Genera una lista conteniendo 
progresiones aritméticos, por ejemplo, como se hace en el fragmento de código fuente 
anterior.


Bucle 'for' con Tuplas
~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``for`` con tipos de estructuras de datos 
:ref:`Tuplas <python_tuplas>`:

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 29-34

El ejemplo anterior itera una :ref:`tupla <python_tuplas>` de parámetros.


Bucle 'for' con Diccionarios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``for`` con tipos de estructuras de datos 
:ref:`Diccionarios <python_diccionarios>`:

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 38-55

El ejemplo anterior itera un :ref:`diccionario <python_diccionarios>` con datos 
básicos de una persona.

.. seealso:: Ver el vídeo `Tutorial Python 11 - Bucles`_.


Referencia
..........

- Introducción a `Bucles 'for'`_.
 
.. _`Bucles 'for'`: http://docs.python.org.ar/tutorial/2/controlflow.html#la-sentencia-for
.. _`Tutorial Python 11 - Bucles`: https://www.youtube.com/watch?v=IyI2ZuOq_xQ
