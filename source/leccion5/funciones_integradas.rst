.. -*- coding: utf-8 -*-


.. _python_funciones_integradas:

Funciones integradas
--------------------


El interprete Python tiene un número de funciones integradas (built-in) dentro del 
módulo ``__builtins__``, las cuales están siempre disponibles. Ellas están listadas 
en orden alfabéticos a continuación:


.. todo:: TODO terminar de escribir esta sección.


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


De lo contrario, devuelve una lista alfabética de nombres que comprende 
(alguno(s) de) los atributos de un objeto dato, y de los atributos 
legibles desde este.

::

    >>> dir(__builtins__)
    ['ArithmeticError', 'AssertionError', 'AttributeError',
    'BaseException', 'BufferError', 'BytesWarning', 
    'DeprecationWarning', 'EOFError', 'Ellipsis', 
    'EnvironmentError', 'Exception', 'False', 'FloatingPointError',
    'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
    'ImportWarning', 'IndentationError', 'IndexError', 'KeyError',
    'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError',
    'None', 'NotImplemented', 'NotImplementedError', 'OSError', 
    'OverflowError', 'PendingDeprecationWarning', 'ReferenceError',
    'RuntimeError', 'RuntimeWarning', 'StandardError', 
    'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 
    'SystemExit', 'TabError', 'True', 'TypeError', 
    'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 
    'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 
    'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', 
    '_', '__debug__', '__doc__', '__import__', '__name__', 
    '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 
    'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 
    'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 
    'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod',
    'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter',
    'float', 'format', 'frozenset', 'getattr', 'globals', 
    'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 
    'intern', 'isinstance', 'issubclass', 'iter', 'len', 
    'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview',
    'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print',
    'property', 'quit', 'range', 'raw_input', 'reduce', 'reload',
    'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted',
    'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr',
    'unicode', 'vars', 'xrange', 'zip']

Si el objeto soporta un método llamado ``__dir__``, ese será usado; de lo contrario se usa 
la lógica ``dir()`` predeterminada y devuelve:

- para un objeto módulo: los atributos del módulo.

::

    >>> import os
    >>> type(os)
    <type 'module'>
    >>> dir(os)
    ['EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 
    'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 
    'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 
    'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 
    'F_OK', 'NGROUPS_MAX', 'O_APPEND', 'O_ASYNC', 'O_CREAT', 
    'O_DIRECT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_LARGEFILE', 
    'O_NDELAY', 'O_NOATIME', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 
    'O_RDONLY', 'O_RDWR', 'O_RSYNC', 'O_SYNC', 'O_TRUNC', 'O_WRONLY', 
    'P_NOWAIT', 'P_NOWAITO', 'P_WAIT', 'R_OK', 'SEEK_CUR', 'SEEK_END', 
    'SEEK_SET', 'ST_APPEND', 'ST_MANDLOCK', 'ST_NOATIME', 'ST_NODEV', 
    'ST_NODIRATIME', 'ST_NOEXEC', 'ST_NOSUID', 'ST_RDONLY', 
    'ST_RELATIME', 'ST_SYNCHRONOUS', 'ST_WRITE', 'TMP_MAX', 'UserDict', 
    'WCONTINUED', 'WCOREDUMP', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 
    'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WSTOPSIG', 'WTERMSIG', 
    'WUNTRACED', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', 
    '__doc__', '__file__', '__name__', 
    ...
    ...
    ... ]
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
    {'Persona': <class '__main__.Persona'>, '__builtins__': <module '__builtin__' (built-in)>, 
    '__package__': None, '__name__': '__main__', 
    'os': <module 'os' from '/usr/lib/python2.7/os.pyc'>, '__doc__': None}
    >>> dir(Persona)
    ['__class__', '__delattr__', '__dict__', '__doc__', 
    '__format__', '__getattribute__', '__hash__', 
    '__init__', '__module__', '__new__', '__reduce__', 
    '__reduce_ex__', '__repr__', '__setattr__', 
    '__sizeof__', '__str__', '__subclasshook__', 
    '__weakref__', 'hablar']
    >>> Persona.__dict__
    dict_proxy({'__module__': '__main__', 
    '__str__': <function __str__ at 0x7fab8aaad758>, 
    '__dict__': <attribute '__dict__' of 'Persona' objects>, 
    'hablar': <function hablar at 0x7fab8aaad7d0>, 
    '__weakref__': <attribute '__weakref__' of 'Persona' objects>, 
    '__doc__': ' Clase que representa una persona. ', 
    '__init__': <function __init__ at 0x7fab8aaad6e0>})
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
    ['__abs__', '__add__', '__and__', '__class__', '__cmp__', 
    '__coerce__', '__delattr__', '__div__', '__divmod__', 
    '__doc__', '__float__', '__floordiv__', '__format__', 
    '__getattribute__', '__getnewargs__', '__hash__', '__hex__', 
    '__index__', '__init__', '__int__', '__invert__', '__long__', 
    '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', 
    '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', 
    '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', 
    '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', 
    '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', 
    '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', 
    '__sizeof__', '__str__', '__sub__', '__subclasshook__', 
    '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 
    'denominator', 'imag', 'numerator', 'real']


