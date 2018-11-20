.. -*- coding: utf-8 -*-


.. _python_modulos:

Módulos Python
--------------

Un módulo le permite a usted organizar lógicamente su código Python. Agrupando 
código relacionado dentro de un módulo hace el código mas fácil de entender y 
usar. Un módulo es un objeto de Python con atributos con nombres arbitrarios 
que puede enlazar y hacer referencia.

Simplemente, un módulo es no es otra cosa sino un archivo con extensión **.py**. 
Un módulo puede definir funciones, clases y variables, también puede incluir 
código ejecutable.

El código Python para un módulo nombrado ``funciones`` normalmente reside un archivo 
llamado ``funciones.py``. A continuación un ejemplo de un simple módulo, ``funciones.py``.

.. literalinclude:: ../../recursos/leccion8/funciones.py
    :language: python
    :lines: 3-6

.. _python_sentencia_import:

Sentencia import
................

La sentencia ``import`` se utiliza para importar un módulo. Usted puede usar 
cualquier archivo de código Python como un módulo ejecutando esta sentencia 
en otro archivo de código Python. La sentencia ``import`` tiene la siguiente 
sintaxis:

::

    >>> import os
    >>> import re, datetime

Cuando el interprete encuentra una sentencia ``import``, este importa el módulo 
si el mismo esta presente en la ruta de búsqueda. Una ruta de búsqueda es una lista 
de directorios que el interprete busca antes de importar un módulo. Por ejemplo, al 
importar el módulo ``funciones.py``, usted necesita colocar la siguiente sentencia al 
tope del otro script Python. A continuación un ejemplo de un simple módulo, 
``mi_mensaje.py``.

.. literalinclude:: ../../recursos/leccion8/mi_mensaje.py
    :language: python
    :lines: 3-16

Cuando el código anterior es ejecutado, ese produce el siguiente resultado:

::

    Se importo el modulo 'funciones.pyc'

    Función 'mensaje' del módulo 'funciones.pyc' se llamo mostrando:
    Hola Python

Un módulo se carga solo una vez, independientemente de la cantidad de veces que se 
importe. Esto evita que la ejecución del módulo ocurra una y otra vez si se producen 
múltiples importaciones.

La primera vez que un módulo es importado en un script de Python, se ejecuta 
su código una vez. Si otro módulo importa el mismo módulo este no se cargará 
nuevamente; los módulos son inicializados una sola vez.

Esto se debe al código objeto compilado que genera en el mismo directorio del 
módulo que cargo con la extensión de archivo **.pyc**, ejecutando las siguientes 
sentencias:

::

    >>> import funciones, os
    >>> archivos = os.listdir(os.path.abspath(
    ...     funciones.__file__).replace("/funciones.pyc", "/"))
    >>> print filter(lambda x: x.startswith('funciones.'), archivos)
    ['funciones.py', 'funciones.pyc']


De esta forma se comprueba que existe el archivo compilado de Python junto con 
el mismo modulo Python.


.. comments

    ::

        >>> archivos = os.listdir(os.__file__.replace("/os.pyc", "/"))
        >>> print filter(lambda x: x.startswith('os.'), archivos)
        ['os.pyc', 'os.py']

    En el ejemplo anterior se el método ``os.__file__`` para obtener la ruta donde esta instalada 
    el modulo ``os`` en su sistema, ejecutando la siguiente sentencia:

    ::

        >>> os.__file__
        '/usr/lib/python2.7/os.pyc'

    Luego se inicializa la variable ``archivos`` generando una lista de archivos usando la función 
    ``os.listdir()``, ejecutando la siguiente sentencia:

    ::

        >>> archivos = os.listdir("/usr/lib/python2.7/")
        >>> type(archivos)
        <type 'list'>
        >>> len(archivos)
        443

    Opcionalmente puede comprobar si la cadena de caracteres **os.pyc** se encuentras una de las 
    posiciones de la lista ``archivos``, ejecutando la siguiente sentencia:

    ::

        >>> "os.pyc" in archivos
        True

    Ya al comprobar que existe la cadena de caracteres "**os.pyc**" se usa una 
    función :ref:`lambda <python_funcion_lambda>` con la función 
    :ref:`filter() <python_funcion_filter>` para filtrar todos los archivos 
    del directorio "*/usr/lib/python2.7/*" por medio del función ``os.listdir()`` 
    que inicien con la cadena de caracteres "**os.**" usando la función 
    :ref:`startswith() <python_funcion_startswith>`.

    ::

        >>> print filter(lambda x: x.startswith('os.'), os.listdir('/usr/lib/python2.7/'))
        ['os.pyc', 'os.py']

    Así de esta forma se comprueba que existe el archivo compilado de Python junto con el mismo modulo Python.

    ::

        >>> os.__file__
        '/usr/lib/python2.7/os.pyc'
        >>> archivos = os.listdir("/usr/lib/python2.7/")
        >>> type(archivos)
        <type 'list'>
        >>> len(archivos)
        443
        >>> "os.pyc" in archivos
        True
        >>> print filter(lambda x: x.startswith('os.'), os.listdir('/usr/lib/python2.7/'))
        >>> ['os.pyc', 'os.py']


