.. -*- coding: utf-8 -*-


.. _python_cls_tipos_builtins:

Clases de tipos integrados
--------------------------

Python integra varias clases de tipos en el modulo ``__builtin__``, a continuación se 
describen algunas clases:


.. _python_cls_builtins_generales:

Clases generales
................

Las clases de uso general se describen a continuación:


.. _python_cls_buffer:

buffer
~~~~~~

El objeto de la clase ``buffer()`` crea un nuevo objeto de búfer que haga referencia 
al objeto dado. El búfer hará referencia a una porción del objeto de destino desde el 
inicio del objeto (o en el desplazamiento especificado). La división se extenderá hasta 
el final del objeto de destino (o con el tamaño especificado).

::

    >>> cadena = 'Hola mundo'
    >>> cadena
    'Hola mundo'
    >>> cadena[5:10]
    'mundo'
    >>> type(cadena)
    <type 'str'>
    >>> cadena_buffer = buffer(cadena, 5, 5)
    >>> type(cadena_buffer)
    <type 'buffer'>
    >>> cadena_buffer
    <read-only buffer for 0x7f42121d3810, size 5, offset 5 at 0x7f42121d23b0>
    >>> print cadena_buffer
    mundo

El búfer en este caso anterior es una sub-cadena, inicia en la posición 5 con un 
ancho de 5 caracteres y es no toma espacio de almacenamiento extra - eso referencia 
a un ``slice`` de una cadena de caracteres.

Este ejemplo anterior no es muy útil para cadenas de caracteres cortas como esta, 
pero eso puede ser necesario cuando usa un gran numero de data. Este ejemplo puede 
usar un tipo mutable ``bytearray()``:

::

    >>> cadena = bytearray(1000000)
    >>> type(cadena)
    <type 'bytearray'>
    >>> cadena_buffer = buffer(cadena, 1)
    >>> cadena_buffer
    <read-only buffer for 0x7f42121d3870, size -1, offset 1 at 0x7f42121d2270>
    >>> type(cadena_buffer)
    <type 'buffer'>
    >>> cadena_buffer[0]
    '\x00'
    >>> cadena[1]
    0
    >>> cadena[1] = 5
    >>> cadena[1]
    5
    >>> cadena_buffer[0]
    '\x05'

Esto puede ser muy útil si usted quiere tener más que una vista en la data y no quiere 
(o puede) contener múltiples copias en memoria.

Note que el búfer ha sido remplazado por el mejor llamado :ref:`memoryview() <python_cls_memoryview>` 
en Python 3, aunque se puede usar en Python 2.7.

Note también que usted no puede implementar una interfaz búfer para sus propios objetos 
sin profundizando en la API de C, ej. usted no puede hacer eso con puramente con código 
Python.

En general un ``slice`` tomará extra almacenamiento, entonces, si ``cadena[5:10]`` será 
una copia. Si usted define ``cadena_buffer = cadena[5:10]`` y entonces ``del cadena``, 
eso liberaría la memoria que fue tomada por ``cadena``, proveyendo que ``cadena_buffer`` 
fue copiada. (Para usar esto usted necesita una gran cadena de caracteres, en este ejemplo 
``cadena`` y rastrear el uso de la memoria de Python). Es sin embargo mucho más eficiente 
que hacer la copia si no existe mucha data involucrada.


.. _python_cls_bytes:

bytes
~~~~~

El objeto de la clase ``bytes`` es agregada en Python 2.6 como un sinónimo para el tipo 
:ref:`str <python_str>` y este también soporta la notación ``b''``.

El uso principal de bytes en Python 2.6 será escribir pruebas de tipo de objeto como 
``isinstance(x, bytes)``. Esto ayudará al convertidor ``2to3``, que no puede decir si 
el código 2.x pretende que las cadenas contengan caracteres o bytes de 8 bits; ahora 
puede usar ``bytes`` o ``str`` para representar exactamente su intención, y el código 
resultante también será correcto en Python 3.0.

::

    >>> arreglo = bytes("Python es interesante.")
    >>> print arreglo
    Python es interesante.
    >>> type(arreglo)
    <type 'str'>


.. _python_cls_staticmethod:

staticmethod
~~~~~~~~~~~~

La clase ``staticmethod`` convierte una función a un método estático. Un método 
estático no recibe un argumento primero implícito. Un método estático no recibe 
un primer argumento implícito. La sintaxis es la siguiente:

::

    >>> staticmethod(function) -> método
    >>>

Para declarar un método estático, use este lenguaje:

::

    class Clase:
        @staticmethod
        def funcion(argumento1, argumento2, ...):
            ...


Se puede llamar en la clase (por ejemplo, ``Clase.funcion()``) o en una instancia (por ejemplo,
``Clase().funcion()``). La instancia se ignora a excepción de su clase.

Los métodos estáticos son similares a los métodos estáticos ``Java`` o ``C++``. Para 
un concepto más avanzado, mire la clase :ref:`classmethod <python_cls_classmethod>` 
integrada en el interprete.

.. todo:: TODO escribir sobre esta clase integrada.


.. comments:

    .. _python_cls_builtins_bool:

    Clases de booleanos
    ...................

    Las clases de tipos :ref:`booleanos <python_bool>` se describen a continuación:


    .. _python_clase_bool:

    bool()
    ~~~~~~

    La clase ``bool()``, es un constructor, el cual crea un tipo de datos 
    :ref:`booleanos <python_bool>`, devuelve un tipo booleano ``True`` cuando el 
    argumento dado es ``True``, de lo contrario ``False``.

    ::

        >>> bool(True)
        True
        >>> bool()
        False


.. _python_cls_builtins_secue:

Clases de secuencias
....................

Las clases de tipos secuencias se describen a continuación:


.. _python_cls_enumerate:

enumerate
~~~~~~~~~

La clase ``enumerate`` devuelve un objeto *enumerate*.  El iterable debe ser otro objeto 
que soporte :ref:`iteradores <python_iter>`. El objeto *enumerate* produce pares que 
contiene una cuenta (desde donde inicia, el cual el valor por defecto es cero) y un valor 
producido por el argumento iterable. 

Cuando la iteración de la secuencia llega al final se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la iteración. 
El objeto enumerate es muy útil para obtener una lista indexada como: 
``(0, seq[0]), (1, seq[1]), (2, seq[2]), ...``.

::

    >>> enumerar = enumerate(xrange(3))
    >>> enumerar.next()
    (0, 0)
    >>> enumerar.next()
    (1, 1)
    >>> enumerar.next()
    (2, 2)
    >>> enumerar.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior usa una secuencia numérica de 3 elementos generada por la función 
integrada :ref:`xrange() <python_fun_xrange>`.

A continuación se le pasa el parámetro de *inicio* con el valor *1* de la secuencia 
generada por la clase ``enumerate``:

::

    >>> enumerar = enumerate(xrange(3), 1)
    >>> enumerar.next()
    (1, 0)
    >>> enumerar.next()
    (2, 1)
    >>> enumerar.next()
    (3, 2)
    >>> enumerar.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior usa una secuencia numérica de 3 elementos generada con el valor 
inicial de *1* por la función integrada :ref:`xrange() <python_fun_xrange>`.


.. _python_cls_reversed:

reversed
~~~~~~~~

La clase ``reversed`` devolver un :ref:`iterador <python_iter>` inverso sobre los 
valores de la secuencia, cuando la iteración de la secuencia llega al final se llama 
a la excepción :ref:`StopIteration <python_exception_stopiteration>` y se causa el 
detener la iteración.

::

    >>> inversa = reversed(xrange(3))
    >>> inversa.next()
    2
    >>> inversa.next()
    1
    >>> inversa.next()
    0
    >>> inversa.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior usa una secuencia numérica de 3 elementos generada por la 
función integrada :ref:`xrange() <python_fun_xrange>`.


.. _python_cls_builtins_archivos:

Clases de archivos
..................

Las clases de tipos *archivos* se describen a continuación:


.. _python_cls_file:

file()
~~~~~~

El objeto ``file()`` se implementan con el paquete del lenguaje C ``stdio`` y se pueden 
crear con la función interna :ref:`open() <python_fun_open>`. También son el resultado 
de otras funciones y métodos internos, por ejemplo, ``os.popen()`` y ``os.fdopen()`` y 
el método ``makefile()`` de los objetos ``socket``.

