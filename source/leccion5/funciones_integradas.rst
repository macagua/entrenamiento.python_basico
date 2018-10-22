.. -*- coding: utf-8 -*-


.. _python_funciones_integradas:

Funciones integradas (built-in)
-------------------------------


El interprete Python tiene un número de funciones integradas dentro de el 
que están siempre disponibles. Ellas están listadas en orden alfabéticos 
a continuación:


.. todo:: TODO escribir esta sección.


----

.. _python_funciones_integradas_es:

Funciones de entrada y salida
.............................

Las funciones de tipos numéricos se describen a continuación:


.. _python_funcion_input:

input()
~~~~~~~

Equivalente a la función ``eval(raw_input(prompt))``

Lee una cadena de caracteres desde la entrada estándar.

::

    >>> dato = input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: 2
    2
    <type 'int'>
    >>> dato = input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: 23.4
    23.4
    <type 'float'>
    >>> dato = input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: 23L
    23L
    <type 'long'>


En el caso que quiera ingresar una cadena de caracteres desde la entrada 
estándar usando la función ``input()``, debe colocar la cadena de caracteres 
entre comillas simples o dobles, como el siguiente ejemplo:

::

    >>> dato = input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: leonardo
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<string>", line 1, in <module>
    NameError: name 'leonardo' is not defined
    >>> dato = input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: "leonardo"
    'leonardo'
    <type 'str'>
    >>> dato = input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: leonardo caballero
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<string>", line 1
        leonardo caballero
                         ^
    SyntaxError: unexpected EOF while parsing
    >>> dato = input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: "leonardo caballero"
    'leonardo caballero'
    <type 'str'>


.. _python_funcion_raw_input:

raw_input()
~~~~~~~~~~~

Lee una cadena de caracteres desde la entrada estándar.

::

    >>> dato = raw_input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: 2
    '2'
    <type 'str'>
    >>> dato = raw_input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: 2.3
    '2.3'
    <type 'str'>
    >>> dato = raw_input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: 23L
    '23L'
    <type 'str'>
    >>> dato = raw_input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: leonardo
    'leonardo'
    <type 'str'>
    >>> dato = raw_input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: "leonardo"
    '"leonardo"'
    <type 'str'>
    >>> dato = raw_input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: leonardo caballero
    'leonardo caballero'
    <type 'str'>
    >>> dato = raw_input("Por favor, ingresa un dato: "); dato; type(dato)
    Por favor, ingresa un dato: "leonardo caballero"
    '"leonardo caballero"'
    <type 'str'>


----

.. _python_funciones_integradas_numericas:

Funciones de numéricas
......................

Las funciones de tipos numéricos se describen a continuación:


.. _python_funcion_abs:

abs()
~~~~~

Devuelve el valor absoluto de un número (entero o de coma flotante).

::

    >>> abs(3)
    3
    >>> abs(-3)
    3
    >>> abs(-2.5)
    2.5
    >>> 


.. _python_funcion_divmod:

divmod()
~~~~~~~~

Debe recibir dos argumentos numéricos, y devuelve dos valores: resultado de 
la división entera, y el resto.

::

    >>> divmod(22, 4)
    (5, 2)
    >>> 


.. _python_funcion_max:

max()
~~~~~

Si recibe más de un argumento, devuelve el mayor de ellos.

::

    >>> max(23, 12, 145, 88)
    145
    >>> type(max(23, 12, 145, 88))
    <type 'int'>
    >>> max("a", "Z")
    'a'
    >>> type(max("a", "Z"))
    <type 'str'>
    >>> 


Si recibe un solo argumento, devuelve el mayor de sus elementos. Debe ser un objeto 
iterable; puede ser una cadena de caracteres, o alguno de los otros tipos de secuencia 
o colección.

::

    >>> max("Hola, Python")
    'y'
    >>> type(max("Hola, Python"))
    <type 'str'>
    >>> 


.. _python_funcion_min:

min()
~~~~~

Tiene un comportamiento similar a ``max()``, pero devuelve el mínimo.

