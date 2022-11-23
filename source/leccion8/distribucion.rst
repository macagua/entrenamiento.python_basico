.. -*- coding: utf-8 -*-


.. _python_distribucion_paquetes:

Distribución de Software
------------------------

La distribución de código Python, le permite hacer portable de forma amigable usando
herramienta de gestión de paquetes Python como la herramienta ``pip``. Esta labor se
hace mediante el módulo :ref:`distutils <python_modulo_distutils>`, y más
reciente incorporando el módulo :ref:`setuptools <python_modulo_setuptools>`.


.. _python_modulo_distutils:

Módulo distutils
................

Permite "empacar" el código de un proyecto de software para ser redistribuido en
otros proyectos Python.

Cada paquete empaquetado se puede distribuir en su propia pagina de proyecto y al
mismo tiempo puede optar a publicar su proyecto en el Python Package Index (PyPI),
con el cual si lo publica allí su proyecto estará a su alcance y sino de muchos mas
programadores, ya que es un repositorio de software publico, solo con ejecutar el
comando ``pip install <paquete>`` lo convierte en una herramienta tremendamente útil
y probablemente sea una de las razones del éxito de Python entre los que empiezan
a programar.


.. _python_modulo_setuptools:

Módulo setuptools
.................

El módulo ``setuptools``, incorpora varias extensiones al módulo ``distutils`` para
distribuciones de software grandes o complejas.


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

A continuación se detallan el significado y uso de la estructura de directorio anterior:

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
  si usted elije la licencia GPL:

  ::

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


.. literalinclude:: ../../recursos/leccion8/distribucion/MANIFEST.in
    :language: text
    :linenos:
    :lines: 1-7


