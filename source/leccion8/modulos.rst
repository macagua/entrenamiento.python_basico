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

El código Python para un módulo nombrado ``funciones`` normalmente reside un
archivo llamado ``utilidades.py``. A continuación un ejemplo de un simple módulo
llamado ``utilidades.py``:

.. literalinclude:: ../../recursos/leccion8/modulos/utilidades.py
    :language: python
    :linenos:
    :lines: 1-8

.. _python_sent_import:

Sentencia import
................

La sentencia ``import`` se utiliza para importar un módulo. Usted puede usar
cualquier archivo de código Python como un módulo ejecutando esta sentencia
en otro archivo de código Python. La sentencia ``import`` tiene la siguiente
sintaxis:

.. code-block:: pycon

    >>> import os
    >>> import re, datetime

Cuando el interprete encuentra una sentencia ``import``, este importa el módulo
si el mismo esta presente en la ruta de búsqueda. Una ruta de búsqueda es una lista
de directorios que el interprete busca antes de importar un módulo.

Por ejemplo, al importar el módulo ``utilidades.py``, usted necesita colocar la
siguiente sentencia al tope del otro script Python. A continuación un ejemplo de
un simple módulo, ``calculo_factura_pipo.py``.

.. literalinclude:: ../../recursos/leccion8/modulos/calculo_factura_pipo.py
    :language: python
    :linenos:
    :lines: 1-22

Cuando el código anterior es ejecutado, ese produce el siguiente resultado:

::

    Importo el modulo ``utilidades.pyc``

    Función ``suma_total`` del módulo ``utilidades.pyc`` llamado y mostró:
    Ingrese un monto: 56987
    Monto total a facturar: 57007 Bs (VES).

Un módulo se carga solo una vez, independientemente de la cantidad de veces que
se importe. Esto evita que la ejecución del módulo ocurra una y otra vez si se
producen múltiples importaciones.

La primera vez que un módulo es importado en un script de Python, se ejecuta su
código una vez. Si otro módulo importa el mismo módulo este no se cargará
nuevamente; los módulos son inicializados una sola vez.

Esto se debe al código objeto compilado que genera en el mismo directorio del
módulo que cargo con la extensión de archivo **.pyc**, ejecutando las siguientes
sentencias:

.. code-block:: pycon

    >>> import funciones, os
    >>> archivos = os.listdir(
    ...     os.path.abspath(funciones.__file__).replace("/utilidades.pyc", "/")
    ... )
    >>> print(filter(lambda x: x.startswith("funciones."), archivos))
    ['utilidades.py', 'utilidades.pyc']


De esta forma se comprueba que existe el archivo compilado de Python junto con
el mismo módulo Python.


.. _python_localizar_modulos:

Localizando módulos
...................

Cuando usted importa un módulo, el interprete Python busca por el módulo en
la secuencia siguiente:

#. El directorio actual.

#. Si el módulo no es encontrado, Python entonces busca en cada directorio en
   la variable de entorno :ref:`PYTHONPATH <python_variable_entorno_path>` del
   sistema operativo.

#. Si todas las anteriores fallan, Python busca la ruta predeterminada. En UNIX,
   la ruta predeterminada normalmente esta ``/usr/local/lib/python/``.

El ruta de búsqueda de módulo es almacenado en el módulo de system ``sys`` como
la variable ``sys.path``. La variable ``sys.path`` contiene el directorio actual,
``PYTHONPATH``, y las predeterminadas dependencia de instalación.


.. _python_variable_entorno_path:

PYTHONPATH
..........

Es una variable de entorno del sistema operativo, consistiendo de una lista de
directorios. La sintaxis de ``PYTHONPATH`` es la misma como la del shell de la
variable ``PATH``.

Así es una típica definición de ``PYTHONPATH`` desde un sistema Windows, ejecutando:

.. code-block:: console

    set PYTHONPATH = C:\python20\lib;

Así es una típica definición de ``PYTHONPATH`` desde un sistema UNIX, ejecutando:

.. code-block:: console

    set PYTHONPATH = /usr/local/lib/python


.. _python_modulos_namespace_alcance:

Espacios de nombres y alcance
.............................

Las :ref:`variables <python_variable>` son nombres (identificadores) que se asignan
a objetos.

Un espacio de nombres o namespace, es un :ref:`diccionario <python_dict>` de nombres de variables (claves)
y sus objetos (valores) correspondientes.

Una sentencia de Python puede acceder a las variables en un espacio de nombres local
y en el espacio de nombres global. Si una *variable local* y una *variable global*
tienen el mismo nombre, la *variable local* sombrea la *variable global*.

Cada :ref:`función <python_funciones>` tiene su propio espacio de nombres local. Los
:ref:`métodos <python_metodos>` de Clase siguen la misma regla de alcance que las
funciones ordinarias.

Python hace conjeturas educadas sobre si las variables son locales o globales. Se supone
que cualquier variable asignada a un valor en una función es local.

Por lo tanto, para asignar un valor a una variable global dentro de una función, primero
debe usar la sentencia :ref:`global <python_sent_global>`.

.. code-block:: pycon

    >>> global nombre
    >>> nombre
    'Leonardo'

La sintaxis ``global nombre``, le dice al interprete Python que la variable ``nombre``
es una *variable global*. Python deja de buscar la variable en el espacio de nombres
local.

Por ejemplo, defina una variable ``Money`` en el espacio de nombres global. Dentro
de la función ``Money``, asigna un valor a ``Money``, por lo tanto, Python asume que
``Money`` es una variable local. Sin embargo, accede al valor de la variable local
``Money`` antes de configurarlo, por lo que el resultado es una excepción
:ref:`UnboundLocalError <python_exception_unboundlocalerror>`. Si descomenta la
sentencia ``global``, se soluciona el problema.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces: :download:`utilidades.py <../../recursos/leccion8/modulos/utilidades.py>`
    y :download:`calculo_factura_pipo.py <../../recursos/leccion8/modulos/calculo_factura_pipo.py>`.


.. tip::
    Para ejecutar el código :file:`utilidades.py` y :file:`calculo_factura_pipo.py`,
    abra una consola de comando, acceda al directorio donde se encuentra ambos programas:

    ::

        leccion8/
        ├── utilidades.py
        └── calculo_factura_pipo.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python calculo_factura_pipo.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion8>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
