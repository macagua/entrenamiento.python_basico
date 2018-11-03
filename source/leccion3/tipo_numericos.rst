.. -*- coding: utf-8 -*-


.. _python_numericos:

Tipo números
------------

En Python se pueden representar números enteros, coma flotante y complejos.

+-------------+-----------------+-------------------------------------+---------------------------+
| **Tipo**    | **Clase**       | **Notas**                           | **Ejemplo**               |
+-------------+-----------------+-------------------------------------+---------------------------+
| ``int``     | Número entero   | Precisión fija, convertido en       | 42                        |
|             |                 | ``long`` en caso de overflow.       |                           |
+-------------+-----------------+-------------------------------------+---------------------------+
| ``long``    | Número entero   | Precisión arbitraria                | 42L ó 456966786151987643L |
+-------------+-----------------+-------------------------------------+---------------------------+
| ``float``   | Número decimal  | Coma flotante de doble precisión    | 3.1415927                 |
+-------------+-----------------+-------------------------------------+---------------------------+
| ``complex`` | Número complejo | Parte real y parte imaginaria *j*.  | (4.5 + 3j)                |
+-------------+-----------------+-------------------------------------+---------------------------+

.. _python_numerico_entero:

Enteros
.......

Los números enteros son aquellos que no tienen decimales, tanto
positivos como negativos (además del cero). En Python se pueden
representar mediante el tipo ``int`` (de integer, entero) o el tipo ``long``
(largo). La única diferencia es que el tipo long permite almacenar
números más grandes. Es aconsejable no utilizar el tipo ``long`` a menos que
sea necesario, para no malgastar memoria.

El tipo ``int`` de Python se implementa a bajo nivel mediante un tipo ``long``
de C. Y dado que Python utiliza C por debajo, como C, y a diferencia de
Java, el rango de los valores que puede representar depende de la
plataforma. En la mayor parte de las máquinas el ``long`` de C se almacena
utilizando 32 bits, es decir, mediante el uso de una variable de tipo
``int`` de Python podemos almacenar números de -2\ :sup:`31` a 2\ :sup:`31`
– 1, o lo que es lo mismo, de -2.147.483.648 a 2.147.483.647. En
plataformas de 64 bits, el rango es de -9.223.372.036.854.775.808 hasta
9.223.372.036.854.775.807.


Ejemplo de enteros
~~~~~~~~~~~~~~~~~~

A continuación, se presentan un ejemplo de su uso:

**Ejemplo de definición de un tipo entero**

.. literalinclude:: ../../recursos/leccion3/tipo_numericos.py
    :language: python
    :lines: 4-6


.. _python_numerico_entero_long:

Enteros long
............

El tipo ``long`` de Python permite almacenar números de cualquier precisión,
limitado por la memoria disponible en la máquina.

Al asignar un número a una variable esta pasará a tener tipo ``int``, a
menos que el número sea tan grande como para requerir el uso del tipo
``long``.

::

    >>> entero = 23
    >>> type(entero)
    <type 'int'>
    >>> 

También podemos indicar a Python que un número se almacene usando long
añadiendo una L al final:

::

    >>> entero = 23L
    >>> type(entero)
    <type 'long'>
    >>> 


El literal que se asigna a la variable también se puede expresar como un
``octal``, anteponiendo un cero:

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
    :lines: 9-11


----

.. _python_numerico_coma_flotante:

Coma flotante
.............

Los números reales son los que tienen decimales. En Python se expresan
mediante el tipo ``float``. En otros lenguajes de programación, como C,
tenemos también el tipo ``double``, similar a ``float`` pero de mayor precisión
(double = doble precisión). Python, sin embargo, implementa su tipo
``float`` a bajo nivel mediante una variable de tipo ``double`` de C, es decir,
utilizando 64 bits, luego en Python siempre se utiliza doble precisión,
y en concreto se sigue el estándar IEEE 754: 1 bit para el signo, 11
para el exponente, y 52 para la mantisa. Esto significa que los valores
que podemos representar van desde ±2,2250738585072020 x 10\ :sup:`-308`
hasta ±1,7976931348623157×10\ :sup:`308`.

