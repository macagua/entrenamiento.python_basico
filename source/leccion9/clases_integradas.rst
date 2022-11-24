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

.. code-block:: pycon

    >>> cadena = "Hola mundo"
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
    >>> print(cadena_buffer)
    mundo

El búfer en este caso anterior es una sub-cadena, inicia en la posición 5 con un
ancho de 5 caracteres y es no toma espacio de almacenamiento extra - eso referencia
a ``cortar`` una :ref:`cadena de caracteres <python_str>`.

Este ejemplo anterior no es muy útil para :ref:`cadena de caracteres <python_str>` cortas como esta,
pero eso puede ser necesario cuando usa un gran numero de data. Este ejemplo puede
usar un tipo mutable ``bytearray()``:

.. code-block:: pycon

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

Note que el búfer ha sido remplazado por un mejor método llamado
:ref:`memoryview() <python_cls_memoryview>` en Python 3, aunque se puede usar en
Python 2.7.

Note también que usted no puede implementar una interfaz búfer para sus propios objetos
sin profundizando en la API de C, ej. usted no puede hacer eso con puramente con código
Python.

En general un ``slice`` tomará extra almacenamiento, entonces, si ``cadena[5:10]`` será
una copia. Si usted define ``cadena_buffer = cadena[5:10]`` y entonces ``del cadena``,
eso liberaría la memoria que fue tomada por ``cadena``, proveyendo que ``cadena_buffer``
fue copiada. (Para usar esto usted necesita una gran :ref:`cadena de caracteres <python_str>`, en este ejemplo
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

.. code-block:: pycon

    >>> arreglo = bytes("Python es interesante.")
    >>> print(arreglo)
    Python es interesante.
    >>> type(arreglo)
    <type 'str'>


.. _python_cls_quit:

quit
~~~~~

Es el método constructor de la clase ``Quitter`` incluida en el módulo ``site`` el
cual le permite salir de la consola interactiva Python:

.. code-block:: pycon

    >>> quit
    Use quit() or Ctrl-D (i.e. EOF) to exit
    >>> quit()
    $

De esta forma puede salir de la consola interactiva Python y volviendo al interprete
del Shell de comando.


.. _python_cls_slice:

slice
~~~~~

La clase ``slice`` crea un objecto ``slice``, esto es usado por el extendido ``slicing``
por ejemplo:

.. code-block:: pycon

    >>> a = range(20)
    >>> a[0:10:2]
    [0, 2, 4, 6, 8]

La sintaxis es la siguiente:

::

    >>> slice(stop)
    >>> slice(start, stop[, step])


.. comments:

    .. todo:: TODO escribir sobre esta clase integrada.


.. _python_cls_staticmethod:

staticmethod
~~~~~~~~~~~~

Los métodos estáticos en Python son extremadamente similar a los métodos de nivel
clase en python, la diferencia esta que un método estático es enlazado a una clase
más bien que los objectos para esa clase.

Esto significa que un método estático puede ser llamado sin un objeto para esa clase.
Esto también significa que los métodos estáticos no pueden modificar el estado de un
objeto como ellos no pueden enlazarse a ese.

Los métodos estáticos Python puede crearse en dos formas, usando el aprovechamiento
``staticmethod()`` o el decorador ``@staticmethod``:

La clase ``staticmethod()`` convierte una función a un método estático. Un método
estático no recibe un primer argumento implícito. La sintaxis es la siguiente:

::

    >>> staticmethod(function) -> método

Para declarar un método estático, a continuación vea el siguiente ejemplo:

.. code-block:: pycon

    >>> class Calculador:
    ...     def sumaNumeros(x, y):
    ...         return x + y
    ...     # crea un static method sumaNumeros
    ...     sumaNumeros = staticmethod(sumaNumeros)
    ...
    >>> print("Resultado:", Calculador.sumaNumeros(15, 110))
    Resultado: 125
    >>> print("Resultado:", Calculador().sumaNumeros(15, 110))
    Resultado: 125

En el ejemplo anterior usted puede notar que se llamo al método ``sumaNumeros`` sin
crear un objeto. Se puede llamar en la clase (por ejemplo, ``Clase.funcion()``) o
en una instancia (por ejemplo, ``Clase().funcion()``). La instancia se ignora a
excepción de su clase.

Los métodos estáticos son similares a los métodos estáticos ``Java`` o ``C++``. Para
un concepto más avanzado, mire la clase :ref:`classmethod <python_cls_classmethod>`
integrada en el interprete.

La clase ``staticmethod`` introduce un cambio en la versión 2.4, agregando sintaxis de
:ref:`decorador <python_decoradores>` de función. La sintaxis es la siguiente:

::

    class Clase:
        @staticmethod
        def funcion(argumento1, argumento2, ...):
            ...

Un ejemplo del uso de :ref:`decoradores <python_decoradores>` para ``staticmethod``
a continuación:

.. code-block:: pycon

    >>> class Calculador:
    ...     @staticmethod
    ...     def sumaNumeros(x, y):
    ...         return x + y
    ...
    >>> print("Resultado:", Calculador.sumaNumeros(15, 110))
    Resultado: 125

Este código fuente es enteramente idéntico al primer ejemplo (usando ``@staticmethod``),
solo que no usa la agradable sintaxis de :ref:`decorador <python_decoradores>`.

Finalmente, se usa el método ``staticmethod()`` escasamente. Hay muchas situaciones donde los
métodos estáticos son necesarios en Python.


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

.. code-block:: pycon

    >>> enumerar = enumerate(range(3))
    >>> next(enumerar)
    (0, 0)
    >>> next(enumerar)
    (1, 1)
    >>> next(enumerar)
    (2, 2)
    >>> next(enumerar)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior usa una secuencia numérica de 3 elementos generada por la función
integrada :ref:`range() <python_fun_range>`.

A continuación se le pasa el parámetro de *inicio* con el valor *1* de la secuencia
generada por la clase ``enumerate``:

.. code-block:: pycon

    >>> enumerar = enumerate(range(3), 1)
    >>> next(enumerar)
    (1, 0)
    >>> next(enumerar)
    (2, 1)
    >>> next(enumerar)
    (3, 2)
    >>> next(enumerar)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior usa una secuencia numérica de 3 elementos generada con el valor
inicial de *1* por la función integrada :ref:`range() <python_fun_range>`.


.. _python_cls_reversed:

reversed
~~~~~~~~

La clase ``reversed`` devolver un :ref:`iterador <python_iter>` inverso sobre los
valores de la secuencia, cuando la iteración de la secuencia llega al final se llama
a la excepción :ref:`StopIteration <python_exception_stopiteration>` y se causa el
detener la iteración.

.. code-block:: pycon

    >>> inversa = reversed(range(3))
    >>> next(inversa)
    2
    >>> next(inversa)
    1
    >>> next(inversa)
    0
    >>> next(inversa)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior usa una secuencia numérica de 3 elementos generada por la
función integrada :ref:`range() <python_fun_range>`.


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

.. code-block:: pycon

    >>> archivo.close()  # cierra el archivo datos.txt


Luego de lo cual no se puede acceder al archivo ``datos.txt``, si intenta una llamada a
la método :ref:`archivo.read() <python_mtd_read>` devuelve una excepción
:ref:`ValueError <python_exception_valueerror>`, porque el archivo está cerrado:

.. code-block:: pycon

    >>> archivo.close()
    >>> archivo.read()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: I/O operation on closed file


.. tip:: Para más detalles: https://docs.python.org/es/3.7/tutorial/inputoutput.html


.. _python_mtd_flush:

flush()
"""""""

El método ``flush()`` permite descargar el bufér interno, como la función de lenguaje C
``fflush()`` de la librería ``stdio``. Puede no tener efecto en ciertos objetos similares
a los archivos.

Python automáticamente flushes los archivos cuando son cerrados. Pero usted podría to flush
la data antes de cerrar cualquier archivo.

.. code-block:: pycon

    >>> archivo = open("datos.txt", "wb")  # Abre un archivo
    >>> print("Nombre del archivo: ", archivo.name)
    Nombre del archivo:  datos.txt
    >>> archivo.flush()
    ... # Aquí eso no hace nada, pero usted puede
    ... # llamarlo con la operación read.
    >>> archivo.close()  # Cerrar archivo abierto


.. _python_mtd_isatty:

isatty()
""""""""

El método ``isatty()`` devuelve ``True`` si el archivo está conectado a un dispositivo
``tty`` (un terminal interactivo de líneas de orden), en caso contrario, ``False``.

.. note::
    Si un objeto similar a los archivos no está asociado a un archivo real, no debe
    implementar este método.

.. code-block:: pycon

    >>> archivo = open("datos.txt", "r")
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

.. code-block:: pycon

    >>> archivo = open("datos.txt", mode="r")
    >>> archivo.fileno()
    6

.. _python_mtd_next:

next()
""""""

El método ``next()`` permite usar un iterador para tratar cada linea del archivo como
el próximo valor, cuando la iteración del archivo llega al final se llama a la excepción
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la
iteración.

.. code-block:: pycon

    >>> archivo = open("/etc/hostname")
    >>> archivo
    <open file '/etc/hostname', mode 'r' at 0x7fa44ba379c0>
    >>> archivo.__iter__()
    <open file '/etc/hostname', mode 'r' at 0x7fa44ba379c0>
    >>> iter(archivo)
    <open file '/etc/hostname', mode 'r' at 0x7fa44ba379c0>
    >>> archivo is archivo.__iter__()
    True
    >>> linea = archivo.__iter__()
    >>> next(linea)
    'laptop\n'
    >>> next(linea)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration


.. _python_mtd_read:

read()
""""""

El método ``read()`` permite leer el contenido del archivo. El argumento es opcional
y si no se especifica (o es -1) devuelve el contenido de todo el archivo. Una vez que
se leyó todo el archivo, una nueva llamada a la función devuelve una :ref:`cadena vacía <python_str>` ('').

.. code-block:: pycon

    >>> archivo = open("datos.txt", "r")
    >>> archivo.read()
    'Este es una prueba \ny otra prueba'
    >>> archivo.read()
    ''

Si desea recibir una salida formateada por consola leyendo un archivo, a continuación
un ejemplo:

.. code-block:: pycon

    >>> archivo = open("datos.txt", "r")
    >>> contenido = archivo.read()
    >>> print(contenido)
    Este es una prueba
    y otra prueba


.. _python_mtd_readline:

readline()
""""""""""

El método ``readline()`` permite leer una sola línea del archivo, devuelve al final de
la línea el carácter de nueva línea y solo se omite en la última línea del archivo (si
no termina con el carácter de nueva línea). Esto hace que el valor de retorno no sea
ambiguo. Si devuelve una :ref:`cadena de caracteres <python_str>` vacía se alcanzó el fin del archivo,
mientras que una línea en blanco se representa con un carácter de nueva línea.

.. code-block:: pycon

    >>> archivo = open("datos.txt", "r")
    >>> print(archivo.readline())  # lee la linea "Este es una prueba "
    >>> print(archivo.readline())  # lee la linea "y otra prueba"
    >>> print(archivo.readline())

    >>>


.. _python_mtd_readlines:

readlines()
"""""""""""

El método ``readlines()`` devuelve una :ref:`lista <python_list>` que contiene todas las líneas del archivo.

.. code-block:: pycon

    >>> archivo = open("datos.txt", "r")
    >>> lineas = archivo.readlines()
    >>> print(lineas)
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

.. code-block:: pycon

    >>> archivo = open("datos.txt", "w")
    >>> lista_de_lineas = [
    ...     "Esta es la 1er linea",
    ...     "Esta es la 2da linea",
    ...     "Esta es la 3era linea",
    ... ]
    >>> archivo.writelines("\n".join(lista_de_lineas))
    >>> archivo.close()
    >>> archivo = open("datos.txt", "r")
    >>> next(archivo)
    'Esta es la 1er linea\n'
    >>> archivo.seek(8)
    >>> next(archivo)
    'la 1er linea\n'
    >>> next(archivo)
    'Esta es la 2da linea\n'
    >>> next(archivo)
    'Esta es la 3era linea'
    >>> next(archivo)
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

.. code-block:: pycon

    >>> archivo = open("datos.txt", "w")
    >>> lista_de_lineas = [
    ...     "Esta es la 1er linea",
    ...     "Esta es la 2da linea",
    ...     "Esta es la 3era linea",
    ... ]
    >>> archivo.writelines("\n".join(lista_de_lineas))
    >>> archivo.close()
    >>> archivo = open("datos.txt", "r")
    >>> next(archivo)
    'Esta es la 1er linea\n'
    >>> archivo.seek(8)
    >>> next(archivo)
    'la 1er linea\n'
    >>> archivo.close()
    >>> archivo = open("datos.txt", "rw+")
    >>> nuevas_lineas = ["\nEsta es la 4ta linea", "Esta es la 5ta linea"]
    >>> # Escribe la secuencia de la lineas al final del archivo.
    ... archivo.seek(0, 2)
    >>> archivo.writelines("\n".join(nuevas_lineas))
    >>> # Ahora lea completamente el archivo desde el inicio.
    ... archivo.seek(0, 0)
    >>> for elemento in range(1, 6):
    ...     linea = next(archivo)
    ...     print("Linea No %d - %s" % (elemento, linea))
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

.. code-block:: pycon

    >>> archivo = open("/etc/hostname")
    >>> archivo.tell()
    0
    >>> linea = iter(archivo)
    >>> next(linea)
    'debacagua9\n'
    >>> archivo.tell()
    11
    >>> len("debacagua9\n")
    11
    >>> next(linea)
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

.. code-block:: pycon

    >>> archivo = open("datos.txt", "w")
    >>> archivo.write("Este es una prueba \ny otra prueba")
    >>> archivo.truncate(20)
    >>> archivo.close()
    >>> archivo = open("datos.txt", "r")
    >>> archivo.read()
    'Este es una prueba \n'

El método ``truncate()`` trunca el archivo. Si se proporciona el argumento opcional,
el archivo se trunca a (como mucho) ese tamaño. El tamaño depende de la posición
actual. La disponibilidad de esta función depende de la versión del sistema operativo
(por ejemplo, no todas las versiones de Unix dan soporte a esta operación).


.. _python_mtd_write:

write()
"""""""

El método ``write()`` permite escribir el contenido de la :ref:`cadena de texto <python_str>` al archivo,
y devuelve la cantidad de caracteres escritos.

Para escribir algo que no sea una :ref:`cadena de caracteres <python_str>`, antes se debe convertir a
:ref:`cadena de caracteres <python_str>`.

.. code-block:: pycon

    >>> archivo = open("datos.txt", "w")
    >>> # escribe el archivo datos.txt
    ... archivo.write("Este es una prueba \ny otra prueba")
    >>>


.. _python_fun_writelines:

writelines()
""""""""""""

El método ``writelines()`` escribe una lista de cadenas al archivo. No se devuelve
ningún valor. El nombre es paralelo a ``readlines()``, ``writelines()`` no añade
separadores de línea.

.. code-block:: pycon

    >>> archivo = open("datos.txt", "w")
    >>> lista_de_lineas = [
    ...     "Plone es el más poderoso, ",
    ...     "escalable, seguro ",
    ...     "y longevo CMS, ",
    ...     "escrito en Python.",
    ... ]
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

.. code-block:: pycon

    >>> archivo = open("datos.txt", "w")
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

.. code-block:: pycon

    >>> archivo = open("datos.txt", "w")
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

.. code-block:: pycon

    >>> archivo = open("datos.txt", "w")
    >>> archivo.name
    'datos.txt'


.. _python_attr_encoding:

encoding
""""""""

El atributo ``encoding`` del objeto :ref:`file <python_cls_file>`, es el encoding
del archivo.

.. code-block:: pycon

    >>> with open("datos.txt", mode="r") as archivo:
    ...     print("Encoding por defecto:", archivo.encoding)
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

.. code-block:: pycon

    >>>
    >>> archivo = open("datos.txt", "w")
    >>> archivo.softspace
    0


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

    classmethod(function) -> método

Para declarar un método de clase, a continuación vea el siguiente ejemplo:

.. code-block:: pycon

    >>> def sumaNumeros(cls, x, y):
    ...     return x + y
    ...
    >>> type(sumaNumeros)
    <type 'function'>
    >>> class Calculador:
    ...     # crea un static method sumaNumeros
    ...     sumaNumeros = classmethod(sumaNumeros)
    ...
    >>> Calculador.sumaNumeros(15, 110)
    125
    >>> Calculador().sumaNumeros(15, 110)
    125
    >>> type(Calculador.sumaNumeros)
    <type 'instancemethod'>

La clase ``classmethod`` introduce un cambio en la versión 2.4, agregando sintaxis de
:ref:`decorador <python_decoradores>` de función. La sintaxis es la siguiente:

::

    class Clase:
        @classmethod
        def funcion(cls, argumento1, argumento2, ...):
            ...

Un ejemplo del uso de :ref:`decoradores <python_decoradores>` para ``classmethod``
a continuación:

.. code-block:: pycon

    >>> class Clase:
    ...     @classmethod
    ...     def funcion(cls, argumento1, argumento2):
    ...         return argumento1 + argumento2
    ...
    >>> Clase.funcion(2, 3)
    5
    >>> Clase().funcion(2, 3)
    5


Se puede llamar en la clase (por ejemplo, ``Clase.funcion()``) o en una instancia
(por ejemplo, ``Clase().funcion()``). La instancia se ignora a excepción de su clase.
Si se llama a un método de clase para una clase derivada, el objeto de clase derivada
se pasa como el primer argumento implícito.

Los métodos de clase son diferentes a los métodos estáticos ``C++`` o ``Java``. Si
quieres eso, mira la clase :ref:`staticmethod <python_cls_staticmethod>` integrada
en el interprete.

.. comments:

    .. todo:: TODO terminar de escribir sobre la clase integrada classmethod.


.. _python_cls_memoryview:

memoryview
~~~~~~~~~~

La clase ``memoryview``  devuelve un objeto *vista de memoria* del argumento dado.

Antes de introducir a que son las *vistas de memoria*, necesita entender primero
sobre del *protocolo Búfer* de Python.

**¿Qué es protocolo Búfer?**

Este protocolo provee una forma de acceder la data interna de un objeto. Esta data
interna es un arreglo de memoria o un búfer. El *protocolo Búfer* le permite un objeto
para exponer esa data interna (búfers) y el otro para acceder a esos búfers sin tener
que copiar intermediamente.

Este protocolo es solamente accesible al usar el nivel API de C y no usando el normal
código base. Por lo tanto, para exponer el mismo protocolo a la base de código Python
normal, las vistas de memoria están presentes.


**¿Qué es una vista de memoria?**

La vista de memoria es una forma segura de exponer el protocolo búfer en Python. Eso
le permite a usted acceder a los búfers internos de un objeto para creación de un
objeto de vista de memoria.

**¿Por que el protocolo búfer y las vistas de memoria son importantes?**

Necesita recordar que cada vez que ejecuta alguna acción en un objeto (llamar a una
función de un objeto, cortar un arreglo), Python necesita crear una copia del objeto.

Si usted tiene una gran data para trabajar con ella (ej. data binaria de una imagen),
debería crear innecesariamente copias de enormes trozos de datos, que casi no sirve
de nada.

Usando el *protocolo búfer*, puede dar otros accesos al objeto para usar/modificar
data grande sin realizar copias de eso. Esto hace que el programa use menos memoria
y incremente la velocidad de ejecución.

**¿Como exponer el protocolo búfer usando las vistas de memoria?**

Los objetos de *vista de memoria* son creados usando la sintaxis:

.. code-block:: pycon

    >>> memoryview(objecto)

El método constructor ``memoryview()`` toma un simple parámetro:

``objecto`` - es el objeto dado como parámetro el cual su data interna es expuesta.

``objecto`` debe ser un tipo el cual soportar el *protocolo búfer* (``bytes``,
``bytearray``). Devuelve el valor de un objeto de vista de memoria del objeto dado
como parámetro desde el método ``memoryview()``.

A continuación, un ejemplo donde se crea una *vista de memoria* usando el tipo
``bytearray`` previamente creado:

.. code-block:: pycon

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

En el ejemplo anterior se crea una *vista de memoria* de un tipo ``bytearray``
mostrando los diversos atributos disponibles.

Continuando el ejemplo anterior, se crea una *vista de memoria* de un tipo
:ref:`buffer <python_cls_buffer>` usando el objeto ``cadena`` previamente creado:

.. code-block:: pycon

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

En el ejemplo anterior se crea una *vista de memoria* de un tipo
:ref:`buffer <python_cls_buffer>` mostrando los diversos atributos disponibles.

A continuación, otro ejemplo donde se crea una *vista de memoria* usando el objeto
``bytearray`` previamente creado:

.. code-block:: pycon

    >>> randomBA = bytearray("ABC", "utf-8")
    >>> randomBA
    bytearray(b'ABC')
    >>> vm = memoryview(randomBA)
    >>> vm
    <memory at 0x7fafc7136c30>
    >>> print(vm[0])
    A
    >>> print(vm[1])
    B
    >>> print(vm[2])
    C

Continuando el ejemplo anterior, se puede crear una :ref:`lista <python_list>` desde
una *vista de memoria* usando el objeto ``vm`` previamente creado:

.. code-block:: pycon

    >>> list = []
    >>> for item in range(3):
    ...     list.append(vm[item])
    ...
    >>> list
    ['A', 'B', 'C']

Continuando el ejemplo anterior, se puede crear :ref:`cadena de caracteres <python_str>`
desde una *vista de memoria* usando el objeto ``vm`` previamente creado:

.. code-block:: pycon

    >>> cad = ""
    >>> for item in range(3):
    ...     cad += vm[item]
    ...
    >>> print(cad)
    ABC

Aquí, es creada un objeto *vista de memoria* llamado ``vm`` desde un objeto ``bytearray``
llamado ``randomBA``.

Entonces, es accedido al índice 0 posición ``vm`` 'A' y el valor es impreso. Luego, es
accedido al índice 1 posición ``vm`` 'B' y el valor es impreso. También, es accedido al
índice 2 posición ``vm`` 'C' y el valor es impreso.

Finalmente, es accedido todos los índices del objeto ``vm`` y convertidos a una :ref:`lista <python_list>`.


A continuación, otro ejemplo donde se modifica la data interna usando vista de memoria:

.. code-block:: pycon

    >>> randomBA = bytearray("ABC", "utf-8")
    >>> print("Antes de actualizar:", randomBA)
    Antes de actualizar: ABC
    >>> vm = memoryview(randomBA)
    >>> chr(90)
    'Z'
    >>> vm[1] = chr(90)
    >>> print("Después de actualizar:", randomBA)
    Después de actualizar: AZC

Aquí, se actualiza el indice 1 de la *vista de memoria* a un valor ASCII - 90 (Z)
usando la función :ref:`chr() <python_fun_chr>`. Desde, el objeto de *vista de memoria*
``vm`` referencia al mismo búfer/memoria, actualiza el índice en el ``vm`` también actualiza
el ``randomBA``.

Desde adentro internamente el tipo ``bytearray`` almacena valores ``ASCII`` para el
alfabeto, es decir, cada posición de la :ref:`lista <python_list>` se debe indicar con su equivalente
numérico en la tabla ``ASCII``.

.. code-block:: pycon

    >>> chr(65)
    'A'
    >>> chr(66)
    'B'
    >>> chr(67)
    'C'
    >>> chr(90)
    'Z'

Entonces se usa la función :ref:`chr() <python_fun_chr>` para indicar su equivalente en
la tabla de valores ``ASCII``.


.. _python_cls_object:

object
~~~~~~

El objeto de la clase ``object`` es el tipo más básico de objeto, es integrado en
el módulo ``__builtin__``. Este objeto se usa como :ref:`herencia <python_poo_herencia>`
cuando se crea una nueva clase en Python.

Todo, incluyendo las clases y tipos de Python son instancias de ``object``. Para
corroborar si un objeto es instancia de una clase se utiliza la función
:ref:`isinstance() <python_fun_isinstance>`.

.. code-block:: pycon

    >>> object
    <type 'object'>


.. _python_cls_property:

property
~~~~~~~~

La clase ``property`` típicamente es usado para definir un atributo property.
La sintaxis es la siguiente:

.. code-block:: pycon

    >>> property(fget=None, fset=None, fdel=None, doc=None)  # devuelve atributo property

El parámetro ``fget`` es una función a ser usada para obtener un valor de un atributo,
y igualmente el parámetro ``fset`` es una función para definir el valor de un atributo,
y el parámetro ``fdel`` es una función para eliminar un atributo.

El método ``property()`` devuelve un atributo ``property`` donde es dado el método
``getter``, ``setter`` y ``deleter``.

Si no hay argumentos son dados, el método ``property()`` devuelven un atributo base
``property`` que no contienen ningún ``getter``, ``setter`` o ``deleter``. Si ``doc``
no es proveído, método ``property()`` toma el :ref:`docstring <python_str_docstrings>`
de la función ``getter``.

A continuación, un ejemplo sencillo:

.. code-block:: pycon

    >>> class Persona:
    ...     def __init__(self, nombre):
    ...         self._nombre = nombre
    ...     def getNombre(self):
    ...         print("Obteniendo nombre")
    ...         return self._nombre
    ...     def setNombre(self, valor):
    ...         print("Definiendo nombre a " + valor)
    ...         self._nombre = valor
    ...     def delNombre(self):
    ...         print("Eliminando nombre")
    ...         del self._nombre
    ...     # Define la property para usar los métodos getNombre,
    ...     # setNombre y delNombre
    ...     nombre = property(getNombre, setNombre, delNombre, "Atributo property nombre")
    ...
    >>> persona1 = Persona("Leo")
    >>> print(persona1.nombre)
    Obteniendo nombre
    Leo
    >>> persona1.nombre = "Leonardo"
    >>> print(persona1.nombre)
    Leonardo
    >>> dir(persona1)
    ['__doc__', '__init__', '__module__', '_nombre', 'delNombre',
    'getNombre', 'nombre', 'setNombre']
    >>> persona1.delNombre()
    Eliminando nombre
    >>> dir(persona1)
    ['__doc__', '__init__', '__module__', 'delNombre', 'getNombre',
    'nombre', 'setNombre']
    >>> print(persona1.nombre)
    Leonardo
    >>> del persona1.nombre
    >>> print(persona1.nombre)
    Obteniendo nombre
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 7, in getNombre
    AttributeError: Persona instance has no attribute '_nombre'

Cuando se elimina ``persona1.delNombre()`` puede notar que ``_nombre`` ya no esta
disponible y si se vuelve a imprimir el valor de nombre ``print(persona1.nombre)``
aun muestra el valor inicializado con el método ``setNombre``, entonces al ejecutar
``del persona1.nombre`` se elimina por completo el valor en memoria, luego si intenta
mostrar el valor del *atributo property* ``nombre`` lanza
:ref:`AttributeError <python_exception_attributeerror>` por no encontró ``_nombre``
el cual es usado como la variable privado para almacenar el nombre de una Persona.

Se definió lo siguiente:

- Un método ``getter`` getNombre() para obtener el nombre de la persona,
- Un método ``setter`` setNombre() para definir el nombre de la persona,
- Un método ``deleter`` delNombre() para eliminar el nombre de la persona.

Ahora tiene definido un *atributo property* ``nombre`` llamando al método ``property()``.

Como se mostró en el código anterior, la referencia ``persona1.nombre`` internamente
llama al método ``getName()`` como *getter*, ``setName()`` como *setter* y ``delName()``
como *deleter* a través de las salidas impresas presente dentro de los métodos.

También se definió el :ref:`docstring <python_str_docstrings>` del atributo con el
valor *'Atributo property nombre'*.

Otra alternativa son los :ref:`decoradores <python_decoradores>` facilitan la definición
de nuevas propiedades o la modificación de las existentes:

A continuación se creará un *atributo property* con métodos ``getter``, ``setter`` y
``deleter`` usando el decorador ``@property`` en vez de usar el método ``property()``,
usted puede usar el decorador Python ``@property`` para asignar el método ``getter``,
``setter`` y ``deleter``:

.. code-block:: pycon

    >>> class Persona:
    ...     def __init__(self, nombre):
    ...         self._nombre = nombre
    ...     @property
    ...     def nombre(self):
    ...         print("Obteniendo nombre")
    ...         return self._nombre
    ...     @nombre.setter
    ...     def nombre(self, valor):
    ...         print("Definiendo nombre a " + valor)
    ...         self._nombre = valor
    ...     @nombre.deleter
    ...     def nombre(self):
    ...         print("Eliminando nombre")
    ...         del self._nombre
    ...
    >>> persona1 = Persona("Leo")
    >>> print("El nombre es:", persona1.nombre)
    El nombre es: Obteniendo nombre
    Leo
    >>> persona1.nombre = "Leonardo"
    >>> print(persona1.nombre)
    Leonardo
    >>> dir(persona1)
    ['__doc__', '__init__', '__module__', '_nombre', 'nombre']
    >>> del persona1.nombre
    >>> dir(persona1)
    ['__doc__', '__init__', '__module__', '_nombre', 'nombre']
    >>> print(persona1.nombre)
    Obteniendo nombre
    Leo

Aquí, en vez de usar el método ``property()``, es usado el
:ref:`decorador <python_decoradores>` @property.

Primero especifica que el método ``nombre()`` es un atributo de la clase ``Persona``.
Esto es hecho usando la sintaxis ``@property`` antes el método *getter* como se
muestra en el código anterior.

Seguidamente se usa el nombre del atributo ``nombre`` para especificar los métodos
*setter* y *deleter*.

Esto es hecho usando la sintaxis @<nombre-de-atributo>.setter (``@nombre.setter``) para
el método *setter* y @<nombre-de-atributo>.deleter (``@nombre.deleter``) para el método
*deleter*.

Note, es usando el mismo método ``nombre()`` con diferentes definiciones para definir
los métodos ``getter``, ``setter`` y ``deleter``.

Ahora, cada vez que se usa ``persona1.nombre``, es internamente llama el apropiado método
para ``getter``, ``setter`` y ``deleter`` como lo muestra la salida impresa presente
dentro de cada método.


.. _python_cls_super:

super
~~~~~

La clase ``super`` típicamente es usada al llamar un método de superclase cooperativo.
Las sintaxis de como usarlo son las siguientes:

.. code-block:: pycon

    >>> super(type, obj)

El código anterior devuelve un súper objeto enlazado; requiere ``isinstance(obj, type)``.

.. code-block:: pycon

    >>> super(type)

El código anterior devuelve un súper objeto no unido.

.. code-block:: pycon

    >>> super(type, type2)

El código anterior devuelve un súper objeto enlazado; requiere ``issubclass(type2, type)``.


Para declarar un método de superclase cooperativo, use esta sintaxis:

::

    class ClaseBase():
        def metodo(self, argumento):
            pass
    class Clase(ClaseBase):
        def metodo(self, argumento):
            super(Clase, self).metodo(argumento)

Un ejemplo sencillo real se muestra a continuación:

.. code-block:: pycon

    >>> class Mamifero(object):
    ...     def __init__(self, mamifero):
    ...         print(mamifero, "es un animal de sangre caliente.")
    ...
    >>> class Perro(Mamifero):
    ...     def __init__(self):
    ...         print("Perro tiene 4 piernas.")
    ...         super(Perro, self).__init__("Perro")
    ...
    >>> perrito = Perro()
    Perro tiene 4 piernas.
    Perro es un animal de sangre caliente.
    >>> isinstance(perrito, Perro)
    True


Aquí, se llama el método ``__init__`` de la clase ``Mamifero`` (desde la clase
``Perro``) usando el código fuente ``super(Perro, self).__init__('Perro')`` en
vez de del tradicional ``Mamifero.__init__(self, 'Perro')``.

Como no necesitamos especificar el nombre de la clase base si usamos ``super()``,
podemos cambiar fácilmente la clase base para el método ``Perro`` (si es necesario).

A continuación un ejemplo de cambiar la clase base a la clase RazaCanina:

.. code-block:: pycon

    >>> class Mamifero(object):
    ...     def __init__(self, mamifero):
    ...         print(mamifero, "es un animal de sangre caliente.")
    ...
    >>> class RazaCanina(Mamifero):
    ...     def __init__(self, nombre, raza):
    ...         print(raza, "es la raza del canino.")
    ...         super(RazaCanina, self).__init__("Perro")
    ...
    >>> class Perro(RazaCanina):
    ...     def __init__(self, raza):
    ...         print("Perro tiene 4 piernas.")
    ...         super(Perro, self).__init__("Perro", raza)
    ...
    >>> perrito = Perro("Pastor Alemán")
    Perro tiene 4 piernas.
    Pastor Alemán es la raza del canino.
    Perro es un animal de sangre caliente.

El método integrado ``super()`` regresa un objeto proxy, un objeto substituto que
tiene la habilidad de llamar al método de la clase base vía delegación. Esto es
llamado indirección (habilidad de referenciar objeto base con el método ``super()``).

Desde que la indirección es calculada en tiempo ejecución, usted puede usar para
apuntar hacia una clase base diferente en tiempo diferente (si usted lo necesita).

A continuación un ejemplo del uso ``super()`` con
:ref:`herencia múltiple <python_poo_herencia_multiple>` de la objetos:

.. code-block:: pycon

    >>> class Animal(object):
    ...     def __init__(self, animal):
    ...         print(
    ...             animal,
    ...             "es un animal.\n\n",
    ...         )
    ...
    >>> class Mamifero(Animal):
    ...     def __init__(self, mamifero):
    ...         print(mamifero, "es un animal de sangre caliente.")
    ...         super(Mamifero, self).__init__(mamifero)
    ...
    >>> class MamiferoNoVolador(Mamifero):
    ...     def __init__(self, mamifero):
    ...         print(mamifero, "no puede volar.")
    ...         super(MamiferoNoVolador, self).__init__(mamifero)
    ...
    >>> class MamiferoNoAcuatico(Mamifero):
    ...     def __init__(self, mamifero):
    ...         print(mamifero, "no puede nadar.")
    ...         super(MamiferoNoAcuatico, self).__init__(mamifero)
    ...
    >>> class Perro(MamiferoNoAcuatico, MamiferoNoVolador):
    ...     def __init__(self):
    ...         print(
    ...             "Perro tiene 4 piernas.\n",
    ...         )
    ...         super(Perro, self).__init__("Perro")
    ...
    >>> perro = Perro()
    Perro tiene 4 piernas.
    Perro no puede nadar.
    Perro no puede volar.
    Perro es un animal de sangre caliente.
    Perro es un animal.

    >>> Perro.__mro__
    (<class '__main__.Perro'>,
    <class '__main__.MamiferoNoAcuatico'>,
    <class '__main__.MamiferoNoVolador'>,
    <class '__main__.Mamifero'>,
    <class '__main__.Animal'>,
    <type 'object'>)
    >>> murcielago = MamiferoNoAcuatico("Murcielago")
    Murcielago no puede nadar.
    Murcielago es un animal de sangre caliente.
    Murcielago es un animal.

    >>> MamiferoNoAcuatico.__mro__
    (<class '__main__.MamiferoNoAcuatico'>,
    <class '__main__.Mamifero'>,
    <class '__main__.Animal'>,
    <type 'object'>)

El orden en resolver la herencia múltiple esta basado en el principio
:ref:`Method Resolution Order (MRO) <python_poo_herencia_multiple_mro>`.

El *MRO* es calculado en Python de la siguiente forma:

Un método en la llamada derivada es siempre llamada antes de método de la clase base.
En nuestro ejemplo, la clase ``Perro`` es llamada antes de las clases ``MamiferoNoAcuatico``
o ``MamiferoNoVolador``. Esas dos clases son llamada antes de la clase ``Mamifero``
el cual es llamada antes de la clase ``Animal`` y la clase ``Animal`` es llamada antes
de la clase ``object``.

Si hay herencia múltiple como ``Perro(MamiferoNoAcuatico, MamiferoNoVolador)``, el
método de ``MamiferoNoAcuatico`` es invocado primero por que ese aparece primero.

.. _python_cls_type:

type
....

Los :ref:`objetos tipo <python_types_objs>` representan los diversos tipos de objeto.
El tipo de un objeto es accesible mediante la función integrada
:ref:`type() <python_fun_type>`. No hay operaciones especiales sobre los tipos. El
módulo estándar ``types`` define nombres para todos los tipos internos estándar.

.. code-block:: pycon

    >>> type(type)
    <type 'type'>


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion9>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
