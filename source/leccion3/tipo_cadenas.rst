.. -*- coding: utf-8 -*-


.. _python_str:

Tipo cadenas de caracteres
--------------------------

Las cadenas de caracteres, son secuencias inmutables que contienen caracteres encerrado 
entre comillas.


.. _python_str_short:

Cadenas cortas
..............

Son caracteres encerrado entre comillas simples (``'``) o dobles (``"``). 

::

    >>> 'Hola Mundo'
    'Hola Mundo'


.. _python_str_long:

Cadenas largas
..............

Son caracteres encerrados entre grupo comillas triples simples (``'''``) o dobles 
(``"""``), están son generalmente son referenciadas como *cadenas de triple comillas*.

::

    >>> """Clase que representa una Persona"""
    'Clase que representa una Persona'
    >>> '''Clase que representa un Supervisor'''
    'Clase que representa un Supervisor'


.. _python_str_clases:

Clases
......

A continuación, una lista de clases integradas Python para los tipos de cadenas de 
caracteres:


.. _python_str_basestring_cls:

basestring
~~~~~~~~~~

Es la *clase base* de las clases ``str`` y ``unicode``.


.. _python_str_cls:

str
~~~

Son *secuencias inmutables* de cadenas de caracteres con soporte a caracteres ``ASCII``.

::

    >>> 'Hola Mundo'
    'Hola Mundo'
    >>> "Hola Mundo"
    'Hola Mundo'


.. _python_unicode_cls:

unicode
~~~~~~~

Son *secuencias inmutables* de cadenas de caracteres con soporte a caracteres ``Unicode``. 

::

    >>> u'Jekechitü'
    u'Jekechit\xfc'


.. _python_str_prefijo:

Prefijo de cadenas
..................

Una cadena puede estar precedida por el carácter: 

- ``r``/``R``, el cual indica, que se trata de una cadena ``raw`` (del 
  inglés, cruda). Las cadenas ``raw`` se distinguen de las normales en que los 
  caracteres escapados mediante la barra invertida (``\``) no se sustituyen por 
  sus contrapartidas. Esto es especialmente útil, por ejemplo, para usar las 
  expresiones regulares.

    ::

        >>> raw = r"\t\nHola Plone\n"
        >>> type(raw)
        <type 'str'>

- ``u``/``U``, el cual indica, que se trata de una cadena que utiliza 
  codificación :ref:`unicode <python_unicode_cls>`.

    ::

        >>> saber_mas = u"Atüjaa oo'omüin..."
        >>> type(saber_mas)
        <type 'unicode'>
        >>> vocales = U"äóè"
        >>> type(vocales)
        <type 'unicode'>


.. _python_str_escape:

Cadenas de escape
.................

Para escapar caracteres dentro de cadenas de caracteres se usa el carácter ``\`` 
seguido de cualquier carácter ASCII.

+-------------------+-----------------------------------+
| Secuencia Escape  | Significado                       |
+===================+===================================+
| ``\newline``      | Ignorado                          |
+-------------------+-----------------------------------+
| ``\\``            | Backslash (``\``)                 |
+-------------------+-----------------------------------+
| ``\'``            | Comillas simple (``'``)           |
+-------------------+-----------------------------------+
| ``\"``            | Comillas doble (``"``)            |
+-------------------+-----------------------------------+
| ``\a``            | Bell ASCII (BEL)                  |
+-------------------+-----------------------------------+
| ``\b``            | Backspace ASCII (BS)              |
+-------------------+-----------------------------------+
| ``\f``            | Formfeed ASCII (FF)               |
+-------------------+-----------------------------------+
| ``\n``            | Linefeed ASCII (LF)               |
+-------------------+-----------------------------------+
| ``\N{name}``      | Carácter llamado *name* en base   |
|                   | de datos Unicode (Solo Unicode)   |
+-------------------+-----------------------------------+
| ``\r``            | Carriage Return ASCII (CR)        |
+-------------------+-----------------------------------+
| ``\t``            | Tabulación Horizontal ASCII (TAB) |
+-------------------+-----------------------------------+
| ``\uxxxx``        | Carácter con valor hex 16-bit     |
|                   | *xxxx* (Solamente Unicode).       |
|                   | Ver :ref:`hex <python_fun_hex>`.  |
+-------------------+-----------------------------------+
| ``\Uxxxxxxxx``    | Carácter con valor hex 32-bit     |
|                   | *xxxxxxxx* (Solamente Unicode).   |
|                   | Ver :ref:`hex <python_fun_hex>`.  |
+-------------------+-----------------------------------+
| ``\v``            | Tabulación Vertical ASCII (VT)    |
+-------------------+-----------------------------------+
| ``\ooo``          | Carácter con valor octal *ooo*.   |
|                   | Ver :ref:`octal <python_fun_oct>`.|
+-------------------+-----------------------------------+
| ``\xhh``          | Carácter con valor hex *hh*.      |
|                   | Ver :ref:`hex <python_fun_hex>`.  |
+-------------------+-----------------------------------+

También es posible encerrar una cadena entre triples comillas (simples o dobles). De 
esta forma puede escribir el texto en varias líneas, y al imprimir la cadena, se 
respetarán los saltos de línea que se introdujeron sin tener que recurrir a los 
carácteres escapados y las comillas como los anteriores.


.. _python_str_operaciones:

Operaciones
...........

Las cadenas también admiten operadores aritméticos como los siguientes: 

- El operador :ref:`suma <python_opers_arit_suma>` para realizar concatenación de 
  cadenas de caracteres:

  ::

      >>> a, b = "uno", "dos"
      >>> a + b
      'unodos'

- El operador :ref:`multiplicación <python_opers_arit_multi>` para repetir la cadena 
  de caracteres por N veces definidas en la multiplicación:

  ::

      >>> c = "tres"
      >>> c * 3
      'trestrestres'


- El operador :ref:`modulo <python_opers_arit_mod>` usado la técnica de interpolación 
  variables dentro de una cadena de caracteres. Más información consulte la sección
  :ref:`formateo % <python_str_formateo_modulo>`.


.. _python_str_comentarios:

Comentarios
...........

Son cadenas de caracteres las cuales constituyen una ayuda esencial tanto para quien 
está desarrollando el programa, como para otras personas que lean el código.

Los comentarios en el código tienen una vital importancia en el desarrollo de todo 
programa, algunas de las funciones más importantes que pueden cumplir los comentarios 
en un programa, son:

- Brindar información general sobre el programa.

- Explicar qué hace cada una de sus partes.

- Aclarar y/o fundamentar el funcionamiento de un bloque específico de código, que no 
  sea evidente de su propia lectura.

- Indicar cosas pendientes para agregar o mejorar.

El signo para indicar el comienzo de un comentario en Python es el carácter numeral 
``#``, a partir del cual y hasta el fin de la línea, todo se considera un comentario y 
es ignorado por el intérprete Python.

::

    >>> # comentarios en linea
    ... 
    >>> 

El carácter ``#`` puede estar al comienzo de línea (en cuyo caso toda la línea será 
ignorada), o después de finalizar una instrucción válida de código.

::

    >>> # Programa que calcula la sucesión 
    ... # de números Fibonacci
    ... 
    >>> # se definen las variables
    ... a, b = 0, 1
    >>> while b < 100: # mientras b sea menor a 100 itere
    ...     print b,
    ...     a, b = b, a + b # se calcula la sucesión Fibonacci
    ... 
    1 1 2 3 5 8 13 21 34 55 89


.. _python_comentarios_multilinea:

Comentarios multilínea
~~~~~~~~~~~~~~~~~~~~~~

Python no dispone de un método para delimitar bloques de comentarios de varias líneas.

Al igual que los comentarios de un sola linea, son cadenas de caracteres, en este caso 
van entre triples comillas (simples o dobles), esto tiene el inconveniente que, aunque 
no genera código ejecutable, el bloque delimitado no es ignorado por el intérprete 
Python, que crea el correspondiente objeto de tipo :ref:`cadena de caracteres <python_str>`.

::

    >>> """comentarios en varias lineas"""
    'comentarios en varias lineas'
    >>> '''comentarios en varias lineas'''
    'comentarios en varias lineas'


A continuación, una comparación entre comentarios multilínea y comentarios en solo 
una linea:

::

    >>> # Calcula la sucesión 
    ... # de números Fibonacci
    ... 
    >>> """Calcula la sucesión 
    ... de números Fibonacci"""
    'Calcula la sucesi\xc3\xb3n \nde n\xc3\xbameros Fibonacci'

Entonces existen al menos dos (02) alternativas para introducir comentarios multilínea 
son:

- Comentar cada una de las líneas con el carácter #: en general todos los editores 
  de programación y entornos de desarrollo (IDEs) disponen de mecanismos que permiten 
  comentar y descomentar fácilmente un conjunto de líneas.

- Utilizar triple comillas (simples o dobles) para generar una cadena multilínea: 
  si bien este método es aceptado.

A continuación, un ejemplo de Comentarios multilínea y de solo una linea:

::

    >>> u"""Calcula la sucesiónde números Fibonacci"""
    u'Calcula la sucesi\xf3nde n\xfameros Fibonacci'
    >>> # se definen las variables
    ... a, b = 0, 1
    >>> while b < 100:
    ...     print b,
    ...     # se calcula la sucesión Fibonacci
    ...     a, b = b, a + b
    ... 
    1 1 2 3 5 8 13 21 34 55 89

Los comentarios multilínea usado con mucha frecuencia como en las varias sintaxis Python 
como :ref:`comentarios de documentación <python_str_docstrings>` a continuación se listan 
las sintaxis más comunes:

- :ref:`Módulos <python_modulos>`.

- :ref:`Funciones <python_funciones>`.

- :ref:`Clases <python_clases>`.

- :ref:`Métodos <python_metodos>`.


.. _python_str_docstrings:

Docstrings
..........

En Python todos los objetos cuentan con una variable especial llamada ``doc``, gracias 
a la cual puede describir para qué sirven los objetos y cómo se usan. Estas variables 
reciben el nombre de ``docstrings``, o 
`cadenas de documentación <http://docs.python.org.ar/tutorial/2/controlflow.html#tut-docstrings>`_.

Ten en cuenta, una buena documentación siempre dará respuesta a las dos preguntas:

- ¿Para qué sirve?

- ¿Cómo se utiliza?


.. _python_str_docstrings_def:

Funciones
~~~~~~~~~

Python implementa un sistema muy sencillo para establecer el valor de las ``docstrings`` 
en las funciones, únicamente tiene que crear un comentario en la primera línea después 
de la declaración.

::

    >>> def hola(arg):
    ...     """El docstring de la función"""
    ...     print "Hola", arg, "!"
    ... 
    >>> hola("Plone")
    Hola Plone !

Puede puede consultar la documentación de la función ``hola()`` debe utilizar la 
función integrada :ref:`help() <python_fun_help>` y pasarle el argumento del objeto 
de función ``hola()``:

::

    >>> help(hola)

    Help on function hola in module __main__:

    hola(arg)
        El docstring de la función

    >>>
    >>> print hola.__doc__
    El docstring de la función


Clases y métodos
~~~~~~~~~~~~~~~~

De la misma forma puede establecer la documentación de la clase después de la 
definición, y de los métodos, como si fueran funciones:

::

    >>> class Clase:
    ...     
    ...     """El docstring de la clase"""
    ...     def __init__(self):
    ...         """El docstring del método constructor de clase"""
    ...     
    ...     def metodo(self):
    ...         """El docstring del método de clase"""
    ... 
    >>> o = Clase()
    >>> help(o)

    Help on instance of Clase in module __main__:

    class Clase
     |  El docstring de la clase
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      El docstring del método constructor de clase
     |  
     |  metodo(self)
     |      El docstring del método de clase

    >>> o.__doc__
    'El docstring de la clase'
    >>> o.__init__.__doc__
    'El docstring del método constructor de clase'
    >>> o.metodo.__doc__
    'El docstring del método de clase'


Scripts y módulos
~~~~~~~~~~~~~~~~~

Cuando tiene un script o módulo, la primera línea del mismo hará referencia al 
``docstrings`` del módulo, en él debe explicar el funcionamiento del mismo:

En el archivo ``mi_modulo.py`` debe contener el siguiente código:

::

    """El docstring del módulo"""

    def despedir():
        """El docstring de la función despedir"""
        print "Adiós! desde función despedir() del módulo prueba"

    def saludar():
        """El docstring de la función saludar"""
        print "Hola! desde función saludar() del módulo prueba"


Entonces, usted debe importar el módulo anterior, para consultar la documentación 
del módulo ``mi_modulo`` debe utilizar la función integrada 
:ref:`help() <python_fun_help>` y pasarle el argumento el nombre de módulo 
``mi_modulo``, de la siguiente manera:

::

    >>> import mi_modulo
    >>> help(mi_modulo)

    Help on module mi_modulo:

    NAME
        mi_modulo - El docstring del módulo
    FUNCTIONS
        despedir()
            El docstring de la función despedir
        saludar()
            El docstring de la función saludar

También puede consultar la documentación de la función ``despedir()`` dentro del 
módulo ``mi_modulo``, usando la función integrada :ref:`help() <python_fun_help>` 
y pasarle el argumento el formato *nombre_modulo.nombre_funcion*, es decir, 
``mi_modulo.despedir``, de la siguiente manera:

::

    >>> help(mi_modulo.despedir)

    Help on function despedir in module mi_modulo:

    despedir()
        El docstring de la función despedir

Opcionalmente , usted puede listar las variables y funciones del módulo con la función 
``dir()``, de la siguiente manera:

::

    >>> dir(mi_modulo)
    ['__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'despedir',
     'saludar']

Como puede apreciar, muchas de estas variables son especiales, puede comprobar sus 
valores:

::

    >>> print mi_modulo.__name__     # Nombre del módulo
    'mi_modulo'
    >>> print mi_modulo.__doc__      # Docstring del módulo
    'El docstring del módulo'
    >>> print mi_modulo.__package__  # Nombre del paquete del módulo


.. todo::
    TODO terminar de escribir la sección docstrings.


.. _python_str_formateo:

Formateo de cadenas
...................

Python soporta múltiples formas de formatear una cadena de caracteres. A continuación 
se describen:


.. _python_str_formateo_modulo:

Formateo %
~~~~~~~~~~

El carácter modulo ``%`` es un operador integrado en Python. Ese es conocido como el 
operador de interpolación. Usted necesitará proveer el % seguido por el tipo que 
necesita ser formateado o convertido. El operador % entonces substituye la frase 
'%tipodato' con cero o mas elementos del tipo de datos especificado:

::

    >>> tipo_calculo = "raíz cuadrada de dos"
    >>> valor = 2**0.5
    >>> print "el resultado de %s es %f" % (tipo_calculo, valor)
    el resultado de raíz cuadrada de dos es 1.414214

También aquí se puede controlar el formato de salida. Por ejemplo, para obtener el 
valor con 8 dígitos después de la coma:

::

    >>> tipo_calculo = "raíz cuadrada de dos"
    >>> valor = 2**0.5
    >>> print "el resultado de %s es %.8f" % (tipo_calculo, valor)
    el resultado de raíz cuadrada de dos es 1.41421356

Con esta sintaxis hay que determinar el tipo del objeto:

- ``%c`` = str, simple carácter.

- ``%s`` = str, cadena de carácter.

- ``%d`` = int, enteros.

- ``%f`` = float, coma flotante.

- ``%o`` = octal.

- ``%x`` = hexadecimal.


A continuación un ejemplo por cada tipo de datos:

::

    >>> print "CMS: %s, ¿Activar S o N?: %c" % ("Plone", "S")
    CMS: Plone, ¿Activar S o N?: S
    >>> print "N. factura: %d, Total a pagar: %f" % (345, 658.23)
    N. factura: 345, Total a pagar: 658.230000
    >>> print "Tipo Octal: %o, Tipo Hexadecimal: %x" % (027, 0x17)
    Tipo Octal: 27, Tipo Hexadecimal: 17


.. _python_str_formatter:

Clase formatter
~~~~~~~~~~~~~~~

``formatter`` es una de las clases integradas ``string``. Ese provee la habilidad 
de hacer variable compleja de substituciones y formateo de valores usando el método 
:ref:`format() <python_mtd_format>`. Es le permite crear y personalizar sus propios 
comportamientos de formatos de cadena de caracteres para reescribir los métodos 
públicos y contiene: ``format()``, ``vformat()``. Ese tiene algunos métodos que son 
destinado para ser remplazados por las sub-clases: ``parse()``, ``get_field()``, 
``get_value()``, ``check_unused_args()``, ``format_field()`` y ``convert_field()``. 


.. _python_mtd_format:

format()
````````

Este método devuelve una versión formateada de una cadena de caracteres, 
usando substituciones desde argumentos ``args`` y ``kwargs``. Las substituciones son 
identificadas entre llaves ``{ }`` dentro de la cadena de caracteres (llamados campos 
de formato), y son sustituidos en el orden con que aparecen como argumentos de 
``format()``, contando a partir de cero (*argumentos posicionales*).

Esto es una forma más clara y elegante es referenciar objetos dentro de la misma 
cadena, y usar este *método* para sustituirlos con los objetos que se le pasan como 
argumentos.

::

    >>> tipo_calculo = "raíz cuadrada de dos"
    >>> valor = 2**0.5
    >>> print "el resultado de {} es {}".format(tipo_calculo, valor)
    el resultado de raíz cuadrada de dos es 1.41421356237

También se puede referenciar a partir de la posición de los valores utilizando índices:

::

    >>> tipo_calculo = "raíz cuadrada de dos"
    >>> valor = 2**0.5
    >>> print "el resultado de {0} es {1}".format(tipo_calculo, valor)
    el resultado de raíz cuadrada de dos es 1.41421356237

Los objetos también pueden ser referenciados utilizando un identificador con una clave y 
luego pasarla como argumento al método:

::

    >>> tipo_calculo = "raíz cuadrada de dos"
    >>> print "el resultado de {nombre} es {resultado}".format(
    ...     nombre=tipo_calculo, resultado=2**0.5)
    el resultado de raíz cuadrada de dos es 1.41421356237


**Formateo avanzado**

Este método soporta muchas técnicas de formateo, aquí algunos ejemplos:

Alinear una cadena de caracteres a la derecha en 30 caracteres, con la siguiente 
sentencia:

::

    >>> print "{:>30}".format("raíz cuadrada de dos")
         raíz cuadrada de dos

Alinear una cadena de caracteres a la izquierda en 30 caracteres (crea espacios a 
la derecha), con la siguiente sentencia:

::

    >>> print "{:30}".format("raíz cuadrada de dos")
    raíz cuadrada de dos         

Alinear una cadena de caracteres al centro en 30 caracteres, con la siguiente 
sentencia:

::

    >>> print "{:^30}".format("raíz cuadrada de dos")
        raíz cuadrada de dos     

Truncamiento a 9 caracteres, con la siguiente sentencia:

::

    >>> print "{:.9}".format("raíz cuadrada de dos")
    raíz cua


Alinear una cadena de caracteres a la derecha en 30 caracteres con truncamiento 
de 9, con la siguiente sentencia:

::

    >>> print "{:>30.9}".format("raíz cuadrada de dos")
                         raíz cua


**Formateo por tipo**

Opcionalmente se puede poner el signo de dos puntos después del número o nombre, y 
explicitar el tipo del objeto:

- ``s`` para cadenas de caracteres (tipo :ref:`str <python_str>`).

- ``d`` para números enteros (tipo :ref:`int <python_numericos>`).

- ``f`` para números de coma flotante (tipo :ref:`float <python_num_float>`).


Esto permite controlar el formato de impresión del objeto. Por ejemplo, usted puede 
utilizar la expresión ``.4f`` para determinar que un número de coma flotante (``f``) 
se imprima con cuatro dígitos después de la coma (``.4``).

::

    >>> tipo_calculo = "raíz cuadrada de dos"
    >>> valor = 2**0.5
    >>> print "el resultado de {0} es {resultado:.4f}".format(
    ...     tipo_calculo, resultado=valor)
    el resultado de raíz cuadrada de dos es 1.4142

Formateo de números enteros, rellenados con espacios, con las siguientes sentencias:

::

    >>> print "{:4d}".format(10)
      10
    >>> print "{:4d}".format(100)
     100
    >>> print "{:4d}".format(1000)
    1000


Formateo de números enteros, rellenados con ceros, con las siguientes sentencias:

::

    >>> print "{:04d}".format(10)
    0010
    >>> print "{:04d}".format(100)
    0100
    >>> print "{:04d}".format(1000)
    1000

Formateo de números flotantes, rellenados con espacios, con las siguientes sentencias:

::

    >>> print "{:7.3f}".format(3.1415926)
      3.142
    >>> print "{:7.3f}".format(153.21)
    153.210

Formateo de números flotantes, rellenados con ceros, con las siguientes sentencias:

::

    >>> print "{:07.3f}".format(3.1415926)
    003.142
    >>> print "{:07.3f}".format(153.21)
    153.210


Convertir a cadenas de caracteres
.................................

Para convertir a *tipos cadenas de caracteres* debe usar la función :ref:`str() <python_fun_str>` 
la cual :ref:`esta integrada <python_fun_builtins>` en el interprete Python.

.. tip:: 
    Para más información consulte las funciones integradas para 
    :ref:`operaciones en cadenas de caracteres <python_fun_builtins_cadenas>`.


----

.. _python_str_ejs:

Ejemplos
........

A continuación, se presentan algunos ejemplos de su uso:


**Ejemplo de cadenas de caracteres con comillas simples**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 9-10


**Ejemplo de cadenas de caracteres con comillas dobles**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 13-14


**Ejemplo de cadenas de caracteres con código escapes**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 17-18


**Ejemplo de cadenas de caracteres con varias lineas**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 21-31


**Ejemplo operadores de repetición de cadenas de caracteres**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 34-35


**Ejemplo operadores de concatenación de cadenas de caracteres**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 38-40


**Ejemplo de medir tamaño de la cadena con función "len()"**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 43


**Ejemplo de acceder a rango de la cadena**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 46


**Ejemplo de consulta de ayuda a la función len**

::

    >>> help(len)

    Help on built-in function len in module __builtin__:

    len(...)
        len(object) -> integer
        
        Return the number of items of a sequence or collection.


**Ejemplo de consulta de ayuda a la clase int**

::

    >>> help(int)

    Help on class int in module __builtin__:

    class int(object)
     |  int(x=0) -> int or long
     |  int(x, base=10) -> int or long
     |  
     |  Convert a number or string to an integer, or return 0 if no arguments
     |  are given.  If x is floating point, the conversion truncates towards zero.
     |  If x is outside the integer range, the function returns a long instead.


**Ejemplo de consulta de ayuda del módulo**

::

    >>> import datetime
    >>> help(datetime)

    Help on built-in module datetime:

    NAME
        datetime - Fast implementation of the datetime type.

    FILE
        (built-in)

    CLASSES
        __builtin__.object
            date
                datetime


Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre las 
:ref:`cadenas de caracteres <python_str_cls>` desde la 
:ref:`consola interactiva <python_interactivo>` de la siguiente manera:

::

    >>> help(str)

Para salir de esa ayuda presione la tecla ``q``.

Usted puede consultar toda la documentación disponible sobre las cadenas de caracteres 
:ref:`unicode <python_unicode_cls>` desde la :ref:`consola interactiva <python_interactivo>` 
de la siguiente manera:

::

    >>> help(unicode)

Para salir de esa ayuda presione la tecla ``q``.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_cadenas.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_cadenas.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando: 

    ::

        python tipo_cadenas.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
