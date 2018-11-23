.. -*- coding: utf-8 -*-


.. _python_distribucion_paquetes:

Distribución de Software
------------------------

La distribución de código Python se hace mediante módulo ``distutils``.


.. _python_modulo_distutils:

Módulo distutils
................

Permite "empacar" el código de un proyecto de software para ser redistribuido en 
otros proyectos Python. 

Cada paquete empaquetado se puede distribuir en su propia pagina de proyecto y al 
mismo tiempo puede optar a publicar su proyecto en el Python Package Index (PyPI), 
con el cual si lo publica allí su proyecto estará a su alcance y sino de muchos mas 
programadores, ya que es un repositorio de software publico, solo con ejecutar el 
comando ``pip install libreria`` lo convierte en una herramienta tremendamente útil 
y probablemente sea una de las razones del éxito de Python entre los que empiezan 
a programar.

.. _python_estructura_proyecto:

Estructura de proyecto
......................

Para poder empaquetar un proyecto necesita como mínimo la estructura de archivos 
siguiente:

::

    DIRECTORIO-DEL-PROYECTO
    ├── LICENSE
    ├── MANIFEST.in
    ├── README.txt
    ├── setup.py
    └── NOMBRE-DEL-PAQUETE
         ├── __init__.py
         ├── ARCHIVO1.py
         ├── ARCHIVO2.py
         └── MODULO (OPCIONAL)
               ├── __init__.py
               └── MAS_ARCHIVOS.py

Vamos a ver qué significan los elementos anteriores:

- ``DIRECTORIO-DEL-PROYECTO`` puede ser cualquiera, no afecta en absoluto, lo que 
  cuenta es lo que hay dentro.

- ``NOMBRE-DEL-PAQUETE`` tiene que ser el nombre del paquete, si el nombre es 
  ``tostadas_pipo``, este directorio tiene que llamarse también ``tostadas_pipo``. 
  Y esto es así. Dentro estarán todos los archivos que forman la librería.

- ``LICENSE``: es el archivo donde se define los términos de licencia usado en su 
  proyecto. Es muy importate que cada paquete cargado a PyPI incluirle una copia de 
  los términos de licencia. Esto le dice a los usuario quien instala el paquete los 
  términos bajos los cuales pueden usarlo en su paquete. Para ayuda a seleccionar 
  una licencia, consulte https://choosealicense.com/. Una vez tenga seleccionado una 
  licencia abra el archivo ``LICENSE`` e ingrese el texto de la licencia. Por ejemplo, 
  si usted elije la licencia GPL: ::

    License
    =======

    PACKAGE-NAME Copyright YEAR, PACKAGE-AUTHOR

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston,
    MA 02111-1307 USA.


- ``MANIFEST.in``: es el archivo donde se define los criterios de inclusión 
  y exclusión de archivos a su distribución de código fuente de su proyecto. 
  Este archivo incluye la configuración del paquete como se indica a continuación:


.. literalinclude:: ../../recursos/leccion8/distutils/MANIFEST.in
    :language: text
    :lines: 1-7


