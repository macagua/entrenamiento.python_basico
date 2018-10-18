.. -*- coding: utf-8 -*-


.. _python_caracteristicas:

Características
---------------

Las `características`_ del lenguaje de programación Python se resumen 
a continuación:

-   Es un `lenguaje interpretado`_, usa :ref:`tipado dinámico <python_tipado_dinamico>`,  
    :ref:`fuertemente tipado <python_fuertemente_tipado>`.

-   Es :ref:`multiplataforma <python_multiplataforma>`, lo cual es ventajoso para hacer 
    ejecutable su código fuente entre varios sistema operativos.

-   Es un lenguaje de programación `multiparadigma`_, el cual soporta varios paradigma de 
    programación como :ref:`orientación a objetos <python_poo>`, `programación imperativa`_ 
    y, en menor medida, `programación funcional`_.


.. _python_tipado_dinamico:

Python es tipado dinámico
.........................

El `tipado dinámico`_ significa que los objetos en tiempo de ejecución (valores) 
tienen un tipo, a diferencia del tipado estático donde las variables tienen un tipo.
A continuación un ejemplo de este concepto:

.. literalinclude:: ../../recursos/leccion1/tipado_dinamico.py
    :linenos:
    :language: python
    :lines: 16-21


.. _python_fuertemente_tipado:

Python es fuertemente tipado
............................

El `fuertemente tipado`_ significa que el tipo de valor no cambia repentinamente. 
Un string que contiene solo dígitos no se convierte mágicamente en un número. Cada 
cambio de tipo requiere una conversión explícita. A continuación un ejemplo de este 
concepto:

.. literalinclude:: ../../recursos/leccion1/fuertemente_tipados.py
    :linenos:
    :language: python
    :lines: 20-27


.. _python_multiplataforma:

Python es multiplataforma
.........................

Python es `multiplataforma`_, lo cual es ventajoso para hacer ejecutable su código fuente 
entre varios sistema operativos, eso quiere decir, soporta las siguientes plataformas para 
su ejecución:

- Versiones Python para `Microsoft Windows (y DOS) <https://www.python.org/downloads/windows/>`_ 
  (arquitectura x86/x86-64 en presentación de ejecutable, archivo Zip, instalador basado en 
  la Web).

- Versiones Python para `Mac OSX (Macintosh) <https://www.python.org/downloads/mac-osx/>`_ (arquitectura 
  32bit/64bit en presentación de instalador ejecutable).

- Versiones Python en `código fuente <https://www.python.org/downloads/source/>`_ (archivo 
  tarball del código fuente comprimido con XZ y con Gz). Para las mayoría de los sistemas 
  Linux/UNIX, usted debe descargar y compilar el código fuente.

- Versiones de `Implementaciones Alternativas Python <https://www.python.org/download/alternatives/>`_, 
  la versión "tradicional" de Python (tiene nombre código ``CPython``). Existen un número de implementaciones alternativas que están disponibles a continuación:

    - `IronPython <http://ironpython.net/>`_, Python ejecutando en .NET.

    - `Jython <http://www.jython.org/>`_, Python ejecutando en el Java Virtual Machine.

    - `PyPy <http://pypy.org/>`_, Una rápida implementación de python con un compilador JIT.

    - `Stackless Python <http://www.stackless.com/>`_, Rama del desarrollo del ``CPython`` que soporta microthreads.

    - `MicroPython <http://micropython.org/>`_, Python ejecutando en micro controladores.

- Versiones de Python en `otras plataformas <https://www.python.org/download/other/>`_,
  la versión "tradicional" de Python (tiene nombre código ``CPython``), mas esta versión ha sido migrada a un número plataformas especializadas y/o antiguas, a continuación se destacan algunas de ellas. 

    - `Pythonista <http://omz-software.com/pythonista/index.html>`_, Python para iOS, ofrece un completo entorno de desarrollo para escribir scripts Python en su iPad o iPhone.

    -  `ActivePython <http://www.activestate.com/activepython/>`_, Python para Solaris, Usted puede 
       comprarlo (versiones comerciales y comunitarias, incluidos los módulos de computación científica,
       no de código abierto), o compilar desde una fuente si tiene un compilador de C.
       Los paquetes UNIX tienen una variedad de versiones de Python para una variedad de versiones de Solaris. Estos utilizan el estándar Sun ``pkgadd``.

  .. note::
  
      Tenga en cuenta que estos migraciones a menudo están muy por detrás de la última versión de Python.



Filosofía "Incluye baterías"
............................

- Python ha mantenido durante mucho tiempo esta filosofía de "baterías incluidas":

	*"Tener una biblioteca estándar rica y versátil que está disponible de inmediato. 
	Sin que el usuario descargue paquetes separados."*

- Esto le da al lenguaje una ventaja en muchos proyectos. 

- Las "baterías incluidas" están en la librería estándar Python.