::

    >>> min(23, 12, 145, 88)
    12
    >>> type(min(23, 12, 145, 88))
    <type 'int'>
    >>> min("Hola, Python")
    ' '
    >>> type(min("Hola, Python"))
    <type 'str'>
    >>> 


----

.. _python_funciones_integradas_cadenas:

Funciones de cadenas de caracteres
..................................

Las funciones de tipos cadenas de caracteres se describen a continuación:


.. _python_funcion_capitalize:

capitalize()
~~~~~~~~~~~~

La función ``capitalize()`` devuelve una cadenas de caracteres con MAYÚSCULA 
la primera palabra. 

::

    >>> 'leonardo caballero'.capitalize()
    'Leonardo caballero'


.. _python_funcion_endswith:

endswith()
~~~~~~~~~~

La función ``endswith()`` devuelve un valor booleano ``True`` o ``False`` 
si coincide que la cadena termine con el criterio enviado por parámetros 
en la función.

::

    >>> 'leonardo caballero'.endswith("do")
    False
    >>> 'leonardo caballero'.endswith("ro")
    True


.. _python_funcion_expandtabs:

expandtabs()
~~~~~~~~~~~~

La función ``expandtabs()`` devuelve una copia de la cadenas de caracteres donde 
todos los caracteres tab (tabulación) son remplazados por uno o más espacios, 
depende en la actual columna y el tamaño del tab dado.

::

    >>> 'Leonardo Caballero\tPython Developer\tleonardoc@plone.org'.expandtabs()
    'Leonardo Caballero      Python Developer        leonardoc@plone.org'

Usted puede indicar el tamaño del tab vía parámetro de la función:

::

    >>> 'Leonardo Caballero\tPython Developer\tleonardoc@plone.org'.expandtabs(4)
    'Leonardo Caballero  Python Developer    leonardoc@plone.org'
    >>> 'Leonardo Caballero\tPython Developer\tleonardoc@plone.org'.expandtabs(2)
    'Leonardo Caballero  Python Developer  leonardoc@plone.org'


.. _python_funcion_find:

find()
~~~~~~

La función ``find()`` devuelve un valor numérico ``0`` si encuentra el criterio 
de búsqueda o ``-1`` si no coincide el criterio de búsqueda enviado por parámetros 
en la función.

::

    >>> 'leonardo caballero'.find("leo")
    0
    >>> 'leonardo caballero'.find("ana")
    -1

.. _python_funcion_format:

format()
~~~~~~~~

La función ``format()`` devuelve una versión formateada, usando sustituciones desde 
``args`` y ``kwargs``. Las sustituciones son identificado por caracteres llaves 
('{' y '}').

::

    >>> nombre = "leonardo"
    >>> apellido = "caballero"
    >>> "Nombre: {0} {1}".format(nombre, apellido)
    'Nombre: leonardo caballero'


.. _python_funcion_index:

index()
~~~~~~~

La función ``index()`` es como la función ``find()`` pero arroja el error ``ValueError`` 
cuando la sub-cadena no es encontrada.

::

    >>> 'leonardo caballero'.index("leo")
    0
    >>> 'leonardo caballero'.index("ana")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: substring not found
    >>> 'leonardo caballero'.index(" ca")
    8


.. _python_funcion_isalnum:

isalnum()
~~~~~~~~~

La función ``isalnum()`` devuelve un valor booleano ``True`` o ``False`` 
si coincide que la cadena contenga caracteres alfanuméricos.

::

    >>> '23456987'.isalnum()
    True
    >>> 'V-23456987'.isalnum()
    False


.. _python_funcion_isalpha:

isalpha()
~~~~~~~~~

La función ``isalpha()`` devuelve un valor booleano ``True`` o ``False`` 
si coincide que la cadena contenga caracteres alfabéticos.

::

    >>> 'leonardo'.isalpha()
    True
    >>> 'leonardo caballero'.isalpha()
    False


.. _python_funcion_isdigit:

isdigit()
~~~~~~~~~

La función ``isdigit()`` devuelve un valor booleano ``True`` o ``False`` 
si coincide que la cadena contenga caracteres dígitos.


