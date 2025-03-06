.. _python_manipular_archivo:

Manipulación de archivos
------------------------

Para escribir o leer :ref:`cadenas de caracteres <python_str>` para/desde archivos (otros tipos deben ser
convertidas a :ref:`cadenas de caracteres <python_str>`). Para esto Python incorpora un tipo integrado
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
en mucho más. `Aquí <https://docs.python.org/es/3.11/library/os.html>`_ la documentación
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
    >>> archivo.write("¡Se Feliz!")
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
    :linenos:
    :lines: 5-45


----


Función open()
..............

A continuación se presenta una práctica más real de implementar el uso de la función
integrada :ref:`open() <python_fun_open>` en Python, el cual se implementa para las
operaciones de lectura y escritura en archivos``.csv``:

.. literalinclude:: ../../recursos/leccion7/txt/main.py
    :language: python
    :linenos:
    :lines: 1-30

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`colesterol.csv <../../recursos/leccion7/txt/colesterol.csv>`.

    - :download:`main.py <../../recursos/leccion7/txt/main.py>`.


.. tip::
    Para ejecutar el código :file:`main.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el programa:

    .. code-block:: pycon
        :class: no-copy

        proyectos/
        └── txt/
            ├── colesterol.csv
            └── main.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 main.py


    La salida esperada será similar a la siguiente:

    .. code-block:: console
        :class: no-copy

        ✅ Archivo leido desde la ruta '~/proyectos/txt/colesterol.csv'.

        nombre,edad,sexo,peso,altura,colesterol
        José Luis Martínez Izquierdo,18,H,85.0,1.79,182.0
        Rosa Díaz Díaz,32,M,65.0,1.73,232.0
        Javier García Sánchez,24,H,,1.81,191.0
        Carmen López Pinzón,35,M,65.0,1.7,200.0
        Marisa López Collado,46,M,51.0,1.58,148.0
        Antonio Ruiz Cruz,68,H,66.0,1.74,249.0
        Antonio Fernández Ocaña,51,H,62.0,1.72,276.0
        Pilar Martín González,22,M,60.0,1.66,
        Pedro Gálvez Tenorio,35,H,90.0,1.94,241.0
        Santiago Reillo Manzano,46,H,75.0,1.85,280.0
        Macarena Álvarez Luna,53,M,55.0,1.62,262.0
        José María de la Guía Sanz,58,H,78.0,1.87,198.0
        Miguel Angel Cuadrado Gutiérrez,27,H,109.0,1.98,210.0
        Carolina Rubio Moreno,20,M,61.0,1.77,194.0

        ✅ Archivo nuevo creado en la ruta '~/proyectos/txt/colesterol_modificado.csv'.

        nombre,edad,sexo,peso,altura,colesterol
        José Luis Martínez Izquierdo,18,H,85.0,1.79,182.0
        Rosa Díaz Díaz,32,M,65.0,1.73,232.0
        Javier García Sánchez,24,H,,1.81,191.0
        Carmen López Pinzón,35,M,65.0,1.7,200.0
        Marisa López Collado,46,M,51.0,1.58,148.0
        Antonio Ruiz Cruz,68,H,66.0,1.74,249.0
        Antonio Fernández Ocaña,51,H,62.0,1.72,276.0
        Pilar Martín González,22,M,60.0,1.66,
        Pedro Gálvez Tenorio,35,H,90.0,1.94,241.0
        Santiago Reillo Manzano,46,H,75.0,1.85,280.0
        Macarena Álvarez Luna,53,M,55.0,1.62,262.0
        José María de la Guía Sanz,58,H,78.0,1.87,198.0
        Miguel Angel Cuadrado Gutiérrez,27,H,109.0,1.98,210.0
        Carolina Rubio Moreno,20,M,61.0,1.77,194.0
        Leonardo Caballero,44,M,61.0,1.77,194.0

        ✅ Archivo nuevo leido desde la ruta '~/proyectos/txt/colesterol_modificado.csv'.


    La estructura de directorio debe ser similar a la siguiente:

    .. code-block:: pycon
        :class: no-copy

        proyectos/
        └── txt/
            ├── colesterol_modificado.csv
            ├── colesterol.csv
            └── main.py

.. tip::
    En lugar de modificar directamente el archivo :file:`colesterol.csv` se
    genera un nuevo archivo llamado :file:`colesterol_modificado.csv` para almacenar los
    cambios realizados.

Asi de esta forma puede ver un ejemplo practico de como manipular un archivo ``.csv`` con
la función integrada :ref:`open() <python_fun_open>`.


----


Módulo csv
..........

A continuación se presenta una práctica más real de implementar el uso del módulo
integrado en Python llamado `csv`_, el cual se implementa para operaciones de archivos
``.csv``:

.. literalinclude:: ../../recursos/leccion7/csv/main.py
    :language: python
    :linenos:
    :lines: 1-38

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`colesterol.csv <../../recursos/leccion7/csv/colesterol.csv>`.

    - :download:`main.py <../../recursos/leccion7/csv/main.py>`.


.. tip::
    Para ejecutar el código :file:`main.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el programa:

    .. code-block:: pycon
        :class: no-copy

        proyectos/
        └── csv/
            ├── colesterol.csv
            └── main.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 main.py


    La salida esperada será similar a la siguiente:

    .. code-block:: console
        :class: no-copy

        ✅ Archivo leido desde la ruta '~/proyectos/csv/colesterol.csv'.

        ['nombre', 'edad', 'sexo', 'peso', 'altura', 'colesterol']
        ['José Luis Martínez Izquierdo', '18', 'H', '85.0', '1.79', '182.0']
        ['Rosa Díaz Díaz', '32', 'M', '65.0', '1.73', '232.0']
        ['Javier García Sánchez', '24', 'H', '', '1.81', '191.0']
        ['Carmen López Pinzón', '35', 'M', '65.0', '1.7', '200.0']
        ['Marisa López Collado', '46', 'M', '51.0', '1.58', '148.0']
        ['Antonio Ruiz Cruz', '68', 'H', '66.0', '1.74', '249.0']
        ['Antonio Fernández Ocaña', '51', 'H', '62.0', '1.72', '276.0']
        ['Pilar Martín González', '22', 'M', '60.0', '1.66', '']
        ['Pedro Gálvez Tenorio', '35', 'H', '90.0', '1.94', '241.0']
        ['Santiago Reillo Manzano', '46', 'H', '75.0', '1.85', '280.0']
        ['Macarena Álvarez Luna', '53', 'M', '55.0', '1.62', '262.0']
        ['José María de la Guía Sanz', '58', 'H', '78.0', '1.87', '198.0']
        ['Miguel Angel Cuadrado Gutiérrez', '27', 'H', '109.0', '1.98', '210.0']
        ['Carolina Rubio Moreno', '20', 'M', '61.0', '1.77', '194.0']

        ✅ Archivo nuevo creado en la ruta '~/proyectos/csv/colesterol_modificado.csv'.

        ['nombre', 'edad', 'sexo', 'peso', 'altura', 'colesterol']
        ['José Luis Martínez Izquierdo', '18', 'H', '85.0', '1.79', '182.0']
        ['Rosa Díaz Díaz', '32', 'M', '65.0', '1.73', '232.0']
        ['Javier García Sánchez', '24', 'H', '', '1.81', '191.0']
        ['Carmen López Pinzón', '35', 'M', '65.0', '1.7', '200.0']
        ['Marisa López Collado', '46', 'M', '51.0', '1.58', '148.0']
        ['Antonio Ruiz Cruz', '68', 'H', '66.0', '1.74', '249.0']
        ['Antonio Fernández Ocaña', '51', 'H', '62.0', '1.72', '276.0']
        ['Pilar Martín González', '22', 'M', '60.0', '1.66', '']
        ['Pedro Gálvez Tenorio', '35', 'H', '90.0', '1.94', '241.0']
        ['Santiago Reillo Manzano', '46', 'H', '75.0', '1.85', '280.0']
        ['Macarena Álvarez Luna', '53', 'M', '55.0', '1.62', '262.0']
        ['José María de la Guía Sanz', '58', 'H', '78.0', '1.87', '198.0']
        ['Miguel Angel Cuadrado Gutiérrez', '27', 'H', '109.0', '1.98', '210.0']
        ['Carolina Rubio Moreno', '20', 'M', '61.0', '1.77', '194.0']
        ['Leonardo Caballero', '44', 'H', '61.0', '1.77', '194.0']

        ✅ Archivo nuevo leido desde la ruta '~/proyectos/csv/colesterol_modificado.csv'.

    La estructura de directorio debe ser similar a la siguiente:

    .. code-block:: pycon
        :class: no-copy

        proyectos/
        └── csv/
            ├── colesterol_modificado.csv
            ├── colesterol.csv
            └── main.py

