.. -*- coding: utf-8 -*-


.. _python_manipular_archivo:

Manipulación de archivos
------------------------

Para escribir o leer cadenas de caracteres para/desde archivos (otros tipos deben ser 
convertidas a cadenas de caracteres). Para esto Python incorpora un tipo integrado 
llamado :ref:`file <python_cls_file>`, el cual es manipulado mediante un objeto fichero 
el cual fue generado a través de una función integrada en Python, a continuación se 
describen los procesos típicos y sus referencias a funciones propias del lenguaje:


.. _python_abrir_archivo:

Abrir archivo
.............

La forma preferida para abrir un archivo es usando la función integrada 
:ref:`open() <python_fun_open>`.


.. _python_leer_archivo:

Leer archivo
............

La forma preferida para leer un archivo es usando algunas de los métodos del tipo objeto 
:ref:`file <python_cls_file>` como :ref:`read() <python_mtd_read>`, 
:ref:`readline() <python_mtd_readline>` y :ref:`readlines() <python_mtd_readlines>`. 


.. _python_escribir_archivo:

Escribir archivo
................

La forma preferida para escribir un archivo es usando el método del tipo objeto 
:ref:`file <python_cls_file>` llamado :ref:`write() <python_mtd_write>`.


.. _python_cerrar_archivo:

Cerrar archivo
..............

La forma preferida para cerrar un archivo es usando el método del tipo objeto 
:ref:`file <python_cls_file>` llamado :ref:`close() <python_mtd_close>`.


.. _python_ejemplos_archivo:

Ejemplos de archivos
....................

A continuación, se presentan algunos ejemplos del uso del tipo objeto 
:ref:`file <python_cls_file>`:

**Ejemplo de iterar un archivo para leerlo**

Usted puede iterar sobre un archivo como se muestra a continuación:

::

    >>> archivo = open('datos.txt', 'r')
    >>> for linea in archivo:
    ...     print linea
    ... 
    Este es una prueba 

    y otra prueba
    >>> archivo.close()


**Ejemplo de iterar un archivo con escritura y lectura**

Usted puede manipular un archivo con permisos de escritura y lectura, ademas de 
interactuar de el mismo como se muestra a continuación:


.. literalinclude:: ../../recursos/leccion7/archivo.py
    :language: python
    :lines: 8-50


Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los tipos 
**file** desde la :ref:`consola interactiva <python_interactivo>` de la 
siguiente forma:

::

    >>> help(file)

Para salir de esa ayuda presione la tecla ``q``.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion7/archivo.py>`.


.. tip::
    Para ejecutar el código :file:`archivo.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando:

    ::

        python archivo.py


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion7>` del 
    entrenamiento para ampliar su conocimiento en esta temática.