- ``README.txt``: es el archivo donde se define la documentación general del paquete,
  este archivo es importante debido a que no solo es usado localmente en un copia
  descargada, sino como información usada el en sitio de PyPI. Entonces abra el archivo
  ``README.txt`` e ingrese el siguiente contenido. Usted puede personalizarlo como quiera:

  ::

    ==================
    NOMBRE-DEL-PAQUETE
    ==================

    Este es un ejemplo simple de un paquete Python.

    Usted puede usar para escribir este contenido la guía
    `Restructured Text (reST) and Sphinx CheatSheet <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_.


- ``setup.py``: es el archivo donde se define el paquete, el formato es el mismo
  para el módulo :ref:`setuptools <python_modulo_setuptools>` y para el módulo
  :ref:`distutils <python_modulo_distutils>`. Lo puede ver a continuación. Este
  archivo incluye la configuración del paquete como se indica a continuación:

.. literalinclude:: ../../recursos/leccion8/distribucion/setup.py
    :language: python
    :linenos:
    :lines: 1-39

Entonces debe cree la siguiente estructura de directorios, ya hecha para seguir
adelante:

::

    distribucion/
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

.. code-block:: console

    $ python ./setup.py -v build
    running build
    running build_py
    creating build
    creating build/lib.linux-x86_64-3.7
    creating build/lib.linux-x86_64-3.7/tostadas_pipo
    copying tostadas_pipo/__init__.py -> build/lib.linux-x86_64-3.7/tostadas_pipo
    copying tostadas_pipo/principal.py -> build/lib.linux-x86_64-3.7/tostadas_pipo
    creating build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades
    copying tostadas_pipo/utilidades/__init__.py -> build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades
    copying tostadas_pipo/utilidades/calculos.py -> build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades
    copying tostadas_pipo/utilidades/impuestos.py -> build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades
    not copying tostadas_pipo/principal.py (output up-to-date)
    not copying tostadas_pipo/__init__.py (output up-to-date)

De esta forma al terminar la ejecución del comando previo debe tener creado un
directorio llamado ``build`` e incluyendo el paquete ``tostadas_pipo`` construido
con todo lo necesario para crear su distribución, como se muestra a continuación:

::

    build/
    └── lib.linux-x86_64-3.7
        └── tostadas_pipo
            ├── __init__.py
            ├── principal.py
            └── utilidades
                ├── calculos.py
                ├── impuestos.py
                └── __init__.py

De esta forma ya construyo el paquete ``tostadas_pipo``  y todas las cosas necesarias
para crear su distribución de código fuente o binaria para su proyecto.


.. _python_distro_crear_pkg:

Crear paquete
...............

Usted puede crear diversos tipos de formatos de instalación y distribución de sus
paquetes Python, a continuación se describen los mas usados:


.. _python_distro_crear_sdist:

Distribución código fuente
~~~~~~~~~~~~~~~~~~~~~~~~~~

Tanto el módulo :ref:`setuptools <python_modulo_setuptools>` y
:ref:`distutils <python_modulo_distutils>` le permiten crear una distribución de código
fuente o source distribution (``sdist``) de su paquete en formatos como **tarball**,
archivo **zip**, etc. Para crear una paquete ``sdist``, ejecute el siguiente comando:

.. code-block:: console

    $ python ./setup.py -v sdist
    running sdist
    running egg_info
    creating tostadas_pipo.egg-info
    writing tostadas_pipo.egg-info/PKG-INFO
    writing top-level names to tostadas_pipo.egg-info/top_level.txt
    writing dependency_links to tostadas_pipo.egg-info/dependency_links.txt
    writing entry points to tostadas_pipo.egg-info/entry_points.txt
    writing manifest file 'tostadas_pipo.egg-info/SOURCES.txt'
    reading manifest file 'tostadas_pipo.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    warning: no previously-included files matching '*.pyc' found anywhere in distribution
    warning: no previously-included files matching '*.pyo' found anywhere in distribution
    warning: no previously-included files matching '*~' found anywhere in distribution
    no previously-included directories found matching 'build'
    no previously-included directories found matching 'dist'
    writing manifest file 'tostadas_pipo.egg-info/SOURCES.txt'
    running check
    creating tostadas_pipo-0.1
    creating tostadas_pipo-0.1/tostadas_pipo
    creating tostadas_pipo-0.1/tostadas_pipo.egg-info
    creating tostadas_pipo-0.1/tostadas_pipo/utilidades
    copying files to tostadas_pipo-0.1...
    copying LICENSE -> tostadas_pipo-0.1
    copying MANIFEST.in -> tostadas_pipo-0.1
    copying README.txt -> tostadas_pipo-0.1
    copying setup.py -> tostadas_pipo-0.1
    copying tostadas_pipo/__init__.py -> tostadas_pipo-0.1/tostadas_pipo
    copying tostadas_pipo/principal.py -> tostadas_pipo-0.1/tostadas_pipo
    copying tostadas_pipo.egg-info/PKG-INFO -> tostadas_pipo-0.1/tostadas_pipo.egg-info
    copying tostadas_pipo.egg-info/SOURCES.txt -> tostadas_pipo-0.1/tostadas_pipo.egg-info
    copying tostadas_pipo.egg-info/dependency_links.txt -> tostadas_pipo-0.1/tostadas_pipo.egg-info
    copying tostadas_pipo.egg-info/entry_points.txt -> tostadas_pipo-0.1/tostadas_pipo.egg-info
    copying tostadas_pipo.egg-info/top_level.txt -> tostadas_pipo-0.1/tostadas_pipo.egg-info
    copying tostadas_pipo/utilidades/__init__.py -> tostadas_pipo-0.1/tostadas_pipo/utilidades
    copying tostadas_pipo/utilidades/calculos.py -> tostadas_pipo-0.1/tostadas_pipo/utilidades
    copying tostadas_pipo/utilidades/impuestos.py -> tostadas_pipo-0.1/tostadas_pipo/utilidades
    not copying tostadas_pipo.egg-info/SOURCES.txt (output up-to-date)
    Reading configuration from tostadas_pipo-0.1/setup.cfg
    Adding new section [egg_info] to tostadas_pipo-0.1/setup.cfg
    Setting egg_info.tag_build to '' in tostadas_pipo-0.1/setup.cfg
    Setting egg_info.tag_date to 0 in tostadas_pipo-0.1/setup.cfg
    Writing tostadas_pipo-0.1/setup.cfg
    creating dist
    Creating tar archive
    removing 'tostadas_pipo-0.1' (and everything under it)

De esta forma al terminar la ejecución del comando previo debe tener creado un
directorio llamado ``dist`` e incluyendo el paquete en formato de archivo tarball
comprimido en *gztar*, como se muestra a continuación:

::

    dist/
    └── tostadas_pipo-0.1.tar.gz

Por defecto, tanto el módulo :ref:`setuptools <python_modulo_setuptools>` y
:ref:`distutils <python_modulo_distutils>` creá el paquete en formato de archivo tarball
comprimido usando *gztar*.).

Usted puede cambiar el formato de paquete a crear de su distribución de código fuente de
su paquete (en formato archivo **tarball**, archivo **zip**, etc.), ejecute el siguiente
comando:

.. code-block:: console

    $ python ./setup.py sdist --formats=zip,gztar,bztar
    running sdist
    running egg_info
    writing tostadas_pipo.egg-info/PKG-INFO
    writing top-level names to tostadas_pipo.egg-info/top_level.txt
    writing dependency_links to tostadas_pipo.egg-info/dependency_links.txt
    writing entry points to tostadas_pipo.egg-info/entry_points.txt
    reading manifest file 'tostadas_pipo.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    warning: no previously-included files matching '*.pyc' found anywhere in distribution
    warning: no previously-included files matching '*.pyo' found anywhere in distribution
    warning: no previously-included files matching '*~' found anywhere in distribution
    no previously-included directories found matching 'build'
    no previously-included directories found matching 'dist'
    writing manifest file 'tostadas_pipo.egg-info/SOURCES.txt'
    running check
    creating tostadas_pipo-0.1
    creating tostadas_pipo-0.1/tostadas_pipo
    creating tostadas_pipo-0.1/tostadas_pipo.egg-info
    creating tostadas_pipo-0.1/tostadas_pipo/utilidades
    copying files to tostadas_pipo-0.1...
    copying LICENSE -> tostadas_pipo-0.1
    copying MANIFEST.in -> tostadas_pipo-0.1
    copying README.txt -> tostadas_pipo-0.1
    copying setup.py -> tostadas_pipo-0.1
    copying tostadas_pipo/__init__.py -> tostadas_pipo-0.1/tostadas_pipo
    copying tostadas_pipo/principal.py -> tostadas_pipo-0.1/tostadas_pipo
    copying tostadas_pipo.egg-info/PKG-INFO -> tostadas_pipo-0.1/tostadas_pipo.egg-info
    copying tostadas_pipo.egg-info/SOURCES.txt -> tostadas_pipo-0.1/tostadas_pipo.egg-info
    copying tostadas_pipo.egg-info/dependency_links.txt -> tostadas_pipo-0.1/tostadas_pipo.egg-info
    copying tostadas_pipo.egg-info/entry_points.txt -> tostadas_pipo-0.1/tostadas_pipo.egg-info
    copying tostadas_pipo.egg-info/top_level.txt -> tostadas_pipo-0.1/tostadas_pipo.egg-info
    copying tostadas_pipo/utilidades/__init__.py -> tostadas_pipo-0.1/tostadas_pipo/utilidades
    copying tostadas_pipo/utilidades/calculos.py -> tostadas_pipo-0.1/tostadas_pipo/utilidades
    copying tostadas_pipo/utilidades/impuestos.py -> tostadas_pipo-0.1/tostadas_pipo/utilidades
    Writing tostadas_pipo-0.1/setup.cfg
    creating 'dist/tostadas_pipo-0.1.zip' and adding 'tostadas_pipo-0.1' to it
    adding 'tostadas_pipo-0.1/MANIFEST.in'
    adding 'tostadas_pipo-0.1/setup.cfg'
    adding 'tostadas_pipo-0.1/PKG-INFO'
    adding 'tostadas_pipo-0.1/LICENSE'
    adding 'tostadas_pipo-0.1/README.txt'
    adding 'tostadas_pipo-0.1/setup.py'
    adding 'tostadas_pipo-0.1/tostadas_pipo/principal.py'
    adding 'tostadas_pipo-0.1/tostadas_pipo/__init__.py'
    adding 'tostadas_pipo-0.1/tostadas_pipo/utilidades/impuestos.py'
    adding 'tostadas_pipo-0.1/tostadas_pipo/utilidades/__init__.py'
    adding 'tostadas_pipo-0.1/tostadas_pipo/utilidades/calculos.py'
    adding 'tostadas_pipo-0.1/tostadas_pipo.egg-info/dependency_links.txt'
    adding 'tostadas_pipo-0.1/tostadas_pipo.egg-info/entry_points.txt'
    adding 'tostadas_pipo-0.1/tostadas_pipo.egg-info/PKG-INFO'
    adding 'tostadas_pipo-0.1/tostadas_pipo.egg-info/SOURCES.txt'
    adding 'tostadas_pipo-0.1/tostadas_pipo.egg-info/top_level.txt'
    Creating tar archive
    Creating tar archive
    removing 'tostadas_pipo-0.1' (and everything under it)


De esta forma al terminar la ejecución del comando previo debe tener creado un
directorio llamado ``dist`` e incluyendo los tres paquetes en formatos de archivos
tarball comprimido en *gzip/bzip2* y archivo comprimido en *zip*.

::

    dist/
    ├── tostadas_pipo-0.1.tar.bz2
    ├── tostadas_pipo-0.1.tar.gz
    └── tostadas_pipo-0.1.zip

De esta forma ya creo el(los) paquete(s) en diversos formato de distribución
de código fuente para su proyecto.


.. _python_distro_crear_bdist:

Distribución binaria
~~~~~~~~~~~~~~~~~~~~

El módulo :ref:`setuptools <python_modulo_setuptools>` y
:ref:`distutils <python_modulo_distutils>` le permiten crear una distribución binaria
construida o built "binary" distribution (``bdist``) de su paquete en formato **egg**,
**wheel**, **rpm**, etc. A continuación se describen los mas usados:

.. figure:: ../_static/images/python_eggs.jpg
    :align: center
    :width: 50%

    Distribución binaria Egg.


Egg
````

Para crear una distribución ``bdist`` de su paquete en formato ``egg``, ejecute el
siguiente comando:

.. code-block:: console

    $ python ./setup.py bdist_egg
    running bdist_egg
    running egg_info
    writing tostadas_pipo.egg-info/PKG-INFO
    writing top-level names to tostadas_pipo.egg-info/top_level.txt
    writing dependency_links to tostadas_pipo.egg-info/dependency_links.txt
    writing entry points to tostadas_pipo.egg-info/entry_points.txt
    reading manifest file 'tostadas_pipo.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    warning: no previously-included files matching '*.pyc' found anywhere in distribution
    warning: no previously-included files matching '*.pyo' found anywhere in distribution
    warning: no previously-included files matching '*~' found anywhere in distribution
    no previously-included directories found matching 'build'
    no previously-included directories found matching 'dist'
    writing manifest file 'tostadas_pipo.egg-info/SOURCES.txt'
    installing library code to build/bdist.linux-x86_64/egg
    running install_lib
    running build_py
    creating build/bdist.linux-x86_64
    creating build/bdist.linux-x86_64/egg
    creating build/bdist.linux-x86_64/egg/tostadas_pipo
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/principal.py -> build/bdist.linux-x86_64/egg/tostadas_pipo
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/__init__.py -> build/bdist.linux-x86_64/egg/tostadas_pipo
    creating build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades/impuestos.py -> build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades/__init__.py -> build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades/calculos.py -> build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades
    byte-compiling build/bdist.linux-x86_64/egg/tostadas_pipo/principal.py to principal.pyc
    byte-compiling build/bdist.linux-x86_64/egg/tostadas_pipo/__init__.py to __init__.pyc
    byte-compiling build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades/impuestos.py to impuestos.pyc
    byte-compiling build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades/__init__.py to __init__.pyc
    byte-compiling build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades/calculos.py to calculos.pyc
    creating build/bdist.linux-x86_64/egg/EGG-INFO
    copying tostadas_pipo.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying tostadas_pipo.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying tostadas_pipo.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying tostadas_pipo.egg-info/entry_points.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying tostadas_pipo.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    zip_safe flag not set; analyzing archive contents...
    creating 'dist/tostadas_pipo-0.1-py3.7.egg' and adding 'build/bdist.linux-x86_64/egg' to it
    removing 'build/bdist.linux-x86_64/egg' (and everything under it)

De esta forma al terminar la ejecución del comando previo debe tener creado un
directorio llamado ``dist`` e incluyendo la distribución ``bdist`` en formato *egg*.

::

    dist/
    └── tostadas_pipo-0.1-py3.7.egg

De esta forma ya creo la distribución ``bdist`` del paquete en formato *egg* para
su proyecto.


Wheel
`````

