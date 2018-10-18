.. -*- coding: utf-8 -*-


.. _python_numericos:

Tipos de Enteros
----------------

Números
.......

Como decíamos, en Python se pueden representar números enteros, reales y
complejos.

Enteros
~~~~~~~

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

El tipo ``long`` de Python permite almacenar números de cualquier precisión,
limitado por la memoria disponible en la máquina.

Al asignar un número a una variable esta pasará a tener tipo ``int``, a
menos que el número sea tan grande como para requerir el uso del tipo
``long``.

::

    # type(entero) daría int
    entero = 23

También podemos indicar a Python que un número se almacene usando long
añadiendo una L al final:

::

    # type(entero) daría long
    entero = 23L

El literal que se asigna a la variable también se puede expresar como un
``octal``, anteponiendo un cero:

::

    # 027 octal = 23 en base 10
    entero = 027

o bien en hexadecimal, anteponiendo un 0x:

::

    # 0x17 hexadecimal = 23 en base 10
    entero = 0x17

Ejemplo de enteros
````````````````````

A continuación, se presentan un ejemplo de su uso:

.. literalinclude:: ../../recursos/leccion3/tipo_numericos.py
    :language: python
    :lines: 9-42

Reales
~~~~~~

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

Ejemplo de reales
`````````````````

A continuación, se presentan un ejemplo de su uso:

.. literalinclude:: ../../recursos/leccion3/tipo_numericos.py
    :language: python
    :lines: 12-21


Complejos
~~~~~~~~~

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