.. tip::
    En lugar de modificar directamente el archivo :file:`colesterol.csv` se
    genera un nuevo archivo llamado :file:`colesterol_modificado.csv` para almacenar los
    cambios realizados.

Asi de esta forma puede ver un ejemplo practico de como manipular un archivo ``.csv`` con
el módulo `csv`_.


----


Librería pandas
...............

A continuación se presenta una práctica más real de implementar el uso de la librería
externa  en Python llamada `pandas`_, el cual se implementa para operaciones de archivos
``.csv``:

.. literalinclude:: ../../recursos/leccion7/pandas/main.py
    :language: python
    :linenos:
    :lines: 1-18

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`colesterol.csv <../../recursos/leccion7/pandas/colesterol.csv>`.

    - :download:`main.py <../../recursos/leccion7/pandas/main.py>`.


.. tip::
    Para ejecutar el código :file:`main.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el programa:

    .. code-block:: pycon
        :class: no-copy

        proyectos/
        └── pandas/
            ├── colesterol.csv
            └── main.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 main.py


    La salida esperada será similar a la siguiente:

    .. code-block:: console
        :class: no-copy

        ✅ El conjunto de datos en la ruta '~/proyectos/pandas/colesterol.csv' fue cargado correctamente.

                                nombre  edad sexo  peso altura colesterol
        0  José Luis Martínez Izquierdo    18    H  85.0   1.79      182.0
        1                Rosa Díaz Díaz    32    M  65.0   1.73      232.0
        2         Javier García Sánchez    24    H   NaN   1.81      191.0
        3           Carmen López Pinzón    35    M  65.0    1.7      200.0
        4          Marisa López Collado    46    M  51.0   1.58      148.0

        📜 El conjunto de datos original contiene '14' lineas.

Asi de esta forma puede ver un ejemplo practico de como manipular un archivo ``.csv`` con
el módulo `pandas`_.


----


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

        python3 archivo.py


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion7>` del
    entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`csv`: https://docs.python.org/es/3.11/library/csv.html#module-csv
.. _`pandas`: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table
