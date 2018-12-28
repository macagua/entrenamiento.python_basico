.. -*- coding: utf-8 -*-


.. _python_fun_builtins:

Funciones integradas
--------------------


El interprete Python tiene un número de funciones integradas (built-in) dentro del 
módulo ``__builtins__``, las cuales están siempre disponibles. Estas funciones están 
listadas en orden alfabéticos a continuación:


.. _python_fun_builtins_generales:

Funciones generales
...................

Las funciones de uso general se describen a continuación:


.. _python_fun_apply:

apply()
~~~~~~~

La función ``apply()`` devuelve el resultado de una función o objeto clase llamado 
con argumentos soportados.

::

    >>> def demo(valor1, valor2, valor3=None):
    ...     return valor1, valor2, valor3
    ... 
    >>> apply(demo, (1, 2), {'valor3': 3})
    (1, 2, 3)


.. _python_fun_callable:

callable()
~~~~~~~~~~

La función ``callable()`` le indica si un objecto puede ser llamado.

::

    >>> callable([1,2,3])
    False
    >>> callable(callable)
    True
    >>> callable(False)
    False
    >>> callable(list)
    True

Una función se puede llamar, una lista no se puede llamar. Incluso la función integrada 
``callable()`` se puede llamar.


.. _python_fun_compile:

compile()
~~~~~~~~~

La función ``compile()`` devuelve un código objeto Python. Usted usa la función 
integrada Python para convertir de la cadena de caracteres de código al código 
objeto.

::

    >>>
    >>> exec(compile('a=5\nb=7\nprint a+b','','exec'))
    12

Aquí, ``exec`` es el modo. El parámetro anterior que eso es el nombre del archivo 
para la forma del archivo el cual el código es leído. Finalmente, es ejecutado 
usando la función ``exec()``.


.. _python_fun_credits:

credits()
~~~~~~~~~

Imprime el texto de la lista de contribuidores.

::

    >>> credits()
        Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
        for supporting Python development.  See www.python.org for more information.


.. _python_fun_copyright:

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


.. _python_fun_dir:

dir()
~~~~~

Si es llamado sin argumentos, devuelve los nombres en el ámbito actual.

::

    >>> dir()
    ['__builtins__', '__doc__', '__name__', '__package__']


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
    ...     """Clase que representa una Persona"""
    ...     def __init__(self, cedula, nombre, apellido, sexo):
    ...         """ Constructor de clase Persona """
    ...         self.cedula = cedula
    ...         self.nombre = nombre
    ...         self.apellido = apellido
    ...         self.sexo = sexo
    ...     def __str__(self):
    ...         """Devuelve una cadena representativa al Persona"""
    ...         return "%s: %s %s, %s." % (
    ...             str(self.cedula), self.nombre,
    ...             self.apellido, self.sexo
    ...         )
    ...     def hablar(self, mensaje):
    ...         """Mostrar mensaje de saludo de Persona"""
    ...         print mensaje
    ... 
    >>> type(Persona)
    <type 'type'>
    >>> vars()
    {'Persona': <class '__main__.Persona'>, 
    '__builtins__': <module '__builtin__' (built-in)>, 
    '__package__': None, '__name__': '__main__', 
    'os': <module 'os' from '/usr/lib/python2.7/os.pyc'>, 
    '__doc__': None}
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
    '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', 
    '__setattr__', '__sizeof__', '__str__', '__sub__', 
    '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 
    'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 
    'real']


.. _python_fun_eval:

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


.. _python_fun_execfile:

execfile()
~~~~~~~~~~

La función ``execfile()`` lee y ejecuta un script Python desde un archivo. Los 
``globals`` y ``locals`` son diccionarios, por defecto a los actuales  ``globals`` 
y ``locals``.  Si solamente ``globals`` es dado, ``locals`` es por defecto a la 
misma.

::

    >>> execfile('./holamundo.py')
    Hola Mundo


.. _python_fun_globals:

globals()
~~~~~~~~~

La función ``globals()`` devuelve un diccionario conteniendo ámbito actual global de 
las variables.

::

    >>> globals()
    {'__builtins__': <module '__builtin__' (built-in)>, 
    '__package__': None, '__name__': '__main__', '__doc__': None}


La función ``globals()`` puede ser usada para devolver los nombres en el ``namespaces`` 
global dependiendo en la locación desde donde ella es llamada.

Si la función ``globals()`` es llamada desde una función, eso devolverá todos los nombres 
que pueden ser accesibles globalmente desde esa función.

El tipo de dato devuelto por función es un tipo diccionario. Por lo tanto, los nombres 
pueden ser extraídos usando la función integrada ``keys()``.


.. _python_fun_help:

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


.. _python_fun_id:

id()
~~~~

La función ``id()`` devuelve la identidad de un objecto. Esto garantiza ser el único 
entre objetos simultáneamente existentes. (Sugerencia: es la dirección de memoria del 
objeto).

::

    >>> lista = range(5)
    >>> lista
    [0, 1, 2, 3, 4]
    >>> id(lista)
    139703096777904


.. _python_fun_len:

len()
~~~~~

Devuelve el número de elementos de un tipo de secuencia o colección.

::

    >>> len("leonardo caballero")
    18


.. _python_fun_license:

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


.. _python_fun_locals:

locals()
~~~~~~~~

La función ``locals()`` devuelve un diccionario conteniendo ámbito actual local de 
las variables.

::

    >>> locals()
    {'__builtins__': <module '__builtin__' (built-in)>, 
    '__package__': None, '__name__': '__main__', '__doc__': None}

La función ``locals()`` puede ser usadas para devolver los nombres en el ``namespaces`` 
local dependiendo en la locación desde donde ella es llamada.

Si la función ``locals()`` es llamada desde una función, eso devolverá todos los nombres 
que pueden ser accesibles localmente desde esa función.

El tipo de dato devuelto por la función es un tipo diccionario. Por lo tanto, los nombres 
pueden ser extraídos usando la función integrada ``keys()``.


.. _python_fun_open:

open()
~~~~~~

