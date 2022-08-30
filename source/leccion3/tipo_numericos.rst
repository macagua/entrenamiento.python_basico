.. -*- coding: utf-8 -*-


.. _python_numericos:

Tipo números
------------

Estos tipos de datos se crean mediante literales numéricos y se devuelven como 
resultados por operadores aritméticos y funciones aritméticas integradas. Los 
objetos numéricos son inmutables; Una vez creado su valor nunca cambia.

Por supuesto, los números de Python están fuertemente relacionados con los números 
matemáticos, pero están sujetos a las limitaciones de la representación numérica en 
las computadoras.

Python distingue entre enteros, números de punto flotante y números complejos:

+-------------+----------+-------------------------------------+-------------------------+
| **Clase**   | **Tipo** | **Notas**                           | **Ejemplo**             |
+-------------+----------+-------------------------------------+-------------------------+
| ``int``     | Números  | Número entero con precisión fija.   | ``42``                  |
+-------------+----------+-------------------------------------+-------------------------+
| ``long``    | Números  | Número entero en caso de overflow.  | ``42L`` ó               |
|             |          |                                     | ``456966786151987643L`` |
+-------------+----------+-------------------------------------+-------------------------+
| ``float``   | Números  | Coma flotante de doble precisión.   | ``3.1415927``           |
+-------------+----------+-------------------------------------+-------------------------+
| ``complex`` | Números  | Parte real y parte imaginaria *j*.  | ``(4.5 + 3j)``          |
+-------------+----------+-------------------------------------+-------------------------+

.. _python_num_entero:

Enteros
.......

Los números enteros son aquellos que no tienen decimales, tanto positivos como negativos 
(además del cero). En Python se pueden representar mediante el tipo ``int`` (de integer, 
entero) o el tipo ``long`` (largo). La única diferencia es que el tipo long permite 
almacenar números más grandes. Es aconsejable no utilizar el tipo ``long`` a menos que
sea necesario, para no malgastar memoria.

El tipo ``int`` de Python se implementa a bajo nivel mediante un tipo ``long`` de C. 
Y dado que Python utiliza C por debajo, como C, y a diferencia de Java, el rango de 
los valores que puede representar depende de la plataforma. En la mayor parte de las 
máquinas el ``long`` de C se almacena utilizando 32 bits, es decir, mediante el uso 
de una variable de tipo ``int`` de Python puede almacenar números de -2\ :sup:`31` 
a 2\ :sup:`31` – 1, o lo que es lo mismo, de -2.147.483.648 a 2.147.483.647. En 
plataformas de 64 bits, el rango es de -9.223.372.036.854.775.808 hasta 
9.223.372.036.854.775.807.


Ejemplo de enteros
~~~~~~~~~~~~~~~~~~

A continuación, se presentan un ejemplo de su uso:

**Ejemplo de definición de un tipo entero**

.. literalinclude:: ../../recursos/leccion3/tipo_numericos.py
    :language: python
    :lines: 5-6


.. _python_num_entero_long:

Enteros long
............

El tipo ``long`` de Python permite almacenar números de cualquier precisión, limitado 
por la memoria disponible en la máquina.

Al asignar un número a una variable esta pasará a tener tipo ``int``, a menos que el 
número sea tan grande como para requerir el uso del tipo ``long``.

::

    >>> entero = 23
    >>> type(entero)
    <type 'int'>

También puede indicar a Python que un número se almacene usando ``long`` añadiendo 
una *L* al final:

::

    >>> entero = 23L
    >>> type(entero)
    <type 'long'>


El literal que se asigna a la variable también se puede expresar como un ``octal``, 
anteponiendo un cero:

::

    # 027 octal = 23 en base 10
    entero = 027

o bien en hexadecimal, anteponiendo un ``0x``:

::

    # 0x17 hexadecimal = 23 en base 10
    entero = 0x17


Ejemplo de enteros long
~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presentan un ejemplo de su uso:

**Ejemplo de definición de un tipo entero long**

.. literalinclude:: ../../recursos/leccion3/tipo_numericos.py
    :language: python
    :lines: 9-10


----

.. _python_num_float:

Coma flotante
.............

Los números reales son los que tienen decimales. En Python se expresan mediante el 
tipo ``float``. En otros lenguajes de programación, como C, tiene también el tipo 
``double``, similar a ``float`` pero de mayor precisión (double = doble precisión). 

Python, sin embargo, implementa su tipo ``float`` a bajo nivel mediante una variable 
de tipo ``double`` de C, es decir, utilizando 64 bits, luego en Python siempre se 
utiliza doble precisión, y en concreto se sigue el estándar IEEE 754: 1 bit para el 
signo, 11 para el exponente, y 52 para la mantisa. Esto significa que los valores 
que puede representar van desde ±2,2250738585072020 x 10\ :sup:`-308` hasta 
±1,7976931348623157×10\ :sup:`308`.

