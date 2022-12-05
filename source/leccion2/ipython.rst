.. -*- coding: utf-8 -*-


.. _python_modulo_ipython:

Interprete ipython
------------------

Para mejorar la experiencia con el interprete Python le sugerimos instalar el
paquete ``ipython``, según su documentación:

Según Wikipedia

  "``ipython`` es un shell interactivo que añade funcionalidades extra al `modo
  interactivo`_ incluido con Python, como resaltado de líneas y errores
  mediante colores, una sintaxis adicional para el shell, completado automático
  mediante tabulador de variables, módulos y atributos; entre otras
  funcionalidades. Es un componente del paquete `SciPy`_."

Para mayor información visite su página principal de `ipython`_ y si necesita instalar
este programa ejecute el siguiente comando, el cual a continuación se presentan
el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ pip install ipython

   .. group-tab:: Windows

      .. code-block:: console

          > pip install ipython


Sustituya el comando ``python`` por ``ipython`` correspondiente a tu sistema
operativo de la siguiente forma:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          $ ipython
          Python 3.7.3 (default, Oct 31 2022, 14:04:00)
          Type 'copyright', 'credits' or 'license' for more information
          IPython 7.34.0 -- An enhanced Interactive Python. Type '?' for help.

              In [1]:

   .. group-tab:: Windows

      .. code-block:: console

          > ipython
          Python 3.7.3 (default, Oct 31 2022, 14:04:00)
          Type 'copyright', 'credits' or 'license' for more information
          IPython 7.34.0 -- An enhanced Interactive Python. Type '?' for help.

              In [1]:

Un ejemplo de uso del comando ``help`` es consultar la ayuda del comando
``dir`` y se ejecuta de la siguiente forma:

.. code-block:: pycon

    In [1]: help(dir)
    Help on built-in function dir in module __builtin__:

    dir(...)
        dir([object]) -> list of strings

        If called without an argument, return the names in the current scope.
        Else, return an alphabetized list of names comprising (some of) the attributes
        of the given object, and of attributes reachable from it.
        If the object supplies a method named __dir__, it will be used; otherwise
        the default dir() logic is used and returns:
        for a module object: the module's attributes.
        for a class object:  its attributes, and recursively the attributes
        of its bases.
        for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.


Entonces presione la tecla **q** para salir de la ayuda de la función ``dir()``.

De nuevo realice la importación de la librería del estándar Python llamada
``os``.

.. code-block:: pycon

    In [2]: import os


También consultar los detalles acerca del 'objeto' para esto use como ejemplo
la librería ``os`` ejecutando el siguiente comando:

.. code-block:: pycon

    In [2]: os?
    Type:        module
    String form: <module 'os' from '/usr/lib/python3.7/os.py'>
    File:        /usr/lib/python3.7/os.py
    Docstring:
    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)

    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).


Escriba la librería *os.* y luego escribe dos **underscore** y presione *dos
veces la tecla tabular* para usar la completado automático del interprete al
`estilo de completación de lineas de comandos`_ en el shell UNIX/Linux para
ayudar a la introspección del lenguaje y sus librerías.

.. code-block:: pycon

    In [3]: os.__
    __all__      __doc__      __name__
    __builtins__ __file__     __package__
    __cached__   __loader__   __spec__
    <unknown>


De nuevo ejecute el método ``file`` para determinar la ubicación de la
librería importada

.. code-block:: pycon

    In [4]: os.__file__
    Out[4]: '/usr/lib/python3.7/os.py'


También puede consultar la documentación de la librería ``os`` de la
siguiente forma:

.. code-block:: pycon

    In [5]: print(os.__doc__)
    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)

    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).


Otro ejemplo es imprimir el **nombre de la clase** con el siguiente comando:

.. code-block:: pycon

    In[6]: os.__name__
    Out[6]: "os"


Y otra forma de consultar la documentación de la librería ``os`` es
ejecutando el siguiente comando:

.. code-block:: pycon

    In [7]: help(os)
    Help on module os:

    NAME
        os - OS routines for NT or Posix depending on what system we're on.

    MODULE REFERENCE
        https://docs.python.org/3.7/library/os

        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.

    DESCRIPTION
        This exports:
          - all functions from posix or nt, e.g. unlink, stat, etc.
          - os.path is either posixpath or ntpath
          - os.name is either 'posix' or 'nt'
          - os.curdir is a string representing the current directory (always '.')
          - os.pardir is a string representing the parent directory (always '..')
          - os.sep is the (or a most common) pathname separator ('/' or '\\')
          - os.extsep is the extension separator (always '.')
          - os.altsep is the alternate pathname separator (None or '/')
          - os.pathsep is the component separator used in $PATH etc
          - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
          - os.defpath is the default search path for executables
          - os.devnull is the file path of the null device ('/dev/null', etc.)

        Programs that import and use 'os' stand a better chance of being
        portable between different platforms.  Of course, they must then
        only use functions that are defined by all platforms (e.g., unlink
        and opendir), and leave all pathname manipulation to os.path
        (e.g., split and join).
    :

Entonces presione la tecla :keys:`q` para salir de la ayuda del módulo ``os``.

Y para cerrar la sesión con el ``ipython`` ejecute el siguiente comando:

.. code-block:: pycon

    In [8]: exit()
    Do you really want to exit ([y]/n)? y

Como puede apreciar este tutorial no le enseña a programar sino a simplemente
aprender a conocer como manejarse en el modo interactivo usando el paquete
``ipython``, con el fin de conocer a través de la introspección del lenguaje,
las librerías estándar y módulos propios escritos en Python que tienes instalado
en tu sistema.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. _`modo interactivo`: https://es.wikipedia.org/wiki/Python#Modo_interactivo
.. _`SciPy`: https://en.wikipedia.org/wiki/SciPy
.. _`ipython`: https://ipython.readthedocs.io/en/stable/
.. _`estilo de completación de lineas de comandos`: https://en.wikipedia.org/wiki/Command_line_completion