.. _python_funcion_eval:

eval()
~~~~~~

Evalúa una cadena como una expresión: 

::

    >>> eval('2 + 5')
    7

Ademas si se han definido anteriormente variables las acepta como parámetros:

::

    >>> numero = 10
    >>> eval('numero * 10 - 5')
    95


.. _python_funcion_len:

len()
~~~~~

Devuelve el número de elementos de una secuencia o colección.

::

    >>> len("leonardo caballero")
    18


.. _python_funcion_help:

help()
~~~~~~

Invoca el menú de ayuda del intérprete de Python:

::

    >>> help()

    Welcome to Python 2.7!  This is the online help utility.

    If this is your first time using Python, you should definitely check out
    the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.

    Enter the name of any module, keyword, or topic to get help on writing
    Python programs and using Python modules.  To quit this help utility and
    return to the interpreter, just type "quit".

    To get a list of available modules, keywords, or topics, type "modules",
    "keywords", or "topics".  Each module also comes with a one-line summary
    of what it does; to list the modules whose summaries contain a given word
    such as "spam", type "modules spam".

    help> 


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

La función ``open()`` :ref:`abre un archivo <python_abrir_archivo>` usando 
el tipo ``file()``, devuelve un objeto del tipo :ref:`archivo <python_objeto_file>` 
(ej. *archivo*), y se llama habitualmente con de dos a tres argumentos: 

::

    file(nombre[, mode[, buffering]]) -> objeto archivo

Los argumentos son:

- ``nombre``, es una cadena de caracteres que indica el *nombre de archivo* 
  (incluso ruta relativa o absoluta).

- ``mode``, es una cadena de unos pocos caracteres describiendo la forma en 
  la que se usará el archivo, como se indica a continuación:

  +----------+-----------------------------------------------------------+
  | **Modo** | **Notas**                                                 |
  +----------+-----------------------------------------------------------+
  | ``r``    | el archivo se abre en modo de solo lectura, no se puede   |
  |          | escribir (argumento por defecto).                         |
  +----------+-----------------------------------------------------------+
  | ``w``    | modo de solo escritura (si existe un archivo con el mismo |
  |          | nombre, se borra).                                        |
  +----------+-----------------------------------------------------------+
  | ``a``    | modo de agregado (``append``), los datos escritos se      |
  |          | agregan al final del archivo.                             |
  +----------+-----------------------------------------------------------+
  | ``r+``   | el archivo se abre para lectura y escritura al mismo      |
  |          | tiempo.                                                   |
  +----------+-----------------------------------------------------------+
  | ``b``    | el archivo se abre en modo binario, para almacenar        |
  |          | cualquier cosa que no sea texto.                          |
  +----------+-----------------------------------------------------------+
  | ``U``    | el archivo se abre con soporte a nueva linea universal,   |
  |          | cualquier fin de linea ingresada sera como un ``\n`` en   |
  |          | Python.                                                   |
  +----------+-----------------------------------------------------------+

