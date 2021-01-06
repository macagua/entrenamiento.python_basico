.. -*- coding: utf-8 -*-


.. _python_interactivo:

Inmersión al modo interactivo
-----------------------------

La *inmersión al modo interactivo* le permite a cualquier usuario el cual **NUNCA** 
ha trabajando con el interprete de `Python`_ pueda tener un primer acercamiento 
**SIN PROGRAMAR**, solamente con conocer el uso del interprete y sus comandos básicos 
usando la técnica de introspección.

.. _python_introspeccion:

Introspección en Python
.......................

En Python como usted lo ira entendiendo **todo en Python es un objeto**, y la 
técnica de introspección, no es más que código el cual examina como objetos 
otros módulos y funciones en memoria, obtiene información sobre ellos y los 
que los maneja.

De paso, usted podrá definir las funciones sin nombre, las llamará a
funciones con argumentos sin orden, y podrá hacer referencia a funciones
cuyos nombres desconocemos.


Python a través de su interprete
................................

Es importante conocer Python a través de su interprete debido a varios
factores:

- Conocer las clases, sus funciones y atributos propios, a través de la
  introspección del lenguaje.

- Disponibilidad de consultar la documentación del lenguaje desde el
  interprete, por mucho tiempo no estaba disponible documentación tipo 
  `Javadoc`_ o `diagramas de clases`_ del propio lenguaje por lo cual
  muchas programadores **Python** se acostumbraron a estudiar su código de
  esta forma, así que le recomiendo que use el interprete ``python`` para
  eso.

- Hoy en día existente herramientas que te permiten generar
  documentación desde los códigos fuentes Python como `Sphinx`_.

La forma mas fácil es iniciar tu relación con Python simplemente ejecutando
el comando ``python`` de la siguiente forma: 

.. code-block:: python

    python
    Python 2.7.13 (default, Sep 26 2018, 18:42:22)
    [GCC 6.3.0 20170516] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>


Puede solicitar la ayudar del interprete de Python, ejecutando:

.. code-block:: python

    >>> help
    Type help() for interactive help, or help(object) for help about object.
    >>> help()

    Welcome to Python 2.7!  This is the online help utility.

    If this is your first time using Python, you should definitely check out
    the tutorial on the Internet at https://docs.python.org/2.7/tutorial/.

    Enter the name of any module, keyword, or topic to get help on writing
    Python programs and using Python modules.  To quit this help utility and
    return to the interpreter, just type "quit".

    To get a list of available modules, keywords, or topics, type "modules",
    "keywords", or "topics".  Each module also comes with a one-line summary
    of what it does; to list the modules whose summaries contain a given word
    such as "spam", type "modules spam".


Para ejecutar la ayuda disponible sobre la sintaxis Python ejecute el
siguiente comando:

.. code-block:: python

    help> modules

    Please wait a moment while I gather a list of all available modules...

    BaseHTTPServer      asynchat            imputil             sha
    Bastion             asyncore            inspect             shelve
    CDROM               atexit              io                  shlex
    CGIHTTPServer       audiodev            ipython_genutils    shutil
    Canvas              audioop             itertools           shutil_backports
    ConfigParser        autoreload          jinja2              signal
    Cookie              babel               json                simplegeneric
    DLFCN               backports           keyword             site
    Dialog              base64              lib2to3             sitecustomize
    DocXMLRPCServer     bdb                 linecache           six
    FileDialog          binascii            linuxaudiodev       smtpd
    FixTk               binhex              locale              smtplib
    HTMLParser          bisect              logging             sndhdr
    IN                  bsddb               macpath             snowballstemmer
    IPython             bz2                 macurl2path         socket
    MimeWriter          cPickle             mailbox             sphinx
    Queue               cProfile            mailcap             sphinx_rtd_theme
    ScrolledText        cStringIO           markupbase          spwd
    SimpleDialog        calendar            markupsafe          sqlite3
    SimpleHTTPServer    cgi                 marshal             sre
    SimpleXMLRPCServer  cgitb               math                sre_compile
    SocketServer        chunk               md5                 sre_constants
    StringIO            cmath               mhlib               sre_parse
    TYPES               cmd                 mimetools           ssl
    Tix                 code                mimetypes           stat
    Tkconstants         codecs              mimify              statvfs
    Tkdnd               codeop              mmap                storemagic
    Tkinter             collections         modulefinder        string
    UserDict            colorsys            multifile           stringold
    UserList            commands            multiprocessing     stringprep
    UserString          compileall          mutex               strop
    _LWPCookieJar       compiler            netrc               struct
    _MozillaCookieJar   contextlib          new                 subprocess
    __builtin__         cookielib           nis                 sunau
    __future__          copy                nntplib             sunaudio
    _abcoll             copy_reg            ntpath              symbol
    _ast                crypt               nturl2path          sympyprinting
    _bisect             csv                 numbers             symtable
    _bsddb              ctypes              opcode              sys
    _codecs             curses              operator            sysconfig
    _codecs_cn          cythonmagic         optparse            syslog
    _codecs_hk          datetime            os                  tabnanny
    _codecs_iso2022     dbhash              os2emxpath          tarfile
    _codecs_jp          dbm                 ossaudiodev         telnetlib
    _codecs_kr          decimal             parser              tempfile
    _codecs_tw          decorator           pathlib2            termios
    _collections        difflib             pdb                 test
    _csv                dircache            pexpect             tests
    _ctypes             dis                 pickle              textwrap
    _ctypes_test        distutils           pickleshare         this
    _curses             doctest             pickletools         thread
    _curses_panel       docutils            pip                 threading
    _elementtree        dumbdbm             pipes               time
    _functools          dummy_thread        pkg_resources       timeit
    _hashlib            dummy_threading     pkgutil             tkColorChooser
    _heapq              easy_install        platform            tkCommonDialog
    _hotshot            email               plistlib            tkFileDialog
    _io                 encodings           popen2              tkFont
    _json               ensurepip           poplib              tkMessageBox
    _locale             enum                posix               tkSimpleDialog
    _lsprof             errno               posixfile           toaiff
    _md5                exceptions          posixpath           token
    _multibytecodec     fcntl               pprint              tokenize
    _multiprocessing    filecmp             profile             trace
    _osx_support        fileinput           prompt_toolkit      traceback
    _pyio               fnmatch             pstats              traitlets
    _random             formatter           pty                 ttk
    _scandir            fpectl              ptyprocess          tty
    _sha                fpformat            pwd                 turtle
    _sha256             fractions           py_compile          types
    _sha512             ftplib              pyclbr              unicodedata
    _socket             functools           pydoc               unittest
    _sqlite3            future_builtins     pydoc_data          urllib
    _sre                gc                  pyexpat             urllib2
    _ssl                gdbm                pygments            urlparse
    _strptime           genericpath         pytz                user
    _struct             getopt              quopri              uu
    _symtable           getpass             random              uuid
    _sysconfigdata      gettext             re                  warnings
    _sysconfigdata_nd   glob                readline            wave
    _testcapi           grp                 repr                wcwidth
    _threading_local    gzip                resource            weakref
    _tkinter            hashlib             rexec               webbrowser
    _warnings           heapq               rfc822              wheel
    _weakref            hmac                rlcompleter         whichdb
    _weakrefset         hotshot             rmagic              wsgiref
    abc                 htmlentitydefs      robotparser         xdrlib
    aifc                htmllib             runpy               xml
    alabaster           httplib             scandir             xmllib
    antigravity         ihooks              sched               xmlrpclib
    anydbm              imaplib             select              xxsubtype
    argparse            imghdr              sets                zipfile
    array               imp                 setuptools          zipimport
    ast                 importlib           sgmllib             zlib

    Enter any module name to get more help.  Or, type "modules spam" to search
    for modules whose descriptions contain the word "spam".

Entonces consulte la ayuda del módulo ``os``, ejecutando:

::

    help> os
    Help on module os:

    NAME
        os - OS routines for NT or Posix depending on what system we're on.

    FILE
        /usr/lib/python2.7/os.py

    MODULE DOCS
        https://docs.python.org/library/os

    DESCRIPTION
        This exports:
          - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
          - os.path is one of the modules posixpath, or ntpath
          - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
          - os.curdir is a string representing the current directory ('.' or ':')
          - os.pardir is a string representing the parent directory ('..' or '::')
          - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
          - os.extsep is the extension separator ('.' or '/')
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

.. tip:: Presione la tecla ``q`` para salir de la ayuda del módulo ``os``.

Seguidamente presione la combinación de tecla **Crtl+d** para salir de la ayuda.

Luego realice la importación de la `librería del estándar`_ Python llamada
``os``, con el siguiente comando:

.. code-block:: python

    >>> import os
    >>>


Previamente importada la librería usted puede usar la función ``dir()`` para
listar o descubrir que atributos, métodos de la clase están disponibles con
la importación