La mayor parte de los lenguajes de programación siguen el mismo esquema para la 
representación interna. Pero como muchos sabréis esta tiene sus limitaciones, 
impuestas por el hardware.

Por eso desde Python 2.4 cuenta también con un nuevo tipo 
`Decimal <https://www.python.org/dev/peps/pep-0327/>`_, para el caso de que se necesite 
representar fracciones de forma más precisa. Sin embargo este tipo está fuera del 
alcance de este tutorial, y sólo es necesario para el ámbito de la programación 
científica y otros relacionados. 

Para aplicaciones normales puedes utilizar el tipo ``float`` sin miedo, como ha venido 
haciéndose desde hace años, aunque teniendo en cuenta que los números en coma flotante 
no son precisos (ni en este ni en otros lenguajes de programación).

Para representar un número real en Python se escribe primero la parte entera, seguido 
de un punto y por último la parte decimal.

::

    real = 0.2703

También se puede utilizar notación científica, y añadir una e (de exponente) para 
indicar un exponente en base 10. Por ejemplo:

::

    real = 0.1e-3

sería equivalente a 0.1 x 10\ :sup:`-3` = 0.1 x 0.001 = 0.0001


Ejemplo de enteros float
~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presentan un ejemplo de su uso:

**Ejemplo de definición de tipo entero coma flotante**

.. literalinclude:: ../../recursos/leccion3/tipo_numericos.py
    :language: python
    :lines: 13-16


**Ejemplo de definición de tipo entero coma flotante con exponente en base 10**

.. literalinclude:: ../../recursos/leccion3/tipo_numericos.py
    :language: python
    :lines: 20-21

----

.. _python_num_complex:

Complejos
.........

Los números complejos son aquellos que tienen parte imaginaria. Si no conocías de su 
existencia, es más que probable que nunca lo vayas a necesitar, por lo que puede 
saltarte este apartado tranquilamente.

De hecho la mayor parte de lenguajes de programación carecen de este tipo, aunque sea 
muy utilizado por ingenieros y científicos en general.

En el caso de que necesite utilizar números complejos, o simplemente tiene curiosidad, 
este tipo, llamado ``complex`` en Python, también se almacena usando coma flotante, 
debido a que estos números son una extensión de los números reales. 

En concreto se almacena en una estructura de C, compuesta por dos variables de tipo 
``double``, sirviendo una de ellas para almacenar la parte real y la otra para la 
parte imaginaria.

Los números complejos en Python se representan de la siguiente forma:

::

    complejo = 2.1 + 7.8j


Ejemplo de enteros complex
~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presentan un ejemplo de su uso:

**Ejemplo de definición de tipo entero complejos**

.. literalinclude:: ../../recursos/leccion3/tipo_numericos.py
    :language: python
    :lines: 24-25


Convertir a numéricos
.....................

Para convertir a :ref:`tipos numéricos <python_numericos>` debe usar las siguientes 
:ref:`funciones integradas <python_fun_builtins>` en el interprete Python:

- La función :ref:`int() <python_fun_int>` devuelve un tipo de datos 
  :ref:`número entero <python_num_entero>`.

- La función :ref:`long() <python_fun_long>` devuelve un tipo de datos 
  :ref:`número entero long <python_num_entero_long>`.

- La función :ref:`float() <python_fun_float>` devuelve un tipo de datos 
  :ref:`número entero float <python_num_float>`.

- La función :ref:`complex() <python_fun_complex>` devuelve un tipo de datos 
  :ref:`número complejo <python_num_complex>`.


Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre las **números enteros** 
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

::

    >>> help(int)

Para salir de esa ayuda presione la tecla ``q``.


Usted puede consultar toda la documentación disponible sobre las **números enteros 
long** desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

::

    >>> help(long)

Para salir de esa ayuda presione la tecla ``q``.


Usted puede consultar toda la documentación disponible sobre las **números coma 
flotante** desde la :ref:`consola interactiva <python_interactivo>` de la siguiente 
forma:

::

    >>> help(float)

Para salir de esa ayuda presione la tecla ``q``.


Usted puede consultar toda la documentación disponible sobre las **números complejos** 
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

::

    >>> help(complex)

Para salir de esa ayuda presione la tecla ``q``.


.. tip:: 
    Para más información consulte las funciones integradas para 
    :ref:`operaciones numéricas <python_fun_builtins_numericas>`.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_numericos.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_numericos.py`, abra una consola de comando, 
    acceda al directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    ::

        python tipo_numericos.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