- ``buffering``, si este argumento es dado, 0 significa sin búfer, 1 significa búfer 
  de línea y los números más grandes especifican el tamaño del búfer.

Para crear y abrir un archivo, seria así:

::

    >>> f = open('datos.txt', 'w')
    >>> type(f)
    <type 'file'>


El archivo será creado si no existe cuando es abierto para escribir 
o agregar data. Es archivo sera truncado cuando es abierto para escritura. 

Agregue una 'U' a modo para abrir el archivo para la entrada con soporte de 
nueva línea universal. Cualquier línea que termine en el archivo de entrada 
se verá como '\n' en Python. Además, un archivo así abierto gana el atributo 
``newlines``; el valor para este atributo es uno de Ninguno (aún no se ha 
leído una nueva línea), ``\r``, ``\n``, ``\r\n`` o una tupla que contiene 
todos los tipos de nueva línea que se han visto.


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

Lee una cadena de caracteres desde la entrada estándar. La nueva línea final 
es despojada. Si el usuario indica un EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), 
lanza una excepción :ref:`EOFError <python_exception_eoferror>`. En sistemas 
Unix, la librería GNU readline es usada si es habilitada.  El prompt de la 
cadena de caracteres, si es dado, es impreso sin una nueva línea final antes 
de leer.

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


.. _python_funcion_bin:

bin()
~~~~~

Devuelve una representación binaria de un numero entero o entero long, 
es decir, lo convierte de entero a binario.

::

    >>> bin(10)
    '0b1010'

.. _python_funcion_divmod:

divmod()
~~~~~~~~

Debe recibir dos argumentos numéricos, y devuelve dos valores: resultado de 
la división entera, y el resto.

::

    >>> divmod(22, 4)
    (5, 2)
    >>> 


.. _python_funcion_hex:

hex()
~~~~~

Devuelve una representación hexadecimal de un numero entero o entero long, 
es decir, lo convierte de entero a hexadecimal.

::

    >>> hex(10)
    '0xa'


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


.. _python_funcion_round:

round()
~~~~~~~

Redondea un numero flotante a una precisión dada en dígitos decimal (por 
defecto 0 dígitos). Esto siempre devuelve un numero flotante. La precisión 
tal vez sea negativa.

En el siguiente ejemplo redondeo de un numero flotante a entero, mayor o igual 
a *.5* al alza:

::

    >>> round(5.5)
    6.0
    >>> 

En este otro ejemplo redondeo de un numero flotante a entero, menor de *.5* a 
la baja:

::

    >>> round(5.4)
    5.0
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
todos los caracteres ``tab`` (tabulación) son remplazados por uno o más espacios, 
depende en la actual columna y el tamaño del tab dado.

::

    >>> 'Leonardo Caballero\tPython Developer\tleonardoc@plone.org'.expandtabs()
    'Leonardo Caballero      Python Developer        leonardoc@plone.org'

Usted puede indicar el tamaño de la tecla ``tab`` vía parámetro de la función:

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

La función integrada ``format()`` devuelve una representación formateada de un valor 
dato controlado por el especificador de formato.

La función integrada ``format()`` es similar al :ref:`método format() <python_metodo_format>` 
disponible en el tipo de :ref:`cadena de caracteres <python_cadenas>`. Internamente, 
ambos llaman al método ``__format__()`` de un objecto.

Mientras, la función integrada ``format()`` es una implementación de bajo nivel para 
formatear un objeto usando ``__format__()`` internamente, el 
:ref:`método format() <python_metodo_format>` del tipo de cadena de caracteres es una 
implementación de alto nivel disponible para ejecutar operaciones de formateo complejas 
en múltiples objeto de :ref:`cadena de caracteres <python_cadenas>`.

La sintaxis de la función integrada ``format()`` es:

::

    format(value[, format_spec])

La a función integrada ``format()`` toma dos parámetros:

- value - valor que necesita formatear.

- format_spec - La especificación en como el valor debe ser formateado.

A continuación, un ejemplo de un valor :ref:`número entero <python_num_entero>`, 
seria de la siguiente forma:

::

    >>> print format(123,"d")
    123

A continuación, un ejemplo de un valor :ref:`número float <python_coma_flotante>`, 
seria de la siguiente forma:

::

    >>> print format(123.456789,"f")
    123.456789

A continuación, un ejemplo de un valor binario, seria de la siguiente forma:

::

    >>> print format(10,"b")
    1010


A continuación, un ejemplo de un valor :ref:`número entero <python_num_entero>` 
con formato especifico, seria de la siguiente forma:

::

    >>> print format(1234,"*>+7,d")
    *+1,234

En el ejemplo anterior cuando se formatea el :ref:`número entero <python_num_entero>` 
*1234*, usted especifico el especificador de formato ``*<+7,d``. Seguidamente, se 
describe cada opción a continuación:

- ``*`` Es la opción del carácter de relleno, el cual rellena los espacio vacío después 
  del formato.
- ``>`` Es la opción de alineación a la derecha, el cual alinea la cadena de caracteres 
  de salida a la derecha.
- ``+`` Es la opción de signo, el cual obliga al número a ser firmado (con un signo a 
  su izquierda).
- ``7`` Es la opción ancho, el cual obliga el número que tome un mínimo de ancho de 7, 
  otros espacios serán rellenado por el carácter de relleno.
- ``,`` Ese es el operador miles, el cual coloca un carácter coma entre todos los números 
  miles.
- ``d`` Es la opción tipo que especifica que el número es un 
  :ref:`número entero <python_num_entero>`.

A continuación, un ejemplo de un valor :ref:`número float <python_coma_flotante>` 
con formato especifico, seria de la siguiente forma:

::

    >>> print format(123.4567, "^-09.3f")
    0123.4570

En el ejemplo anterior cuando se formatea el :ref:`número float <python_coma_flotante>` 
*123.4567*, usted especifico el especificador de formato ``^-09.3f``. Seguidamente, se 
describe cada opción a continuación:

- ``^`` Es la opción de alineación centrar, el cual alinea la cadena de 
  caracteres de salida al centro del espacio restante. 
- ``-`` Es la opción de signo el cual obliga solo a los números negativos a mostrar el signo.
- ``0`` Ese es el carácter, el cual es colocado en lugar de los espacios vacíos.
- ``9`` Es la opción de ancho, el cual establece el ancho mínimo del número en 9 
  (incluido el punto decimal, la coma y el signo de miles).
- ``.3`` Ese es el operador de precisión que define la precisión del número 
  flotante dado a 3 lugares.
- ``f`` Es la opción tipo que especifica que el número es un 
  :ref:`número float <python_coma_flotante>`.

A continuación, un ejemplo de usar la función ``format()`` sobre escribiendo el método 
especial ``__format__()`` de una :ref:`clase <python_metodos_especiales>`, seria de la 
siguiente forma:

::

    >>> class Persona:
    ...     def __format__(self, formato):
    ...         if(formato == 'edad'):
    ...             return '23'
    ...         return 'Formato nulo'
    ... 
    >>> print format(Persona(), "edad")
    23

En el ejemplo anterior cuando se sobre escribe el método especial ``__format__()`` de 
la clase ``Persona``. Ese ahora acepta el argumento del método llamado ``edad`` el 
cual devuelve *23*. 

El método ``format()`` internamente ejecuta ``Persona().__format__("edad")``, el cual 
devuelve el mensaje *23*. Si no hay formato especificado, el mensaje devuelto es 
*Formato nulo*. 


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


.. _python_funcion_lstrip:

lstrip()
~~~~~~~~

La función ``lstrip()`` devuelve una copia de la cadena de caracteres con 
todos los espacios al inicio removido. Si la cadena de caracteres es dada 
y no es :ref:`None <python_objeto_none>`, remove characters in chars instead. 
Si la cadena de caracteres es ``unicode``, la cadena de caracteres serán 
convertidas a ``unicode`` antes de before stripping.

::

    >>> "leonardo caballero ".lstrip()
    'leonardo caballero '


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