Cuando falla una operación de archivos por una cuestión de E/S, se lanza la excepción 
:ref:`IOError <python_exception_ioerror>`. Esto incluye situaciones donde la operación 
no esté definida por cualquier motivo, como usar :ref:`seek() <python_mtd_seek>` 
en un dispositivo ``tty`` o intentar escribir en un archivo abierto para lectura.

Métodos
````````

El objeto ``file()`` implementa los siguientes métodos integrados:


.. _python_mtd_close:

close()
"""""""

El método ``close()`` permite cerrar la manipulación del archivo. No es posible escribir 
ni leer en un archivo cerrado. Cualquier operación que requiera que el archivo esté 
abierto lanzará :ref:`IOError <python_exception_ioerror>` si el archivo se ha cerrado. 
Está permitido llamar a ``close()`` más de una vez.

Una vez que se terminó de usar el archivo es necesario cerrarlo, para liberar los 
recursos tomados por el manejo del archivo. Eso se hace con la sentencia ``archivo.close()``:

::

    >>> archivo.close() # cierra el archivo datos.txt


Luego de lo cual no se puede acceder al archivo ``datos.txt``, si intenta una llamada a 
la método :ref:`archivo.read() <python_mtd_read>` devuelve una excepción 
:ref:`ValueError <python_exception_valueerror>`, porque el archivo está cerrado:

::

    >>> archivo.close()
    >>> archivo.read()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: I/O operation on closed file


.. tip:: Para más detalles: http://docs.python.org/tutorial/inputoutput.html


.. _python_mtd_flush:

flush()
"""""""

El método ``flush()`` permite descargar el tampón interno, como la función de lenguaje C 
``fflush()`` de la librería ``stdio``. Puede no tener efecto en ciertos objetos similares 
a los archivos.

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de este método integrado.


.. _python_mtd_isatty:

isatty()
""""""""

El método ``isatty()`` devuelve ``True`` si el archivo está conectado a un dispositivo 
``tty`` (un terminal interactivo de líneas de orden), en caso contrario, ``False``. 

.. note:: 
    Si un objeto similar a los archivos no está asociado a un archivo real, no debe 
    implementar este método.

::

    >>> archivo = open('datos.txt', 'r')
    >>> archivo.isatty()
    False


.. _python_mtd_fileno:

fileno()
""""""""

El método ``fileno()`` devuelve el "descriptor de archivo" utilizado por la 
implementación subyacente para solicitar operaciones E/S del sistema operativo. 
Puede ser útil para interfaces de bajo nivel que utilicen descriptores de archivos, 
por ejemplo, el módulo ``fcntl`` o ``os.read()`` y similares. 

.. note:: 
    Si un objeto similar a los archivos no tiene un descriptor de archivo, no debe 
    implementar este método.

::

    >>> archivo = open("datos.txt",mode="r")
    >>> archivo.fileno()
    6

.. _python_mtd_next:

next()
""""""

El método ``next()`` permite usar un iterador para tratar cada linea del archivo como 
el próximo valor, cuando la iteración del archivo llega al final se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la 
iteración.

::

    >>> archivo = open('/etc/hostname')
    >>> archivo
    <open file '/etc/hostname', mode 'r' at 0x7fa44ba379c0>
    >>> archivo.__iter__()
    <open file '/etc/hostname', mode 'r' at 0x7fa44ba379c0>
    >>> iter(archivo)
    <open file '/etc/hostname', mode 'r' at 0x7fa44ba379c0>
    >>> archivo is archivo.__iter__()
    True
    >>> linea = archivo.__iter__()
    >>> linea.next()
    'laptop\n'
    >>> linea.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration


.. _python_mtd_read:

read()
""""""

El método ``read()`` permite leer el contenido del archivo. El argumento es opcional 
y si no se especifica (o es -1) devuelve el contenido de todo el archivo. Una vez que 
se leyó todo el archivo, una nueva llamada a la función devuelve una cadena vacía ('').

::

    >>> archivo = open('datos.txt', 'r')
    >>> archivo.read()
    'Este es una prueba \ny otra prueba'
    >>> archivo.read()
    ''

