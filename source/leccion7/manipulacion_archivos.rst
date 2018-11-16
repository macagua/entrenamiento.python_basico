.. -*- coding: utf-8 -*-


.. _python_manipular_archivo:

Manipulación de archivos
------------------------

Para escribir o leer cadenas de caracteres para/desde archivos (otros tipos deben 
ser convertidas a cadenas de caracteres). Para esto Python incorpora un tipo integrado 
llamado ``file``, el cual es manipulado mediante un objeto fichero el cual fue generado 
a través de una función integrada en Python, a continuación se describen los procesos 
típicos y sus referencias a funciones propias del lenguaje:


.. _python_abrir_archivo:

Abrir archivo
.............

La forma preferida para abrir un archivo es usando la función integrada 
:ref:`open() <python_funcion_open>`.


.. _python_leer_archivo:

Leer archivo
............

La forma preferida para leer un archivo es usando algunas de las funciones del 
objeto ``file`` como :ref:`read() <python_funcion_read>`, 
:ref:`readline() <python_funcion_readline>` y :ref:`readlines() <python_funcion_readlines>`. 


.. _python_escribir_archivo:

Escribir archivo
................

La forma preferida para escribir un archivo es usando la función del objeto 
``file`` llamada :ref:`write() <python_funcion_write>`.


.. _python_cerrar_archivo:

Cerrar archivo
..............

La forma preferida para cerrar un archivo es usando la función del objeto 
``file`` llamada :ref:`close() <python_funcion_close>`.


.. _python_ejemplos_archivo:

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


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion7/archivo.py>`.


.. tip::
    Para ejecutar el código :file:`archivo.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando: ::

        python2 archivo.py


----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los tipos 
**file** desde la :ref:`consola interactiva <python_interactivo>` de la 
siguiente forma:

::

    >>> help(file)

Para salir de esa ayuda presione la tecla ``q``.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion7>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