La mayor parte de los lenguajes de programación siguen el mismo esquema
para la representación interna. Pero como muchos sabréis esta tiene sus
limitaciones, impuestas por el hardware. Por eso desde Python 2.4
contamos también con un nuevo tipo 
`*Decimal* <https://www.python.org/dev/peps/pep-0327/>`_, para el caso de
que se necesite representar fracciones de forma más precisa. Sin embargo
este tipo está fuera del alcance de este tutorial, y sólo es necesario
para el ámbito de la programación científica y otros relacionados. Para
aplicaciones normales puedes utilizar el tipo ``float`` sin miedo, como ha
venido haciéndose desde hace años, aunque teniendo en cuenta que los
números en coma flotante no son precisos (ni en este ni en otros
lenguajes de programación).

Para representar un número real en Python se escribe primero la parte
entera, seguido de un punto y por último la parte decimal.

::

    real = 0.2703

También se puede utilizar notación científica, y añadir una e (de
exponente) para indicar un exponente en base 10. Por ejemplo:

::

    real = 0.1e-3

sería equivalente a 0.1 x 10\ :sup:`-3` = 0.1 x 0.001 = 0.0001


Ejemplo de enteros float
~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presentan un ejemplo de su uso:

**Ejemplo de definición de tipo entero coma flotante**

.. literalinclude:: ../../recursos/leccion3/tipo_numericos.py
    :language: python
    :lines: 14-18


**Ejemplo de definición de tipo entero coma flotante con exponente en base 10**

.. literalinclude:: ../../recursos/leccion3/tipo_numericos.py
    :language: python
    :lines: 22-24

----

.. _python_numerico_complejo:

Complejos
.........

Los números complejos son aquellos que tienen parte imaginaria. Si no
conocías de su existencia, es más que probable que nunca lo vayas a
necesitar, por lo que puedes saltarte este apartado tranquilamente. De
hecho la mayor parte de lenguajes de programación carecen de este tipo,
aunque sea muy utilizado por ingenieros y científicos en general.

En el caso de que necesitéis utilizar números complejos, o simplemente
tengáis curiosidad, os diré que este tipo, llamado ``complex`` en Python,
también se almacena usando coma flotante, debido a que estos números son
una extensión de los números reales. En concreto se almacena en una
estructura de C, compuesta por dos variables de tipo ``double``, sirviendo
una de ellas para almacenar la parte real y la otra para la parte
imaginaria.

Los números complejos en Python se representan de la siguiente forma:

::

    complejo = 2.1 + 7.8j


Ejemplo de enteros complex
~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presentan un ejemplo de su uso:

**Ejemplo de definición de tipo entero complejos**

.. literalinclude:: ../../recursos/leccion3/tipo_numericos.py
    :language: python
    :lines: 28-30


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_numericos.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_numericos.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando: ::

        python2 tipo_numericos.py


----


Convertir a tipos numéricos
...........................

Para convertir a tipos numéricos debes usar las :ref:`funciones integradas <python_funciones_integradas>` 
al interprete disponible, a continuación se describen algunas de ellas para 
tipos de datos numéricos:


.. _python_funcion_int:

int()
~~~~~

La función ``int()`` devuelve un número entero. Es un constructor, que crea un 
:ref:`entero <python_numerico_entero>` a partir de un 
:ref:`entero float <python_numerico_coma_flotante>`, 
:ref:`entero complex <python_numerico_complejo>` o una 
:ref:`cadena de caracteres <python_cadenas>` que sean coherentes con un número 
entero.


::

    >>> int(2.5)
    2
    >>>

También puede convertir una cadena de caracteres a un número entero.

::

    >>> int("23")
    23
    >>> 


La función ``int()`` sólo procesa correctamente cadenas que contengan exclusivamente 
números. Si la cadena contiene cualquier otro carácter, la función devuelve una excepción 
:ref:`ValueError <python_exception_valueerror>`.

::

    >>> int("2.5")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: '2.5'
    >>>
    >>> int("doscientos")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'doscientos'
    >>> 


