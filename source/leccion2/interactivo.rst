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

.. code-block:: pycon

    python3
    Python 3.7.3 (default, Jan 22 2021, 20:04:44)
    [GCC 8.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>


Puede solicitar la ayudar del interprete de Python, ejecutando:

.. code-block:: pycon

    >>> help
    Type help() for interactive help, or help(object) for help about object.
    >>> help()

    Welcome to Python 3.7's help utility!

    If this is your first time using Python, you should definitely check out
    the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

    Enter the name of any module, keyword, or topic to get help on writing
    Python programs and using Python modules.  To quit this help utility and
    return to the interpreter, just type "quit".

    To get a list of available modules, keywords, symbols, or topics, type
    "modules", "keywords", "symbols", or "topics".  Each module also comes
    with a one-line summary of what it does; to list the modules whose name
    or summary contain a given string such as "spam", type "modules spam".

    help>


Para ejecutar la ayuda disponible sobre la sintaxis Python ejecute el
siguiente comando:

.. code-block:: pycon

    help> modules

    Please wait a moment while I gather a list of all available modules...

    Crypto              brain_namedtuple_enum imaplib             regex
    HtmlTagNames        brain_nose          imghdr              reportbug
    HtmlVoidElements    brain_numpy         imp                 reprlib
    OpenSSL             brain_pkg_resources importlib           requests
    PIL                 brain_pytest        importlib_metadata  resource
    PyQt5               brain_qt            importlib_resources restructuredtext_lint
    __future__          brain_re            inspect             rlcompleter
    _abc                brain_six           invoke              roman
    _ast                brain_ssl           io                  rstcheck
    _asyncio            brain_subprocess    ipaddress           runpy
    _bisect             brain_threading     ipython_genutils    safety
    _blake2             brain_typing        isort               sarge
    _bootlocale         brain_uuid          iteration_utilities sched
    _bz2                brlapi              itertools           scour
    _cffi_backend       bs4                 itsdangerous        scspell
    _codecs             builtins            jinja2              secrets
    _codecs_cn          bz2                 jinja2_ansible_filters secretstorage
    _codecs_hk          cProfile            joblib              select
    _codecs_iso2022     cairo               jsbeautifier        selectors
    _codecs_jp          calendar            json                setuptools
    _codecs_kr          caribou             jsonschema          shelve
    _codecs_tw          certifi             jupyter             shlex
    _collections        cfgv                jupyter_core        shutil
    _collections_abc    cgi                 kazam               signal
    _compat_pickle      cgitb               keyring             simplejson
    _compression        chardet             keyword             sip
    _contextvars        chunk               lazy_object_proxy   sipconfig
    _crypt              clang               ldap                sipconfig_nd7
    _csv                click               ldap3               site
    _ctypes             cmakelint           ldapurl             sitecustomize
    _ctypes_test        cmath               ldif                six
    _curses             cmd                 lib2to3             slapdtest
    _curses_panel       coala_utils         libfuturize         smbc
    _datetime           coalib              libpasteurize       smmap
    _dbm                code                linecache           smtpd
    _dbus_bindings      codecs              locale              smtplib
    _dbus_glib_bindings codeop              logging             sndhdr
    _decimal            collections         louis               snowballstemmer
    _distutils_hack     colorama            lsb_release         socket
    _dummy_thread       colorlog            lxml                socketserver
    _elementtree        colorsys            lzma                softwareproperties
    _functools          compileall          macpath             soupsieve
    _hashlib            concurrent          mailbox             speaklater
    _heapq              configobj           mailcap             speechd
    _imp                configparser        mako                speechd_config
    _io                 contextlib          mando               spellchecker
    _json               contextvars         markdown            sphinx
    _ldap               copier              markups             sphinx_rtd_theme
    _locale             copy                markupsafe          spwd
    _lsprof             copyreg             marshal             sqlalchemy
    _lzma               cpp                 math                sqlite3
    _markupbase         cpplint             mccabe              sqlparse
    _md5                crypt               mdx_math            sre_compile
    _multibytecodec     cryptography        meld                sre_constants
    _multiprocessing    cssbeautifier       mimetypes           sre_parse
    _opcode             csv                 mmap                sshtunnel
    _openshot           ctypes              modulefinder        ssl
    _operator           cups                multiprocessing     stat
    _osx_support        cupshelpers         munkres             statistics
    _pickle             curl                mypy                stevedore
    _posixsubprocess    curses              nacl                string
    _py_abc             dataclasses         nbformat            stringprep
    _pydecimal          datetime            netrc               struct
    _pyio               dateutil            nis                 subprocess
    _pyrsistent_version dbm                 nltk                suds
    _queue              dbus                nntplib             sunau
    _random             deb822              nodeenv             symbol
    _sha1               debconf             ntpath              symtable
    _sha256             debian              nturl2path          sys
    _sha3               debian_bundle       numbers             sysconfig
    _sha512             debianbts           olefile             syslog
    _signal             decimal             opcode              tabnanny
    _sitebuiltins       dennis              openshot            tarfile
    _smbc               dependency_management openshot_qt         telnetlib
    _socket             difflib             operator            tempfile
    _sqlite3            dis                 optparse            template_remover
    _sre                distlib             orca                termcolor
    _ssl                distro              os                  termios
    _stat               distro_info         ossaudiodev         test
    _string             distutils           packaging           tests
    _strptime           djlint              paramiko            textile
    _struct             docker              parser              textwrap
    _symtable           docopt              passlib             this
    _sysconfigdata_m_linux_x86_64-linux-gnu doctest             past                threading
    _testbuffer         docutils            pathlib             time
    _testcapi           dummy_threading     pathspec            timeit
    _testimportmultiple dunamai             pbr                 tkinter
    _testmultiphase     editor              pdb                 token
    _thread             editorconfig        pickle              tokenize
    _threading_local    email               pickletools         toml
    _tkinter            enchant             pip                 tomli
    _tracemalloc        encodings           pipes               tqdm
    _uuid               ensurepip           pipx                trace
    _version            entrypoints         pkg_resources       traceback
    _warnings           enum                pkgutil             tracemalloc
    _weakref            eradicate           platform            traitlets
    _weakrefset         errno               platformdirs        tty
    _xxtestfuzz         faulthandler        plistlib            turtle
    _yaml               fcntl               plumbum             typeguard
    abc                 filecmp             polib               types
    aifc                fileinput           poplib              typing
    alabaster           filelock            posix               typing_extensions
    alembic             flask               posixpath           ufw
    antigravity         flask_babelex       pprint              unicodedata
    appdirs             flask_compress      pre_commit          unidiff
    apt                 flask_gravatar      profile             unittest
    apt_inst            flask_login         prompt_toolkit      uno
    apt_pkg             flask_mail          proselint           unohelper
    aptsources          flask_migrate       pstats              urllib
    argcomplete         flask_paranoid      psutil              urllib3
    argparse            flask_principal     psycopg2            userpath
    array               flask_security      pty                 uu
    asn1crypto          flask_sqlalchemy    pvectorc            uuid
    ast                 flask_wtf           pwd                 validate
    astroid             fnmatch             py_compile          venv
    asynchat            formatter           pyasn1              virtualenv
    asyncio             fractions           pyasn1_modules      vobject
    asyncore            ftplib              pyatspi             vulture
    atexit              functools           pyclbr              warnings
    attr                future              pycodestyle         wave
    attrs               gc                  pycurl              wcwidth
    audioop             genericpath         pydantic            weakref
    autoflake           getopt              pydoc               webbrowser
    autopep8            getpass             pydoc_data          webencodings
    babel               gettext             pydocstyle          websocket
    backports           gi                  pyexpat             werkzeug
    bandit              git                 pyflakes            wheel
    base64              gitdb               pygls               wrapt
    bcrypt              glob                pygments            wsgiref
    bdb                 gnomemusic          pygtkcompat         wtforms
    bears               gpg                 pyinotify           xdg
    binascii            grp                 pylint              xdrlib
    binhex              gtweak              pyparsing           xml
    bisect              guess_language      pyprint             xmlrpc
    blinker             gzip                pyroma              xxlimited
    brain_attrs         hashlib             pyrsistent          xxsubtype
    brain_builtin_inference heapq               pysimplesoap        yaml
    brain_collections   hmac                pytz                yamlinclude
    brain_curses        html                qrcode              yamllint
    brain_dateutil      html5lib            questionary         yapf
    brain_fstrings      html_linter         queue               yapftests
    brain_functools     http                quopri              zipapp
    brain_gi            httpie              radon               zipfile
    brain_hashlib       httplib2            random              zipimport
    brain_io            identify            re                  zipp
    brain_mechanize     idna                readline            zlib
    brain_multiprocessing imagesize           redshift_gtk        zmq

    Enter any module name to get more help.  Or, type "modules spam" to search
    for modules whose name or summary contain the string "spam".

Entonces consulte la ayuda del módulo ``os``, ejecutando:

.. code-block:: pycon

    help> os
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

.. tip:: Presione la tecla :keys:`q` para salir de la ayuda del módulo ``os``.

Seguidamente presione la combinación de tecla **Crtl+d** para salir de la ayuda.

Luego realice la importación de la `librería del estándar`_ Python llamada
``os``, con el siguiente comando:

.. code-block:: pycon

    >>> import os
    >>>


Previamente importada la librería usted puede usar la función ``dir()`` para
listar o descubrir que atributos, métodos de la clase están disponibles con
la importación

.. code-block:: pycon

    >>> dir(os)
    ['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'DirEntry',
    'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST',
    'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE',
    'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE',
    'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 'GRND_NONBLOCK',
    'GRND_RANDOM', 'MutableMapping', 'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND',
    'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECT', 'O_DIRECTORY', 'O_DSYNC',
    'O_EXCL', 'O_LARGEFILE', 'O_NDELAY', 'O_NOATIME', 'O_NOCTTY', 'O_NOFOLLOW',
    'O_NONBLOCK', 'O_PATH', 'O_RDONLY', 'O_RDWR', 'O_RSYNC', 'O_SYNC',
    'O_TMPFILE', 'O_TRUNC', 'O_WRONLY', 'POSIX_FADV_DONTNEED', 'POSIX_FADV_NOREUSE',
    'POSIX_FADV_NORMAL', 'POSIX_FADV_RANDOM', 'POSIX_FADV_SEQUENTIAL',
    'POSIX_FADV_WILLNEED', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL',
    'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'PathLike', 'RTLD_DEEPBIND',
    'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD',
    'RTLD_NOW', 'RWF_DSYNC', 'RWF_HIPRI', 'RWF_NOWAIT', 'RWF_SYNC', 'R_OK',
    'SCHED_BATCH', 'SCHED_FIFO', 'SCHED_IDLE', 'SCHED_OTHER', 'SCHED_RESET_ON_FORK',
    'SCHED_RR', 'SEEK_CUR', 'SEEK_DATA', 'SEEK_END', 'SEEK_HOLE', 'SEEK_SET',
    'ST_APPEND', 'ST_MANDLOCK', 'ST_NOATIME', 'ST_NODEV', 'ST_NODIRATIME', 'ST_NOEXEC',
    'ST_NOSUID', 'ST_RDONLY', 'ST_RELATIME', 'ST_SYNCHRONOUS', 'ST_WRITE', 'TMP_MAX',
    'WCONTINUED', 'WCOREDUMP', 'WEXITED', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED',
    'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG',
    'WUNTRACED', 'W_OK', 'XATTR_CREATE', 'XATTR_REPLACE', 'XATTR_SIZE_MAX', 'X_OK',
    '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
    '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit',
    '_fspath', '_fwalk', '_get_exports_list', '_putenv', '_spawnvef', '_unsetenv',
    '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'chown',
    'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 'cpu_count', 'ctermid',
    'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'environb',
    'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp',
    'execvpe', 'extsep', 'fchdir', 'fchmod', 'fchown', 'fdatasync', 'fdopen', 'fork',
    'forkpty', 'fpathconf', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fstatvfs', 'fsync',
    'ftruncate', 'fwalk', 'get_blocking', 'get_exec_path', 'get_inheritable',
    'get_terminal_size', 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid',
    'getgid', 'getgrouplist', 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp',
    'getpid', 'getppid', 'getpriority', 'getrandom', 'getresgid', 'getresuid', 'getsid',
    'getuid', 'getxattr', 'initgroups', 'isatty', 'kill', 'killpg', 'lchown', 'linesep',
    'link', 'listdir', 'listxattr', 'lockf', 'lseek', 'lstat', 'major', 'makedev', 'makedirs',
    'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path',
    'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'pipe2', 'popen', 'posix_fadvise',
    'posix_fallocate', 'pread', 'preadv', 'putenv', 'pwrite', 'pwritev', 'read', 'readlink',
    'readv', 'register_at_fork', 'remove', 'removedirs', 'removexattr', 'rename', 'renames',
    'replace', 'rmdir', 'scandir', 'sched_get_priority_max', 'sched_get_priority_min',
    'sched_getaffinity', 'sched_getparam', 'sched_getscheduler', 'sched_param',
    'sched_rr_get_interval', 'sched_setaffinity', 'sched_setparam', 'sched_setscheduler',
    'sched_yield', 'sendfile', 'sep', 'set_blocking', 'set_inheritable', 'setegid', 'seteuid',
    'setgid', 'setgroups', 'setpgid', 'setpgrp', 'setpriority', 'setregid', 'setresgid',
    'setresuid', 'setreuid', 'setsid', 'setuid', 'setxattr', 'spawnl', 'spawnle', 'spawnlp',
    'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 'stat_result',
    'statvfs', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd',
    'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sync',
    'sys', 'sysconf', 'sysconf_names', 'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size',
    'times', 'times_result', 'truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink',
    'unsetenv', 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitid', 'waitid_result',
    'waitpid', 'walk', 'write', 'writev']
    >>>


Otro ejemplo de uso, es poder usar el método ``file`` para determinar la
ubicación de la librería importada de la siguiente forma:

.. code-block:: pycon

    >>> os.__file__
    '/usr/lib/python3.7/os.pyc'
    >>>

También puede consultar la documentación de la librería ``os`` ejecutando el
siguiente comando:

.. code-block:: pycon

    >>> print(os.__doc__)
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

.. code-block:: pycon

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

.. code-block:: console

    sudo apt install ipython


Sustituya el comando ``python3`` por ``ipython3`` de la siguiente forma:

.. code-block:: console

    $ ipython3
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

.. code-block:: python

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


Interprete bpython
..................

Alternativamente puedes usar el paquete `bpython` que mejora aun mas la experiencia
de trabajo con el paquete `ipython`.

Para mayor información visite su página principal de `interprete bpython`_ y si necesita
instalar este programa ejecute el siguiente comando:

.. code-block:: console

    sudo apt install -y python-pip
    sudo pip3 install bpython

Luego cierra sesión de **root** y vuelve al usuario y sustituya el comando
``python`` por ``ipython`` de la siguiente forma:

.. code-block:: console

    bpython


Dentro de interprete Python puede apreciar que ofrece otra forma de presentar
la documentación y la estructura del lenguaje, con los siguientes comandos de ejemplos:

.. code-block:: console

    >>> print('Hola Mundo')
    Hola Mundo
    >>> for item in range(
    ┌───────────────────────────────────────────────────────────────────────────────┐
    │ range: (stop)                                                                 │
    │ range(stop) -> range object                                                   │
    │ range(start, stop[, step]) -> range object                                    │
    │                                                                               │
    │ Return an object that produces a sequence of integers from start (inclusive)  │
    │ to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.     │
    │ start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.      │
    │ These are exactly the valid indices for a list of 4 elements.                 │
    │ When step is given, it specifies the increment (or decrement).                │
    └───────────────────────────────────────────────────────────────────────────────┘


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


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::


.. _`Python`: https://www.python.org/
.. _`Javadoc`: https://es.wikipedia.org/wiki/Javadoc
.. _`diagramas de clases`: https://es.wikipedia.org/wiki/Diagrama_de_clases
.. _`Sphinx`: https://en.wikipedia.org/wiki/Sphinx_%28documentation_generator%29
.. _`librería del estándar`: https://docs.python.org/es/3.7/library/index.html
.. _`modo interactivo`: https://es.wikipedia.org/wiki/Python#Modo_interactivo
.. _`SciPy`: https://en.wikipedia.org/wiki/SciPy
.. _`ipython`: https://ipython.readthedocs.io/en/stable/
.. _`bpython`: https://pypi.org/project/bpython/
.. _`interprete bpython`: https://bpython-interpreter.org/
.. _`estilo de completación de lineas de comandos`: https://en.wikipedia.org/wiki/Command_line_completion