Si desea recibir una salida formateada por consola leyendo un archivo, a continuación 
un ejemplo:

::

    >>> archivo = open('datos.txt', 'r')
    >>> contenido = archivo.read()
    >>> print contenido
    Este es una prueba
    y otra prueba


.. _python_mtd_readline:

readline()
""""""""""

El método ``readline()`` permite leer una sola línea del archivo, devuelve al final de 
la línea el carácter de nueva línea y solo se omite en la última línea del archivo (si 
no termina con el carácter de nueva línea). Esto hace que el valor de retorno no sea 
ambiguo. Si devuelve una cadena de caracteres vacía se alcanzó el fin del archivo, 
mientras que una línea en blanco se representa con un carácter de nueva línea.

::

    >>> archivo = open('datos.txt', 'r')
    >>> print archivo.readline() # lee la linea "Este es una prueba "
    >>> print archivo.readline() # lee la linea "y otra prueba"
    >>> print archivo.readline()
        
    >>> 


.. _python_mtd_readlines:

readlines()
"""""""""""

El método ``readlines()`` devuelve una lista que contiene todas las líneas del archivo.

::

    >>> archivo = open('datos.txt', 'r')
    >>> lineas = archivo.readlines()
    >>> print lineas
    ['Este es una prueba \n', 'y otra prueba']


.. _python_mtd_seek:

seek()
""""""

El método ``seek()`` mueve la posición actual del cursos del archivo, como la función 
del lenguaje C ``fseek()`` de la librería ``stdio``. No devuelve ningún valor.

El método ``seek()`` lleva la siguiente nomenclatura:

::

    >>> seek(posicion_actual[, punto_referencia])

A continuación, un ejemplo que escribir y leer el archivo ``datos.txt`` agregando una 
lista de lineas al principio del archivo, como al final del archivo:

::

    >>> archivo = open('datos.txt', 'w')
    >>> lista_de_lineas = ["Esta es la 1er linea", \
    ...     "Esta es la 2da linea", "Esta es la 3era linea"]
    >>> archivo.writelines("\n".join(lista_de_lineas))
    >>> archivo.close()
    >>> archivo = open('datos.txt', 'r')
    >>> archivo.next()
    'Esta es la 1er linea\n'
    >>> archivo.seek(8)
    >>> archivo.next()
    'la 1er linea\n'
    >>> archivo.next()
    'Esta es la 2da linea\n'
    >>> archivo.next()
    'Esta es la 3era linea'
    >>> archivo.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration
    >>> archivo.close()

En el ejemplo anterior, puede ver que se escriben tres lineas y se pasa como argumento 
``posicion_actual`` el valor *8* el cual posiciona el curso de búsqueda en dicha posición 
de la primera linea con ``archivo.seek(8)`` y muestra una parte de la linea.

El argumento ``punto_referencia`` es opcional, con un valor predeterminado de ``0`` (es 
el principio del archivo); otros valores posibles son ``1`` (la posición actual del 
archivo) y ``2`` (el final del archivo). No hay valor de retorno.

::

    >>> archivo = open('datos.txt', 'w')
    >>> lista_de_lineas = ["Esta es la 1er linea", \
    ...     "Esta es la 2da linea", "Esta es la 3era linea"]
    >>> archivo.writelines("\n".join(lista_de_lineas))
    >>> archivo.close()
    >>> archivo = open('datos.txt', 'r')
    >>> archivo.next()
    'Esta es la 1er linea\n'
    >>> archivo.seek(8)
    >>> archivo.next()
    'la 1er linea\n'
    >>> archivo.close()
    >>> archivo = open('datos.txt', 'rw+')
    >>> nuevas_lineas = ["\nEsta es la 4ta linea", \
    ...     "Esta es la 5ta linea"]
    >>> # Escribe la secuencia de la lineas al final del archivo.
    ... archivo.seek(0, 2)
    >>> archivo.writelines("\n".join(nuevas_lineas))
    >>> # Ahora lea completamente el archivo desde el inicio.
    ... archivo.seek(0,0)
    >>> for elemento in range(1, 6):
    ...    linea = archivo.next()
    ...    print "Linea No %d - %s" % (elemento, linea)
    ... 
    Linea No 1 - Esta es la 1er linea

    Linea No 2 - Esta es la 2da linea

    Linea No 3 - Esta es la 3era linea

    Linea No 4 - Esta es la 4ta linea

    Linea No 5 - Esta es la 5ta linea
    >>> # Cerrar archivo abierto
    ... archivo.close()
    >>> 

