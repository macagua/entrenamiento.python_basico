.. -*- coding: utf-8 -*-

LECCIÓN 4: TIPOS DE DATOS BÁSICOS Y VARIABLES PYTHON
====================================================

En Python tenemos como tipos de datos simples números: enteros,
de coma flotante y complejos, como pueden ser 3, 15.57 o 7 + 5j;
cadenas de texto, como "Hola Mundo" y valores booleanos: True (cierto)
y False (falso).

Vamos a crear un par de variables a modo de ejemplo. Una de tipo 
cadena y una de tipo entero:

::

    # esto es una cadena
    c = "Hola Mundo"

    # y esto es un entero
    e = 23

    # podemos comprobarlo con la función type
    type(c)
    type(e)

Como puede ver en Python, a diferencia de muchos otros lenguajes, no se
declara el tipo de la variable al crearla. En Java, por ejemplo,
escribiríamos:

::

    String c = "Hola Mundo";
    int e = 23;

También nos ha servido nuestro pequeño ejemplo para presentaros los
comentarios inline en Python: cadenas de texto que comienzan con el
carácter ‘#’ y que Python ignora totalmente. Hay más tipos de
comentarios, de los que hablaremos más adelante.

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
representar mediante el tipo int (de integer, entero) o el tipo long
(largo). La única diferencia es que el tipo long permite almacenar
números más grandes. Es aconsejable no utilizar el tipo long a menos que
sea necesario, para no malgastar memoria.

El tipo int de Python se implementa a bajo nivel mediante un tipo long
de C. Y dado que Python utiliza C por debajo, como C, y a diferencia de
Java, el rango de los valores que puede representar depende de la
plataforma. En la mayor parte de las máquinas el long de C se almacena
utilizando 32 bits, es decir, mediante el uso de una variable de tipo
int de Python podemos almacenar números de -2\ :sup:`31` a 2\ :sup:`31`
– 1, o lo que es lo mismo, de -2.147.483.648 a 2.147.483.647. En
plataformas de 64 bits, el rango es de -9.223.372.036.854.775.808 hasta
9.223.372.036.854.775.807.

El tipo long de Python permite almacenar números de cualquier precisión,
limitado por la memoria disponible en la máquina.

Al asignar un número a una variable esta pasará a tener tipo int, a
menos que el número sea tan grande como para requerir el uso del tipo
long.

::

    # type(entero) daría int
    entero = 23

También podemos indicar a Python que un número se almacene usando long
añadiendo una L al final:

::

    # type(entero) daría long
    entero = 23L

El literal que se asigna a la variable también se puede expresar como un
octal, anteponiendo un cero:

::

    # 027 octal = 23 en base 10
    entero = 027

o bien en hexadecimal, anteponiendo un 0x:

::

    # 0x17 hexadecimal = 23 en base 10
    entero = 0x17

Reales
~~~~~~

Los números reales son los que tienen decimales. En Python se expresan
mediante el tipo float. En otros lenguajes de programación, como C,
tenemos también el tipo double, similar a float pero de mayor precisión
(double = doble precisión). Python, sin embargo, implementa su tipo
float a bajo nivel mediante una variable de tipo double de C, es decir,
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
aplicaciones normales podeis utilizar el tipo float sin miedo, como ha
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

Complejos
~~~~~~~~~

Los números complejos son aquellos que tienen parte imaginaria. Si no
conocías de su existencia, es más que probable que nunca lo vayas a
necesitar, por lo que puedes saltarte este apartado tranquilamente. De
hecho la mayor parte de lenguajes de programación carecen de este tipo,
aunque sea muy utilizado por ingenieros y científicos en general.

En el caso de que necesitéis utilizar números complejos, o simplemente
tengáis curiosidad, os diré que este tipo, llamado complex en Python,
también se almacena usando coma flotante, debido a que estos números son
una extensión de los números reales. En concreto se almacena en una
estructura de C, compuesta por dos variables de tipo double, sirviendo
una de ellas para almacenar la parte real y la otra para la parte
imaginaria.

Los números complejos en Python se representan de la siguiente forma:

::

    complejo = 2.1 + 7.8j

Ejemplo de tipos de enteros
...........................

.. literalinclude:: enteros.py
    :linenos:
    :language: python

Tipo Cadenas
------------

Las cadenas no son más que texto encerrado entre comillas simples
(‘cadena’) o dobles (“cadena”). Dentro de las comillas se pueden añadir
caracteres especiales escapándolos con ‘\\’, como ‘\\n’, el carácter de
nueva línea, o ‘\\t’, el de tabulación.

Una cadena puede estar precedida por el carácter ‘u’ o el carácter ‘r’,
los cuales indican, respectivamente, que se trata de una cadena que
utiliza codificación Unicode y una cadena raw (del inglés, cruda). Las
cadenas raw se distinguen de las normales en que los caracteres
escapados mediante la barra invertida (\\) no se sustituyen por sus
contrapartidas. Esto es especialmente útil, por ejemplo, para las
expresiones regulares.

::

    unicode = u"äóè"
    raw = r"\n"

También es posible encerrar una cadena entre triples comillas (simples o
dobles). De esta forma podremos escribir el texto en varias líneas, y al
imprimir la cadena, se respetarán los saltos de línea que introdujimos
sin tener que recurrir al carácter \\n, así como las comillas sin tener
que escaparlas.

Las cadenas también admiten operadores como la suma (concatenación de
cadenas) y la multiplicación.

::

    a = "uno"
    b = "dos"

    c = a + b # c es "unodos"
    c = a * 3 # c es "unounouno"

Ejemplo de tipos de cadenas
...........................

.. literalinclude:: cadenas.py
    :linenos:
    :language: python

Tipos de booleanos
------------------

Como decíamos el tipo booleano sólo puede tener dos valores: True
(cierto) y False (falso). Estos valores son especialmente importantes
para las expresiones condicionales y los bucles, como veremos más
adelante.

En realidad el tipo bool (el tipo de los booleanos) es una subclase del
tipo int. Puede que esto no tenga mucho sentido para tí si no conoces
los términos de la orientación a objetos, que veremos más adelantes,
aunque tampoco es nada importante.


Ejemplo de tipos de booleanos
.............................

.. literalinclude:: booleanos.py
    :linenos:
    :language: python

Tipos de conjuntos
------------------

Un conjunto, es una colección no ordenada y sin elementos repetidos. 
Los usos básicos de éstos incluyen verificación de pertenencia y 
eliminación de entradas duplicadas.

Ejemplo de tipos de conjuntos
.............................

.. literalinclude:: conjuntos.py
    :linenos:
    :language: python

Tipos de listas
---------------

La lista en Python son variables que almacenan arrays, 
internamente cada posicion puede ser un tipo de datos distinto.

Ejemplo de tipos de listas
..........................

.. literalinclude:: listas.py
    :linenos:
    :language: python

Tipos de tuplas
---------------

Una tupla es una lista inmutable. Una tupla no puede 
modificarse de ningún modo después de su creación.

Ejemplo de tipos de tuplas
..........................

.. literalinclude:: tuplas.py
    :linenos:
    :language: python

Tipos de diccionarios
---------------------

El diccionario, que define una relación uno a uno entre
claves y valores.

Ejemplo de tipos de diccionarios
................................

.. literalinclude:: diccionarios.py
    :linenos:
    :language: python

Operadores aritméticos
----------------------

Los valores numéricos son además el resultado de  una serie
de operadores aritméticos y matemáticos:

+----------------+-------------------+---------------------------+
| **Operador**   | **Descripción**   | **Ejemplo**               |
+----------------+-------------------+---------------------------+
| +              | Suma              | r = 3 + 2 # r es 5        |
+----------------+-------------------+---------------------------+
| -              | Resta             | r = 4 – 7 # r es -3       |
+----------------+-------------------+---------------------------+
| -              | Negación          | r = -7 # r es -7          |
+----------------+-------------------+---------------------------+
| \*             | Multiplicación    | r = 2 \* 6 # r es 12      |
+----------------+-------------------+---------------------------+
| \*\*           | Exponente         | r = 2 \*\* 6 # r es 64    |
+----------------+-------------------+---------------------------+
| /              | División          | r = 3.5 / 2 # r es 1.75   |
+----------------+-------------------+---------------------------+
| //             | División entera   | r = 3.5 // 2 # r es 1.0   |
+----------------+-------------------+---------------------------+
| %              | Módulo            | r = 7 % 2 # r es 1        |
+----------------+-------------------+---------------------------+

