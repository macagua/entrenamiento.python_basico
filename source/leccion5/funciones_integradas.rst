.. -*- coding: utf-8 -*-


.. _python_funciones_integradas:

Funciones integradas (built-in)
-------------------------------


El interprete Python tiene un número de funciones integradas dentro de el 
que están siempre disponibles. Ellas están listadas en orden alfabéticos 
a continuación:


.. todo:: TODO escribir esta sección.


----

.. _python_funciones_generales:

Funciones generales
...................

Las funciones de uso general se describen a continuación:


.. _python_funcion_credits:

credits()
~~~~~~~~~

Imprime el texto de la lista de contribuidores.

::

    >>> credits()
        Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
        for supporting Python development.  See www.python.org for more information.


.. _python_funcion_copyright:

copyright()
~~~~~~~~~~~

Imprime el texto de la nota de copyright.

::

    >>> copyright()
    Copyright (c) 2001-2016 Python Software Foundation.
    All Rights Reserved.

    Copyright (c) 2000 BeOpen.com.
    All Rights Reserved.

    Copyright (c) 1995-2001 Corporation for National Research Initiatives.
    All Rights Reserved.

    Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
    All Rights Reserved.


.. _python_funcion_dir:

dir()
~~~~~

Si es llamado sin argumentos, devuelve los nombres en el ámbito actual.

::

    >>> dir()
    ['__builtins__', '__doc__', '__name__', '__package__']
    >>> 


De lo contrario, devuelve una lista alfabética de nombres comprising 
(alguno(s) de) los atributos de un objeto dato, y de los atributos 
legibles desde este.

::

    >>> dir(__builtins__)
    ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']

Si el objeto soporta un método llamado ``__dir__``, ese será usado; otherwise
the default ``dir()`` logic is used y devuelve:

- para un objeto módulo: los atributos del módulo.

::

    >>> import os
    >>> type(os)
    <type 'module'>
    >>> dir(os)
    ['EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 'F_OK', 'NGROUPS_MAX', 'O_APPEND', 'O_ASYNC', 'O_CREAT', 'O_DIRECT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_LARGEFILE', 'O_NDELAY', 'O_NOATIME', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_RDONLY', 'O_RDWR', 'O_RSYNC', 'O_SYNC', 'O_TRUNC', 'O_WRONLY', 'P_NOWAIT', 'P_NOWAITO', 'P_WAIT', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'ST_APPEND', 'ST_MANDLOCK', 'ST_NOATIME', 'ST_NODEV', 'ST_NODIRATIME', 'ST_NOEXEC', 'ST_NOSUID', 'ST_RDONLY', 'ST_RELATIME', 'ST_SYNCHRONOUS', 'ST_WRITE', 'TMP_MAX', 'UserDict', 'WCONTINUED', 'WCOREDUMP', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__doc__', '__file__', '__name__', 
    ...
    ...
    ... ]
    >>>
    >>> os.__doc__
    "OS routines for NT or Posix depending on what system we're on.\n\nThis exports:\n  - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.\n  - os.path is one of the modules posixpath, or ntpath\n  - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'\n  - os.curdir is a string representing the current directory ('.' or ':')\n  - os.pardir is a string representing the parent directory ('..' or '::')\n  - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\\\')\n
    ...
    ...
    ...
    >>> 
    >>> print os.__doc__
    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
      - os.path is one of the modules posixpath, or ntpath
      - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
      - os.curdir is a string representing the current directory ('.' or ':')
      - os.pardir is a string representing the parent directory ('..' or '::')
      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
    ...
    ...
    ...
    >>> 

- para un objeto clase: sus atributos, y recursivamente los atributos
  de sus clases bases.

::

    >>> class Persona(object):
    ...     """ Clase que representa una persona. """
    ...     def __init__(self, cedula, nombre, apellido, sexo):
    ...         """ Constructor de clase Persona """
    ...         self.cedula = cedula
    ...         self.nombre = nombre
    ...         self.apellido = apellido
    ...         self.sexo = sexo
    ...     def __str__(self):
    ...         """ Devuelve una cadena representativa al Persona """
    ...         return "%s: %s %s, %s." % (
    ...             str(self.cedula), self.nombre,
    ...             self.apellido, self.sexo
    ...         )
    ...     def hablar(self, mensaje):
    ...         """ Mostrar mensaje de saludo de Persona """
    ...         print mensaje
    ... 
    >>> type(Persona)
    <type 'type'>
    >>> vars()
    {'Persona': <class '__main__.Persona'>, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', 'os': <module 'os' from '/usr/lib/python2.7/os.pyc'>, '__doc__': None}
    >>> dir(Persona)
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'hablar']
    >>> Persona.__dict__
    dict_proxy({'__module__': '__main__', '__str__': <function __str__ at 0x7fab8aaad758>, '__dict__': <attribute '__dict__' of 'Persona' objects>, 'hablar': <function hablar at 0x7fab8aaad7d0>, '__weakref__': <attribute '__weakref__' of 'Persona' objects>, '__doc__': ' Clase que representa una persona. ', '__init__': <function __init__ at 0x7fab8aaad6e0>})
    >>> Persona.__doc__
    ' Clase que representa una persona. '
    >>> Persona.__init__.__doc__
    ' Constructor de clase Persona '
    >>> Persona.hablar.__doc__
    ' Mostrar mensaje de saludo de Persona '

- para cualquier otro objecto: sus atributos, sus atributos de clases, y
  recursivamente los atributos de esas clases bases de las clases.