Para crear una distribución ``bdist`` de su paquete en formato **wheel**, ejecute el
siguiente comando:

.. code-block:: console

    $ python ./setup.py bdist_wheel
    running bdist_wheel
    running build
    running build_py
    installing to build/bdist.linux-x86_64/wheel
    running install
    running install_lib
    creating build/bdist.linux-x86_64/wheel
    creating build/bdist.linux-x86_64/wheel/tostadas_pipo
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/principal.py -> build/bdist.linux-x86_64/wheel/tostadas_pipo
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/__init__.py -> build/bdist.linux-x86_64/wheel/tostadas_pipo
    creating build/bdist.linux-x86_64/wheel/tostadas_pipo/utilidades
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades/impuestos.py -> build/bdist.linux-x86_64/wheel/tostadas_pipo/utilidades
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades/__init__.py -> build/bdist.linux-x86_64/wheel/tostadas_pipo/utilidades
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades/calculos.py -> build/bdist.linux-x86_64/wheel/tostadas_pipo/utilidades
    running install_egg_info
    running egg_info
    writing tostadas_pipo.egg-info/PKG-INFO
    writing top-level names to tostadas_pipo.egg-info/top_level.txt
    writing dependency_links to tostadas_pipo.egg-info/dependency_links.txt
    writing entry points to tostadas_pipo.egg-info/entry_points.txt
    reading manifest file 'tostadas_pipo.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    warning: no previously-included files matching '*.pyc' found anywhere in distribution
    warning: no previously-included files matching '*.pyo' found anywhere in distribution
    warning: no previously-included files matching '*~' found anywhere in distribution
    no previously-included directories found matching 'build'
    no previously-included directories found matching 'dist'
    writing manifest file 'tostadas_pipo.egg-info/SOURCES.txt'
    Copying tostadas_pipo.egg-info to build/bdist.linux-x86_64/wheel/tostadas_pipo-0.1-py3.7.egg-info
    running install_scripts
    adding license file "LICENSE" (matched pattern "LICEN[CS]E*")
    creating build/bdist.linux-x86_64/wheel/tostadas_pipo-0.1.dist-info/WHEEL
    creating 'dist/tostadas_pipo-0.1-py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
    adding 'tostadas_pipo/__init__.py'
    adding 'tostadas_pipo/principal.py'
    adding 'tostadas_pipo/utilidades/__init__.py'
    adding 'tostadas_pipo/utilidades/calculos.py'
    adding 'tostadas_pipo/utilidades/impuestos.py'
    adding 'tostadas_pipo-0.1.dist-info/LICENSE'
    adding 'tostadas_pipo-0.1.dist-info/METADATA'
    adding 'tostadas_pipo-0.1.dist-info/WHEEL'
    adding 'tostadas_pipo-0.1.dist-info/entry_points.txt'
    adding 'tostadas_pipo-0.1.dist-info/top_level.txt'
    adding 'tostadas_pipo-0.1.dist-info/RECORD'
    removing build/bdist.linux-x86_64/wheel


