.. -*- coding: utf-8 -*-


.. _python_bucle_for:

Bucle for
----------

La sentencia ``for`` en Python difiere un poco de lo que uno puede estar
acostumbrado en lenguajes como C o Pascal.  En lugar de siempre iterar sobre
una progresión aritmética de números (como en Pascal) o darle al usuario la
posibilidad de definir tanto el paso de la iteración como la condición de fin
(como en C), la sentencia `for` de Python itera sobre los ítems de cualquier 
secuencia (una lista o una cadenas de caracteres), en el orden que aparecen
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
    :lines: 14-17


Bucle 'for' con Listas y función 'range'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``for`` con tipos de 
estructuras de datos :ref:`Listas <python_listas>` con la función 
:ref:`range <python_funcion_range>` y la función :ref:`len <python_funcion_len>`:

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 34-39

Si se necesita iterar sobre una secuencia de números. Genera una lista conteniendo 
progresiones aritméticos, por ejemplo, como se hace en el fragmento de código fuente 
anterior.


Bucle 'for' con Tuplas
~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``for`` con tipos de 
estructuras de datos :ref:`Tuplas <python_tuplas>`:

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 48-50

El ejemplo anterior itera una :ref:`tupla <python_tuplas>` de parámetros.


Bucle 'for' con Diccionarios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``for`` con tipos de 
estructuras de datos :ref:`Diccionarios <python_diccionarios>`:

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 59-73

El ejemplo anterior itera un :ref:`diccionario <python_diccionarios>` con datos 
básicos de una persona.


Bucle 'for' con 'else'
~~~~~~~~~~~~~~~~~~~~~~

Al igual que la :ref:`sentencia if <python_condicional_if>` y 
:ref:`bucle while <python_bucle_while>`, la estructura ``for`` también puede 
combinarse con una sentencia ``else``. 

El nombre de la sentencia ``else`` es equivocada, ya que el bloque ``else`` se 
ejecutará en todos los casos, es decir, cuando la expresión condicional del ``for`` 
sea ``False``, (a comparación de la :ref:`sentencia if <python_condicional_if>`).

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 82-89

La sentencia ``else`` tiene la ventaja de mantener el mismo nombre y la misma sintaxis 
que en las demás estructuras de control.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion4/bucle_for.py>`.


.. tip::
    Para ejecutar el código :file:`bucle_for.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando: ::

        python2 bucle_for.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion4>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
