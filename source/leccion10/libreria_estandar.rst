.. -*- coding: utf-8 -*-


.. _python_libreria_estandar:

Librería estándar Python
------------------------

La `librería estándar`_ Python 3 incluye los siguientes módulos y librerías:

- :ref:`Funciones integradas <python_fun_builtins>` y funciones integradas no esenciales

- Constantes integradas, con el módulo `site`_.

- Tipos integrados, incluye 13 tipos, como :ref:`Booleano <python_bool>`, :ref:`Numérico <python_int>` y otros.

- Manejo de :ref:`excepciones integradas <python_excepciones_builtins>`.

- Servicios :ref:`cadenas de caracteres <python_str>`, incluye 11 librerías, como `string`_, `re`_ y otros.

- Tipos de datos, incluye 19 librerías, como :ref:`datetime <python_modulo_datetime>`, `pprint`_ y otros.

- Módulos numéricos y matemáticos, incluye 9 librerías, como `decimal`_, `math`_ y otros.

- Acceso a archivos y directorios, incluye 12 librerías, como `os.path`_, `fileinput`_ y otros.

- Persistencia de datos, incluye 13 librerías, como :ref:`pickle <python_modulo_pickle>`, :ref:`sqlite3 <python_modulo_sqlite3>` y otros.

- Compresión de datos y de archivo, incluye 5 librerías, como `zlib`_, `gzip`_ y otros.

- Formatos de archivo, incluye 6 librerías, como `csv`_, `configparser`_ y otros.

- Servicios criptográficos, incluye 4 librerías, como `hashlib`_, `secrets`_ y otros.

- Servicios genéricos del sistema operativo, incluye 17 librerías, como `os`_, `time`_ y otros.

- Servicios opcionales del sistema operativo, incluye 9 librerías, como `threading`_, `readline`_ y otros.

- Comunicación entre procesos y redes, incluye 7 librerías, como `subprocess`_, `socket`_ y otros.

- Manejo de datos de Internet, incluye 16 librerías, como :ref:`email <python_modulo_email>`, :ref:`json <python_modulo_json>` y otros.

- Procesamiento de marcado estructurado, incluye 15 librerías, como `html.parser`_, `html.entities`_ y otros.

- Protocolos de Internet y soporte, incluye 25 librerías, como `cgi`_, `wsgiref`_ y otros.

- Servicios multimedia, incluye 10 librerías, como `audioop`_, `wave`_ y otros.

- Internacionalización, incluye las librerías `gettext`_ y `locale`_.

- Program Frameworks, incluye las librerías `cmd`_ y `shlex`_.

- Interfaces gráficas de usuario con Tk, incluye 7 librerías, como `tkinter`_, `IDLE`_ y otros.

- Herramientas de desarrollo, incluye 6 librerías, como `unittest`_, `test`_ y otros.

- Depuración y Profiling, incluye 7 librerías, como :ref:`pdb <python_modulo_pdb>`, `trace`_ y otros.

- Empaquetado y distribución de software, incluye las librerías `distutils`_ y `ensurepip`_.

- Python Runtime Services, incluye 16 librerías, como `sys`_, `site`_ y otros.

- Intérpretes de Python personalizados, incluye las librerías `code`_ y `codeop`_.

- Importación de módulos, incluye 7 librerías, como `imp`_, `runpy`_ y otros.

- Python Language Services, incluye 13 librerías, como `parser`_, `dis`_ y otros.

- Paquete compilador de Python, incluye 5 librerías.

- Servicios Misceláneos, `formatter`_ librería incluida.

- Servicios específicos de MS Windows, incluye 4 librerías, como `msilib`_, `winsound`_ y otros.

- Servicios específicos de Unix, incluye 16 librerías, como `subprocess`_, `syslog`_ y otros.