De esta forma al terminar la ejecución del comando previo debe tener creado un
directorio llamado ``dist`` e incluyendo la distribución ``bdist`` en formato *whl*.

::

    dist/
    ├── tostadas_pipo-0.1-py3.7.egg
    └── tostadas_pipo-0.1-py3-none-any.whl

De esta forma ya creo la distribución ``bdist`` del paquete en formato *whl* para
su proyecto.


.. _python_distro_instalar:

Instalar paquete
................

Para instalar el paquete de su proyecto, hay dos formas de instalación disponibles
a continuación:


.. _python_distro_instalar_sdist:

Instalar distribución código fuente
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para instalar una distribución código fuente de su paquete previamente creado, se
realizar usando la herramienta ``pip``, ejecutando el siguiente comando:

.. code-block:: console

    pip install --user dist/tostadas_pipo-0.1.tar.gz

Si al ejecutar el comando anterior muestra el mensaje:

.. code-block:: console

    pip
    bash: pip: no se encontró la orden

Esto es debido a que no tiene instalado dicha herramienta, así que debe ejecutar
el siguiente comando:

.. code-block:: console

    sudo apt install -y python-pip

De nuevo vuelva a ejecutar en su consola de comando el comando:

.. code-block:: console

    pip install --user dist/tostadas_pipo-0.1.tar.gz
    Processing ./dist/tostadas_pipo-0.1.tar.gz
    Building wheels for collected packages: tostadas-pipo
      Running setup.py bdist_wheel for tostadas-pipo ... done
      Stored in directory: /home/leonardo/.cache/pip/wheels/fd/f9/75/a6965566a3c5a8bff507d7daa30760caca0a7525a3de61eac2
    Successfully built tostadas-pipo
    Installing collected packages: tostadas-pipo
    Successfully installed tostadas-pipo-0.1