.. code-block:: python

    >>> dir(os)
    ['EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST',
    'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE',
    'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE',
    'EX_USAGE', 'F_OK', 'NGROUPS_MAX', 'O_APPEND', 'O_CREAT', 'O_DIRECT',
    'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_LARGEFILE', 'O_NDELAY',
    'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_RDONLY', 'O_RDWR', 'O_RSYNC',
    'O_SYNC', 'O_TRUNC', 'O_WRONLY', 'P_NOWAIT', 'P_NOWAITO', 'P_WAIT',
    'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'UserDict',
    'WCONTINUED', 'WCOREDUMP', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED',
    'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WSTOPSIG', 'WTERMSIG',
    'WUNTRACED', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__',
    '__doc__', '__file__', '__name__', '_copy_reg', '_execvpe', '_exists',
    '_exit', '_get_exports_list', '_make_stat_result',
    '_make_statvfs_result', '_pickle_stat_result', '_pickle_statvfs_result',
    '_spawnvef', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'chown',
    'chroot', 'close', 'confstr', 'confstr_names', 'ctermid', 'curdir',
    'defpath', 'devnull', 'dup', 'dup2', 'environ', 'errno', 'error',
    'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp',
    'execvpe', 'extsep', 'fchdir', 'fdatasync', 'fdopen', 'fork', 'forkpty',
    'fpathconf', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'getcwd',
    'getcwdu', 'getegid', 'getenv', 'geteuid', 'getgid', 'getgroups',
    'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid',
    'getsid', 'getuid', 'isatty', 'kill', 'killpg', 'lchown', 'linesep',
    'link', 'listdir', 'lseek', 'lstat', 'major', 'makedev', 'makedirs',
    'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty',
    'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pipe',
    'popen', 'popen2', 'popen3', 'popen4', 'putenv', 'read', 'readlink',
    'remove', 'removedirs', 'rename', 'renames', 'rmdir', 'sep', 'setegid',
    'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp', 'setregid',
    'setreuid', 'setsid', 'setuid', 'spawnl', 'spawnle', 'spawnlp',
    'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'stat',
    'stat_float_times', 'stat_result', 'statvfs', 'statvfs_result',
    'strerror', 'symlink', 'sys', 'sysconf', 'sysconf_names', 'system',
    'tcgetpgrp', 'tcsetpgrp', 'tempnam', 'times', 'tmpfile', 'tmpnam',
    'ttyname', 'umask', 'uname', 'unlink', 'unsetenv', 'urandom', 'utime',
    'wait', 'wait3', 'wait4', 'waitpid', 'walk', 'write']
    >>>


Otro ejemplo de uso, es poder usar el método ``file`` para determinar la
ubicación de la librería importada de la siguiente forma:

.. code-block:: python

    >>> os.__file__
    '/usr/lib/python2.7/os.pyc'
    >>>

También puede consultar la documentación de la librería ``os`` ejecutando el
siguiente comando:

.. code-block:: python

    >>> print os.__doc__
    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
      - os.path is one of the modules posixpath, or ntpath
      - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
      - os.curdir is a string representing the current directory ('.' or ':')
      - os.pardir is a string representing the parent directory ('..' or '::')
      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
      - os.extsep is the extension separator ('.' or '/')
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
    >>>


Ejecute el comando exit() para salir del interprete...

.. code-block:: python

    >>> exit()


.. _python_interprete_interactivo:

Interprete ipython
..................

Para mejorar la experiencia con el interprete Python le sugerimos instalar el
paquete ``ipython``, según su documentación:

Según Wikipedia

  "``ipython`` es un shell interactivo que añade funcionalidades extra al `modo
  interactivo`_ incluido con Python, como resaltado de líneas y errores
  mediante colores, una sintaxis adicional para el shell, completado automático
  mediante tabulador de variables, módulos y atributos; entre otras
  funcionalidades. Es un componente del paquete `SciPy`_."

Para mayor información visite su página principal de `ipython`_ y si necesita instalar
este programa ejecute el siguiente comando:

.. code-block:: sh

    sudo apt-get install ipython


Luego cierra sesión de **root** y vuelve al usuario y sustituya el comando
``python`` por ``ipython`` de la siguiente forma:

.. code-block:: sh

    ipython
    Python 2.7.13 (default, Sep 26 2018, 18:42:22) 
    Type "copyright", "credits" or "license" for more information.

    IPython 5.8.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

        In [1]:


Un ejemplo de uso del comando ``help`` es consultar la ayuda del comando
``dir`` y se ejecuta de la siguiente forma:

.. code-block:: python

    In [1]: help(dir)
    Help on built-in function dir in module __builtin__:

    dir(...)
        dir([object]) -> list of strings

        Return an alphabetized list of names comprising (some of) the
        attributes of the given object, and of attributes reachable 
        from it:

        No argument:  the names in the current scope.
        Module object:  the module attributes.
        Type or class object:  its attributes, and recursively the
        attributes of its bases.
        Otherwise:  its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.


Entonces presione la tecla **q** para salir de la ayuda de la función ``dir()``.

De nuevo realice la importación de la librería del estándar Python llamada
``os``.

.. code-block:: python

    In [2]: import os


También consultar los detalles acerca del 'objeto' para esto use como ejemplo
la librería ``os`` ejecutando el siguiente comando:

.. code-block:: ipython

    In [2]: os?
    Type:        module
    String form: <module 'os' from '/usr/lib/python2.7/os.pyc'>
    File:        /usr/lib/python2.7/os.py
    Docstring:
    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
      - os.path is one of the modules posixpath, or ntpath
      - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
      - os.curdir is a string representing the current directory ('.' or ':')
      - os.pardir is a string representing the parent directory ('..' or '::')
      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
      - os.extsep is the extension separator ('.' or '/')
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

.. code-block:: python

    In [3]: os.__
    os.__all__      os.__file__
    os.__builtins__ os.__name__
    os.__doc__      os.__package__


De nuevo ejecute el método ``file`` para determinar la ubicación de la
librería importada

.. code-block:: python

    In [4]: os.__file__
    Out[4]: '/usr/lib/python2.7/os.pyc'


También puede consultar la documentación de la librería ``os`` de la
siguiente forma:

.. code-block:: ipython

    In [5]: print os.__doc__
    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
      - os.path is one of the modules posixpath, or ntpath
      - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
      - os.curdir is a string representing the current directory ('.' or ':')
      - os.pardir is a string representing the parent directory ('..' or '::')
      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
      - os.extsep is the extension separator ('.' or '/')
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

.. code-block:: python

    In [6]: os.__name__
    Out[6]: 'os'


Y otra forma de consultar la documentación de la librería ``os`` es
ejecutando el siguiente comando:

.. code-block:: ipython

    In [7]: help(os)
    Help on module os:

    NAME
        os - OS routines for NT or Posix depending on what system we're on.

    FILE
        /usr/lib/python2.7/os.py

    MODULE DOCS
        https://docs.python.org/library/os

    DESCRIPTION
        This exports:
          - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
          - os.path is one of the modules posixpath, or ntpath
          - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
          - os.curdir is a string representing the current directory ('.' or ':')
          - os.pardir is a string representing the parent directory ('..' or '::')
          - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
          - os.extsep is the extension separator ('.' or '/')
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

Entonces presione la tecla ``q`` para salir de la ayuda del módulo ``os``.

Y para cerrar la sesión con el ``ipython`` ejecute el siguiente comando:

.. code-block:: ipython

    In [8]: exit()
    Do you really want to exit ([y]/n)? y


Interprete bpython
..................

Alternativamente puedes usar el paquete `bpython` que mejora aun mas la experiencia 
de trabajo con el paquete `ipython`.

Para mayor información visite su página principal de `interprete bpython`_ y si necesita instalar
este programa ejecute el siguiente comando:

.. code-block:: sh

    sudo apt-get install python-pip
    sudo pip install bpython

Luego cierra sesión de **root** y vuelve al usuario y sustituya el comando
``python`` por ``ipython`` de la siguiente forma:

.. code-block:: sh

    bpython
    

Dentro de interprete Python puede apreciar que ofrece otra forma de presentar 
la documentación y la estructura del lenguaje, con los siguientes comandos de ejemplos:

.. code-block:: python

    >>> print 'Hola Mundo'
    Hola Mundo
    >>> for item in xrange(
    +───────────────────────────────────────────────────────────────────────+
    │ xrange: ([start, ] stop[, step])                                      │
    │ xrange([start,] stop[, step]) -> xrange object                        │
    │                                                                       │
    │ Like range(), but instead of returning a list, returns an object that │
    │ generates the numbers in the range on demand.  For looping, this is   │
    │ slightly faster than range() and more memory efficient.               │
    +───────────────────────────────────────────────────────────────────────+

     <C-r> Rewind  <C-s> Save  <F8> Pastebin  <F9> Pager  <F2> Show Source


Conclusiones
............

Como puede apreciar este tutorial no le enseña a programar sino a simplemente
aprender a conocer como manejarse en shell de Python y en el modo interactivo 
usando el paquete ``ipython`` y otros adicionales como ``bpython``, con el fin 
de conocer a través de la introspección del lenguaje, las librerías estándar y 
módulos propios escritos en Python que tienes instalado en tu sistema.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion2>` 
    del entrenamiento para ampliar su conocimiento en esta temática.


.. _`Python`: https://www.python.org/ 
.. _`Javadoc`: https://es.wikipedia.org/wiki/Javadoc
.. _`diagramas de clases`: https://es.wikipedia.org/wiki/Diagrama_de_clases
.. _`Sphinx`: https://en.wikipedia.org/wiki/Sphinx_%28documentation_generator%29
.. _`librería del estándar`: https://docs.python.org/2/library/index.html
.. _`modo interactivo`: https://es.wikipedia.org/wiki/Python#Modo_interactivo
.. _`SciPy`: https://en.wikipedia.org/wiki/SciPy
.. _`ipython`: https://ipython.readthedocs.io/
.. _`bpython`: https://pypi.org/project/bpython/
.. _`interprete bpython`: https://bpython-interpreter.org/
.. _`estilo de completación de lineas de comandos`: https://en.wikipedia.org/wiki/Command_line_completion