La función ``open()`` es definida dentro del modulo integrado ``io``, esta le permite
:ref:`abrir un archivo <python_abrir_archivo>` usando el tipo objeto ``file``, devuelve 
un objeto del tipo :ref:`file <python_cls_file>` (ej. *archivo*), y se llama 
habitualmente con de dos a tres argumentos: 

::

    file(nombre[, modo[, buffering]]) -> objeto archivo

Los argumentos son:

- ``nombre``, es una :ref:`cadena de caracteres <python_str>` que indica el *nombre de archivo* 
  (incluso ruta relativa o absoluta).

- ``modo``, es una cadena de unos pocos caracteres describiendo la forma en 
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

    >>> archivo = open('datos.txt', 'w')
    >>> type(archivo)
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


.. _python_fun_range:

range()
~~~~~~~

La función ``range()`` devuelve una lista conteniendo una progresión aritmética 
de enteros.

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


.. _python_fun_reload:

reload()
~~~~~~~~

Cuando el modulo es importado dentro de un script, el código en la porción del nivel 
superior de un modulo es ejecutado solamente una vez.

Por lo tanto, si usted quiere volver a ejecutar la porción del nivel superior el código 
de un modulo, usted puede usar la función ``reload()``. Esta función importa otra vez 
un modulo previamente importado. La sintaxis de la función ``reload()`` es la siguiente:

::

    >>> reload(module_name)

Aquí, ``module_name`` es el nombre del modulo que usted quiere volver a cargar y no la 
:ref:`cadena de caracteres <python_str>` contendiente el nombre del modulo. Por ejemplo, 
para recargar el modulo ``clases.py``, debe hacer lo siguiente:

::

    >>> import clases
    >>> reload(clases)


.. _python_fun_xrange:

xrange()
~~~~~~~~

El tipo ``xrange`` es un tipo secuencia inmutable utilizada normalmente en bucles. La 
ventaja de la función ``xrange()`` sobre la función ``range()``, es que devuelve 
un objeto ``xrange`` el cual ocupa siempre la misma cantidad de memoria, 
independientemente del rango el cual represente. 

::

    >>> for item in range(5):
    ...     print item
    ... 
    0
    1
    2
    3
    4
    >>> for item in xrange(5):
    ...     print item
    ... 
    0
    1
    2
    3
    4
    >>>

Como la función ``xrange()``, devuelve un objeto el cual genera los números en el 
rango a demanda. Para bucles, esto es un poco mas rápido que la función ``range()`` 
y más eficiente en la memoria.

::

    >>> print xrange(5)
    xrange(5)
    >>> type(xrange(5))
    <type 'xrange'>
    >>> dir(xrange(5))
    ['__class__', '__delattr__', '__doc__', '__format__', 
    '__getattribute__', '__getitem__', '__hash__', '__init__', 
    '__iter__', '__len__', '__new__', '__reduce__', '__reduce_ex__', 
    '__repr__', '__reversed__', '__setattr__', '__sizeof__', 
    '__str__', '__subclasshook__']

La ventaja de la función ``xrange()`` es *excepto* en hardware impedido en cuestión 
de memoria (por ejemplo, MS-DOS) o cuando nunca se utilizan todos los elementos 
del rango (por ejemplo, porque se suele interrumpir la ejecución del bucle con la 
sentencia :ref:`break <python_sent_break>`).


.. _python_fun_type:

type()
~~~~~~~

La función ``type()`` devuelve el tipo del objeto que recibe como argumento.

::

    >>> type(2)
    <type 'int'>
    >>> type(2.5)
    <type 'float'>
    >>> type(True)
    <type 'bool'>
    >>> type("Hola Mundo")
    <type 'str'>
    >>> type(int)
    <type 'type'>
    >>> type(str)
    <type 'type'>
    >>> type(None)
    <type 'NoneType'>
    >>> type(object)
    <type 'type'>
    >>> import os
    >>> type(os)
    <type 'module'>
    >>> type(format)
    <type 'builtin_function_or_method'>

.. tip::

    La función ``type()`` devuelve el tipo del objeto, en base al modulo integrado 
    ``types``, el cual define los nombres para todos los símbolos tipo conocidos 
    en el interprete estándar.

    ::

        >>> import types
        >>> help(types)

        Help on module types:

        NAME
            types - Define names for all type symbols known in the standard interpreter.

        FILE
            /usr/lib/python2.7/types.py

        MODULE DOCS
            https://docs.python.org/library/types

        DESCRIPTION
            Types that are part of optional modules (e.g. array) are not listed.

        CLASSES
            __builtin__.basestring(__builtin__.object)
                __builtin__.str
                __builtin__.unicode

        >>> 


.. _python_fun_vars:

vars()
~~~~~~

La función ``vars()`` devuelve un diccionario conteniendo ámbito actual de las 
variables.

::

    >>> vars()
    {'__builtins__': <module '__builtin__' (built-in)>, '__package__': 
    None, '__name__': '__main__', '__doc__': None}


La función ``vars()`` sin argumentos, equivale a la función :ref:`locals() <python_fun_locals>`. 
Si se llama con un argumento equivale a la sentencia ``object.__dict__``.


----


.. _python_fun_builtins_es:

Funciones de entrada y salida
.............................

Las funciones de tipos numéricos se describen a continuación:


.. _python_fun_input:

input()
~~~~~~~

Equivalente a la función ``eval(raw_input(prompt))``

Lee una :ref:`cadena de caracteres <python_str>` desde la entrada estándar.

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


En el caso que quiera ingresar una :ref:`cadena de caracteres <python_str>` desde la 
entrada estándar usando la función ``input()``, debe colocar la cadena de caracteres 
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


.. _python_fun_raw_input:

raw_input()
~~~~~~~~~~~

Lee una :ref:`cadena de caracteres <python_str>` desde la entrada estándar. La nueva 
línea final es despojada. Si el usuario indica un EOF (*Unix*: ``Ctl-D``, *Windows*: 
``Ctl-Z+Return``), lanza una excepción :ref:`EOFError <python_exception_eoferror>`. 
En sistemas Unix, la librería **GNU readline** es usada si es habilitada.  El ``prompt`` 
de la cadena de caracteres, si es dado, es impreso sin una nueva línea final antes 
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