La librería estándar Python
...........................

La librería estándar Python incluye los siguientes módulos y librerías:

- Funciones incorporadas y funciones incorporadas no esenciales

- Constantes incorporadas, con el módulo ``site``.

- Tipos incorporados, incluye 13 tipos, como ``Booleano``, ``Numérico`` y otros.

- Manejo de Excepciones

- Servicios cadenas de caracteres, incluye 11 librerías, como ``string``, ``re`` y otros.

- Tipos de datos, incluye 19 librerías, como ``datetime``, ``pprint`` y otros.

- Módulos numéricos y matemáticos, incluye 9 librerías, como ``decimal``, ``math`` y otros.

- Acceso a archivos y directorios, incluye 12 librerías, como ``os.path``, ``fileinput`` y otros.

- Persistencia de datos, incluye 13 librerías, como ``pickle``, ``sqlite3`` y otros.

- Compresión de datos y de archivo, incluye 5 librerías, como ``zlib``, ``gzip`` y otros.

- Formatos de archivo, incluye 6 librerías, como ``csv``, ``ConfigParser`` y otros.

- Servicios criptográficos, incluye 4 librerías, como ``hashlib``, ``md5`` y otros.

- Servicios genéricos del sistema operativo, incluye 17 librerías, como ``os``, ``time`` y otros.

- Servicios opcionales del sistema operativo, incluye 9 librerías, como ``threading``, ``readline`` y otros.

- Comunicación entre procesos y redes, incluye 7 librerías, como ``subprocess``, ``socket`` y otros.

- Manejo de datos de Internet, incluye 16 librerías, como ``email``, ``json`` y otros.

- Procesamiento de marcado estructurado, incluye 15 librerías, como ``HTMLParser``, ``htmllib`` y otros.

- Protocolos de Internet y soporte, incluye 25 librerías, como ``cgi``, ``wsgiref`` y otros.

- Servicios multimedia, incluye 10 librerías, como ``audioop``, ``wave`` y otros.

- Internacionalización, incluye las librerías ``gettext`` y ``locale``.

- Program Frameworks, incluye las librerías ``cmd`` y ``shlex``.

- Interfaces gráficas de usuario con Tk, incluye 7 librerías, como ``Tkinter``, ``IDLE`` y otros.

- Herramientas de desarrollo, incluye 6 librerías, como ``unittest``, ``test`` y otros.

- Depuración y Profiling, incluye 7 librerías, como ``pdb``, ``trace`` y otros.

- Empaquetado y distribución de software, incluye las librerías ``distutils`` y ``ensurepip``.

- Python Runtime Services, incluye 16 librerías, como ``sys``, ``site`` y otros.

- Intérpretes de Python personalizados, incluye las librerías ``code`` y ``codeop``.

- Ejecución restringida, incluye las librerías ``rexec`` y ``Bastion``.

- Importación de módulos, incluye 7 librerías, como ``imp``, ``runpy`` y otros.

- Python Language Services, incluye 13 librerías, como ``parser``, ``dis`` y otros.

- Paquete compilador de Python, incluye 5 librerías.

- Servicios Misceláneos, ``formatter`` librería incluida.

- Servicios específicos de MS Windows, incluye 4 librerías, como ``msilib``, ``winsound`` y otros.

- Servicios específicos de Unix, incluye 16 librerías, como ``commands``, ``syslog`` y otros.

- Servicios específicos de Mac OS X, incluye 9 librerías, como ``ic``, ``MacOS`` y otros.

- Módulos de MacPython OSA, incluye 12 librerías, como ``aepack``, ``aetypes`` y otros.

- Servicios específicos de SGI IRIX, incluye  12 librerías, como ``gl``, ``jpeg`` y otros.

- Servicios específicos de SunOS, las librerías ``sunaudiodev`` y ``SUNAUDIODEV``.


.. seealso:: Ver el vídeo `Tutorial Python 1 - Introducción al Lenguaje de Programación`_.

.. _`características`: https://es.wikipedia.org/wiki/Python#Caracter.C3.ADsticas_y_paradigmas
.. _`multiparadigma`: https://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n_multiparadigma
.. _`programación imperativa`: https://es.wikipedia.org/wiki/Programaci%C3%B3n_imperativa
.. _`programación funcional`: https://es.wikipedia.org/wiki/Programaci%C3%B3n_funcional
.. _`lenguaje interpretado`: https://es.wikipedia.org/wiki/Lenguaje_interpretado
.. _`tipado dinámico`: https://es.wikipedia.org/wiki/Tipado_din%C3%A1mico
.. _`fuertemente tipado`: https://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n_fuertemente_tipado
.. _`multiplataforma`: https://es.wikipedia.org/wiki/Multiplataforma
.. _`Tutorial Python 1 - Introducción al Lenguaje de Programación`: https://www.youtube.com/watch?v=CjmzDHMHxwU