::

    >>> 'leonardo caballero'.isdigit()
    False
    >>> '23456987'.isdigit()
    True


.. _python_funcion_islower:

islower()
~~~~~~~~~

La función ``islower()`` devuelve un valor booleano ``True`` o ``False`` 
si coincide que la cadena contenga caracteres en MINÚSCULAS.

::

    >>> 'leonardo caballero'.islower()
    True
    >>> 'leonardo CABALLERO'.islower()
    False


.. _python_funcion_istitle:

istitle()
~~~~~~~~~

La función ``istitle()`` devuelve un valor booleano ``True`` o ``False`` 
si coincide que la cadenas de caracteres sean capitales en cada palabra. 

::

    >>> "leonardo caballero".title()
    'Leonardo Caballero'
    >>> "leonardo Caballero".istitle()
    False


.. _python_funcion_isspace:

isspace()
~~~~~~~~~

La función ``isspace()`` devuelve un valor booleano ``True`` o ``False`` 
si no es vacía, y todos sus caracteres son espacios en blanco.

::

    >>> " ".isspace()
    True
    >>> "  ".isspace()
    True
    >>> "a ".isspace()
    False
    >>> " A ".isspace()
    False


.. _python_funcion_isupper:

isupper()
~~~~~~~~~

La función ``isupper()`` devuelve un valor booleano ``True`` o ``False`` 
si coincide que la cadenas de caracteres estén en MAYÚSCULAS en cada palabra. 

::

    >>> 'LEONARDO CABALLERO'.isupper()
    True
    >>> 'LEONARDO caballero'.isupper()
    False


.. _python_funcion_lower:

lower()
~~~~~~~

La función ``lower()`` devuelve una cadenas de caracteres con MINÚSCULAS 
en cada palabra. 

::

    >>> 'LEONARDO CABALLERO'.lower()
    'leonardo caballero'


.. _python_funcion_replace:

replace()
~~~~~~~~~

La función ``replace()`` si encuentra el criterio de la búsqueda de la 
sub-cadena o la remplaza con la nueva sub-cadena enviado por parámetros 
en la función.

::

    >>> 'leonardo caballero'.replace(" cab", " Cab")
    'leonardo Caballero'


.. _python_funcion_split:

split()
~~~~~~~

La función ``split()`` devuelve una lista con la cadenas de caracteres separada 
por cada indice de la lista. 

::

    >>> 'leonardo caballero'.split()
    ['leonardo', 'caballero']


.. _python_funcion_splitlines:

splitlines()
~~~~~~~~~~~~

La función ``splitlines()`` devuelve una lista con la cadenas de caracteres separada 
por cada salto de linea en cada indice de la lista.

::

    >>> 'leonardo jose\ncaballero garcia'.splitlines()
    ['leonardo jose', 'caballero garcia']


.. _python_funcion_startswith:

startswith()
~~~~~~~~~~~~

La función ``startswith()`` devuelve un valor booleano ``True`` o ``False`` 
si coincide que la cadena inicie con el criterio enviado por parámetros 
en la función.

::

    >>> 'leonardo caballero'.startswith("ca")
    False
    >>> 'leonardo caballero'.startswith("leo")
    True


.. _python_funcion_swapcase:

swapcase()
~~~~~~~~~~

La función ``swapcase()`` devuelve una cadenas de caracteres convertida al opuesto 
sea MAYÚSCULAS o MINÚSCULAS.

::

    >>> 'leonardo caballero'.swapcase()
    'LEONARDO CABALLERO'
    >>> 'LEONARDO CABALLERO'.swapcase()
    'leonardo caballero'
    >>> 


.. _python_funcion_title:

title()
~~~~~~~

La función ``title()`` devuelve una cadenas de caracteres con capitales 
en cada palabra. 

::

    >>> "leonardo caballero".title()
    'Leonardo Caballero'


.. _python_funcion_upper:

upper()
~~~~~~~

La función ``upper()`` devuelve una cadenas de caracteres con MAYÚSCULAS 
en cada palabra. 

::

    >>> "leonardo caballero".upper()
    'LEONARDO CABALLERO'