Puede que tengáis dudas sobre cómo funciona el operador de módulo, y
cuál es la diferencia entre división y división entera.

El operador de módulo no hace otra cosa que devolvernos el resto de la
división entre los dos operandos. En el ejemplo, 7 / 2 sería 3, con 1 de
resto, luego el módulo es 1.

La diferencia entre división y división entera no es otra que la que
indica su nombre. En la división el resultado que se devuelve es un
número real, mientras que en la división entera el resultado que se
devuelve es solo la parte entera.

No obstante hay que tener en cuenta que si utilizamos dos operandos
enteros, Python determinará que queremos que la variable resultado
también sea un entero, por lo que el resultado de, por ejemplo, 3 / 2 y
3 // 2 sería el mismo: 1.

Si quisiéramos obtener los decimales necesitaríamos que al menos uno de
los operandos fuera un número real, bien indicando los decimales

::

    r = 3.0 / 2

o bien utilizando la función float (no es necesario que sepais lo que
significa el término función, ni que recordeis esta forma, lo veremos un
poco más adelante):

::

    r = float(3) / 2

Esto es así porque cuando se mezclan tipos de números, Python convierte
todos los operandos al tipo más complejo de entre los tipos de los
operandos.

Ejemplo de operadores numéricos
...............................

.. literalinclude:: operadores_numericos.py
    :linenos:
    :language: python

Operadores relacionales
-----------------------

Los valores booleanos son además el resultado de expresiones que
utilizan operadores relacionales (comparaciones entre valores):

+----------------+------------------------------+---------------------------+
| **Operador**   | **Descripción**              | **Ejemplo**               |
+----------------+------------------------------+---------------------------+
| ==             | ¿son iguales a y b?          | r = 5 == 3 # r es False   |
+----------------+------------------------------+---------------------------+
| !=             | ¿son distintos a y b?        | r = 5 != 3 # r es True    |
+----------------+------------------------------+---------------------------+
| <              | ¿es a menor que b?           | r = 5 < 3 # r es False    |
+----------------+------------------------------+---------------------------+
| >              | ¿es a mayor que b?           | r = 5 > 3 # r es True     |
+----------------+------------------------------+---------------------------+
| <=             | ¿es a menor o igual que b?   | r = 5 <= 5 # r es True    |
+----------------+------------------------------+---------------------------+
| >=             | ¿es a mayor o igual que b?   | r = 5 >= 3 # r es True    |
+----------------+------------------------------+---------------------------+

Ejemplo de operadores relacionales
...................................

.. literalinclude:: operadores_relacionales.py
    :linenos:
    :language: python

Vídeo tutorial
--------------

 - `Tutorial Python 4 - Enteros, reales y operadores aritméticos`_.

 - `Tutorial Python 5 - Booleanos, operadores lógicos y cadenas`_.

Referencia
----------

 - `Python - Tipos básicos`_.

.. _¿Qué es Python?: http://es.wikipedia.org/wiki/Python
.. _Características: http://es.wikipedia.org/wiki/Python#Caracter.C3.ADsticas_y_paradigmas
.. _¿Por qué Python?: http://es.wikipedia.org/wiki/Python#Filosof.C3.ADa
.. _Tutorial Python 4 - Enteros, reales y operadores aritméticos: https://www.youtube.com/watch?v=ssnkfbBbcuw
.. _Tutorial Python 5 - Booleanos, operadores lógicos y cadenas: https://www.youtube.com/watch?v=ZrxcqbFYjiw
.. _Python - Tipos básicos: http://mundogeek.net/archivos/2008/01/17/python-tipos-basicos/