.. _python_fun_builtins_numericas:

Funciones numéricas
...................

Las funciones de tipos numéricos se describen a continuación:


.. _python_fun_abs:

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


.. _python_fun_bin:

bin()
~~~~~

Devuelve una representación binaria de un :ref:`número entero <python_num_entero>` 
o :ref:`entero long <python_num_entero_long>`, es decir, lo convierte de entero a binario.

::

    >>> bin(10)
    '0b1010'


.. _python_fun_cmp:

cmp()
~~~~~

La función ``cmp()`` devuelve un valor negativo si ``x<y``, un valor cero si ``x==y``, 
un valor positivo si ``x>y``:

::

    >>> cmp(1,2)
    -1
    >>> cmp(2,2)
    0
    >>> cmp(2,1)
    1


.. _python_fun_complex:

complex()
~~~~~~~~~

La función ``complex()`` devuelve un número complejo ``complex``. Es un constructor, 
que crea un :ref:`entero complex <python_num_complex>` a partir de un 
:ref:`entero <python_num_entero>`, :ref:`entero long <python_num_entero_long>`, 
:ref:`entero float <python_num_float>` (cadenas de caracteres formadas por números y 
hasta un punto), o una :ref:`cadena de caracteres <python_str>` que sean coherentes 
con un número entero.

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

La función ``complex()`` sólo procesa correctamente cadenas que contengan 
exclusivamente números.Si la cadena contiene cualquier otro carácter, la 
función devuelve una excepción :ref:`ValueError <python_exception_valueerror>`.

::

    >>> complex("qwerty")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: complex() arg is a malformed string


.. _python_fun_divmod:

divmod()
~~~~~~~~

Debe recibir dos argumentos numéricos, y devuelve dos valores: resultado de 
la división entera, y el resto.

::

    >>> divmod(22, 4)
    (5, 2)


.. _python_fun_float:

float()
~~~~~~~

La función ``float()`` devuelve un número coma flotante ``float``. Es un constructor, 
que crea un :ref:`coma flotante <python_num_float>` a partir de un 
:ref:`entero <python_num_entero>`, :ref:`entero long <python_num_entero_long>`, 
:ref:`entero float <python_num_float>` (cadenas de caracteres formadas por 
números y hasta un punto) o una :ref:`cadena de caracteres <python_str>` que sean 
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


.. _python_fun_hex:

hex()
~~~~~

Devuelve una representación hexadecimal de un :ref:`número entero <python_num_entero>` 
o :ref:`entero long <python_num_entero_long>`, es decir, lo convierte de entero a 
hexadecimal.

::

    >>> hex(10)
    '0xa'


.. _python_fun_int:

int()
~~~~~

La función ``int()`` devuelve un número entero. Es un constructor, que crea un 
:ref:`entero <python_num_entero>` a partir de un :ref:`entero float <python_num_float>`, 
:ref:`entero complex <python_num_complex>` o una 
:ref:`cadena de caracteres <python_str>` que sean coherentes con un número entero.


::

    >>> int(2.5)
    2

También puede convertir una cadena de caracteres a un número entero.

::

    >>> int("23")
    23


La función ``int()`` sólo procesa correctamente cadenas que contengan exclusivamente 
números. Si la cadena contiene cualquier otro carácter, la función devuelve una 
excepción :ref:`ValueError <python_exception_valueerror>`.

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


.. _python_fun_long:

long()
~~~~~~

La función ``long()`` devuelve un número entero ``long``. Es un constructor, que crea 
un :ref:`entero long <python_num_entero_long>` a partir de un 
:ref:`entero <python_num_entero>`, :ref:`entero float <python_num_float>` 
o una :ref:`cadena de caracteres <python_str>` que sean coherentes con un número 
entero.

::

    >>> long(23)
    23L
    >>> long(23.4)
    23L

También puede convertir una cadena de caracteres a un número entero.

::

    >>> long("23")
    23


La función ``long()`` sólo procesa correctamente cadenas que contengan exclusivamente 
números. Si la cadena contiene cualquier otro carácter, la función devuelve una 
excepción :ref:`ValueError <python_exception_valueerror>`.

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


.. _python_fun_max:

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


Si recibe un solo argumento, devuelve el mayor de sus elementos. Debe ser un objeto 
iterable; puede ser una :ref:`cadena de caracteres <python_str>`, o alguno de los 
otros tipos de secuencia o colección.

::

    >>> max("Hola, Plone")
    'o'
    >>> type(max("Hola, Plone"))
    <type 'str'>


.. _python_fun_min:

min()
~~~~~

Tiene un comportamiento similar a ``max()``, pero devuelve el mínimo.

::

    >>> min(23, 12, 145, 88)
    12
    >>> type(min(23, 12, 145, 88))
    <type 'int'>
    >>> min("Hola, Plone")
    ' '
    >>> type(min("Hola, Plone"))
    <type 'str'>


.. _python_fun_pow:

pow()
~~~~~

La función ``pow()`` si recibe dos (02) argumentos, eleva el primero argumento 
a la potencia del segundo argumento.

::

    >>> pow(2, 3)
    8
    >>> pow(10, 2)
    100
    >>> pow(10, -2)
    0.01

Si recibe un tercer argumento opcional, éste funciona como módulo.

::

    >>> pow(2, 3, 3)
    2


.. _python_fun_reduce:

reduce()
~~~~~~~~

La función ``reduce()`` aplica una función de dos argumentos de forma acumulativa a 
los elementos de un tipo de secuencia, de izquierda a derecha, para reducir la 
secuencia a un solo valor. La sintaxis seria la siguiente:

::

    >>> reduce(funcion, secuencia[, inicial]) -> valor

A continuación un ejemplo:

::

    >>> reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
    15
    >>> ((((1+2)+3)+4)+5)
    15