.. _python_funcion_long:

long()
~~~~~~

La función ``long()`` devuelve un número entero ``long``. Es un constructor, que crea un 
:ref:`entero long <python_numerico_entero_long>` a partir de un 
:ref:`entero <python_numerico_entero>`, :ref:`entero float <python_numerico_coma_flotante>` 
o una :ref:`cadena de caracteres <python_cadenas>` que sean coherentes con un número entero.

::

    >>> long(23)
    23L
    >>> long(23.4)
    23L
    >>>

También puede convertir una cadena de caracteres a un número entero.

::

    >>> long("23")
    23
    >>> 


La función ``long()`` sólo procesa correctamente cadenas que contengan exclusivamente 
números. Si la cadena contiene cualquier otro carácter, la función devuelve una excepción 
:ref:`ValueError <python_exception_valueerror>`.

::

    >>> long("23.4")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for long() with base 10: '23.4'
    >>>
    >>> long("23,4")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for long() with base 10: '23,4'
    >>> 


.. _python_funcion_float:

float()
~~~~~~~

La función ``float()`` devuelve un número coma flotante ``float``. Es un constructor, 
que crea un :ref:`coma flotante <python_numerico_coma_flotante>` a partir de un 
:ref:`entero <python_numerico_entero>`, :ref:`entero long <python_numerico_entero_long>`, 
:ref:`entero float <python_numerico_coma_flotante>` (cadenas de caracteres formadas por 
números y hasta un punto) o una :ref:`cadena de caracteres <python_cadenas>` que sean 
coherentes con un número entero.

::

    >>> float(2)
    2.0
    >>> float(23L)
    23.0
    >>> float(2.5)
    2.5
    >>> float("2")
    2.0
    >>> float("2.5")
    2.5
    >>> 


.. _python_funcion_complex:

complex()
~~~~~~~~~

La función ``complex()`` devuelve un número complejo ``complex``. Es un constructor, 
que crea un :ref:`entero complex <python_numerico_complejo>` a partir de un 
:ref:`entero <python_numerico_entero>`, :ref:`entero long <python_numerico_entero_long>`, 
:ref:`entero float <python_numerico_coma_flotante>` (cadenas de caracteres formadas por 
números y hasta un punto), o una :ref:`cadena de caracteres <python_cadenas>` que sean 
coherentes con un número entero.

::

    >>> complex(23)
    (23+0j)
    >>> complex(23L)
    (23+0j)
    >>> complex(23.4)
    (23.4+0j)
    >>> complex("23")
    (23+0j)
    >>> complex("23.6")
    (23.6+0j)
    >>> 

La función ``complex()`` sólo procesa correctamente cadenas que contengan 
exclusivamente números.Si la cadena contiene cualquier otro carácter, la 
función devuelve una excepción :ref:`ValueError <python_exception_valueerror>`.

::

    >>> complex("qwerty")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: complex() arg is a malformed string
    >>> 

----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre las **números 
enteros** desde la :ref:`consola interactiva <python_interactivo>` de la 
siguiente forma:

::

    >>> help(int)

Para salir de esa ayuda presione la tecla ``q``.


Usted puede consultar toda la documentación disponible sobre las **números 
enteros long** desde la :ref:`consola interactiva <python_interactivo>` de la 
siguiente forma:

::

    >>> help(long)

Para salir de esa ayuda presione la tecla ``q``.


Usted puede consultar toda la documentación disponible sobre las **números 
coma flotante** desde la :ref:`consola interactiva <python_interactivo>` de la 
siguiente forma:

::

    >>> help(float)

Para salir de esa ayuda presione la tecla ``q``.


Usted puede consultar toda la documentación disponible sobre las **números 
complejos** desde la :ref:`consola interactiva <python_interactivo>` de la 
siguiente forma:

::

    >>> help(complex)

Para salir de esa ayuda presione la tecla ``q``.


.. tip:: 
    Para más información consulte las funciones integradas para 
    :ref:`operaciones numéricas <python_funciones_integradas_numericas>`.

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