De esta forma tiene instalado una distribución código fuente en formato **tarball**
de su paquete en el interprete Python usando la herramienta ``pip``.


.. _python_distro_instalar_bdist:

Instalar distribución binaria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para instalar una distribución binaria de su paquete previamente creado, se
realizar usando la herramienta ``pip``, ejecutando el siguiente comando:

.. code-block:: console

    $ pip install --user ./dist/tostadas_pipo-0.1-py3-none-any.whl
    Processing ./dist/tostadas_pipo-0.1-py3-none-any.whl
    Installing collected packages: tostadas-pipo
    Successfully installed tostadas-pipo-0.1

De esta forma tiene instalado una distribución binaria en formato **wheel** de su
paquete en el interprete Python usando la herramienta ``pip``.

----

.. note::
    `pip <https://pip.pypa.io/en/stable/>`_, es una herramienta para instalación y
    administración de paquetes Python.

----

.. _python_distro_install_source_pkg:

Instalar de código de proyecto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para instalar el paquete desde el código de proyecto, ejecute el siguiente comando:

.. code-block:: console

    $ python ./setup.py -v install --user
    running install
    running bdist_egg
    running egg_info
    writing tostadas_pipo.egg-info/PKG-INFO
    writing top-level names to tostadas_pipo.egg-info/top_level.txt
    writing dependency_links to tostadas_pipo.egg-info/dependency_links.txt
    reading manifest file 'tostadas_pipo.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    warning: no previously-included files matching '*.pyo' found anywhere in distribution
    warning: no previously-included files matching '*~' found anywhere in distribution
    no previously-included directories found matching 'build'
    no previously-included directories found matching 'dist'
    writing manifest file 'tostadas_pipo.egg-info/SOURCES.txt'
    installing library code to build/bdist.linux-x86_64/egg
    running install_lib
    running build_py
    not copying tostadas_pipo/principal.py (output up-to-date)
    not copying tostadas_pipo/__init__.py (output up-to-date)
    not copying tostadas_pipo/utilidades/impuestos.py (output up-to-date)
    not copying tostadas_pipo/utilidades/__init__.py (output up-to-date)
    not copying tostadas_pipo/utilidades/calculos.py (output up-to-date)
    not copying tostadas_pipo/utilidades/__init__.py (output up-to-date)
    not copying tostadas_pipo/utilidades/calculos.py (output up-to-date)
    not copying tostadas_pipo/utilidades/impuestos.py (output up-to-date)
    creating build/bdist.linux-x86_64
    creating build/bdist.linux-x86_64/egg
    creating build/bdist.linux-x86_64/egg/tostadas_pipo
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/principal.py -> build/bdist.linux-x86_64/egg/tostadas_pipo
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/__init__.py -> build/bdist.linux-x86_64/egg/tostadas_pipo
    creating build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades/impuestos.py -> build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades/__init__.py -> build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades
    copying build/lib.linux-x86_64-3.7/tostadas_pipo/utilidades/calculos.py -> build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades
    byte-compiling build/bdist.linux-x86_64/egg/tostadas_pipo/principal.py to principal.pyc
    byte-compiling build/bdist.linux-x86_64/egg/tostadas_pipo/__init__.py to __init__.pyc
    byte-compiling build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades/impuestos.py to impuestos.pyc
    byte-compiling build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades/__init__.py to __init__.pyc
    byte-compiling build/bdist.linux-x86_64/egg/tostadas_pipo/utilidades/calculos.py to calculos.pyc
    creating build/bdist.linux-x86_64/egg/EGG-INFO
    copying tostadas_pipo.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying tostadas_pipo.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying tostadas_pipo.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying tostadas_pipo.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    zip_safe flag not set; analyzing archive contents...
    creating dist
    creating 'dist/tostadas_pipo-0.1-py3.7.egg' and adding 'build/bdist.linux-x86_64/egg' to it
    adding 'tostadas_pipo/principal.py'
    adding 'tostadas_pipo/principal.pyc'
    adding 'tostadas_pipo/__init__.pyc'
    adding 'tostadas_pipo/__init__.py'
    adding 'tostadas_pipo/utilidades/impuestos.pyc'
    adding 'tostadas_pipo/utilidades/calculos.pyc'
    adding 'tostadas_pipo/utilidades/impuestos.py'
    adding 'tostadas_pipo/utilidades/__init__.pyc'
    adding 'tostadas_pipo/utilidades/__init__.py'
    adding 'tostadas_pipo/utilidades/calculos.py'
    adding 'EGG-INFO/zip-safe'
    adding 'EGG-INFO/dependency_links.txt'
    adding 'EGG-INFO/PKG-INFO'
    adding 'EGG-INFO/SOURCES.txt'
    adding 'EGG-INFO/top_level.txt'
    removing 'build/bdist.linux-x86_64/egg' (and everything under it)
    Processing tostadas_pipo-0.1-py3.7.egg
    Copying tostadas_pipo-0.1-py3.7.egg to /home/leonardo/.local/lib/python3.7/site-packages
    Adding tostadas-pipo 0.1 to easy-install.pth file
    Saving /home/leonardo/.local/lib/python3.7/site-packages/easy-install.pth

    Installed /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo-0.1-py3.7.egg
    Processing dependencies for tostadas-pipo==0.1
    Finished processing dependencies for tostadas-pipo==0.1