En el ejemplo anterior, calcula el siguiente calculo ``((((1+2)+3)+4)+5)``. 

Si el argumento ``inicial`` está presente, se coloca antes de los elementos de la 
secuencia en el cálculo y sirve como valor predeterminado cuando la secuencia está 
vacía.

::

    >>> reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 5 * 5)
    40

En el ejemplo anterior, la función, usada es ``lambda x, y: x + y``, la secuencia es 
la lista ``[1, 2, 3, 4, 5]`` y el argumento ``inicial`` es ``5 * 5``

::

    >>> reduce(lambda x, y: x + y, [0, 0, 0, 0, 0], 5 * 5)
    25

En el ejemplo anterior, la función, usada es ``lambda x, y: x + y``, la secuencia es 
la lista ``[0, 0, 0, 0, 0]`` y el argumento ``inicial`` es ``5 * 5``


.. _python_fun_round:

round()
~~~~~~~

La función ``round()`` redondea un número flotante a una precisión dada en 
dígitos decimal (por defecto 0 dígitos). Esto siempre devuelve un número 
flotante. La precisión tal vez sea negativa.

En el siguiente ejemplo redondeo de un número flotante a entero, mayor o 
igual a *.5* al alza:

::

    >>> round(5.5)
    6.0

En este otro ejemplo redondeo de un número flotante a entero, menor de *.5* 
a la baja:

::

    >>> round(5.4)
    5.0


.. _python_fun_sum:

sum()
~~~~~

La función ``sum()`` devuelve una lista ordenada de los elementos de la secuencia 
que recibe como argumento (lista o cadena). La secuencia original no es modificada.

::

    >>> lista = [1, 2, 3, 4]
    >>> sum(lista)
    10


.. _python_fun_oct:

oct()
~~~~~

La función ``oct()`` convierte un número entero en una cadena en base octal, 
antecedida del prefijo *'0'*.

::

    >>> oct(8)
    '010'
    >>> oct(123)
    '0173'


----


.. _python_fun_builtins_bool:

Funciones de booleanos
......................

Las funciones de tipos :ref:`booleanos <python_bool>` se describen a continuación:


.. _python_fun_bool:

bool()
~~~~~~

La función ``bool()``, es un constructor, el cual crea un tipo de datos 
:ref:`booleanos <python_bool>`, devuelve un tipo booleano ``True`` cuando el 
argumento dado es ``True``, de lo contrario ``False``.

::

    >>> bool()
    False
    >>> bool(True)
    True

Convertir desde un tipo :ref:`entero <python_numericos>` a tipo *booleano*:

::

    >>> bool(0)
    False
    >>> bool(1)
    True

Convertir desde un tipo :ref:`entero float <python_num_float>` de forma recursiva 
usando la función :ref:`int() <python_fun_int>` a tipo *booleano*:

::

    >>> bool(int(0.1))
    False
    >>> bool(int(1.0))
    True

Convertir desde un tipo :ref:`cadena de caracteres <python_str>` de forma recursiva 
usando la función :ref:`str() <python_fun_str>` y la función :ref:`int() <python_fun_int>` 
a tipo *booleano*:

::

    >>> bool(int(str('0')))
    False
    >>> bool(int(str('1')))
    True

----


.. _python_fun_builtins_cadenas:

Funciones de cadenas de caracteres
..................................

Las funciones de tipos :ref:`cadena de caracteres <python_str>` se describen a 
continuación:


.. _python_fun_capitalize:

capitalize()
~~~~~~~~~~~~

La función ``capitalize()`` devuelve una :ref:`cadenas de caracteres <python_str>` 
con MAYÚSCULA la primera palabra. 

::

    >>> 'leonardo caballero'.capitalize()
    'Leonardo caballero'


.. _python_fun_chr:

chr()
~~~~~

La función ``chr()`` recibe como argumento un entero, y devuelve una cadena con 
el carácter cuyo código *Unicode* corresponde a ese valor. El rango válido para 
el argumento es de 0 a 256.

::

    >>> chr(64)
    '@'
    >>> chr(36)
    '$'
    >>> chr(94)
    '^'
    >>> chr(126)
    '~'


.. _python_fun_endswith:

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


.. _python_fun_expandtabs:

expandtabs()
~~~~~~~~~~~~

La función ``expandtabs()`` devuelve una copia de la :ref:`cadena de caracteres <python_str>` 
donde todos los caracteres ``tab`` (tabulación) son remplazados por uno o más espacios, 
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


.. _python_fun_find:

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


.. _python_fun_format:

format()
~~~~~~~~

La función integrada ``format()`` devuelve una representación formateada de un valor 
dato controlado por el especificador de formato.

La función integrada ``format()`` es similar al :ref:`método format() <python_mtd_format>` 
disponible en el tipo de :ref:`cadena de caracteres <python_str>`. Internamente, 
ambos llaman al método ``__format__()`` de un objecto.

Mientras, la función integrada ``format()`` es una implementación de bajo nivel para 
formatear un objeto usando ``__format__()`` internamente, el 
:ref:`método format() <python_mtd_format>` del tipo de cadena de caracteres es una 
implementación de alto nivel disponible para ejecutar operaciones de formateo complejas 
en múltiples objeto de :ref:`cadena de caracteres <python_str>`.

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

A continuación, un ejemplo de un valor :ref:`número float <python_num_float>`, 
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

A continuación, un ejemplo de un valor :ref:`número float <python_num_float>` 
con formato especifico, seria de la siguiente forma:

::

    >>> print format(123.4567, "^-09.3f")
    0123.4570

En el ejemplo anterior cuando se formatea el :ref:`número float <python_num_float>` 
*123.4567*, usted especifico el especificador de formato ``^-09.3f``. Seguidamente, se 
describe cada opción a continuación:

- ``^`` Es la opción de alineación centrar, el cual alinea la cadena de 
  caracteres de salida al centro del espacio restante. 

- ``-`` Es la opción de signo el cual obliga solo a los números negativos a mostrar 
  el signo.

- ``0`` Ese es el carácter, el cual es colocado en lugar de los espacios vacíos.

