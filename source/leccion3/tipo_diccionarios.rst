.. -*- coding: utf-8 -*-


.. _python_dict:

Tipo diccionarios
-----------------

El diccionario, define una relación uno a uno entre claves y valores.

+-----------+----------+---------------------+----------------------------------+
| **Clase** | **Tipo** | **Notas**           | **Ejemplo**                      |
+-----------+----------+---------------------+----------------------------------+
| ``dict``  | Mapeos   | Mutable, sin orden. | ``{'cms':"Plone", 'version':5}`` |
+-----------+----------+---------------------+----------------------------------+

Un objeto *mapping* mapea valores *hashable* a objetos arbitrariamente. Los objetos
Mapeos son objetos mutable. El **diccionario** es el único tipo de mapeo estándar
actual. Para otro contenedores ver los integrados en las clases ":ref:`lista <python_list>`",
":ref:`conjuntos <python_set>`", y ":ref:`tupla <python_tuple>`", y el modulo
"``collections``".

Los diccionarios pueden ser creados colocando una lista separada por coma de pares
"key:value" entre ``{}``, por ejemplo: "``{'python': 27, 'plone': 51}``" o
"``{27:'python', 51:'plone'}``", o por el constructor ":ref:`dict() <python_fun_dict>`".


.. code-block:: pycon

    >>> diccionario = {
    ...     "clave1": 234,
    ...     "clave2": True,
    ...     "clave3": "Valor 1",
    ...     "clave4": [1, 2, 3, 4],
    ... }
    >>> print(diccionario, type(diccionario))
    {'clave4': [1, 2, 3, 4], 'clave1': 234,
    'clave3': 'Valor 1', 'clave2': True} <type 'dict'>

Usted puede acceder a los valores del diccionario usando cada su clave, se presenta
unos ejemplos a continuación:

.. code-block:: pycon

    >>> diccionario["clave1"]
    234
    >>> diccionario["clave2"]
    True
    >>> diccionario["clave3"]
    'Valor 1'
    >>> diccionario["clave4"]
    [1, 2, 3, 4]

Un diccionario puede almacenar los diversos tipos de datos integrados en Python usando
la función :ref:`type() <python_fun_type>`, usted puede pasar el diccionario con la
clave que usted desea determinar el tipo de dato, se presenta unos ejemplos a
continuación:

.. code-block:: pycon

    >>> type(diccionario["clave1"])
    <type 'int'>
    >>> type(diccionario["clave2"])
    <type 'bool'>
    >>> type(diccionario["clave3"])
    <type 'str'>
    >>> type(diccionario["clave4"])
    <type 'list'>


.. _python_dict_opers:

Operaciones
...........

Los objetos de tipo **diccionario** permite una serie de operaciones usando operadores
integrados en el interprete Python para su tratamiento, a continuación algunos de
estos:


.. _python_dict_opers_showv:

Acceder a valor de clave
~~~~~~~~~~~~~~~~~~~~~~~~

Esta operación le permite acceder a un valor especifico del *diccionario* mediante su
clave.

.. code-block:: pycon

    >>> versiones = {"python": 3.11, "zope": 5.2, "plone": 6.0, "django": 4.2.7}
    >>> versiones["zope"]
    5.2


.. _python_dict_opers_setv:

Asignar valor a clave
~~~~~~~~~~~~~~~~~~~~~

Esta operación le permite asignar el valor especifico del *diccionario* mediante su
clave.

.. code-block:: pycon

    >>> versiones = {"python": 3.11, "zope": 5.2, "plone": None}
    >>> versiones["plone"]
    >>> versiones["plone"] = 6.0
    >>> versiones
    {'python': 3.11, 'zope': 5.2, 'plone': 6.0}
    >>> versiones["plone"]
    6.0


.. _python_dict_opers_in:

Iteración in
~~~~~~~~~~~~

Este operador es el mismo operador integrado :ref:`in <python_opers_in>` en el
interprete Python pero aplicada al uso de la secuencia de tipo **diccionario**.

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0, django=4.2.7)
    >>> print(versiones)
    {'zope': 5.2, 'python': 3.11, 'plone': 6.0, 'django': 4.2.7}
    >>> "plone" in versiones
    True
    >>> "flask" in versiones
    False

En el ejemplo anterior este operador devuelve ``True`` si la clave esta en el diccionario
``versiones``, de lo contrario devuelve ``False``.