En el ejemplo anterior se pudo usar el método ``seek()`` con el argumento 
``punto_referencia`` al final del archivo para agregar nuevas lineas y luego se uso 
de nuevo el argumento ``punto_referencia`` para ubicarse al inicio del archivo para 
mostrar todo el contenido del archivo.


.. _python_mtd_tell:

tell()
""""""

El método ``tell()`` devuelve la posición actual del archivo, como la función del 
lenguaje C ``ftell()`` de la librería ``stdio``.

::

    >>> archivo = open('/etc/hostname')
    >>> archivo.tell()
    0
    >>> linea = iter(archivo)
    >>> linea.next()
    'debacagua9\n'
    >>> archivo.tell()
    11
    >>> len('debacagua9\n')
    11
    >>> linea.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration
    >>> archivo.tell()
    11

Cuando la iteración de la secuencia llega al final se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la iteración. 


.. _python_mtd_truncate:

truncate()
""""""""""

::

    >>> archivo = open('datos.txt', 'w')
    >>> archivo.write('Este es una prueba \ny otra prueba')
    >>> archivo.truncate(20)
    >>> archivo.close()
    >>> archivo = open('datos.txt', 'r')
    >>> archivo.read()
    'Este es una prueba \n'

El método ``truncate()`` trunca el archivo. Si se proporciona el argumento opcional, 
el archivo se trunca a (como mucho) ese tamaño. El tamaño depende de la posición 
actual. La disponibilidad de esta función depende de la versión del sistema operativo 
(por ejemplo, no todas las versiones de Unix dan soporte a esta operación).


.. _python_mtd_write:

write()
"""""""

El método ``write()`` permite escribir el contenido de la cadena de texto al archivo, 
y devuelve la cantidad de caracteres escritos.

Para escribir algo que no sea una cadena de caracteres, antes se debe convertir a 
cadena de caracteres.

::

    >>> archivo = open('datos.txt', 'w')
    >>> # escribe el archivo datos.txt
    ... archivo.write('Este es una prueba \ny otra prueba')
    >>>


.. _python_fun_writelines:

writelines()
""""""""""""

El método ``writelines()`` escribe una lista de cadenas al archivo. No se devuelve 
ningún valor. El nombre es paralelo a ``readlines()``, ``writelines()`` no añade 
separadores de línea.

::

    >>> archivo = open('datos.txt', 'w')
    >>> lista_de_lineas = ['Plone es el más poderoso, ', \
    ...     'escalable, seguro ', 'y longevo CMS, ', \
    ...     'escrito en Python.']
    >>> archivo.writelines("\n".join(lista_de_lineas))
    >>> archivo.close()


Atributos
`````````

Los objetos archivo también ofrecen otros atributos interesantes. No son necesarios 
para los objetos de interfaz tipo archivo, pero deberían implementarse si tienen 
sentido en un objeto particular.


.. _python_attr_closed:

closed
""""""

El atributo ``closed`` del objeto :ref:`file <python_cls_file>` de tipo 
:ref:`booleano <python_bool>` indica el estado actual. Es un atributo de sólo lectura, 
que se cambia mediante el método :ref:`close() <python_mtd_close>`. Puede no estar 
disponible en todos los objetos con interfaz tipo archivo.

::

    >>> archivo = open('datos.txt', 'w')
    >>> archivo.closed
    False
    >>> archivo.close()
    >>> archivo.closed
    True


.. _python_attr_mode:

mode
""""

El atributo ``mode`` del objeto :ref:`file <python_cls_file>`, es el modo de E/S del 
archivo. Si se creó el archivo con la función integrada :ref:`open() <python_fun_open>`, 
será el valor del parámetro ``mode``. Es un atributo de sólo lectura y puede no estar 
disponible en todos los objetos con interfaz tipo archivo.