- ``README.txt``: es el archivo donde se define la documentación general del paquete, 
  este archivo es importante debido a que no solo es usado localmente en un copia 
  descargada, sino como información usada el en sitio de PyPI. Entonces abra el archivo 
  ``README.txt`` e ingrese el siguiente contenido. Usted puede personalizarlo como quiera: ::

    ==================
    NOMBRE-DEL-PAQUETE
    ==================

    Este es un ejemplo simple de un paquete Python. 

    Usted puede usar para escribir este contenido la guía 
    `Restructured Text (reST) and Sphinx CheatSheet <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_.


- ``setup.py``: es el archivo donde se define el paquete, el formato es el mismo 
  para el modulo ``setuptools`` y para el modulo ``distutils`` así que no hay que 
  preocuparse por nada más. Lo vemos a continuación. Este archivo incluye la 
  configuración del paquete como se indica a continuación:

.. literalinclude:: ../../recursos/leccion8/distutils/setup.py
    :language: python
    :lines: 2-50

Entonces debe cree la siguiente estructura de directorios, ya hecha para seguir 
adelante:

:: 

    distro_distutils/
    ├── LICENSE
    ├── MANIFEST.in
    ├── README.txt
    ├── setup.py
    └── tostadas_pipo
        ├── __init__.py
        ├── principal.py
        └── utilidades
            ├── calculos.py
            ├── impuestos.py
            └── __init__.py


.. _python_distro_build_pkg:

Construir dependencias
......................

Para construir cualquier cosas requeridas para instalar el paquete, ejecutando 
el siguiente comando:

::

    python2 ./setup.py -v build
    running build
    running build_py
    creating build
    creating build/lib.linux-x86_64-2.7
    creating build/lib.linux-x86_64-2.7/tostadas_pipo
    copying tostadas_pipo/__init__.py -> build/lib.linux-x86_64-2.7/tostadas_pipo
    copying tostadas_pipo/principal.py -> build/lib.linux-x86_64-2.7/tostadas_pipo
    creating build/lib.linux-x86_64-2.7/tostadas_pipo/utilidades
    copying tostadas_pipo/utilidades/__init__.py -> build/lib.linux-x86_64-2.7/tostadas_pipo/utilidades
    copying tostadas_pipo/utilidades/calculos.py -> build/lib.linux-x86_64-2.7/tostadas_pipo/utilidades
    copying tostadas_pipo/utilidades/impuestos.py -> build/lib.linux-x86_64-2.7/tostadas_pipo/utilidades
    not copying tostadas_pipo/principal.py (output up-to-date)
    not copying tostadas_pipo/__init__.py (output up-to-date)

De esta forma al terminar la ejecución del comando previo debe tener generado un 
directorio llamado ``build`` e incluyendo el paquete ``tostadas_pipo`` construido 
con todo lo necesario para generar su distribución, como se muestra a continuación:

::

    build/
    └── lib.linux-x86_64-2.7
        └── tostadas_pipo
            ├── __init__.py
            ├── principal.py
            └── utilidades
                ├── calculos.py
                ├── impuestos.py
                └── __init__.py

De esta forma ya construyo el paquete ``tostadas_pipo``  y todas las cosas necesarias 
para generar su distribución de código fuente para su proyecto.


.. _python_distro_generar_pkg:

Generar paquete
...............

Para crear una distribución de código fuente de su paquete, ejecute el siguiente 
comando: 

::

    python2 ./setup.py -v sdist
    running sdist
    running check
    reading manifest template 'MANIFEST.in'
    no previously-included directories found matching 'build'
    no previously-included directories found matching 'dist'
    writing manifest file 'MANIFEST'
    creating tostadas_pipo-0.1
    creating tostadas_pipo-0.1/tostadas_pipo
    creating tostadas_pipo-0.1/tostadas_pipo/utilidades
    making hard links in tostadas_pipo-0.1...
    hard linking LICENSE -> tostadas_pipo-0.1
    hard linking MANIFEST.in -> tostadas_pipo-0.1
    hard linking README.txt -> tostadas_pipo-0.1
    hard linking setup.py -> tostadas_pipo-0.1
    hard linking tostadas_pipo/__init__.py -> tostadas_pipo-0.1/tostadas_pipo
    hard linking tostadas_pipo/principal.py -> tostadas_pipo-0.1/tostadas_pipo
    hard linking tostadas_pipo/utilidades/__init__.py -> tostadas_pipo-0.1/tostadas_pipo/utilidades
    hard linking tostadas_pipo/utilidades/calculos.py -> tostadas_pipo-0.1/tostadas_pipo/utilidades
    hard linking tostadas_pipo/utilidades/impuestos.py -> tostadas_pipo-0.1/tostadas_pipo/utilidades
    creating dist
    Creating tar archive
    removing 'tostadas_pipo-0.1' (and everything under it)

De esta forma al terminar la ejecución del comando previo debe tener generado un 
directorio llamado ``dist`` e incluyendo el paquete en formato de archivo tarball 
comprimido en *gzip*, como se muestra a continuación:

::

    dist/
    └── tostadas_pipo-0.1.tar.gz

Por defecto, el módulo ``distutils`` genera el paquete en formato de archivo 
tarball comprimido usando *gzip*.).

Usted puede cambiar el formato de paquete a generar de su distribución de código 
fuente de su paquete (en formato archivo tarball, archivo zip, etc.), ejecute el 
siguiente comando:

::

    python2 ./setup.py sdist --formats=zip,gztar,bztar
    running sdist
    running check
    reading manifest template 'MANIFEST.in'
    no previously-included directories found matching 'build'
    no previously-included directories found matching 'dist'
    writing manifest file 'MANIFEST'
    creating tostadas_pipo-0.1
    creating tostadas_pipo-0.1/tostadas_pipo
    creating tostadas_pipo-0.1/tostadas_pipo/utilidades
    making hard links in tostadas_pipo-0.1...
    hard linking LICENSE -> tostadas_pipo-0.1
    hard linking MANIFEST.in -> tostadas_pipo-0.1
    hard linking README.txt -> tostadas_pipo-0.1
    hard linking setup.py -> tostadas_pipo-0.1
    hard linking tostadas_pipo/__init__.py -> tostadas_pipo-0.1/tostadas_pipo
    hard linking tostadas_pipo/principal.py -> tostadas_pipo-0.1/tostadas_pipo
    hard linking tostadas_pipo/utilidades/__init__.py -> tostadas_pipo-0.1/tostadas_pipo/utilidades
    hard linking tostadas_pipo/utilidades/calculos.py -> tostadas_pipo-0.1/tostadas_pipo/utilidades
    hard linking tostadas_pipo/utilidades/impuestos.py -> tostadas_pipo-0.1/tostadas_pipo/utilidades
    creating dist
    creating 'dist/tostadas_pipo-0.1.zip' and adding 'tostadas_pipo-0.1' to it
    adding 'tostadas_pipo-0.1/MANIFEST.in'
    adding 'tostadas_pipo-0.1/PKG-INFO'
    adding 'tostadas_pipo-0.1/LICENSE'
    adding 'tostadas_pipo-0.1/README.txt'
    adding 'tostadas_pipo-0.1/setup.py'
    adding 'tostadas_pipo-0.1/tostadas_pipo/principal.py'
    adding 'tostadas_pipo-0.1/tostadas_pipo/__init__.py'
    adding 'tostadas_pipo-0.1/tostadas_pipo/utilidades/impuestos.py'
    adding 'tostadas_pipo-0.1/tostadas_pipo/utilidades/__init__.py'
    adding 'tostadas_pipo-0.1/tostadas_pipo/utilidades/calculos.py'
    Creating tar archive
    Creating tar archive
    removing 'tostadas_pipo-0.1' (and everything under it)

De esta forma al terminar la ejecución del comando previo debe tener generado un 
directorio llamado ``dist`` e incluyendo los tres paquetes en formatos de archivos 
tarball comprimido en *gzip/bzip2* y archivo comprimido en *zip*.

::

    dist/
    ├── tostadas_pipo-0.1.tar.bz2
    ├── tostadas_pipo-0.1.tar.gz
    └── tostadas_pipo-0.1.zip

De esta forma ya genero el(los) paquete(s) en diversos formato de distribución 
de código fuente para su proyecto.


.. _python_distro_instalar:

Instalar paquete
................

Para instalar el paquete de su proyecto, hay dos formas de instalación disponibles 
a continuación:


.. _python_distro_install_pkg_gen:

Instalar paquete generado
~~~~~~~~~~~~~~~~~~~~~~~~~

Para instalar el paquete generado se usa la herramienta ``pip``, ejecutando el 
siguiente comando:

::

    pip install --user dist/tostadas_pipo-0.1.tar.gz

Si al ejecutar el comando anterior muestra el mensaje:

::

      pip
      bash: pip: no se encontró la orden

Esto es debido a que no tiene instalado dicha herramienta, así que debe ejecutar 
el siguiente comando:

::

    sudo apt-get install -y python-pip 

De nuevo vuelva a ejecutar en su consola de comando el comando:

::

    pip install --user dist/tostadas_pipo-0.1.tar.gz
    Processing ./dist/tostadas_pipo-0.1.tar.gz
    Building wheels for collected packages: tostadas-pipo
      Running setup.py bdist_wheel for tostadas-pipo ... done
      Stored in directory: /home/leonardo/.cache/pip/wheels/fd/f9/75/a6965566a3c5a8bff507d7daa30760caca0a7525a3de61eac2
    Successfully built tostadas-pipo
    Installing collected packages: tostadas-pipo
    Successfully installed tostadas-pipo-0.1


De esta forma tiene instalado su paquete en su interprete Python usando la 
herramienta ``pip``.

.. note::
    `pip <https://pip.readthedocs.io/>`_, es una herramienta para instalación y 
    administración de paquetes Python.


