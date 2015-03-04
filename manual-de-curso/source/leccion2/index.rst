.. -*- coding: utf-8 -*-

.. _python_interactivo:

Inmersión al modo interactivo de Python
=======================================

.. sidebar:: Sobre este artículo

    :Autor(es): Leonardo J. Caballero G.
    :Correo(s): leonardocaballero@gmail.com
    :Compatible con: Python 2.4 o versiones superiores
    :Fecha: 31 de Diciembre de 2013

Descripción general
-------------------

Este articulo se basa en el documento `Una pequeña inmersión al modo interactivo de Python`_ 
generado por la `fundación Cenditel`_ y la idea principal de este tutorial es para alguien que 
**NUNCA** ha trabajando con el interprete de `Python`_ pueda tener un primer acercamiento 
**SIN PROGRAMAR**, solamente con conocer el uso del interprete y sus comandos básicos.

.. _python_caracteristicas:

Características de Python
-------------------------

-   Es un lenguaje de programación `multiparadigma`_.

-   Soporta `orientación a objetos`_, `programación imperativa`_ y, en
    menor medida, `programación funcional`_.

-   Es un `lenguaje interpretado`_, usa `tipado dinámico`_, es 
    `fuertemente tipado`_ y es `multiplataforma`_.

.. _python_introspeccion:

Introspección en Python
-----------------------

Según el libro Inmersión en Python ...Como usted sabe, `todo en Python es un objeto`_, 
y la introspección es código que examina como objetos otros
módulos y funciones en memoria, obtiene información sobre ellos y los maneja.

De paso, usted podrá definir las funciones sin nombre, las llamará a
funciones con argumentos sin orden, y podrá hacer referencia a funciones
cuyos nombres desconocemos.


Python a través de su interprete
................................

Es importante conocer Python a través de su interprete debido a varios
factores:

-   Conocer las clases, sus funciones y atributos propios, a través de la
    introspección del lenguaje.

-   Disponibilidad de consultar la documentación del lenguaje desde el
    interprete, por mucho tiempo no estaba disponible documentación tipo 
    `Javadoc`_ o `diagramas de clases`_ del propio lenguaje por lo cual
    muchas programadores **Python** se acostumbraron a estudiar su código de
    esta forma, así que le recomiendo que use el interprete ``python`` para
    eso.

-   Hoy en día existente herramientas que te permiten generar
    documentación desde los códigos fuentes Python como `Sphinx`_.

La forma mas fácil es iniciar tu relación con Python simplemente ejecutando
el comando ``python`` de la siguiente forma: 

.. code-block:: python

    $ python
    Python 2.5.2 (r252:60911, Jan  4 2009, 17:40:26)
    [GCC 4.3.2] on linux2
    Type "help", "copyright", "credits" or "license" for more
    information.
    >>>


Pidiendo la ayudar del interprete de Python

.. code-block:: python

    >>> help
    Type help() for interactive help, or help(object) for help about object.
    >>> help()

    Welcome to Python 2.5!  This is the online help utility.

    If this is your first time using Python, you should definitely check
    out the tutorial on the Internet at http://www.python.org/doc/tut/.

    Enter the name of any module, keyword, or topic to get help on
    writing Python programs and using Python modules. To quit this help 
    utility and return to the interpreter, just type "quit".

    To get a list of available modules, keywords, or topics, type
    "modules", "keywords", or "topics".  Each module also comes with 
    a one-line summary of what it does; to list the modules whose 
    summaries contain a given word such as "spam", type "modules spam".
    help>


Para ejecutar la ayuda disponible sobre la sintaxis Python ejecute el
siguiente comando:

.. code-block:: python

    help> modules

      Please wait a moment while I gather a list of all available
      modules...

      /usr/lib/python2.5/site-packages/apt/__init__.py:18: FutureWarning:
      apt API not stable yet
        warnings.warn("apt API not stable yet", FutureWarning)
      Data Dir: /usr/share/colorblind
      Data Dir: /usr/share/gnome-applets/invest-applet
      Alacarte            _ctypes             gksu                platform
      AppInstall          _ctypes_test        gksu2               plistlib
      ArgImagePlugin      _curses             glchess             popen2
      ArrayPrinter        _curses_panel       glob                poplib
      BaseHTTPServer      _dbus_bindings      gmenu               posix
      Bastion             _dbus_glib_bindings gnome               posixfile
      BdfFontFile         _elementtree        gnome_sudoku        posixpath
      BeautifulSoup       _functools          gnomeapplet         pprint
      BeautifulSoupTests  _hashlib            gnomecanvas         profile
      BmpImagePlugin      _heapq              gnomedesktop
      pspersistence
      BufrStubImagePlugin _hotshot            gnomekeyring        pstats
      CDROM               _imaging            gnomeprint          pty
      CGIHTTPServer       _imagingft          gnomevfs            pwd
      Canvas              _imagingmath        gobject             pxssh
      ConfigParser        _ldap               gopherlib
      py_compile
      ContainerIO         _locale             grp                 pyatspi
      Cookie              _lsprof             gst                 pyclbr
      Crypto              _multibytecodec     gtk                 pydoc
      CurImagePlugin      _mysql              gtkhtml2            pyexpat
      DLFCN               _mysql_exceptions   gtkmozembed         pygst
      DcxImagePlugin      _numpy              gtksourceview       pygtk
      Dialog              _random             gtksourceview2      pynotify
      DocXMLRPCServer     _socket             gtkspell
      pythonloader
      EpsImagePlugin      _sqlite3            gtkunixprint
      pythonscript
      ExifTags            _sre                gtop                pyuno
      FileDialog          _ssl                gzip                quopri
      FitsStubImagePlugin _strptime           hashlib             random
      FixTk               _struct             heapq               re
      FliImagePlugin      _symtable           hitcount            readline
      FontFile            _testcapi           hmac                repr
      FpxImagePlugin      _threading_local    hotshot             resource
      Ft                  _types              hpmudext            rexec
      GMenuSimpleEditor   _weakref            htmlentitydefs      rfc822
      GbrImagePlugin      aifc                htmllib
      rlcompleter
      GdImageFile         anydbm              httplib
      robotparser
      GifImagePlugin      apt                 ibrowse             rsvg
      GimpGradientFile    apt_inst            idlelib             runpy
      GimpPaletteFile     apt_pkg             igrid               scanext
      GribStubImagePlugin aptsources          ihooks              sched
      HTMLParser          argparse            imaplib             select
      Hdf5StubImagePlugin array               imghdr
      serpentine
      IN                  arrayfns            imp                 sets
      IPy                 astyle              imputil
      setuptools
      IPython             asynchat            inspect             sexy
      IcnsImagePlugin     asyncore            invest              sgmllib
      IcoImagePlugin      atexit              ipipe               sha
      ImImagePlugin       atk                 ipy_app_completers  shelve
      Image               atom                ipy_autoreload      shlex
      ImageChops          audiodev            ipy_bzr             shutil
      ImageColor          audioop             ipy_completers      signal
      ImageDraw           base64              ipy_constants       site
      ImageDraw2          bdb                 ipy_defaults
      sitecustomize
      ImageEnhance        binascii            ipy_editors         smtpd
      ImageFile           binhex              ipy_exportdb        smtplib
      ImageFileIO         bisect              ipy_extutil         sndhdr
      ImageFilter         bonobo              ipy_fsops           socket
      ImageFont           brlapi              ipy_gnuglobal       spwd
      ImageGL             bsddb               ipy_greedycompleter sqlite3
      ImageGrab           bugbuddy            ipy_jot             sqlobject
      ImageMath           bz2                 ipy_kitcfg          sre
      ImageMode           cPickle             ipy_legacy
      sre_compile
      ImageOps            cProfile            ipy_leo
      sre_constants
      ImagePalette        cStringIO           ipy_lookfor         sre_parse
      ImagePath           cairo               ipy_p4              stat
      ImageQt             calendar            ipy_profile_doctest statvfs
      ImageSequence       cgi                 ipy_profile_none    string
      ImageStat           cgitb               ipy_profile_scipy   stringold
      ImageTransform      chunk               ipy_profile_sh
      stringprep
      ImageWin            clearcmd            ipy_profile_zope    strop
      ImtImagePlugin      cmath               ipy_pydb            struct
      InterpreterExec     cmd                 ipy_rehashdir
      subprocess
      InterpreterPasteInput code                ipy_render          sunau
      IptcImagePlugin     codecs              ipy_server          sunaudio
      JpegImagePlugin     codeop              ipy_signals         svn
      McIdasImagePlugin   collections         ipy_stock_completers symbol
      MicImagePlugin      colorblind          ipy_system_conf     symtable
      MimeWriter          colorsys            ipy_traits_completer sys
      MpegImagePlugin     commands            ipy_vimserver       syslog
      MspImagePlugin      compileall          ipy_which           tabnanny
      MySQLdb             compiler            ipy_winpdb          tarfile
      Numeric             configobj           ipy_workdir         telnetlib
      Numeric_headers     constants           itertools           tempfile
      ORBit               contextlib          jobctrl
      templatetags
      OggConvert          cookielib           keyword
      terminatorlib
      OleFileIO           copy                ldap                termios
      PIL                 copy_reg            ldapurl             test
      PSDraw              crypt               ldif                textwrap
      PaletteFile         csv                 ledit               this
      PalmImagePlugin     ctypes              libsvn              thread
      PcdImagePlugin      cups                libxml2             threading
      PcfFontFile         cupsext             libxml2mod          time
      PcxImagePlugin      cupsutils           linecache           timeit
      PdfImagePlugin      curses              linuxaudiodev
      tkColorChooser
      PhysicalQInput      datetime            locale
      tkCommonDialog
      PhysicalQInteractive dbhash              logging
      tkFileDialog
      PixarImagePlugin    dbm                 macpath             tkFont
      PngImagePlugin      dbus                macurl2path
      tkMessageBox
      PpmImagePlugin      dbus_bindings       mailbox
      tkSimpleDialog
      Precision           debconf             mailcap             toaiff
      PsdImagePlugin      decimal             markupbase          token
      Queue               deskbar             marshal             tokenize
      ScrolledText        difflib             math                totem
      SgiImagePlugin      dircache            md5                 trace
      SimpleDialog        dis                 mediaprofiles       traceback
      SimpleHTTPServer    distutils           metacity            tty
      SimpleXMLRPCServer  django              mhlib               turtle
      SocketServer        doctest             mimetools           types
      SpiderImagePlugin   drv_libxml2         mimetypes           umath
      StringIO            dsextras            mimify
      unicodedata
      SunImagePlugin      dsml                mmap                unittest
      TYPES               dumbdbm             modulefinder        uno
      TarIO               dummy_thread        multiarray          unohelper
      TgaImagePlugin      dummy_threading     multifile           urllib
      TiffImagePlugin     easy_install        mutex               urllib2
      TiffTags            egg                 nautilusburn        urlparse
      Tix                 email               netrc               user
      Tkconstants         encodings           new                 uu
      Tkdnd               envbuilder          nis                 uuid
      Tkinter             envpersist          nntplib             validate
      UserArray           errno               ntpath
      virtualenv
      UserDict            evolution           nturl2path
      virtualenv_support
      UserList            exceptions          numeric_formats     vte
      UserString          ext_rescapture      numeric_version     warnings
      WalImageFile        fcntl               opcode              wave
      WmfImagePlugin      fdpexpect           operator            weakref
      XVThumbImagePlugin  filecmp             optparse
      webbrowser
      XbmImagePlugin      fileinput           orca                whichdb
      XpmImagePlugin      fnmatch             os                  win32clip
      _LWPCookieJar       foomatic            os2emxpath          wnck
      _MozillaCookieJar   formatter           ossaudiodev         wsgiref
      __builtin__         formencode          pango               xdg
      __future__          fpformat            pangocairo          xdrlib
      _ast                ftplib              parser              xml
      _bisect             functools           pcardext            xmllib
      _bsddb              gc                  pdb                 xmlrpclib
      _codecs             gconf               pexpect             xxsubtype
      _codecs_cn          gda                 pickle              z3c
      _codecs_hk          gdata               pickleshare         zc
      _codecs_iso2022     gdbm                pickletools         zipfile
      _codecs_jp          gdl                 pip                 zipimport
      _codecs_kr          getopt              pipes               zlib
      _codecs_tw          getpass             pkg_resources       zopeskel
      _csv                gettext             pkgutil

      Enter any module name to get more help.  Or, type "modules spam" to
      search for modules whose descriptions contain the word "spam".

      help> os
      Help on module os:

      NAME
          os - OS routines for Mac, NT, or Posix depending on what
          system we're on.

      FILE
          /usr/lib/python2.5/os.py

      MODULE DOCS
          http://www.python.org/doc/current/lib/module-os.html

      DESCRIPTION
          This exports:
            - all functions from posix, nt, os2, mac, or ce, e.g. unlink, stat, etc.
            - os.path is one of the modules posixpath, ntpath, or macpath
            - os.name is 'posix', 'nt', 'os2', 'mac', 'ce' or 'riscos'
            - os.curdir is a string representing the current directory ('.' or ':')
            - os.pardir is a string representing the parent directory ('..' or '::')
            - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
            - os.extsep is the extension separator ('.' or '/')
            - os.altsep is the alternate pathname separator (None or '/')
            - os.pathsep is the component separator used in $PATH etc
            - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
            - os.defpath is the default search path for executables
            - os.devnull is the file path of the null device ('/dev/null', etc.)

          Programs that import and use 'os' stand a better chance of
          being portable between different platforms.  Of course, 
          they must then only use functions that are defined by all 
          platforms (e.g., unlink and opendir), and leave all pathname 
          manipulation to os.path
      :


