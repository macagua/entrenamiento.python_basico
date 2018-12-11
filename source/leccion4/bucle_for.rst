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
estructuras de datos :ref:`listas <python_list>`:

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 12-15


Bucle 'for' con Listas y función 'range'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``for`` con tipos de 
estructuras de datos :ref:`listas <python_list>` con la función 
:ref:`range() <python_fun_range>` y la función :ref:`len() <python_fun_len>`:

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 32-37

Si se necesita iterar sobre una secuencia de números. Genera una lista conteniendo 
progresiones aritméticos, por ejemplo, como se hace en el fragmento de código fuente 
anterior.


Bucle 'for' con Tuplas
~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``for`` con tipos de 
estructuras de datos :ref:`Tuplas <python_tuple>`:

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 46-48

El ejemplo anterior itera una :ref:`tupla <python_tuple>` de parámetros.


Bucle 'for' con Diccionarios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``for`` con tipos de 
estructuras de datos :ref:`Diccionarios <python_diccionarios>`:

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 57-71

El ejemplo anterior itera un :ref:`diccionario <python_diccionarios>` con datos 
básicos de una persona.


Bucle 'for' con 'else'
~~~~~~~~~~~~~~~~~~~~~~

Al igual que la sentencia :ref:`if <python_condi_if>` y el bucle 
:ref:`while <python_bucle_while>`, la estructura ``for`` también puede combinarse 
con una sentencia :ref:`else <python_sent_else>`. 

El nombre de la sentencia :ref:`else <python_sent_else>` es equivocada, ya que el bloque 
:ref:`else <python_sent_else>` se ejecutará en todos los casos, es decir, cuando la 
expresión condicional del bucle ``for`` sea ``False``, (a comparación de la 
:ref:`sentencia if <python_condi_if>`).

.. literalinclude:: ../../recursos/leccion4/bucle_for.py
    :linenos:
    :language: python
    :lines: 80-87

La sentencia ``else`` tiene la ventaja de mantener el mismo nombre y la misma sintaxis 
que en las demás estructuras de control.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion4/bucle_for.py>`.


.. tip::
    Para ejecutar el código :file:`bucle_for.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando:

    ::

        python bucle_for.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion4>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