De esta forma tiene instalado su paquete en su interprete Python usando el comando ``install``
disponible con el script ``setup.py``.

----

.. warning::

    Al instalar el paquete usando el parámetro ``--user`` el paquete es instalado en el
    directorio ``$HOME/.local/lib/python3.7/site-packages/``.

----

.. _python_distro_check_install:

Comprobar la instalación
~~~~~~~~~~~~~~~~~~~~~~~~

Usted puede comprobar luego de realizar la instalación de la distribución de código fuente
o binaria de su paquete, ejecute el siguiente comando:

.. code-block:: console

    $ pip list --user --format=freeze | grep "tostadas"
    tostadas-pipo==0.1

De esta forma la herramienta de gestión de paquete indica que el ``tostadas-pipo`` en su
versión **0.1** esta instalado en su interprete Python.


.. _python_distro_usar_pkg:

Usar paquete
............

Usar el paquete ``tostadas_pipo-0.1``, recuerde que debe usarlo como una librería,
entonces puede probar el correcto funcionamiento del paquete, importando este,
ejecutando el siguiente comando:

.. code-block:: console

    $ python -c 'from tostadas_pipo.utilidades.impuestos import impuesto_iva; print("Función importada " + impuesto_iva.__doc__[1:36] + ".")'
    Función importada Calcula el impuesto del IVA de 14%.