Localizando módulos
...................

Cuando usted importa un módulo, el interprete Python busca por el módulo en 
la secuencia siguiente:

#. El directorio actual.

#. Si el módulo no es encontrado, Python entonces busca en cada directorio en 
   la variable de entorno ``PYTHONPATH`` del sistema operativo.

#. Si todas las anteriores fallan, Python busca la ruta predeterminada. En UNIX, 
   la ruta predeterminada normalmente esta ``/usr/local/lib/python/``.

El ruta de búsqueda de módulo es almacenado en el modulo de system ``sys`` como 
la variable ``sys.path``. La variable ``sys.path`` contiene el directorio actual, 
``PYTHONPATH``, y las predeterminadas dependencia de instalación.


PYTHONPATH
..........

Es una variable de entorno del sistema operativo, consistiendo de una lista de directorios. 
La sintaxis de ``PYTHONPATH`` es la misma como la del shell de la variable ``PATH``.

Así es una típica definición de ``PYTHONPATH`` desde un sistema Windows, ejecutando:

::

    set PYTHONPATH = C:\python20\lib;

Así es una típica definición de ``PYTHONPATH`` desde un sistema UNIX, ejecutando:

::

    set PYTHONPATH = /usr/local/lib/python


Espacios de nombres y alcance
.............................

Las variables son nombres (identificadores) que se asignan a objetos. Un namespace 
o espacio de nombres es un diccionario de nombres de variables (claves) y sus objetos 
(valores) correspondientes.

Una sentencia de Python puede acceder a las variables en un espacio de nombres local 
y en el espacio de nombres global. Si una variable local y una global tienen el mismo 
nombre, la variable local sombrea la variable global.

Cada función tiene su propio espacio de nombres local. Los métodos de Clase siguen la 
misma regla de alcance que las funciones ordinarias.

Python hace conjeturas educadas sobre si las variables son locales o globales. Se supone 
que cualquier variable asignada a un valor en una función es local.

Por lo tanto, para asignar un valor a una variable global dentro de una función, primero 
debe usar la sentencia ``global``.

La sentencia ``global VarName`` le dice a Python que ``VarName`` es una variable global. 
Python deja de buscar el espacio de nombres local para la variable.

Por ejemplo, definimos una variable ``Money`` en el espacio de nombres global. Dentro de 
la función ``Money``, asignamos un valor a ``Money``, por lo tanto, Python asume que ``Money`` 
es una variable local. Sin embargo, accedimos al valor de la variable local ``Money`` antes de 
configurarlo, por lo que el resultado es una excepción 
:ref:`UnboundLocalError <python_exception_unboundlocalerror>`. Si no se comenta la sentencia 
``global``, se soluciona el problema. Uncommenting the global statement fixes the problem.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los 
    siguientes enlaces: :download:`funciones.py <../../recursos/leccion8/funciones.py>` 
    y :download:`mi_mensaje.py <../../recursos/leccion8/mi_mensaje.py>`.


.. tip::
    Para ejecutar el código :file:`funciones.py` y :file:`mi_mensaje.py`, 
    abra una consola de comando, acceda al directorio donde se encuentra ambos programas: :: 

        leccion8/
        ├── funciones.py
        └── mi_mensaje.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando: ::

        python2 mi_mensaje.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion8>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