- ``9`` Es la opción de ancho, el cual establece el ancho mínimo del número en 9 
  (incluido el punto decimal, la coma y el signo de miles).

- ``.3`` Ese es el operador de precisión que define la precisión del número 
  flotante dado a 3 lugares.

- ``f`` Es la opción tipo que especifica que el número es un 
  :ref:`número float <python_num_float>`.

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


.. _python_fun_index:

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


.. _python_fun_intern:

intern()
~~~~~~~~

La función ``intern()`` introduce la cadena en la tabla de cadenas internadas (si no 
está ya allí). Esto ingresa la cadena en la tabla (global) de cadenas internas cuyo 
propósito es acelerar las búsquedas en el tipo diccionario. 

Al utilizar la función ``intern()``, se asegura de que nunca cree dos objetos de cadena 
de caracteres que tengan el mismo valor: cuando solicita la creación de un segundo 
objeto de cadena de caracteres con el mismo valor que un objeto de cadena existente, 
recibe una referencia al objeto de cadena preexistente. De esta manera, estás ahorrando 
memoria. Además, la comparación de objetos de cadena de caracteres ahora es muy eficiente 
porque se lleva a cabo comparando las direcciones de memoria de los dos objetos de 
cadena de caracteres en lugar de su contenido.

Esencialmente, la función ``intern()`` busca (o almacena si no está presente) la 
cadena de caracteres en una colección de cadenas de caracteres internadas, por lo 
que todas las instancias internadas compartirán la misma identidad. Cambia el costo 
único de buscar esta cadena de caracteres para realizar comparaciones más rápidas 
(la comparación puede devolver ``True`` después de solo verificar la identidad, en 
lugar de tener que comparar cada carácter), y reducir el uso de la memoria.

Sin embargo, Python internará automáticamente cadenas de caracteres que sean pequeñas 
o que parezcan identificadores, por lo que es posible que no obtengas ninguna mejora 
porque tus cadenas de caracteres ya están internadas entre bastidores.

A continuación uno ejemplo de comparación de cadena de caracteres con operadores de relacionales:

::

    >>> cadena0, cadena1 = 'python', 'python'
    >>> cadena0 == cadena1
    True
    >>> cadena0 is cadena1
    True
    >>> cadena0, cadena1 = 'python 2.7', 'python 2.7'
    >>> cadena0 is cadena1
    False

A continuación uno ejemplo de comparación de cadena de caracteres con el operador 
:ref:`is <python_opers_is>`:

::

    >>>
    >>> cadena0 = intern('plone cms')
    >>> cadena1 = 'plone cms'
    >>> cadena0 is cadena1
    False
    >>> cadena1 = intern('plone cms')
    >>> cadena0 is cadena1
    True


.. _python_fun_isalnum:

isalnum()
~~~~~~~~~

La función ``isalnum()`` devuelve un valor booleano ``True`` o ``False`` 
si coincide que la cadena contenga caracteres alfanuméricos.

::

    >>> '23456987'.isalnum()
    True
    >>> 'V-23456987'.isalnum()
    False


.. _python_fun_isalpha:

isalpha()
~~~~~~~~~

La función ``isalpha()`` devuelve un valor booleano ``True`` o ``False`` 
si coincide que la cadena contenga caracteres alfabéticos.

::

    >>> 'leonardo'.isalpha()
    True
    >>> 'leonardo caballero'.isalpha()
    False


.. _python_fun_isdigit:

isdigit()
~~~~~~~~~

La función ``isdigit()`` devuelve un valor booleano ``True`` o ``False`` 
si coincide que la cadena contenga caracteres dígitos.


::

    >>> 'leonardo caballero'.isdigit()
    False
    >>> '23456987'.isdigit()
    True


.. _python_fun_islower:

islower()
~~~~~~~~~

La función ``islower()`` devuelve un valor booleano ``True`` o ``False`` 
si coincide que la cadena contenga caracteres en MINÚSCULAS.

::

    >>> 'leonardo caballero'.islower()
    True
    >>> 'leonardo CABALLERO'.islower()
    False


.. _python_fun_istitle:

istitle()
~~~~~~~~~

La función ``istitle()`` devuelve un valor booleano ``True`` o ``False`` si coincide 
que la :ref:`cadena de caracteres <python_str>` sean capitales en cada palabra. 

::

    >>> "leonardo caballero".title()
    'Leonardo Caballero'
    >>> "leonardo Caballero".istitle()
    False


.. _python_fun_isspace:

isspace()
~~~~~~~~~

La función ``isspace()`` devuelve un valor booleano ``True`` o ``False`` si no es 
vacía, y todos sus caracteres son espacios en blanco.

::

    >>> " ".isspace()
    True
    >>> "  ".isspace()
    True
    >>> "a ".isspace()
    False
    >>> " A ".isspace()
    False


.. _python_fun_isupper:

isupper()
~~~~~~~~~

La función ``isupper()`` devuelve un valor booleano ``True`` o ``False`` si coincide 
que la :ref:`cadena de caracteres <python_str>` estén en MAYÚSCULAS en cada palabra. 

::

    >>> 'LEONARDO CABALLERO'.isupper()
    True
    >>> 'LEONARDO caballero'.isupper()
    False


.. _python_fun_lstrip:

lstrip()
~~~~~~~~

La función ``lstrip()`` devuelve una copia de la :ref:`cadena de caracteres <python_str>` 
con el espacio en blanco inicial eliminado. Si se dan la cadena de caracteres y no es 
:ref:`None <python_obj_none>`, elimina los caracteres en la cadena de caracteres en su 
lugar. Si la cadena de caracteres son ``unicode``, serán convertidas a ``unicode`` antes 
de eliminar.

::

    >>> " leonardo caballero ".lstrip()
    'leonardo caballero '


.. _python_fun_lower:

lower()
~~~~~~~

La función ``lower()`` devuelve una :ref:`cadenas de caracteres <python_str>` con MINÚSCULAS 
en cada palabra. 