::

    >>> archivo = open('datos.txt', 'w')
    >>> archivo.mode
    'w'


.. _python_attr_name:

name
""""

El atributo ``name`` del objeto :ref:`file <python_cls_file>`, es el nombre del archivo 
si se creó el objeto archivo mediante la función integrada :ref:`open() <python_fun_open>`, 
el nombre del archivo. En caso contrario, alguna cadena que indique el origen del archivo, 
de la forma "<...>". Es un atributo de sólo lectura y puede no estar disponible en todos 
los objetos con interfaz tipo archivo.

::

    >>> archivo = open('datos.txt', 'w')
    >>> archivo.name
    'datos.txt'


.. _python_attr_encoding:

encoding
""""""""

El atributo ``encoding`` del objeto :ref:`file <python_cls_file>`, es el encoding 
del archivo.

::

    >>> with open("datos.txt",mode="r") as archivo:
    ...     print "Encoding por defecto:", archivo.encoding
    ...     archivo.close()
    ... 
    Encoding por defecto: None


.. _python_attr_softspace:

softspace
"""""""""

El atributo ``softspace`` del objeto :ref:`file <python_cls_file>` del tipo 
:ref:`booleano <python_bool>` indica si se debe escribir un espacio antes de escribir 
otro valor al usar la sentencia :ref:`print <python_sent_print>`. Las clases que intenten 
simular un objeto archivo deberían tener un atributo escribible ``softspace``, que 
debería inicializarse a cero.

Esto será automático en la mayoría de las clases implementadas en Python (se debe 
tener cuidado en las clases que redefinan el acceso a los atributos). Los tipos 
implementados en el lenguaje C tendrán que proporcionar un atributo ``softspace`` 
escribible. 

Nota: Este atributo no se usa para controlar la sentencia ``print``, sino para permitir 
que la implementación de ``print`` lleve la cuenta de su estado interno.

::

    >>> archivo.softspace
    0

.. todo:: TODO escribir un ejemplo del uso de este atributo integrado.


.. _python_cls_builtins_objetos:

Clases de objetos
.................

Las clases de objetos se describen a continuación:


.. _python_cls_classmethod:

classmethod
~~~~~~~~~~~

La clase ``classmethod`` convierte una función para ser un método de clase. Un método 
de clase recibe la clase como primer argumento implícito, al igual que un método de 
instancia recibe la instancia. La sintaxis es la siguiente:

::

    >>> classmethod(function) -> método

.. todo:: TODO escribir un ejemplo real del uso de esta clase integrada.

Para declarar un método de clase, use este idioma:

::

    class Clase:
        @classmethod
        def funcion(cls, argumento1, argumento2, ...):
            ...

Se puede llamar en la clase (por ejemplo, ``Clase.funcion()``) o en una instancia (por ejemplo, 
``Clase().funcion()``). La instancia se ignora a excepción de su clase. Si se llama a un método 
de clase para una clase derivada, el objeto de clase derivada se pasa como el primer 
argumento implícito.

Los métodos de clase son diferentes a los métodos estáticos ``C++`` o ``Java``. Si 
quieres eso, mira la clase :ref:`staticmethod <python_cls_staticmethod>` integrada en 
el interprete.

.. todo:: TODO escribir sobre esta clase integrada.


.. _python_cls_memoryview:

memoryview
~~~~~~~~~~

La clase ``memoryview`` crea un nuevo objecto *memoryview* el cual referencias al objecto 
dado. La sintaxis es la siguiente:

::

    >>> memoryview(object)

A continuación unos ejemplos básico de su uso:

::

    >>> cadena = bytearray(1000000)
    >>> memoryview(cadena)
    <memory at 0x7f6202179cc8>
    >>> memoryview(cadena).format
    'B'
    >>> memoryview(cadena).itemsize
    1L
    >>> memoryview(cadena).ndim
    1L
    >>> memoryview(cadena).readonly
    False
    >>> memoryview(cadena).shape
    (1000000L,)
    >>> memoryview(cadena).strides
    (1L,)
    >>> memoryview(cadena).suboffsets
    >>> cadena_buffer = buffer(cadena, 1)
    >>> memoryview(cadena_buffer)
    <memory at 0x7f6202179cc8>
    >>> memoryview(cadena_buffer).format
    'B'
    >>> memoryview(cadena_buffer).itemsize
    1L
    >>> memoryview(cadena_buffer).ndim
    1L
    >>> memoryview(cadena_buffer).readonly
    True
    >>> memoryview(cadena_buffer).shape
    (999999L,)
    >>> memoryview(cadena_buffer).strides
    (1L,)
    >>> memoryview(cadena_buffer).suboffsets


