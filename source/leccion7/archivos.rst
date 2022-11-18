.. -*- coding: utf-8 -*-


.. _python_manipular_archivo:

Manipulación de archivos
------------------------

Para escribir o leer cadenas de caracteres para/desde archivos (otros tipos deben ser
convertidas a cadenas de caracteres). Para esto Python incorpora un tipo integrado
llamado :ref:`file <python_cls_file>`, el cual es manipulado mediante un objeto archivo
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


.. _python_archivos_mdl_os:

Archivos con modulo os
......................

El módulo ``os`` de Python le permite a usted realizar operaciones dependiente del
*Sistema Operativo* como crear una carpeta, listar contenidos de una carpeta, conocer
acerca de un proceso, finalizar un proceso, etc. Este módulo tiene métodos para ver
variables de entornos del *Sistema Operativo* con las cuales Python esta trabajando
en mucho más. `Aquí <https://docs.python.org/es/3.7/library/os.html>`_ la documentación
Python para el módulo ``os``.

A continuación algunos útiles métodos del módulo ``os`` que pueden ayudar a manipular
archivos y carpeta en su programa Python:

*Crear una nueva carpeta*

.. code-block:: pycon

    >>> import os
    >>> os.makedirs("Ana_Poleo")


*Listar el contenidos de una carpeta*

.. code-block:: pycon

    >>> import os
    >>> os.listdir("./")
    ['Ana_Poleo']


*Mostrar el actual directorio de trabajo*

.. code-block:: pycon

    >>> import os
    >>> os.getcwd()
    '/home/usuario/python/'


*Mostrar el tamaño del archivo en ``bytes`` del archivo pasado en parámetro*

.. code-block:: pycon

    >>> import os
    >>> os.path.getsize("Ana_Poleo")
    4096


*¿Es un archivo el parámetro pasado?*

.. code-block:: pycon

    >>> import os
    >>> os.path.isfile("Ana_Poleo")
    False


*¿Es una carpeta el parámetro pasado?*

.. code-block:: pycon

    >>> import os
    >>> os.path.isdir("Ana_Poleo")
    True


*Cambiar de directorio*

.. code-block:: pycon

    >>> import os
    >>> os.chdir("Ana_Poleo")
    >>> os.getcwd()
    '/home/usuario/python/Ana_Poleo'
    >>> os.listdir("./")
    []
    >>> os.chdir("../")
    >>> os.getcwd()
    '/home/usuario/python'


*Renombrar un archivo*

.. code-block:: pycon

    >>> import os
    >>> os.rename("Ana_Poleo", "Ana_Carolina")
    >>> os.listdir("./")
    ['Ana_Carolina']


*Eliminar un archivo*

.. code-block:: pycon

    >>> import os
    >>> os.chdir("Ana_Carolina")
    >>> archivo = open(os.getcwd() + "/datos.txt", "w")
    >>> archivo.write("Se Feliz!")
    >>> archivo.close()
    >>> os.getcwd()
    '/home/usuario/python/Ana_Carolina'
    >>> os.listdir("./")
    ['datos.txt']
    >>> os.remove(os.getcwd() + "/datos.txt")
    >>> os.listdir("./")
    []


*Eliminar una carpeta*

.. code-block:: pycon

    >>> os.rmdir("Ana_Carolina")
    >>> os.chdir("Ana_Carolina")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    OSError: [Errno 2] No such file or directory: 'Ana_Carolina'

Lanza una excepción :ref:`OSError <python_exception_oserror>` cuando intenta acceder
al directorio que previamente elimino y este no encuentra.


.. _python_ejemplos_archivo:

Ejemplos de archivos
....................

A continuación, se presentan algunos ejemplos del uso del tipo objeto
:ref:`file <python_cls_file>`:

**Iterar un archivo para leerlo**

Usted puede iterar sobre un archivo como se muestra a continuación:

.. code-block:: pycon

    >>> archivo = open("datos.txt", "r")
    >>> for linea in archivo:
    ...     print(linea)
    ...
    Este es una prueba

    y otra prueba
    >>> archivo.close()


**Iterar un archivo con escritura y lectura**

Usted puede manipular un archivo con permisos de escritura y lectura, ademas de
interactuar de el mismo como se muestra a continuación:


.. literalinclude:: ../../recursos/leccion7/archivo.py
    :language: python
    :lines: 6-46


Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los tipos objeto
:ref:`file <python_cls_file>` desde la :ref:`consola interactiva <python_interactivo>`
de la siguiente forma:

.. code-block:: pycon

    >>> help(file)

Para salir de esa ayuda presione la tecla :keys:`q`.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion7/archivo.py>`.


.. tip::
    Para ejecutar el código :file:`archivo.py`, abra una consola de comando, acceda al
    directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    .. code-block:: console

        $ python archivo.py


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion7>` del
    entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