::

    >>> 'LEONARDO CABALLERO'.lower()
    'leonardo caballero'


.. _python_fun_ord:

ord()
~~~~~

La función ``ord()`` es el inverso de :ref:`chr() <python_fun_chr>` dada una 
cadena representando un carácter Unicode, devuelve el entero del código correspondiente.

::

    >>> ord('@')
    64
    >>> ord('$')
    36
    >>> ord('^')
    94
    >>> ord('~')
    126


.. _python_fun_replace:

replace()
~~~~~~~~~

La función ``replace()`` si encuentra el criterio de la búsqueda de la 
sub-cadena o la remplaza con la nueva sub-cadena enviado por parámetros 
en la función.

::

    >>> 'leonardo caballero'.replace(" cab", " Cab")
    'leonardo Caballero'


.. _python_fun_split:

split()
~~~~~~~

La función ``split()`` devuelve una lista con la :ref:`cadena de caracteres <python_str>` 
separada por cada indice de la lista. 

::

    >>> 'leonardo caballero'.split()
    ['leonardo', 'caballero']


.. _python_fun_splitlines:

splitlines()
~~~~~~~~~~~~

La función ``splitlines()`` devuelve una lista con la :ref:`cadena de caracteres <python_str>` 
separada por cada salto de linea en cada indice de la lista.

::

    >>> 'leonardo jose\ncaballero garcia'.splitlines()
    ['leonardo jose', 'caballero garcia']


.. _python_fun_startswith:

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


.. _python_fun_str:

str()
~~~~~

La función ``str()`` es el constructor del tipo de :ref:`cadenas de caracteres <python_str>`, 
se usa crear una *carácter* o *cadenas de caracteres* mediante la misma función ``str()``. 

Puede convertir un :ref:`número entero <python_num_entero>` a una *cadena de caracteres*, 
de la siguiente forma:

::

    >>> str(2)
    '2'

Puede convertir un :ref:`número float <python_num_float>` a una *cadena de caracteres*, 
de la siguiente forma:

::

    >>> str(2.5)
    '2.5'
    >>> str(-2.5)
    '-2.5'

Puede convertir un :ref:`número complex <python_num_complex>` a una *cadena de caracteres*, 
de la siguiente forma:

::

    >>> str(2.3+0j)
    '(2.3+0j)'

Puede convertir un tipo :ref:`booleano <python_bool>` a una *cadena de caracteres*, 
de la siguiente forma:

::

    >>> str(True)
    'True'
    >>> str(False)
    'False'


.. _python_fun_swapcase:

swapcase()
~~~~~~~~~~

La función ``swapcase()`` devuelve una :ref:`cadenas de caracteres <python_str>` 
convertida al opuesto sea MAYÚSCULAS o MINÚSCULAS.

::

    >>> 'leonardo caballero'.swapcase()
    'LEONARDO CABALLERO'
    >>> 'LEONARDO CABALLERO'.swapcase()
    'leonardo caballero'


.. _python_fun_title:

title()
~~~~~~~

La función ``title()`` devuelve una :ref:`cadenas de caracteres <python_str>` con 
capitales en cada palabra. 

::

    >>> "leonardo caballero".title()
    'Leonardo Caballero'


.. _python_fun_unichr:

unichr()
~~~~~~~~

La función ``unichr()`` devuelve una *cadena de caracteres* *Unicode* de un carácter 
con un numero entero.

::

    >>> unichr(64)
    u'@'
    >>> unichr(36)
    u'$'
    >>> unichr(94)
    u'^'
    >>> unichr(126)
    u'~'


.. _python_fun_upper:

upper()
~~~~~~~

La función ``upper()`` devuelve una :ref:`cadenas de caracteres <python_str>` con 
MAYÚSCULAS en cada palabra. 

::

    >>> "leonardo caballero".upper()
    'LEONARDO CABALLERO'


----


.. _python_fun_builtins_secuencias:

Funciones de secuencias
.......................

Las funciones de secuencias se describen a continuación:


.. _python_fun_all:

all()
~~~~~

La función ``all()`` toma un contenedor como un argumento. Esta devuelve las funciones 
integradas ``True`` si todo los valores en el objeto iterable python tienen un valor 
de tipo :ref:`booleano <python_bool>` igual a ``True``. Un valor vacío tiene un tipo 
:ref:`booleano <python_bool>` igual a ``False``.

::

    >>> all([' ',' ',' '])
    True
    >>> all({'*','',''})
    False


.. _python_fun_any:

any()
~~~~~

La función ``any()`` ese toma un argumento y devuelve ``True`` incluso si, un valor en 
el objeto iterable tiene un valor de tipo :ref:`booleano <python_bool>` igual a ``True``.

::

    >>> any((1,0,0))
    True
    >>> any((0,0,0))
    False
    >>> any(range(5))
    True
    >>> any(range(0))
    False


.. _python_fun_coerce:

coerce()
~~~~~~~~

La función ``coerce()`` devuelve una tupla que consta de los dos argumentos numéricos 
convertidos en un tipo común, utilizando las mismas reglas que las operaciones 
aritméticas. Si la coerción no es posible, levante una excepción 
:ref:`TypeError <python_exception_typeerror>`.

::

    >>> coerce(3, 4)
    (3, 4)
    >>> coerce(3, 4.2)
    (3.0, 4.2)


.. _python_fun_dict:

dict()
~~~~~~

La función ``dict()`` es el constructor del tipo de :ref:`diccionario <python_dict>`, 
esta función se usa crear un diccionario:

::

    >>> dict(python=2.7, zope=2.13, plone=5.1)
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}

También puede crear un diccionario indicando a las claves usando comillas simples:

::

    >>> {'python': 2.7, 'zope': 2.13, 'plone': 5.1}
    {'python': 2.7, 'zope': 2, 'plone': 5.1}
    >>> dict({'python': 2.7, 'zope': 2.13, 'plone': 5.1})
    {{'python': 2.7, 'zope': 2.13, 'plone': 5.1}

Convertir desde un grupo de dos :ref:`listas <python_list>` de forma recursiva usando 
la función :ref:`zip() <python_fun_zip>` a tipo *diccionario*:

::

    >>> dict(zip(['python', 'zope', 'plone'], [2.7, 2.13, 5.1]))
    {'python': 2.7, 'zope': 2.13, 'plone': 5.1}

Convertir desde un grupo de :ref:`tuplas <python_tuple>` respectivamente en una 
:ref:`lista <python_list>` a tipo *diccionario*:

::

    >>> dict([('zope', 2.13), ('python', 2.7), ('plone', 5.1)])
    {'plone': 5.1, 'zope': 2.13, 'python': 2.7}


.. _python_fun_frozenset:

frozenset()
~~~~~~~~~~~

La función ``frozenset()`` es el constructor del tipo de :ref:`conjuntos <python_set>`, 
se usa crear un conjunto *inmutable* mediante la misma función ``frozenset()`` de un objeto 
iterable :ref:`lista <python_list>`:

::

    >>> versiones = [6, 2.1, 2.5, 3.6, 4, 5, 6, 4, 2.5]
    >>> print versiones, type(versiones)
    [6, 2.1, 2.5, 3.6, 4, 5, 6, 4, 2.5] <type 'list'>
    >>> versiones_plone = frozenset(versiones)
    >>> print versiones_plone, type(versiones_plone)
    frozenset([2.5, 4, 5, 6, 2.1, 3.6]) <type 'frozenset'>


.. _python_fun_iter:

iter()
~~~~~~

La función ``iter()`` obtiene un :ref:`iterador <python_iter>` de un objeto. En la 
primera forma, el argumento debe proporcionar su propio *iterador*, o ser una secuencia.

::

    >>> elemento = iter("Plone")
    >>> elemento
    <iterator object at 0x7eff6ce10250>
    >>> elemento.next()
    'P'
    >>> elemento.next()
    'l'
    >>> elemento.next()
    'o'
    >>> elemento.next()
    'n'
    >>> elemento.next()
    'e'
    >>> elemento.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior, cuando se itera en la secuencia de tipo 
:ref:`cadena de caracteres <python_str>`, al llegar al final mediante el iterador 
llamado ``elemento`` se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la 
iteración.


.. _python_fun_list:

list()
~~~~~~

La función ``list()`` es el constructor del tipo de :ref:`lista <python_list>`, 
se usa crear una lista mediante la misma función ``list()`` de un iterable. Por 
ejemplo, una lista podría crearse mediante la función :ref:`range(10) <python_fun_range>`:

::

    >>> lista = list(range(10))
    >>> print lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


.. _python_fun_next:

next()
~~~~~~

La función ``next()`` devuelve el próximo elemento desde un :ref:`iterador <python_iter>`.

::

    >>> elemento = iter([1,2,3,4,5])
    >>> next(elemento)
    1
    >>> next(elemento)
    2
    >>> next(elemento)
    3
    >>> next(elemento)
    4
    >>> next(elemento)
    5
    >>> next(elemento)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior, cuando se itera en la secuencia de tipo :ref:`lista <python_list>`, 
al llegar al final mediante el iterador llamado ``elemento`` se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la 
iteración.


.. _python_fun_tuple:

tuple()
~~~~~~~

La función ``tuple()`` es el constructor del tipo de :ref:`tuplas <python_tuple>`, 
se usa crear una tupla mediante la misma función ``tuple()`` de un iterable. Por 
ejemplo, una tupla podría crearse mediante la función :ref:`range(10) <python_fun_range>`:

::

    >>> tupla = tuple(range(4, 9))
    >>> print tupla
    (4, 5, 6, 7, 8)


.. _python_fun_set:

set()
~~~~~

La función ``set()`` es el constructor del tipo de :ref:`conjuntos <python_set>`, 
se usa crear un conjunto *mutable* mediante la misma función ``set()`` de un objeto 
iterable :ref:`lista <python_list>`:

::

    >>> versiones = [2.1, 2.5, 3.6, 4, 5, 6, 4]
    >>> print versiones, type(versiones)
    [2.1, 2.5, 3.6, 4, 5, 6, 4] <type 'list'>
    >>> versiones_plone = set(versiones)
    >>> print versiones_plone, type(versiones_plone)
    set([2.5, 4, 5, 6, 2.1, 3.6]) <type 'set'>


.. _python_fun_sorted:

sorted()
~~~~~~~~

La función ``sorted()`` devuelve una lista ordenada de los elementos del tipo secuencia 
que recibe como argumento (lista o cadena de caracteres). La secuencia original no es 
modificada.

::

    >>> lista = [23, 13, 7, 37]
    >>> sorted(lista)
    [7, 13, 23, 37]

La función ``sorted()`` siempre devuelve una lista, aunque reciba como argumento una 
:ref:`cadena de caracteres <python_str>`.

::

    >>> cadena = "asdlk"
    >>> sorted(cadena)
    ['a', 'd', 'k', 'l', 's']

.. _python_fun_zip:

zip()
~~~~~

La función ``zip()`` devuelve una lista de :ref:`tuplas <python_tuple>`, donde cada 
tupla contiene el elemento i-th desde cada una de los tipos de secuencias de argumento. 
La lista devuelta es truncada en longitud a la longitud de la secuencia de argumentos 
más corta.

::

    >>> zip(['python', 'zope', 'plone'], [2.7, 2.13, 5.1])
    [('python', 2.7), ('zope', 2.13), ('plone', 5.1)]


----


.. _python_fun_objetos:

Funciones de objetos
....................

Las funciones de objetos se describen a continuación:


.. _python_fun_delattr:

delattr()
~~~~~~~~~

La función ``delattr()`` elimina un atributo con nombre en un objeto; 
``delattr(x, 'y')`` es equivalente a ``del x.y``.

::

    >>> class Persona:
    ...     """Clase que representa una Persona"""
    ...     cedula = "V-13458796"
    ...     nombre = "Leonardo"
    ...     apellido = "Caballero"
    ...     sexo = "M"
    ... 
    >>> macagua = Persona()
    >>> macagua.sexo
    'M'
    >>> delattr(Persona,'sexo')
    >>> macagua.sexo
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: Persona instance has no attribute 'sexo'


.. _python_fun_getattr:

getattr()
~~~~~~~~~

La función ``getattr()`` obtiene un atributo nombrado desde un objeto; de la siguiente 
forma ``getattr(instancia, 'atributo')``  el cual es equivalente a ``instancia.atributo``. 
Cuando un argumento predeterminado es dato, es es devuelto cuando el atributo no existe; 
sin eso, una excepción es lanzada en ese caso.

::

    >>> class Persona:
    ...     """Clase que representa una Persona"""
    ...     cedula = "V-13458796"
    ...     nombre = "Leonardo"
    ...     apellido = "Caballero"
    ...     sexo = "M"
    ... 
    >>> macagua = Persona()
    >>> getattr(macagua,'sexo')
    'M'
    >>> macagua.sexo
    'M'

.. _python_fun_hasattr:

hasattr()
~~~~~~~~~

La función ``hasattr()`` devuelve un tipo booleano cuando el objeto tiene un atributo 
con el nombre dado. (Esta hecho llamando a la función ``getattr(instancia, atributo)`` 
y capturar excepciones.)

::

    >>> class Persona:
    ...     """Clase que representa una Persona"""
    ...     cedula = "V-13458796"
    ...     nombre = "Leonardo"
    ...     apellido = "Caballero"
    ...     sexo = "M"
    ... 
    >>> macagua = Persona()
    >>> hasattr(macagua, 'nombre')
    True
    >>> hasattr(macagua, 'apellido')
    True
    >>> hasattr(macagua, 'cedula')
    True
    >>> hasattr(macagua, 'sexo')
    True
    >>> hasattr(macagua, 'email')
    False


.. _python_fun_hash:

hash()
~~~~~~

La función ``hash()`` devuelve un valor hash de tipo entero para el objeto. 

::

    >>> class Persona:
    ...     """Clase que representa una Persona"""
    ...     cedula = "V-13458796"
    ...     nombre = "Leonardo"
    ...     apellido = "Caballero"
    ...     sexo = "M"
    ... 
    >>> macagua = Persona
    >>> type(macagua)
    <type 'classobj'>

Dos objetos con el mismo valor tienen el mismo valor hash.

::

    >>> type(Persona)
    <type 'classobj'>
    >>> type(macagua)
    <type 'classobj'>
    >>> hash(macagua)
    8742669316448
    >>> hash(Persona)
    8742669316448

Lo contrario no es necesariamente cierto, pero es probable.


.. _python_fun_isinstance:

isinstance()
~~~~~~~~~~~~

La función ``isinstance()`` le permite corroborar si un objeto es una 
:ref:`instancia <python_instancias>` de una clase. 

::

    isinstance(objeto, tipo)

Esta función devuelve ``True`` si el objeto especificado es del tipo especificado, 
de lo contrario ``False``.

Los parámetros son:

- *objeto*, es requerido. Un objeto.

- *tipo*, un tipo o una clase, o una tupla de tipos y/o clases

Un ejemplo de uso con la clase ``Persona`` seria como lo siguiente:

::

    >>> persona1 = Persona("V-13458796", "Leonardo", "Caballero", "M")
    >>> isinstance(persona1, Persona)
    True


Si el tipo de parámetro es una tupla, esta función devuelve ``True`` si le objeto es 
uno de los tipos en la tupla.

::

    >>> persona1 = Persona("V-13458796", "Leonardo", "Caballero", "M")
    >>> isinstance(persona1, (Persona, int))
    True

Aquí puede decir que ``persona1`` es una instancia de la clase ``Persona``.

Las clases dan la posibilidad de crear estructuras de datos más complejas. En el 
ejemplo, una clase ``Persona`` que realizará un seguimiento del ``cedula``, 
``nombre``, ``apellido`` y ``sexo`` (que pasará como atributos).


.. _python_fun_issubclass:

issubclass()
~~~~~~~~~~~~

La función ``issubclass()`` le permite corroborar si un objeto es instancia de una 
clase. 

::

    issubclass(subclase, clase)

Esta función devuelve ``True`` si la clase especificada es una subclase de la clase 
base, de lo contrario ``False``.

Un ejemplo de uso con la subclase ``Supervisor`` que deriva de la clase ``Persona`` 
seria como lo siguiente:

::

    >>> sV1 = Supervisor("V-16987456", "Jen", "Paz", "D", "Chivo")
    >>> issubclass(sV1, Persona)
    True


Si el tipo de parámetro es una tupla, esta función devuelve ``True`` si le objeto es 
uno de los tipos en la tupla.

::

    >>> sV1 = Supervisor("V-16987456", "Jen", "Paz", "D", "Chivo")
    >>> issubclass(sV1, (Persona, Empleado, Supervisor, Destreza))
    True

Aquí puede decir que ``sV1`` es una subclase derivada de la clase ``Persona``.

Las clases dan la posibilidad de crear estructuras de datos más complejas. En el ejemplo, 
una clase ``Persona`` que realizará un seguimiento del ``cedula``, ``nombre``, ``apellido`` 
y ``sexo`` (que pasará como atributos).


.. _python_fun_setattr:

setattr()
~~~~~~~~~

La función ``setattr()`` establecer un atributo con nombre en un objeto; 
``setattr(x, 'y', v)`` es equivalente a ``x.y = v``.

::

    >>> class Persona:
    ...     """Clase que representa una Persona"""
    ...     cedula = "V-13458796"
    ...     nombre = "Leonardo"
    ...     apellido = "Caballero"
    ...     sexo = "M"
    ... 
    >>> setattr(macagua, 'email', 'leonardoc@plone.org')
    >>> getattr(macagua,'email')
    'leonardoc@plone.org'


.. important::

    La lista de todas las funciones disponibles en el lenguaje Python con la descripción 
    correspondiente se puede encontrar en la siguiente dirección URL: 

    - https://docs.python.org/2/library/functions.html