::

    >>> type(int)
    <type 'type'>
    >>> dir(int)
    ['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']


.. _python_funcion_len:

len()
~~~~~

Devuelve el numero de elementos de una secuencia o colección.

::

    >>> len("leonardo caballero")
    18


.. _python_funcion_license:

license()
~~~~~~~~~

Imprime el texto de la licencia.

::

    >>> license
    Type license() to see the full license text
    >>> license()
    A. HISTORY OF THE SOFTWARE
    ==========================

    Python was created in the early 1990s by Guido van Rossum at Stichting
    Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
    as a successor of a language called ABC.  Guido remains Python's
    principal author, although it includes many contributions from others.

    In 1995, Guido continued his work on Python at the Corporation for
    National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)
    in Reston, Virginia where he released several versions of the
    software.

    In May 2000, Guido and the Python core development team moved to
    BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
    year, the PythonLabs team moved to Digital Creations (now Zope
    Corporation, see http://www.zope.com).  In 2001, the Python Software
    Foundation (PSF, see http://www.python.org/psf/) was formed, a
    non-profit organization created specifically to own Python-related
    Intellectual Property.  Zope Corporation is a sponsoring member of
    the PSF.

    All Python releases are Open Source (see http://www.opensource.org for
    Hit Return for more, or q (and Return) to quit: 


.. _python_funcion_open:

open()
~~~~~~

La función ``open()`` abre un archivo usando el tipo ``file()``, devuelve 
un objeto del tipo :ref:`file <python_objeto_file>` (ej. *archivo*), y se 
invoca habitualmente con de dos a tres argumentos: 

::

    file(nombre[, mode[, buffering]]) -> objeto archivo

Los argumentos son:

- ``nombre``, es una cadena de caracteres que indica el *nombre de archivo* 
  (incluso ruta relativa o absoluta).

- ``mode``, es una cadena de unos pocos caracteres describiendo la forma en 
  la que se usará el archivo, como se indica a continuación:

  +----------+-------------------------------------------------------------------------------------------+
  | **Modo** | **Notas**                                                                                 |
  +----------+-------------------------------------------------------------------------------------------+
  | ``r``    | el archivo se abre en modo de solo lectura, no se puede escribir (argumento por defecto). |
  +----------+-------------------------------------------------------------------------------------------+
  | ``w``    | modo de solo escritura (si existe un archivo con el mismo nombre, se borra).              |
  +----------+-------------------------------------------------------------------------------------------+
  | ``a``    | modo de agregado (``append``), los datos escritos se agregan al final del archivo.        |
  +----------+-------------------------------------------------------------------------------------------+
  | ``r+``   | el archivo se abre para lectura y escritura al mismo tiempo.                              |
  +----------+-------------------------------------------------------------------------------------------+
  | ``b``    | el archivo se abre en modo binario, para almacenar cualquier cosa que no sea texto.       |
  +----------+-------------------------------------------------------------------------------------------+
  | ``U``    | el archivo se abre con soporte a nueva linea universal, cualquier fin de linea ingresada  |
  |          | sera como un ``\n`` en Python.                                                            |
  +----------+-------------------------------------------------------------------------------------------+


- ``buffering``, si este argumento es dado, 0 significa unbuffered, 1 significa 
  linea buffered y números grande especifico el tamaño del buffer. 
  If the buffering argument is given, 0 means unbuffered, 1 means line
  buffered, and larger numbers specify the buffer size.

Para crear en un archivo:

::

    >>> f = open('datos.txt', 'w') # abre el archivo datos.txt
    >>> type(f)
    <type 'file'>


El archivo será creado si no existe cuando es abierto para escribir 
o agregar data. Es archivo sera truncated cuando es abierto para escritura. 

Add a 'U' to modo to open the file for input with universal newline
support.  Any line ending in the input file will be seen as a '\n'
in Python.  Also, a file so opened gains the attribute 'newlines';
the value for this attribute is one of None (no newline read yet),
'\r', '\n', '\r\n' or a tuple containing all the newline types seen.


.. tip::

    Ver para futura información desde el :ref:`modo interactivo <python_interactivo>` 
    Python, lo siguiente:

    ::

        >>> file.__doc__


.. _python_funcion_range:

range()
~~~~~~~

Devuelve una lista conteniendo una progresión aritmética de enteros.

range(inicio, detener[, paso]) -> lista de enteros

    ::

        >>> range(3,9)
        [3, 4, 5, 6, 7, 8]

``range(i, j)`` devuelve ``[i, i+1, i+2, ..., j-1]``; inicia (!) por defecto en **0**.

Cuando el ``paso`` es definido como un tercer argumento, ese especifica el incremento 
(o decremento).

    ::

        >>> range(3,9,2)
        [3, 5, 7]

En el ejemplo anterior, la función ``range(3,9,2)`` devuelve **[3, 5, 7]**, es decir, 
el rango inicia en **3** y termina en **9** incrementando cada **2** números.

range(detener) -> lista de enteros

    ::

        >>> range(4)
        [0, 1, 2, 3]

En el ejemplo anterior, la función ``range(4)`` devuelve **[0, 1, 2, 3]**. ¡El punto 
final es omitido! Hay exactamente los indices validos para una lista de **4** elementos.


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


.. tip:: Para mayor información consulte la sección :ref:`format() <python_funcion_format_detalle>` detallada.


.. _python_funcion_index:

index()
~~~~~~~

La función ``index()`` es como la función ``find()`` pero arroja una excepción 
:ref:`ValueError <python_exception_valueerror>` cuando la sub-cadena no es encontrada.

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