El comando previo muestra la :ref:`docstring <python_str_docstrings>` de la
función importada ``impuesto_iva`` sino muestra ningún mensaje de error, el
paquete ``tostadas_pipo-0.1`` se instalo correctamente.


.. _python_distro_eliminar_pkg:

Eliminar paquete
................

Para eliminar paquete usando la herramienta ``pip``, ejecute el siguiente comando:

.. code-block:: console

    $ pip uninstall tostadas_pipo
    Uninstalling tostadas-pipo-0.1:
      /home/leonardo/.local/bin/tostadas_pipo
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo-0.1.dist-info/DESCRIPTION.rst
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo-0.1.dist-info/INSTALLER
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo-0.1.dist-info/METADATA
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo-0.1.dist-info/RECORD
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo-0.1.dist-info/WHEEL
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo-0.1.dist-info/metadata.json
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo-0.1.dist-info/top_level.txt
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo/__init__.py
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo/__init__.pyc
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo/principal.py
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo/principal.pyc
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo/utilidades/__init__.py
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo/utilidades/__init__.pyc
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo/utilidades/calculos.py
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo/utilidades/calculos.pyc
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo/utilidades/impuestos.py
      /home/leonardo/.local/lib/python3.7/site-packages/tostadas_pipo/utilidades/impuestos.pyc
    Proceed (y/n)? y
      Successfully uninstalled tostadas-pipo-0.1