.. todo:: TODO terminar de escribir sobre esta clase integrada memoryview.


.. _python_cls_object:

object
~~~~~~

El objeto de la clase ``object`` es el tipo más básico de objeto, es integrado en 
el módulo ``__builtin__``. Este objeto se usa como :ref:`herencia <python_poo_herencia>` 
cuando se crea una nueva clase en Python.

Todo, incluyendo las clases y tipos de Python son instancias de ``object``. Para 
corroborar si un objeto es instancia de una clase se utiliza la función 
:ref:`isinstance() <python_fun_isinstance>`.

::

    >>> object
    <type 'object'>


.. _python_cls_property:

property
~~~~~~~~

La clase ``property`` típicamente es usado para definir un atributo administrado.
La sintaxis es la siguiente:

::

    >>> property(fget=None, fset=None,
    ...     fdel=None, doc=None) # devuelve atributo property

El parámetro ``fget`` es una función a ser usada para obtener un valor de un atributo, 
y igualmente el parámetro ``fset`` es una función para definir el valor de un atributo, 
y el parámetro ``fdel`` es una función para eliminar un atributo. 

::

    >>> class Clase(object):
    ...     def get_atributo(self): return self._atributo
    ...     def set_atributo(self, valor): self._atributo = valor
    ...     def del_atributo(self): del self._atributo
    ...     atributo = property(get_atributo, 
    ...         set_atributo, del_atributo, 
    ...         "Yo soy la propiedad 'atributo'.")
    ... 
    >>> c = Clase()
    >>> dir(c)
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', 
    '__getattribute__', '__hash__', '__init__', '__module__', 
    '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
    '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
    '__weakref__', 'atributo', 'del_atributo', 'get_atributo',
    'set_atributo']

Los decoradores facilitan la definición de nuevas propiedades o la modificación de 
las existentes:

::

    >>> class Clase(object):
    ...     @property
    ...     def atributo(self):
    ...         "Yo soy la propiedad 'atributo'."
    ...         return self._atributo
    ...     @atributo.setter
    ...     def atributo(self, valor):
    ...         self._atributo = valor
    ...     @atributo.deleter
    ...     def atributo(self):
    ...         del self._atributo
    ... 
    >>> c = Clase()
    >>> dir(c)
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', 
    '__getattribute__', '__hash__', '__init__', '__module__',
    '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
    '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    '__weakref__', 'atributo']

.. todo:: TODO terminar de escribir sobre la clase integrada property.


.. _python_cls_super:

super
~~~~~

La clase ``super`` típicamente es usada al llamar un método de superclase cooperativo.
La sintaxis son las siguientes:

::

    >>> super(type, obj) # devuelve un súper objeto enlazado; requiere isinstance(obj, type)
    >>> super(type) # devuelve un súper objeto no unido
    >>> super(type, type2) # devuelve un súper objeto enlazado; requiere issubclass(type2, type)


Para declarar un método de superclase cooperativo, use este idioma:

::

    class ClaseBase():
        def metodo(self, argumento):
            pass
    class Clase(ClaseBase):
        def metodo(self, argumento):
            super(Clase, self).metodo(argumento)

.. todo:: TODO terminar de escribir sobre la clase integrada super.


.. _python_cls_type:

type
....

Los :ref:`objetos tipo <python_types_objs>` representan los diversos tipos de objeto. 
El tipo de un objeto es accesible mediante la función integrada 
:ref:`type() <python_fun_type>`. No hay operaciones especiales sobre los tipos. El 
módulo estándar ``types`` define nombres para todos los tipos internos estándar.

::

    >>> type(type)
    <type 'type'>


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion9>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
