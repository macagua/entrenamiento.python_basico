.. -*- coding: utf-8 -*-


.. _python_1er_programa:

Su primer programa
------------------

En informática, un programa **Hola Mundo** es el que imprime el texto
*«¡Hola, Mundo!»* en un dispositivo de visualización, en la mayoría de
los casos una pantalla de monitor. Este programa suele ser usado como
introducción al estudio de un lenguaje de programación, siendo un primer
ejercicio típico, y se lo considera fundamental desde el punto de vista
didáctico.

El *Hola Mundo* se caracteriza por su sencillez, especialmente cuando se
ejecuta en una interfaz de línea de comandos. En interfaces gráficas la
creación de este programa requiere de más pasos.

El programa *Hola Mundo* también puede ser útil como prueba de configuración
para asegurar que el compilador, el entorno de desarrollo y el entorno de
ejecución estén instalados correctamente y funcionando.


.. _python_hola_mundo:

¡Hola, Mundo!
.............

Programa ¡Hola, Mundo! en diversas versiones de Python:

.. _python3_hola_mundo:

**Python 3.x:** ::

  print("Hola Mundo");


.. _python_ejecucion:

Ejecución
.........

Dependiendo del sistema operativo que este usando debe realizar procedimientos 
distintos para cada plataforma cuando usted quiere escribir y ejecutar un programa 
Python. A continuación un procedimiento básico para las principales plataformas:

.. _python_ejecutar_windows:

Ejecutar un programa en Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cree un directorio llamado ``proyectos`` la unidad ``C:\`` y dentro
de este, cree un archivo de texto plano con el siguiente nombre
``holamundo.py`` y escriba la sintaxis de :ref:`Python 3 <python3_hola_mundo>`
respectivamente.

Luego ejecute desde la consola de ``MS-DOS`` el siguiente comando:

::

  C:\Python37\python C:\proyectos\holamundo.py

Usted debe ver la línea *Hola Mundo*.

Enhorabuena, usted ha ejecutado su primer programa Python.


.. _python_ejecutar_macos:

Ejecutar un programa en macOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Haga clic en ``Archivo`` y luego la nueva Ventana del ``Finder``.

#. Haga clic en ``Documentos``.

#. Haga clic en ``Archivo`` y luego en ``Nueva carpeta``.

#. Llame a la carpeta ``proyectos``.

#. Usted va a almacenar todos los programas relacionados con la clase allí.

#. Haga clic en ``Aplicaciones`` y, a continuación ``TextEdit``.

#. Haga clic en ``TextEdit`` en la barra de menú y seleccione ``Preferencias``.

#. Seleccione ``Texto plano``.

#. En el vacío ``TextEdit`` tipo de ventana en el siguiente programa, tal y
   como escribe la sintaxis de :ref:`Python 3 <python3_hola_mundo>` respectivamente.

#. Desde el archivo de menú en TextEdit.

#. Haga clic en ``Guardar como``.

#. En el campo Guardar como: escriba ``holamundo.py``.

#. Seleccione ``Documentos`` y la carpeta de archivos ``proyectos``.

#. Haga clic en ``Guardar``.

*Funcionamiento de su Primer Programa*

#. Seleccione ``Aplicaciones``, a continuación, ``Utilidades y Terminal``.

#. En la ventana ``Terminal`` ejecute ``ls`` y presione la tecla ``Enter``.
   Se debe dar una lista de todas las carpetas de nivel superior. Usted debe
   ver la carpeta de ``Documentos``.

#. Ejecute ``cd Documentos`` y presione la tecla ``Enter``.

#. Ejecute ``ls`` y presione la tecla ``Enter`` y debería ver la carpeta ``proyectos``.

#. Ejecute ``cd proyectos`` y presione la tecla ``Enter``.

#. Ejecute ``ls`` y presione la tecla ``Enter`` y usted debería ver el archivo ``holamundo.py``.

#. Para ejecutar el programa, escriba el siguiente comando ``python3.7 holamundo.py`` 
   y presione la tecla ``Enter``.

#. Usted debe ver la línea *Hola Mundo*.

Enhorabuena, usted ha ejecutado su primer programa Python.


.. _python_ejecutar_linux:

Ejecutar un programa en Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cree un directorio llamado ``proyectos`` el ``home`` de su usuario
y dentro de este, cree un archivo de texto plano con el siguiente
nombre ``holamundo.py`` y escriba la sintaxis de :ref:`Python 3 <python3_hola_mundo>` respectivamente.

Luego ejecute desde la consola de comando el siguiente comando:

::

    python3.7 $HOME/proyectos/holamundo.py

Usted debe ver la línea *Hola Mundo*.

Enhorabuena, usted ha ejecutado su primer programa Python.

----

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion1/holamundo.py>`.


.. tip::
    Para ejecutar el código :file:`holamundo.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando:

    ::

        python3.7 holamundo.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion2>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