Entonces presione la convinación de tecla **Crtl+d** para salir de la ayuda.

Luego realice la importación de la `librería del estándar`_ Python llamada
``os`` 

.. code-block:: python

    >>> import os
    >>>


Previamente importada la librería usted puede usar el comando ``dir`` para
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
    '/usr/lib/python2.5/os.pyc'
    >>>

También puede consultar la documentación de la librería ``os`` ejecutando el
siguiente comando:

.. code-block:: python

    >>> os.__doc__
    "OS routines for Mac, NT, or Posix depending on what system we're
    on.\n\nThis exports:\n  - all functions from posix, nt, os2, mac, or ce,
    e.g. unlink, stat, etc.\n  - os.path is one of the modules posixpath,
    ntpath, or macpath\n  - os.name is 'posix', 'nt', 'os2', 'mac', 'ce' or
    'riscos'\n  - os.curdir is a string representing the current directory
    ('.' or ':')\n  - os.pardir is a string representing the parent directory
    ('..' or '::')\n  - os.sep is the (or a most common) pathname separator
    ('/' or ':' or '\\\\')\n  - os.extsep is the extension separator ('.' or
    '/')\n  - os.altsep is the alternate pathname separator (None or '/')\n
    - os.pathsep is the component separator used in $PATH etc\n  - os.linesep
    is the line separator in text files ('\\r' or '\\n' or '\\r\\n')\n  -
    os.defpath is the default search path for executables\n  - os.devnull is
    the file path of the null device ('/dev/null', etc.)\n\nPrograms that
    import and use 'os' stand a better chance of being\nportable between
    different platforms.  Of course, they must then\nonly use functions that
    are defined by all platforms (e.g., unlink\nand opendir), and leave all
    pathname manipulation to os.path\n(e.g., split and join).\n"
    >>>


