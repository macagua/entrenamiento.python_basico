.. -*- coding: utf-8 -*-


.. _python_objeto_tipos_integrados:

Objetos de tipos integrados
---------------------------

.. todo:: TODO Escribir sobre los objetos de tipos integrados.


.. _python_objeto_ellipsis:

El objeto elipsis
.................

Éste objeto lo utiliza la notación de corte extendida. No tiene ninguna operación 
especial. Existe exactamente un objeto ``elipsis``, llamado ``Ellipsis`` (un nombre 
interno).

.. note::
    El tipo se muestra de este modo: ``<type 'ellipsis'>``.


----


.. _python_objeto_none:

El objeto nulo
..............

Éste es el objeto devuelto por las funciones que no devuelven un valor explícito. 
No tiene ninguna operación especial. Existe exactamente un objeto nulo, llamado 
``None`` (un nombre interno).

.. note::
    El tipo se muestra de este modo: ``<type 'NoneType'>``.

----

.. _python_objeto_file:

El objeto fichero
.................

Los objetos fichero se implementan con el paquete C ``stdio`` y se pueden crear 
con la función interna :ref:`open() <python_funcion_open>`. También son el resultado 
de otras funciones y métodos internos, por ejemplo, ``os.popen()`` y ``os.fdopen()`` 
y el método ``makefile()`` de los objetos ``socket``.

Cuando falla una operación de ficheros por una cuestión de E/S, se lanza la excepción 
:ref:`IOError <python_exception_ioerror>`. Esto incluye situaciones donde la operación 
no esté definida por cualquier motivo, como usar :ref:`seek() <python_funcion_seek>` 
en un dispositivo ``tty`` o intentar escribir en un fichero abierto para lectura.

Métodos
~~~~~~~


.. _python_funcion_close:

close()
````````

La función ``close()`` permite cerrar la manipulación del archivo. No es posible escribir 
ni leer en un fichero cerrado. Cualquier operación que requiera que el fichero esté 
abierto lanzará :ref:`IOError <python_exception_ioerror>` si el fichero se ha cerrado. Está 
permitido llamar a ``close()`` más de una vez.

Una vez que se terminó de usar el archivo es necesario cerrarlo, para liberar los recursos 
tomados por el manejo del archivo. Eso se hace con la sentencia ``f.close()``:

::

	>>> f.close() # cierra el archivo datos.txt


Luego de lo cual no se puede acceder al archivo ``datos.txt``, si intenta una llamada a 
la función :ref:`f.read() <python_funcion_read>` devuelve una excepción 
:ref:`ValueError <python_exception_valueerror>`, porque el archivo está cerrado:

::

	>>> f.close()
	>>> f.read()
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: I/O operation on closed file


.. tip:: Para más detalles: http://docs.python.org/tutorial/inputoutput.html


.. _python_funcion_flush:

flush()
````````

La función ``flush()`` permite descargar el tampón interno, como la función C ``fflush()`` 
de la librería ``stdio``. Puede no tener efecto en ciertos objetos similares a los ficheros.


.. _python_funcion_isatty:

isatty()
`````````

La función ``isatty()`` devuelve ``True`` si el fichero está conectado a un dispositivo 
``tty`` (un terminal interactivo de líneas de orden), en caso contrario, ``False``. 

.. note:: 
	Si un objeto similar a los ficheros no está asociado a un fichero real, no debe 
	implementar este método.


.. _python_funcion_fileno:

fileno()
````````

La función ``fileno()`` devuelve el "descriptor de fichero" utilizado por la implementación 
subyacente para solicitar operaciones E/S del sistema operativo. Puede ser útil para 
interfaces de bajo nivel que utilicen descriptores de ficheros, por ejemplo, el módulo 
``fcntl`` o ``os.read()`` y similares. 

.. note:: 
	Si un objeto similar a los ficheros no tiene un descriptor de fichero, no debe implementar 
	este método.


.. _python_funcion_next:

next()
````````

La función ``next()`` permite x.next() -> el próximo valor, o causa una :ref:`StopIteration <python_exception_stopiteration>`


.. _python_funcion_read:

read()
````````

La función ``read()`` permite leer el contenido del archivo. El argumento 
es opcional y si no se especifica (o es -1) devuelve el contenido de todo 
el archivo. Una vez que se leyó todo el archivo, una nueva llamada a 
la función devuelve una cadena vacía ('').

::

	>>> f = open('datos.txt', 'r')
	>>> f.read()
	'Este es una prueba \ny otra prueba'
	>>> f.read()
	''

Si desea recibir una salida formateada por consola leyendo un archivo, a 
continuación un ejemplo:

::

	>>> f = open('datos.txt', 'r')
	>>> s = f.read()
	>>> print s
	This is a test
	and another test


.. _python_funcion_readline:

readline()
````````````

La función ``readline()`` permite leer una sola línea del archivo, 
devuelve al final de la línea el carácter de nueva línea y solo 
se omite en la última línea del archivo (si no termina con el carácter 
de nueva línea). Esto hace que el valor de retorno no sea ambiguo. 
Si devuelve una cadena de caracteres vacía se alcanzó el fin del archivo, 
mientras que una línea en blanco se representa con un carácter de nueva línea.

::

	>>> f = open('datos.txt', 'r')
	>>> print f.readline() # lee la linea "Este es una prueba "
	>>> print f.readline() # lee la linea "y otra prueba"
	>>> print f.readline()
		
	>>> 


.. _python_funcion_readlines:

readlines()
````````````

La función ``readlines()`` devuelve una lista que contiene todas las 
líneas del archivo.

::

	>>> f = open('datos.txt', 'r')
	>>> lines = f.readlines()
	>>> print(lines)
	['Este es una prueba \n', 'y otra prueba']


.. _python_funcion_seek:

seek()
````````

La función ``seek()`` establece la posición actual del fichero, como la función C 
``fseek()`` de la librería ``stdio``.

::

	seek(offset[, whence]) -> None.  Move to new file position.

El argumento ``whence`` es opcional, con un valor predeterminado de ``0`` (posicionamiento 
absoluto); otros valores posibles son ``1`` (posicionamiento relativo a la posición actual) 
y ``2`` (posicionamiento relativo al final del fichero). No hay valor de retorno.


.. _python_funcion_tell:

tell()
````````

La función ``tell()`` devuelve la posición actual del fichero, como la función C ``ftell()`` 
de la librería ``stdio``.


.. _python_funcion_truncate:

truncate()
````````````

::

	truncate([size]) -> None

La función ``truncate()`` trunca el fichero. Si se proporciona el argumento opcional ``size``, 
el fichero se trunca a (como mucho) ese tamaño. El tamaño depende de la posición actual. La 
disponibilidad de esta función depende de la versión del sistema operativo (por ejemplo, no 
todas las versiones de Unix dan soporte a esta operación).


.. _python_funcion_write:

write()
````````

La función ``write()`` permite escribir el contenido de la cadena de 
texto al archivo, y devuelve la cantidad de caracteres escritos.

Para escribir algo que no sea una cadena de caracteres, antes se 
debe convertir a cadena de caracteres.

::

	>>> f = open('datos.txt', 'w')
	>>> f.write('Este es una prueba \ny otra prueba') # escribe el archivo datos.txt


.. _python_funcion_writelines:

writelines()
````````````

La función ``writelines()`` escribe una lista de cadenas al fichero. No se devuelve 
ningún valor. El nombre es paralelo a ``readlines()``, ``writelines()`` no añade 
separadores de línea.


Atributos
~~~~~~~~~

Los objetos fichero también ofrecen otros atributos interesantes. No son necesarios 
para los objetos de interfaz tipo fichero, pero deberían implementarse si tienen sentido 
en un objeto particular.


.. _python_atributo_closed:

closed
````````

El atributo ``closed`` del objeto *fichero* de tipo :ref:`Booleano <python_booleanos>` 
indica el estado actual. Es un atributo de sólo lectura, que se cambia mediante el método 
:ref:`close() <python_funcion_close>`. Puede no estar disponible en todos los objetos con 
interfaz tipo fichero.


.. _python_atributo_mode:

mode
````

El atributo ``mode`` del objeto *fichero*, es el modo de E/S del fichero. Si se creó el 
fichero con la función integrada :ref:`open() <python_funcion_open>`, será el valor del 
parámetro ``mode``. Es un atributo de sólo lectura y puede no estar disponible en todos 
los objetos con interfaz tipo fichero.


.. _python_atributo_name:

name
````

El atributo ``name`` del objeto *fichero*, es el nombre del fichero si se creó el objeto 
fichero mediante la función integrada :ref:`open() <python_funcion_open>`, el nombre del 
fichero. En caso contrario, alguna cadena que indique el origen del fichero, de la forma 
"<...>". Es un atributo de sólo lectura y puede no estar disponible en todos los objetos 
con interfaz tipo fichero.


.. _python_atributo_encoding:

encoding
````````

El atributo ``encoding`` del objeto *fichero* es el encoding del fichero.


.. _python_atributo_errors:

errors
````````

El atributo ``errors`` del objeto *fichero* es el manipulador de error Unicode.


.. _python_atributo_softspace:

softspace
````````````

El atributo ``softspace`` del objeto *fichero* de tipo :ref:`Booleano <python_booleanos>` 
indica si se debe escribir un espacio antes de escribir otro valor al usar la sentencia 
:ref:`print <python_sentencia_print>`. Las clases que intenten simular un objeto fichero 
deberían tener un atributo escribible ``softspace``, que debería inicializarse a cero. 

Esto será automático en la mayoría de las clases implementadas en Python (se debe tener 
cuidado en las clases que redefinan el acceso a los atributos). Los tipos implementados 
en C tendrán que proporcionar un atributo ``softspace`` escribible. Nota: Este atributo 
no se usa para controlar la sentencia ``print``, sino para permitir que la implementación 
de ``print`` lleve la cuenta de su estado interno.

----

.. _python_objeto_object:

El objeto object
................

El objeto de la clase ``object`` es el tipo más básico de objeto, es integrado en 
el módulo ``__builtin__``. Este objeto se usa como :ref:`herencia <python_poo_herencia>` 
cuando se crea una nueva clase en Python.

Todo, incluyendo las clases y tipos de Python son instancias de object. Para corroborar 
si un objeto es instancia de una clase se utiliza la función 
:ref:`isinstance() <python_funcion_isinstance>`.


.. note::
    Los tipos se muestran de este modo: ``<type 'object'>``.

----

.. _python_objeto_type:

El objeto tipo
..............

Los objetos tipo representan los diversos tipos de objeto. El tipo de un objeto es 
accesible mediante la función integrada :ref:`type() <python_funcion_type>`. No hay 
operaciones especiales sobre los tipos. El módulo estándar ``types`` define nombres 
para todos los tipos internos estándar.

.. note::
    Los tipos se muestran de este modo: ``<type 'type'>``.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion9>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