.. _python_dict_mtds:

Métodos
.......

Los objetos de tipo **diccionario** integra una serie de métodos integrados a
continuación:


.. _python_dict_mtd_clear:

clear()
~~~~~~~

Este método remueve todos los elementos desde el **diccionario**.

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> print(versiones)
    {'zope': 5.2, 'python': 3.11, 'plone': 6.0}
    >>> versiones.clear()
    >>> print(versiones)
    {}


.. _python_dict_mtd_copy:

copy()
~~~~~~

Este método devuelve una copia superficial del tipo **diccionario**:

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> otro_versiones = versiones.copy()
    >>> versiones == otro_versiones
    True


.. _python_dict_mtd_fromkeys:

fromkeys()
~~~~~~~~~~

Este método crea un nuevo **diccionario** con *claves* a partir de un tipo de dato
*secuencia*. El valor de ``value`` por defecto es el tipo :ref:`None <python_obj_none>`.

.. code-block:: pycon

    >>> secuencia = ("python", "zope", "plone")
    >>> versiones = dict.fromkeys(secuencia)
    >>> print("Nuevo Diccionario : %s" % str(versiones))
    Nuevo Diccionario : {'python': None, 'zope': None, 'plone': None}

En el ejemplo anterior inicializa los valores de cada clave a ``None``, más puede
inicializar un *valor* común por defecto para cada *clave*:

.. code-block:: pycon

    >>> versiones = dict.fromkeys(secuencia, 0.1)
    >>> print("Nuevo Diccionario : %s" % str(versiones))
    Nuevo Diccionario : {'python': 0.1, 'zope': 0.1, 'plone': 0.1}


.. _python_dict_mtd_get:

get()
~~~~~

Este método devuelve el valor en base a una coincidencia de búsqueda en un diccionario
mediante una clave, de lo contrario devuelve el objeto :ref:`None <python_obj_none>`.

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> versiones.get("plone")
    6.0
    >>> versiones.get("php")
    >>>


.. _python_dict_mtd_has_key:

has_key()
~~~~~~~~~

Este método devuelve el valor ``True`` si el diccionario tiene presente la clave
enviada como argumento.

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> versiones.has_key("plone")
    True
    >>> versiones.has_key("django")
    False


.. _python_dict_mtd_items:

items()
~~~~~~~

Este método devuelve una :ref:`lista <python_list>` de pares de diccionarios (clave, valor), como 2 :ref:`tuplas <python_tuple>`.

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> versiones.items()
    dict_items([('python', 3.11), ('zope', 5.2), ('plone', 6.0)])
    >>> for clave, valor in versiones.items():
    ...     print(clave, valor)
    ...
    python 3.11
    zope 5.2
    plone 6.0


.. _python_dict_mtd_iterkeys:

iterkeys()
~~~~~~~~~~

Este método devuelve un :ref:`iterador <python_iter>` sobre las claves del diccionario.
Lanza una excepción :ref:`StopIteration <python_exception_stopiteration>` si llega al
final de la posición del **diccionario**.

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> print(versiones)
    {'python': 3.11, 'zope': 5.2, 'plone': 6.0}
    >>> versiones.keys()
    dict_keys(['python', 'zope', 'plone'])
    >>> for clave in versiones.keys():
    ...     print(clave)
    ...
    zope
    python
    plone
    >>> versiones_iter = iter(versiones)
    >>> print(next(versiones_iter))
    python
    >>> print(next(versiones_iter))
    zope
    >>> print(next(versiones_iter))
    plone
    >>> print(next(versiones_iter))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration


.. _python_dict_mtd_keys:

keys()
~~~~~~

Este método devuelve una :ref:`lista <python_list>` de las claves del **diccionario**:

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> versiones.keys()
    dict_keys(['python', 'zope', 'plone'])
    >>> for clave in versiones.keys():
    ...     print(clave)
    ...
    python
    zope
    plone


.. _python_dict_mtd_pop:

pop()
~~~~~

Este método remueve específicamente una clave de **diccionario** y devuelve valor
correspondiente. Lanza una excepción :ref:`KeyError <python_exception_keyerror>`
si la **clave** no es encontrada.

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> versiones
    {'zope': 5.2, 'python': 3.11, 'plone': 6.0}
    >>> versiones.pop("zope")
    5.2
    >>> versiones
    {'python': 3.11, 'plone': 6.0}
    >>> versiones.pop("django")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'django'