- Acceso a dispositivos de audio compatibles con Open Sound System - OSS, la librería `ossaudiodev`_.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion10>`
    del entrenamiento para ampliar su conocimiento en esta temática.

.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::

.. _`librería estándar`: https://docs.python.org/es/3.7/library/index.html
.. _`site`: https://docs.python.org/es/3.7/library/site.html
.. _`pprint`: https://docs.python.org/es/3.7/library/pprint.html
.. _`string`: https://docs.python.org/es/3.7/library/string.html
.. _`re`: https://docs.python.org/es/3.7/library/re.html
.. _`decimal`: https://docs.python.org/es/3.7/library/decimal.html
.. _`math`: https://docs.python.org/es/3.7/library/math.html
.. _`os.path`: https://docs.python.org/es/3.7/library/os.path.html
.. _`fileinput`: https://docs.python.org/es/3.7/library/fileinput.html
.. _`zlib`: https://docs.python.org/es/3.7/library/zlib.html
.. _`gzip`: https://docs.python.org/es/3.7/library/gzip.html
.. _`csv`: https://docs.python.org/es/3.7/library/csv.html
.. _`configparser`: https://docs.python.org/es/3.7/library/configparser.html
.. _`hashlib`: https://docs.python.org/es/3.7/library/hashlib.html
.. _`secrets`: https://docs.python.org/es/3.7/library/secrets.html
.. _`os`: https://docs.python.org/es/3.7/library/os.html
.. _`time`: https://docs.python.org/es/3.7/library/time.html
.. _`threading`: https://docs.python.org/es/3.7/library/threading.html
.. _`readline`: https://docs.python.org/es/3.7/library/readline.html
.. _`subprocess`: https://docs.python.org/es/3.7/library/subprocess.html
.. _`socket`: https://docs.python.org/es/3.7/library/socket.html
.. _`html.entities`: https://docs.python.org/es/3.7/library/html.entities.html
.. _`html.parser`: https://docs.python.org/es/3.7/library/html.parser.html
.. _`cgi`: https://docs.python.org/es/3.7/library/cgi.html
.. _`wsgiref`: https://docs.python.org/es/3.7/library/wsgiref.html
.. _`audioop`: https://docs.python.org/es/3.7/library/audioop.html
.. _`wave`: https://docs.python.org/es/3.7/library/wave.html
.. _`gettext`: https://docs.python.org/es/3.7/library/gettext.html
.. _`locale`: https://docs.python.org/es/3.7/library/locale.html
.. _`shlex`: https://docs.python.org/es/3.7/library/shlex.html
.. _`cmd`: https://docs.python.org/es/3.7/library/cmd.html
.. _`tkinter`: https://docs.python.org/es/3.7/library/tkinter.html
.. _`IDLE`: https://docs.python.org/es/3.7/library/idle.html
.. _`unittest`: https://docs.python.org/es/3.7/library/unittest.html
.. _`test`: https://docs.python.org/es/3.7/library/test.html
.. _`trace`: https://docs.python.org/es/3.7/library/trace.html
.. _`distutils`: https://docs.python.org/es/3.7/library/distutils.html
.. _`ensurepip`: https://docs.python.org/es/3.7/library/ensurepip.html
.. _`sys`: https://docs.python.org/es/3.7/library/sys.html
.. _`code`: https://docs.python.org/es/3.7/library/code.html
.. _`codeop`: https://docs.python.org/es/3.7/library/codeop.html
.. _`imp`: https://docs.python.org/es/3.7/library/imp.html
.. _`runpy`: https://docs.python.org/es/3.7/library/runpy.html
.. _`parser`: https://docs.python.org/es/3.7/library/parser.html
.. _`dis`: https://docs.python.org/es/3.7/library/dis.html
.. _`formatter`: https://docs.python.org/es/3.7/library/formatter.html
.. _`msilib`: https://docs.python.org/es/3.7/library/msilib.html
.. _`winsound`: https://docs.python.org/es/3.7/library/winsound.html
.. _`syslog`: https://docs.python.org/es/3.7/library/syslog.html
.. _`ossaudiodev`: https://docs.python.org/es/3.7/library/ossaudiodev.html
