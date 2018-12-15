.. -*- coding: utf-8 -*-


.. _python_cls_tipos_builtins:

Clases de tipos integrados
--------------------------

Python integra varias clases de tipos en el modulo ``__builtin__``, a continuación se 
describen algunas clases:

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


.. _python_cls_builtins_archivos:

Clases de archivos
..................

Las clases de tipos *archivos* se describen a continuación:


.. _python_cls_file:

file()
~~~~~~

El objeto ``file()`` se implementan con el paquete C ``stdio`` y se pueden crear con 
la función interna :ref:`open() <python_fun_open>`. También son el resultado de otras 
funciones y métodos internos, por ejemplo, ``os.popen()`` y ``os.fdopen()`` y el método 
``makefile()`` de los objetos ``socket``.

Cuando falla una operación de ficheros por una cuestión de E/S, se lanza la excepción 
:ref:`IOError <python_exception_ioerror>`. Esto incluye situaciones donde la operación 
no esté definida por cualquier motivo, como usar :ref:`seek() <python_mtd_seek>` 
en un dispositivo ``tty`` o intentar escribir en un fichero abierto para lectura.

Métodos
````````

El objeto ``file()`` implementa los siguientes métodos integrados:


.. _python_mtd_close:

close()
"""""""

El método ``close()`` permite cerrar la manipulación del archivo. No es posible escribir 
ni leer en un fichero cerrado. Cualquier operación que requiera que el fichero esté 
abierto lanzará :ref:`IOError <python_exception_ioerror>` si el fichero se ha cerrado. 
Está permitido llamar a ``close()`` más de una vez.

Una vez que se terminó de usar el archivo es necesario cerrarlo, para liberar los 
recursos tomados por el manejo del archivo. Eso se hace con la sentencia ``f.close()``:

::

    >>> f.close() # cierra el archivo datos.txt


Luego de lo cual no se puede acceder al archivo ``datos.txt``, si intenta una llamada a 
la método :ref:`f.read() <python_mtd_read>` devuelve una excepción 
:ref:`ValueError <python_exception_valueerror>`, porque el archivo está cerrado:

::

    >>> f.close()
    >>> f.read()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: I/O operation on closed file


.. tip:: Para más detalles: http://docs.python.org/tutorial/inputoutput.html


.. _python_mtd_flush:

flush()
"""""""

El método ``flush()`` permite descargar el tampón interno, como la función C ``fflush()`` 
de la librería ``stdio``. Puede no tener efecto en ciertos objetos similares a los 
ficheros.

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_mtd_isatty:

isatty()
""""""""

El método ``isatty()`` devuelve ``True`` si el fichero está conectado a un dispositivo 
``tty`` (un terminal interactivo de líneas de orden), en caso contrario, ``False``. 

.. note:: 
    Si un objeto similar a los ficheros no está asociado a un fichero real, no debe 
    implementar este método.

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_mtd_fileno:

fileno()
""""""""

El método ``fileno()`` devuelve el "descriptor de fichero" utilizado por la 
implementación subyacente para solicitar operaciones E/S del sistema operativo. 
Puede ser útil para interfaces de bajo nivel que utilicen descriptores de ficheros, 
por ejemplo, el módulo ``fcntl`` o ``os.read()`` y similares. 

.. note:: 
    Si un objeto similar a los ficheros no tiene un descriptor de fichero, no debe 
    implementar este método.

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_mtd_next:

next()
""""""

El método ``next()`` permite x.next() -> el próximo valor, o causa una 
:ref:`StopIteration <python_exception_stopiteration>`

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_mtd_read:

read()
""""""

El método ``read()`` permite leer el contenido del archivo. El argumento es opcional 
y si no se especifica (o es -1) devuelve el contenido de todo el archivo. Una vez que 
se leyó todo el archivo, una nueva llamada a la función devuelve una cadena vacía ('').

::

    >>> f = open('datos.txt', 'r')
    >>> f.read()
    'Este es una prueba \ny otra prueba'
    >>> f.read()
    ''

Si desea recibir una salida formateada por consola leyendo un archivo, a continuación 
un ejemplo:

::

    >>> f = open('datos.txt', 'r')
    >>> s = f.read()
    >>> print s
    This is a test
    and another test


.. _python_mtd_readline:

readline()
""""""""""

El método ``readline()`` permite leer una sola línea del archivo, devuelve al final de 
la línea el carácter de nueva línea y solo se omite en la última línea del archivo (si 
no termina con el carácter de nueva línea). Esto hace que el valor de retorno no sea 
ambiguo. Si devuelve una cadena de caracteres vacía se alcanzó el fin del archivo, 
mientras que una línea en blanco se representa con un carácter de nueva línea.

::

    >>> f = open('datos.txt', 'r')
    >>> print f.readline() # lee la linea "Este es una prueba "
    >>> print f.readline() # lee la linea "y otra prueba"
    >>> print f.readline()
        
    >>> 


.. _python_mtd_readlines:

readlines()
"""""""""""

El método ``readlines()`` devuelve una lista que contiene todas las líneas del archivo.

::

    >>> f = open('datos.txt', 'r')
    >>> lines = f.readlines()
    >>> print(lines)
    ['Este es una prueba \n', 'y otra prueba']