.. _python_dict_mtd_popitem:

popitem()
~~~~~~~~~

Este método remueve y devuelve algún par (clave, valor) del **diccionario** como
una 2 :ref:`tuplas <python_tuple>`. Lanza una excepción :ref:`KeyError <python_exception_keyerror>` si
el **diccionario** esta vació.

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> versiones
    {'zope': 5.2, 'python': 3.11, 'plone': 6.0}
    >>> versiones.popitem()
    ('zope', 5.2)
    >>> versiones
    {'python': 3.11, 'plone': 6.0}
    >>> versiones.popitem()
    ('python', 3.11)
    >>> versiones
    {'plone': 6.0}
    >>> versiones.popitem()
    ('plone', 6.0)
    >>> versiones
    {}
    >>> versiones.popitem()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'popitem(): dictionary is empty'


.. _python_dict_mtd_setdefault:

setdefault()
~~~~~~~~~~~~

Este método es similar a :ref:`get(key, default_value) <python_dict_mtd_get>`, pero además
asigna la clave ``key`` al valor por ``default_value`` para la clave si esta no se encuentra
en el **diccionario**.

.. code-block:: pycon

    D.setdefault(key[,default_value])

A continuación un ejemplo de como trabaja el método ``setdefault()`` cuando la clave
esta en el diccionario:

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> zope = versiones.setdefault("zope")
    >>> print("Versiones instaladas:", versiones)
    Versiones instaladas: {'zope': 5.2, 'python': 3.11, 'plone': 6.0}
    >>> print("Versión de Zope:", zope)
    Versión de Zope: 5.2

A continuación un ejemplo de como trabaja el método ``setdefault()`` la clave no esta
en el diccionario:

.. code-block:: pycon

    >>> paquetes = {"python": 3.11, "zope": 5.2}
    >>> print(paquetes)
    {'python': 3.11, 'zope': 5.2}
    >>> plone = paquetes.setdefault("plone")
    >>> print("paquetes: ", paquetes)
    paquetes:  {'python': 3.11, 'zope': 5.2, 'plone': None}
    >>> print("plone: ", plone)
    plone:  None

Si el valor no es proveído, el valor ``default_value`` será el tipo objeto integrado
:ref:`None <python_obj_none>`.

A continuación un ejemplo de como trabaja el método ``setdefault()`` la clave no esta
en el diccionario pero esta vez el ``default_value`` es proveído:

.. code-block:: pycon

    >>> pkgs = {"python": 3.11, "zope": 5.2, "plone": None}
    >>> print(pkgs)
    {'python': 3.11, 'zope': 5.2, 'plone': None}
    >>> django = paquetes.setdefault("django", 4.2.7)
    >>> print("paquetes =", pkgs)
    paquetes = {'python': 3.11, 'zope': 5.2, 'plone': None}
    >>> print("django =", django)
    django = 4.2.7

A continuación otro ejemplo en donde puedes agrupar N :ref:`tuplas <python_tuple>`
por el valor el cual se repite más y construir un diccionario que cuyas claves son
los valores más repetidos y cuyos valores este agrupados en tipo
:ref:`listas <python_list>`:

.. code-block:: pycon

    >>> PKGS = (
    ...     ("zope", "Zope"),
    ...     ("zope", "zope.pagetemplate"),
    ...     ("plone", "Plone"),
    ...     ("plone", "ZODB3"),
    ...     ("plone", "plone.volto"),
    ... )
    >>>
    >>> paquetes = {}
    >>> for clave, valor in PKGS:
    ...     if paquetes.has_key(clave):
    ...         paquetes[clave].append(valor)
    ...     else:
    ...         paquetes[clave] = [valor]
    ...
    >>> print(paquetes)
    {'zope': ['Zope', 'zope.pagetemplate'], 'plone': ['Plone', 'ZODB3', 'plone.volto']}

En el tipo :ref:`tupla <python_tuple>` ``PKGS`` los elementos más repetidos son ``'zope'``
y ``'plone'`` estos se convierten en clave del diccionario ``paquetes`` y los otros elementos
se agregan en listas como sus respectivos valores.

A continuación un mejor aprovechamiento implementando el método ``setdefault()``:

.. code-block:: pycon

    >>> PKGS = (
    ...     ("zope", "Zope"),
    ...     ("zope", "zope.pagetemplate"),
    ...     ("plone", "Plone"),
    ...     ("plone", "ZODB3"),
    ...     ("plone", "plone.volto"),
    ... )
    >>> paquetes = {}
    >>> for clave, valor in PKGS:
    ...     paquetes.setdefault(clave, []).append(valor)
    ...
    >>> print(paquetes)
    {'zope': ['Zope', 'zope.pagetemplate'], 'plone': ['Plone', 'ZODB3', 'plone.volto']}

En el ejemplo anterior puede ver que el aprovechamiento del método ``setdefault()``
a comparación de no usar el respectivo método.


.. _python_dict_mtd_update:

update()
~~~~~~~~

Este método actualiza un **diccionario** agregando los pares clave-valores en un
segundo diccionario. Este método no devuelve nada.

El método ``update()`` toma un diccionario o un objeto iterable de pares clave/valor
(generalmente :ref:`tuplas <python_tuple>`). Si se llama a ``update()`` sin pasar parámetros, el diccionario
permanece sin cambios.

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> print(versiones)
    {'zope': 5.2, 'python': 3.11, 'plone': 6.0}
    >>> versiones_adicional = dict(django=4.2.7)
    >>> print(versiones_adicional)
    {'django': 4.2.7}
    >>> versiones.update(versiones_adicional)

Como puede apreciar este método no devuelve nada, más si muestra de nuevo el diccionario
``versiones`` puede ver que este fue actualizado con el otro diccionario
``versiones_adicional``.

.. code-block:: pycon

    >>> print(versiones)
    {'zope': 5.2, 'python': 3.11, 'plone': 6.0, 'django': 4.2.7}


.. _python_dict_mtd_values:

values()
~~~~~~~~

Este método devuelve una :ref:`lista <python_list>` de los valores del **diccionario**:

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> versiones.values()
    dict_values([3.11, 5.2, 6.0])
    >>> for valor in versiones.values():
    ...     print(valor)
    ...
    3.11
    5.2
    6.0


.. _python_dict_fun:

Funciones
.........

Los objetos de tipo **diccionario** tienen disponibles una serie de *funciones*
integradas en el interprete Python para su tratamiento, a continuación algunas
de estas:

.. _python_dict_fun_len:

len()
~~~~~

Esta función es la misma función integrada :ref:`len() <python_fun_len>` en el
interprete Python pero aplicada al uso de la secuencia de tipo **diccionario**.

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0)
    >>> len(versiones)
    3


.. _python_dict_snt:

Sentencias
..........

Los objetos de tipo **diccionario** tienen disponibles una serie de *sentencias*
integradas en el interprete Python para su tratamiento, a continuación algunas
de estas:

.. _python_dict_snt_del:

del
~~~

Esta sentencia es la misma sentencia integrada :ref:`del <python_sent_del>` en el
interprete Python pero aplicada al uso de la secuencia de tipo **diccionario**.

.. code-block:: pycon

    >>> versiones = dict(python=3.11, zope=5.2, plone=6.0, django=4.2.7)
    >>> print(versiones)
    {'python': 3.11, 'zope': 5.2, 'plone': 6.0, 'django': 4.2.7}
    >>> del versiones["django"]
    >>> print(versiones)
    {'python': 3.11, 'zope': 5.2, 'plone': 6.0}

En el código fuente anterior se usa la sentencia ``del`` para eliminar un elemento del
diccionario mediante su respectiva clave.


Convertir a diccionarios
........................

Para convertir a *tipos diccionarios* debe usar la función :ref:`dict() <python_fun_dict>`
la cual :ref:`esta integrada <python_fun_builtins>` en el interprete Python.

.. tip::
    Para más información consulte las funciones integradas para
    :ref:`operaciones de secuencias <python_fun_builtins_secuencias>`.


.. _python_dict_ejs:

Ejemplos
........

A continuación, se presentan un ejemplo de su uso:

**Definir un diccionario**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :linenos:
    :lines: 4-12

**Operaciones con tipo diccionario con funciones propias**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :linenos:
    :lines: 18-20

**Iteración avanzada sobre diccionarios con función items**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :linenos:
    :lines: 25-26

**Caso real de usar tipo diccionario**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :linenos:
    :lines: 29-46


Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los **diccionarios**
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

.. code-block:: pycon

    >>> help(dict)


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion3/tipo_diccionarios.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_diccionarios.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    .. code-block:: console

        $ python tipo_diccionarios.py


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