.. _python_distro_install_distutils_pkg:

Instalar de código de proyecto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para instalar el paquete desde el código de proyecto, ejecute el siguiente comando:

::

    python2 ./setup.py -v install --user
    running install
    running build
    running build_py
    not copying tostadas_pipo/__init__.py (output up-to-date)
    not copying tostadas_pipo/principal.py (output up-to-date)
    not copying tostadas_pipo/utilidades/__init__.py (output up-to-date)
    not copying tostadas_pipo/utilidades/calculos.py (output up-to-date)
    not copying tostadas_pipo/utilidades/impuestos.py (output up-to-date)
    not copying tostadas_pipo/principal.py (output up-to-date)
    not copying tostadas_pipo/__init__.py (output up-to-date)
    running install_lib
    creating /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo
    copying build/lib.linux-x86_64-2.7/tostadas_pipo/principal.py -> /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo
    copying build/lib.linux-x86_64-2.7/tostadas_pipo/__init__.py -> /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo
    creating /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo/utilidades
    copying build/lib.linux-x86_64-2.7/tostadas_pipo/utilidades/impuestos.py -> /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo/utilidades
    copying build/lib.linux-x86_64-2.7/tostadas_pipo/utilidades/__init__.py -> /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo/utilidades
    copying build/lib.linux-x86_64-2.7/tostadas_pipo/utilidades/calculos.py -> /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo/utilidades
    byte-compiling /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo/principal.py to principal.pyc
    byte-compiling /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo/__init__.py to __init__.pyc
    byte-compiling /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo/utilidades/impuestos.py to impuestos.pyc
    byte-compiling /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo/utilidades/__init__.py to __init__.pyc
    byte-compiling /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo/utilidades/calculos.py to calculos.pyc
    running install_egg_info
    Writing /home/leonardo/venv/lib/python2.7/site-packages/tostadas_pipo-0.1-py2.7.egg-info