.. _python_mtd_seek:

seek()
""""""

El método ``seek()`` establece la posición actual del fichero, como la función C 
``fseek()`` de la librería ``stdio``.

::

    seek(offset[, whence]) -> None.  Move to new file position.

El argumento ``whence`` es opcional, con un valor predeterminado de ``0`` (posicionamiento 
absoluto); otros valores posibles son ``1`` (posicionamiento relativo a la posición actual) 
y ``2`` (posicionamiento relativo al final del fichero). No hay valor de retorno.


.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_mtd_tell:

tell()
""""""

El método ``tell()`` devuelve la posición actual del fichero, como la función C ``ftell()`` 
de la librería ``stdio``.

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_mtd_truncate:

truncate()
""""""""""

::

    truncate([size]) -> None

El método ``truncate()`` trunca el fichero. Si se proporciona el argumento opcional ``size``, 
el fichero se trunca a (como mucho) ese tamaño. El tamaño depende de la posición actual. La 
disponibilidad de esta función depende de la versión del sistema operativo (por ejemplo, no 
todas las versiones de Unix dan soporte a esta operación).

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_mtd_write:

write()
"""""""

El método ``write()`` permite escribir el contenido de la cadena de texto al archivo, 
y devuelve la cantidad de caracteres escritos.

Para escribir algo que no sea una cadena de caracteres, antes se debe convertir a 
cadena de caracteres.

::

    >>> f = open('datos.txt', 'w')
    >>> # escribe el archivo datos.txt
    ... f.write('Este es una prueba \ny otra prueba')
    >>>


.. _python_fun_writelines:

writelines()
""""""""""""

El método ``writelines()`` escribe una lista de cadenas al fichero. No se devuelve 
ningún valor. El nombre es paralelo a ``readlines()``, ``writelines()`` no añade 
separadores de línea.

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


Atributos
`````````

Los objetos fichero también ofrecen otros atributos interesantes. No son necesarios 
para los objetos de interfaz tipo fichero, pero deberían implementarse si tienen 
sentido en un objeto particular.


.. _python_atributo_closed:

closed
""""""

El atributo ``closed`` del objeto *fichero* de tipo :ref:`booleano <python_bool>` 
indica el estado actual. Es un atributo de sólo lectura, que se cambia mediante el 
método :ref:`close() <python_mtd_close>`. Puede no estar disponible en todos los 
objetos con interfaz tipo fichero.

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_atributo_mode:

mode
""""

El atributo ``mode`` del objeto *fichero*, es el modo de E/S del fichero. Si se creó 
el fichero con la función integrada :ref:`open() <python_fun_open>`, será el valor 
del parámetro ``mode``. Es un atributo de sólo lectura y puede no estar disponible 
en todos los objetos con interfaz tipo fichero.

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_atributo_name:

name
""""

El atributo ``name`` del objeto *fichero*, es el nombre del fichero si se creó el objeto 
fichero mediante la función integrada :ref:`open() <python_fun_open>`, el nombre del 
fichero. En caso contrario, alguna cadena que indique el origen del fichero, de la forma 
"<...>". Es un atributo de sólo lectura y puede no estar disponible en todos los objetos 
con interfaz tipo fichero.

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_atributo_encoding:

encoding
""""""""

El atributo ``encoding`` del objeto *fichero* es el encoding del fichero.

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_atributo_errors:

errors
""""""

El atributo ``errors`` del objeto *fichero* es el manipulador de error Unicode.

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_atributo_softspace:

softspace
"""""""""

El atributo ``softspace`` del objeto *fichero* de tipo :ref:`booleano <python_bool>` 
indica si se debe escribir un espacio antes de escribir otro valor al usar la sentencia 
:ref:`print <python_sent_print>`. Las clases que intenten simular un objeto fichero 
deberían tener un atributo escribible ``softspace``, que debería inicializarse a cero. 

Esto será automático en la mayoría de las clases implementadas en Python (se debe 
tener cuidado en las clases que redefinan el acceso a los atributos). Los tipos 
implementados en C tendrán que proporcionar un atributo ``softspace`` escribible. 

Nota: Este atributo no se usa para controlar la sentencia ``print``, sino para permitir 
que la implementación de ``print`` lleve la cuenta de su estado interno.

::

    >>>

.. todo:: TODO escribir un ejemplo del uso de esta función integrada.


.. _python_cls_object:

object
......

El objeto de la clase ``object`` es el tipo más básico de objeto, es integrado en 
el módulo ``__builtin__``. Este objeto se usa como :ref:`herencia <python_poo_herencia>` 
cuando se crea una nueva clase en Python.

Todo, incluyendo las clases y tipos de Python son instancias de ``object``. Para 
corroborar si un objeto es instancia de una clase se utiliza la función 
:ref:`isinstance() <python_fun_isinstance>`.

::

    >>> object
    <type 'object'>


.. _python_cls_type:

type
....

Los objetos tipo representan los diversos tipos de objeto. El tipo de un objeto es 
accesible mediante la función integrada :ref:`type() <python_fun_type>`. No hay 
operaciones especiales sobre los tipos. El módulo estándar ``types`` define nombres 
para todos los tipos internos estándar.

::

    >>> type(type)
    <type 'type'>


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion9>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
