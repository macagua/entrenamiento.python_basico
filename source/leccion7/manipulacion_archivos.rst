.. -*- coding: utf-8 -*-


.. _python_manipular_archivo:

Manipulación de archivos
------------------------

Para escribir o leer cadenas de texto para/desde archivos (otros tipos deben 
ser convertidas a cadenas de textos). 

Crear archivo
.............

Para crear o escribir en un archivo:

::

	>>> f = open('archivo.txt', 'w') # abre el archivo archivo.txt
	>>> type(f)
	<type 'file'>
	>>> f.write('Este es una prueba \ny otra prueba')
	>>> f.close()


Leer archivo
............

Para leer un archivo:

::

	>>> f = open('archivo.txt', 'r')
	>>> s = f.read()
	>>> print s
	This is a test
	and another test
	>>> f.close()


.. tip:: Para más detalles: http://docs.python.org/tutorial/inputoutput.html


Iterando sobre un archivo
.........................

Usted puede iterar sobre un archivo como se muestra a continuación:

::

	>>> f = open('archivo.txt', 'r')
	>>> for line in f:
	...     print line
	... 
	Este es una prueba 

	y otra prueba
	>>> f.close()


Modos de archivo
................

Usando la función ``open`` se puede manipular los archivos en diversos 
modos, los cuales se describen a continuación:

- Solamente Lectura: ``r``

- Solamente Escritura: ``w``
	*Nota: Crea un nuevo archivo o sobrescribe un archivo existente.*

- Append un archivo: ``a``

- Lectura y Escritura: ``r+``

- Modo Binario: ``b``
	*Nota: Usar para archivos binarios, específicamente en Windows.*


Referencia
..........

- `Input and Output - Scipy lecture notes`_.

.. _`Input and Output - Scipy lecture notes`: https://www.pybonacci.org/scipy-lecture-notes-ES/intro/language/io.html