De esta forma tiene instalado su paquete en su interprete Python usando el comando ``install`` disponible con el script ``setup.py``.


.. _python_distro_usar_pkg:

Usar paquete
............

Usar el paquete ``tostadas_pipo-0.1``, recuerde que debe usarlo como una librería, 
entonces puede probar el correcto funcionamiento del paquete, importando este, 
ejecutando el siguiente comando:

::

    python -c 'from tostadas_pipo.utilidades.impuestos import impuesto_iva14; print "Función importada " + impuesto_iva14.__doc__[1:36] + "."'
    Función importada Calcula el impuesto del IVA de 14 %.

El comando previo muestra la ``docstring`` de la función importada ``impuesto_iva14`` 
sino muestra ningún mensaje de error, el paquete ``tostadas_pipo-0.1`` se instalo 
correctamente.


.. _python_distro_eliminar_pkg:

Eliminar paquete
................

Para eliminar paquete usando la herramienta ``pip``, ejecute el siguiente comando:

::

    pip uninstall tostadas_pipo
    Uninstalling tostadas-pipo-0.1:
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo-0.1.dist-info/DESCRIPTION.rst
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo-0.1.dist-info/INSTALLER
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo-0.1.dist-info/METADATA
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo-0.1.dist-info/RECORD
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo-0.1.dist-info/WHEEL
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo-0.1.dist-info/metadata.json
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo-0.1.dist-info/top_level.txt
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo/__init__.py
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo/__init__.pyc
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo/principal.py
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo/principal.pyc
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo/utilidades/__init__.py
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo/utilidades/__init__.pyc
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo/utilidades/calculos.py
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo/utilidades/calculos.pyc
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo/utilidades/impuestos.py
      /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo/utilidades/impuestos.pyc
    Proceed (y/n)? y
      Successfully uninstalled tostadas-pipo-0.1

``pip`` esta habiliado a desinstalar la mayoria de paquetes instalados. Las excepciones 
conocidas son:

- Los paquetes ``distutils`` puros instalados sin la herramienta ``pip`` usando el 
  :ref:`código de proyecto distutils <python_distro_install_distutils_pkg>`, 
  which leave behind no metadata to determine what files were installed.

- Los scripts wrappers instalados ``python setup.py develop``.


Si alguno de esos casos previos es el suyo, debe seguir los siguientes pasos para eliminar manualmente el paquete instalado:

#. Al instalar el paquete usando el parámetro ``--user`` el paquete es instalado 
   en el directorio ``$HOME/.local/lib/python2.7/site-packages/`` puede verificar 
   su correcta instalación, ejecute el siguiente comando:

    ::

        ls -p $HOME/.local/lib/python2.7/site-packages/ | grep "tostadas_pipo"
        tostadas_pipo/
        tostadas_pipo-0.1.egg-info/

#. Para eliminar el paquete usando la herramienta ``pip``, ejecute el siguiente 
   comando: 

    ::

        pip uninstall tostadas_pipo
        DEPRECATION: Uninstalling a distutils installed project (tostadas-pipo) has been deprecated and will be removed in a future version. This is due to the fact that uninstalling a distutils project will only partially uninstall the project.
        Uninstalling tostadas-pipo-0.1:
          /home/leonardo/.local/lib/python2.7/site-packages/tostadas_pipo-0.1.egg-info
        Proceed (y/n)? y
          Successfully uninstalled tostadas-pipo-0.1

   Aunque ``pip`` indique **Successfully uninstalled tostadas-pipo-0.1**, no es cierto, 
   solo removió el directorio ``tostadas_pipo-0.1.egg-info`` y dejo instalado el 
   directorio del paquete ``tostadas_pipo``.

#. Luego de ejecutar el comando previo, puede verificar si aun instalado el paquete 
   parcialmente, con el siguiente comando:

    ::

        ls -p $HOME/.local/lib/python2.7/site-packages/ | grep "tostadas_pipo"
        tostadas_pipo/

   Si el comando previo muestra el resultado **tostadas_pipo**, es el directorio del 
   paquete ``tostadas_pipo``, el cual no se ha eliminado. 

#. Entonces tiene que eliminar manualmente el directorio aun encontrado ejecutando el 
   siguiente comando:

    ::

        rm -rf $HOME/.local/lib/python2.7/site-packages/tostadas_pipo

#. Al ejecutar el comando previo, de nuevo verifique que ya fue eliminado de su sistema, 
   ejecutando el siguiente comando:

    ::

        ls -p $HOME/.local/lib/python2.7/site-packages/ | grep "tostadas_pipo"

   Si el comando previo, no muestra el resultado **tostadas_pipo**, es el directorio del 
   paquete ``tostadas_pipo``, fue eliminado completamente de su sistema. 

De esta forma ya tiene eliminado su paquete de forma manual de su sistema.



Ayuda integrada
...............

Usted puede consultar toda la ayuda comandos disponibles del módulo ``distutils``, 
ejecute el comando siguiente:

::

    python2 ./setup.py --help-commands
    Standard commands:
      build            build everything needed to install
      build_py         "build" pure Python modules (copy to build directory)
      build_ext        build C/C++ extensions (compile/link to build directory)
      build_clib       build C/C++ libraries used by Python extensions
      build_scripts    "build" scripts (copy and fixup #! line)
      clean            clean up temporary files from 'build' command
      install          install everything from build directory
      install_lib      install all Python modules (extensions and pure Python)
      install_headers  install C/C++ header files
      install_scripts  install scripts (Python or otherwise)
      install_data     install data files
      sdist            create a source distribution (tarball, zip file, etc.)
      register         register the distribution with the Python package index
      bdist            create a built (binary) distribution
      bdist_dumb       create a "dumb" built distribution
      bdist_rpm        create an RPM distribution
      bdist_wininst    create an executable installer for MS Windows
      upload           upload binary package to PyPI
      check            perform some checks on the package

Para consultar toda la ayuda del módulo ``distutils``, ejecute el comando siguiente:

::

    python2 setup.py --help

----


.. important::
    Usted puede descargar el código usado en esta sección, haciendo clic en el 
    siguiente enlace: :download:`distro_distutils.zip <../../recursos/leccion8/distro_distutils.zip>`.


.. tip::
    Para poder definir un instalador y construirlo para así poder hacer que su proyecto 
    se pueda distribuir de forma más fácil debe crear la :ref:`estructura de proyecto <python_estructura_proyecto>` usando el código descomprimido del archivo 
    :file:`distro_distutils.zip`, siga los pasos para construir los archivos, 
    generar el instalador y probar su instalación.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion8>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
