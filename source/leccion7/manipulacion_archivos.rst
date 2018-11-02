.. -*- coding: utf-8 -*-


.. _python_manipular_archivo:

Manipulación de archivos
------------------------

Para escribir o leer cadenas de caracteres para/desde archivos (otros tipos deben 
ser convertidas a cadenas de caracteress). 

open()
......

La función ``open`` devuelve un objeto del tipo ``file`` (i.e. archivo), y se 
invoca habitualmente con dos argumentos: 'nombre de archivo' y 'modo'. El primero 
es una cadena de caracteres que indica el *nombre de archivo*. El segundo es otra 
cadena de unos pocos caracteres describiendo la forma en la que se usará el archivo, 
como se indica a continuación.

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
| ``wb``   | el archivo se abre en modo binario, para almacenar cualquier cosa que no sea texto        | 
+----------+-------------------------------------------------------------------------------------------+

.. note::

	- **Modo** ``wb`` usar para archivos binarios, específicamente en Windows.


Para crear en un archivo:

::

	>>> f = open('datos.txt', 'w') # abre el archivo datos.txt
	>>> type(f)
	<type 'file'>


read()
......

La función ``read()`` permite leer el contenido del archivo. El argumento 
es opcional y si no se especifica (o es -1) devuelve el contenido de todo 
el archivo. Una vez que se leyó todo el archivo, una nueva llamada a 
la función devuelve un string vacío ('').

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


readline()
..........

La función ``readline()`` permite leer una sola línea del archivo, 
devuelve al final de la línea el caracter de nueva línea y solo 
se omite en la última línea del archivo (si no termina con el caracter 
de nueva línea). Esto hace que el valor de retorno no sea ambigüo. 
Si retorna una cadena de caracteres vacía se alcanzó el fin del archivo, 
mientras que una línea en blanco se representa con un caracter de nueva línea.

::

	>>> f = open('datos.txt', 'r')
	>>> print f.readline() # lee la linea "Este es una prueba "
	>>> print f.readline() # lee la linea "y otra prueba"
	>>> print f.readline()
		
	>>> 


readlines()
...........

La función ``readlines()`` devuelve una lista que contiene todas las 
líneas del archivo.

::

	>>> f = open('datos.txt', 'r')
	>>> lines = f.readlines()
	>>> print(lines)
	['Este es una prueba \n', 'y otra prueba']


write()
.......

La función ``write()`` permite escribir el contenido de la cadena de 
texto al archivo, y devuelve la cantidad de caracteres escritos.

Para escribir algo que no sea una cadena de caracteres, antes se 
debe convertir a cadena de caracteres.

::

	>>> f = open('datos.txt', 'w')
	>>> f.write('Este es una prueba \ny otra prueba') # escribe el archivo datos.txt


close()
.......

La función ``close()`` permite cerrar la manipulación del archivo.

Una vez que se terminó de usar el archivo es necesario cerrarlo, para liberar 
los recursos tomados por el manejo del archivo. Eso se hace con la sentencia 
``f.close()``:

::

	>>> f.close() # cierra el archivo datos.txt


Luego de lo cual no se puede acceder al archivo ``datos.txt``, si intenta 
una invocación a la función ``f.read()`` devuelve un error, porque el archivo 
está cerrado:

::

	>>> f.close()
	>>> f.read()
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: I/O operation on closed file


.. tip:: Para más detalles: http://docs.python.org/tutorial/inputoutput.html


Ejemplos de archivos
....................

A continuación, se presentan algunos ejemplos del uso del tipo ``file``:

**Ejemplo de iterar sobre un archivo**

Usted puede iterar sobre un archivo como se muestra a continuación:

::

	>>> f = open('datos.txt', 'r')
	>>> for line in f:
	...     print line
	... 
	Este es una prueba 

	y otra prueba
	>>> f.close()


----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los tipos 
**file** desde la :ref:`consola interactiva <python_interactivo>` de la 
siguiente forma:

::

    >>> help(file)

Para salir de esa ayuda presione la tecla ``q``.


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion7>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