``pip`` esta habilitado a desinstalar la mayoría de paquetes instalados. Las excepciones
conocidas son:

- Los paquetes basado en solamente en el módulo :ref:`distutils <python_modulo_distutils>` los
  cuales fueron instalados sin la herramienta ``pip`` usando el comando ``python setup.py install``
  desde el :ref:`código del paquete <python_distro_install_source_pkg>`.

  Instalándolo de esta forma, al momento de desintalarlo usando el comando ``pip uninstall tostadas_pipo``
  este comando removerá solo la metadata, no detrás dejando de la instalación metadata para
  determinar que archivos fueron instalados.

  Entonces para solventar este problema tiene que ir manualmente al directorio ``site-packages`` a
  eliminar manualmente el paquete que instalo.

  .. warning::

      Esta entrando a la cueva de los Dragones!!!

- Los scripts wrappers instalados ejecutando el comando ``python setup.py develop``.

De esta forma ya tiene eliminado su paquete de forma manual de su sistema.


Ayuda integrada
...............

Usted puede consultar toda la ayuda comandos disponibles del módulo
:ref:`setuptools <python_modulo_setuptools>` y :ref:`distutils <python_modulo_distutils>`,
ejecute el comando siguiente:

.. code-block:: console

    $ python ./setup.py --help-commands
    Standard commands:
      build             build everything needed to install
      build_py          "build" pure Python modules (copy to build directory)
      build_ext         build C/C++ extensions (compile/link to build directory)
      build_clib        build C/C++ libraries used by Python extensions
      build_scripts     "build" scripts (copy and fixup #! line)
      clean             clean up temporary files from 'build' command
      install           install everything from build directory
      install_lib       install all Python modules (extensions and pure Python)
      install_headers   install C/C++ header files
      install_scripts   install scripts (Python or otherwise)
      install_data      install data files
      sdist             create a source distribution (tarball, zip file, etc.)
      register          register the distribution with the Python package index
      bdist             create a built (binary) distribution
      bdist_dumb        create a "dumb" built distribution
      bdist_rpm         create an RPM distribution
      bdist_wininst     create an executable installer for MS Windows
      upload            upload binary package to PyPI
      check             perform some checks on the package

    Extra commands:
      saveopts          save supplied options to setup.cfg or other config file
      testr             Run unit tests using testr
      compile_catalog   compile message catalogs to binary MO files
      develop           install package in 'development mode'
      upload_docs       Upload documentation to PyPI
      extract_messages  extract localizable strings from the project code
      init_catalog      create a new catalog based on a POT file
      test              run unit tests after in-place build
      update_catalog    update message catalogs from a POT file
      setopt            set an option in setup.cfg or another config file
      install_egg_info  Install an .egg-info directory for the package
      rotate            delete older distributions, keeping N newest files
      bdist_wheel       create a wheel distribution
      egg_info          create a distribution's .egg-info directory
      alias             define a shortcut to invoke one or more commands
      easy_install      Find/get/install Python packages
      bdist_egg         create an "egg" distribution

    usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
       or: setup.py --help [cmd1 cmd2 ...]
       or: setup.py --help-commands
       or: setup.py cmd --help

Para consultar toda la ayuda del módulo :ref:`setuptools <python_modulo_setuptools>`
y :ref:`distutils <python_modulo_distutils>`, ejecute el comando siguiente:

.. code-block:: console

    $ python setup.py --help

----


.. important::
    Usted puede descargar el código usado en esta sección, haciendo clic en el
    siguiente enlace: :download:`distribucion.zip <../../recursos/leccion8/distribucion.zip>`.


.. tip::
    Para poder definir un instalador y construirlo para así poder hacer que su proyecto
    se pueda distribuir de forma más fácil debe crear la
    :ref:`estructura de proyecto <python_estructura_proyecto>` usando el código descomprimido
    del archivo :file:`distribucion.zip`, siga los pasos para construir los archivos,
    crear el instalador y probar su instalación.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion8>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