Ejecute el comando exit() para salir del interprete...

.. code-block:: python

    >>> exit()

.. _python_interprete_interactivo:

Interprete interactivo de Python
................................

Para mejorar la experiencia con el interprete Python le sugerimos instalar el
programa IPython, según su documentación:

Según Wikipedia

  "IPython es un shell interactivo que añade funcionalidades extra al `modo
  interactivo`_ incluido con Python, como resaltado de líneas y errores
  mediante colores, una sintaxis adicional para el shell, autocompletado
  mediante tabulador de variables, módulos y atributos; entre otras
  funcionalidades. Es un componente del paquete `SciPy`_."

Para mayor información visite su `página principal de ipython`_ y si necesita instalar
este programa ejecute el siguiente comando:

.. code-block:: sh

    # aptitude install ipython python-pip


Luego cierra sesión de **root** y vuelve al usuario y sustituya el comando
``python`` por ``ipython`` de la siguiente forma:

.. code-block:: sh

    $  ipython
    Python 2.5.2 (r252:60911, Jan 24 2010, 17:44:40)
    Type "copyright", "credits" or "license" for more information.

    IPython 0.8.4 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object'. ?object also works, ?? prints
    more.

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


Entonces presione la tecla **q** para salir de la ayuda

De nuevo realice la importación de la librería del estándar Python llamada
``os``

.. code-block:: python

    In [2]: import os


También consultar los detalles acerca del 'objeto' para esto use como ejemplo
la librería ``os`` ejecutando el siguiente comando:

.. code-block:: python

    In [2]: os?
    Type:           module
    Base Class:     <type 'module'>
    String Form:    <module 'os' from '/usr/lib/python2.5/os.pyc'>
    Namespace:      Interactive
    File:           /usr/lib/python2.5/os.py
    Docstring:
        OS routines for Mac, NT, or Posix depending on what system
        we're on.

        This exports:
          - all functions from posix, nt, os2, mac, or ce, e.g. unlink, stat, etc.
          - os.path is one of the modules posixpath, ntpath, or macpath
          - os.name is 'posix', 'nt', 'os2', 'mac', 'ce' or 'riscos'
          - os.curdir is a string representing the current directory ('.' or ':')
          - os.pardir is a string representing the parent directory ('..' or '::')
          - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
          - os.extsep is the extension separator ('.' or '/')
          - os.altsep is the alternate pathname separator (None or '/')
          - os.pathsep is the component separator used in $PATH etc
          - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
          - os.defpath is the default search path for executables
          - os.devnull is the file path of the null device ('/dev/null', etc.)

        Programs that import and use 'os' stand a better chance of
        being portable between different platforms.  Of course, 
        they must then only use functions that are defined by all 
        platforms (e.g., unlink and opendir), and leave all pathname 
        manipulation to os.path (e.g., split and join).


Escriba la librería *os.* y luego escribe dos **underscore** y presione *dos
veces la tecla tabular* para usar la autocompletado del interprete al 
`estilo de completación de lineas de comandos`_ en el shell UNIX/Linux para
ayudar a la introspección del lenguaje y sus librerías.

.. code-block:: python

    In [3]: os.__
    os.__all__           os.__class__         os.__dict__
    os.__file__          os.__hash__          os.__name__
    os.__reduce__        os.__repr__          os.__str__
    os.__builtins__      os.__delattr__       os.__doc__
    os.__getattribute__  os.__init__          os.__new__
    os.__reduce_ex__     os.__setattr__



De nuevo ejecute el método ``file`` para determinar la ubicación de la
librería importada

.. code-block:: python

    In [4]: os.__file__
    Out[4]: '/usr/lib/python2.5/os.pyc'


También puede consultar la documentación de la librería ``os`` de la
siguiente forma:

.. code-block:: python

    In [5]: os.__doc__
    Out[5]: "OS routines for Mac, NT, or Posix depending on what system
    we're on.\n\nThis exports:\n  - all functions from posix, nt, os2, mac,
    or ce, e.g. unlink, stat, etc.\n  - os.path is one of the modules
    posixpath, ntpath, or macpath\n  - os.name is 'posix', 'nt', 'os2',
    'mac', 'ce' or 'riscos'\n  - os.curdir is a string representing the
    current directory ('.' or ':')\n  - os.pardir is a string representing
    the parent directory ('..' or '::')\n  - os.sep is the (or a most common)
    pathname separator ('/' or ':' or '\\\\')\n  - os.extsep is the extension
    separator ('.' or '/')\n  - os.altsep is the alternate pathname separator
    (None or '/')\n  - os.pathsep is the component separator used in $PATH
    etc\n  - os.linesep is the line separator in text files ('\\r' or '\\n'
    or '\\r\\n')\n  - os.defpath is the default search path for executables\n
    - os.devnull is the file path of the null device ('/dev/null',
    etc.)\n\nPrograms that import and use 'os' stand a better chance of
    being\nportable between different platforms.  Of course, they must
    then\nonly use functions that are defined by all platforms (e.g.,
    unlink\nand opendir), and leave all pathname manipulation to
    os.path\n(e.g., split and join).\n"


Otro ejemplo es imprimir el **nombre de la clase** con el siguiente comando:

.. code-block:: python

    In [6]: os.__name__
    Out[6]: 'os'


Y otra forma de consultar la documentación de la librería ``os`` es
ejecutando el siguiente comando:

.. code-block:: python

    In [7]: help(os)
    Help on module os:

    NAME
        os - OS routines for Mac, NT, or Posix depending on what
        system we're on.

    FILE
        /usr/lib/python2.5/os.py

    MODULE DOCS
        http://www.python.org/doc/current/lib/module-os.html

    DESCRIPTION
        This exports:
          - all functions from posix, nt, os2, mac, or ce, e.g. unlink, stat, etc.
          - os.path is one of the modules posixpath, ntpath, or macpath
          - os.name is 'posix', 'nt', 'os2', 'mac', 'ce' or 'riscos'
          - os.curdir is a string representing the current directory ('.' or ':')
          - os.pardir is a string representing the parent directory ('..' or '::')
          - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
          - os.extsep is the extension separator ('.' or '/')
          - os.altsep is the alternate pathname separator (None or '/')
          - os.pathsep is the component separator used in $PATH etc
          - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
          - os.defpath is the default search path for executables
          - os.devnull is the file path of the null device ('/dev/null', etc.)

        Programs that import and use 'os' stand a better chance of
        being portable between different platforms.  Of course, 
        they must then only use functions that are defined by all 
        platforms (e.g., unlink and opendir), and leave all pathname 
        manipulation to os.path
    :


Entonces presione la tecla **q** para salir de la ayuda

Y para borrar la sesión con el IPython ejecute el siguiente comando:

.. code-block:: python

    In [8]: exit()
    Do you really want to exit ([y]/n)? y

Interprete interactivo con el paquete bpython
..............................................

Alternativamente puedes usar el `paquete bpython` que mejora aun mas la experiencia 
de trabajo con el paquete `ipython`

Para mayor información visite su `página principal de bpython`_ y si necesita instalar
este programa ejecute el siguiente comando:

.. code-block:: sh

    # pip install bpython

Luego cierra sesión de **root** y vuelve al usuario y sustituya el comando
``python`` por ``ipython`` de la siguiente forma:

.. code-block:: sh

    $  bpython
    

Dentro de interprete Python puede apreciar que ofrece otra forma de presentar 
la documentación y la estructura del lenguaje, con los siguientes comandos de ejemplos:

.. code-block:: python

    >>> print 'Hola mundo'
    Hola mundo
    >>> for item in xrange(
    ┌───────────────────────────────────────────────────────────────────────┐
    │ xrange: ([start, ] stop[, step])                                      │
    │ xrange([start,] stop[, step]) -> xrange object                        │
    │                                                                       │
    │ Like range(), but instead of returning a list, returns an object that │
    │ generates the numbers in the range on demand.  For looping, this is   │
    │ slightly faster than range() and more memory efficient.               │
    └───────────────────────────────────────────────────────────────────────┘

     <C-r> Rewind  <C-s> Save  <F8> Pastebin  <F9> Pager  <F2> Show Source


Conclusiones
------------

Como puede apreciar este tutorial no le enseña a programar sino a simplemente
aprender a conocer como manejarse en el modo interactivo de Python/IPython
con el fin de conocer a través de la introspección del lenguaje, las
librerías estándar / propias de Python que tienes instalado en tu sistema.

.. seealso:: 
  
  -   `Python`_.
  -   `Inmersión en Python`_.
  -   `Guía de aprendizaje de Python`_.
  -   `La librería estándar de Python`_.
  -   `Guide to Python introspection`_.

Referencias
-----------

-   `Una pequeña inmersión al modo interactivo de Python`_ de la fundación Cenditel.

.. _Python: http://www.python.org/ 
.. _multiparadigma: http://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n_multiparadigma
.. _orientación a objetos: http://es.wikipedia.org/wiki/Programaci%C3%B3n_orientada_a_objetos
.. _programación imperativa: http://es.wikipedia.org/wiki/Programaci%C3%B3n_imperativa
.. _programación funcional: http://es.wikipedia.org/wiki/Programaci%C3%B3n_funcional
.. _lenguaje interpretado: http://es.wikipedia.org/wiki/Lenguaje_interpretado
.. _tipado dinámico: http://es.wikipedia.org/wiki/Tipado_din%C3%A1mico
.. _fuertemente tipado: http://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n_fuertemente_tipado
.. _multiplataforma: http://es.wikipedia.org/wiki/Multiplataforma
.. _todo en Python es un objeto: http://es.diveintopython.org/odbchelper_objects.html
.. _Javadoc: http://es.wikipedia.org/wiki/Javadoc
.. _diagramas de clases: http://es.wikipedia.org/wiki/Diagrama_de_clases
.. _Sphinx: http://en.wikipedia.org/wiki/Sphinx_%28documentation_generator%29
.. _La librería estándar de Python: http://pyspanishdoc.sourceforge.net/tut/node12.html
.. _librería del estándar: http://pyspanishdoc.sourceforge.net/tut/node12.html
.. _modo interactivo: http://es.wikipedia.org/wiki/Python#Modo_interactivo
.. _SciPy: http://en.wikipedia.org/wiki/SciPy
.. _página principal de ipython: http://ipython.scipy.org/
.. _paquete bpython: http://pypi.python.org/pypi/bpython/
.. _página principal de bpython: http://bpython-interpreter.org/
.. _estilo de completación de lineas de comandos: http://en.wikipedia.org/wiki/Command_line_completion
.. _Inmersión en Python: http://es.diveintopython.org/
.. _Guía de aprendizaje de Python: http://pyspanishdoc.sourceforge.net/tut/tut.html
.. _Guide to Python introspection: http://www.ibm.com/developerworks/linux/library/l-pyint.html
.. _Una pequeña inmersión al modo interactivo de Python: http://plataforma.cenditel.gob.ve/wiki/Plone%3AUnaPequenaInmersionPython
.. _fundación Cenditel: https://twitter.com/cenditel
