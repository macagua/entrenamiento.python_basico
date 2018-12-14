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


::

    >>> diccionario = {
    ...     "clave1":234,
    ...     "clave2":True,
    ...     "clave3":"Valor 1",
    ...     "clave4":[1,2,3,4]
    ... }
    >>> print diccionario, type(diccionario)
    {'clave4': [1, 2, 3, 4], 'clave1': 234, 
    'clave3': 'Valor 1', 'clave2': True} <type 'dict'>

Usted puede acceder a los valores del diccionario usando cada su clave, se presenta 
unos ejemplos a continuación:

::

    >>> diccionario['clave1']
    234
    >>> diccionario['clave2']
    True
    >>> diccionario['clave3']
    'Valor 1'
    >>> diccionario['clave4']
    [1, 2, 3, 4]

Un diccionario puede almacenar los diversos tipos de datos integrados en Python usando 
la función :ref:`type() <python_fun_type>`, usted puede pasar el diccionario con la 
clave que usted desea determinar el tipo de dato, se presenta unos ejemplos a 
continuación:

::

    >>> type(diccionario['clave1'])
    <type 'int'>
    >>> type(diccionario['clave2'])
    <type 'bool'>
    >>> type(diccionario['clave3'])
    <type 'str'>
    >>> type(diccionario['clave4'])
    <type 'list'>


.. _python_dict_mtds:

Métodos
.......

Los objetos de tipo **diccionario** integra una serie de métodos integrados a 
continuación:


.. _python_dict_mtd_clear:

clear()
~~~~~~~

Este método remueve todos los elementos desde el **diccionario**.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> print versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> versiones.clear()
    >>> print versiones
    {}


.. _python_dict_mtd_copy:

copy()
~~~~~~

Este método devuelve una copia superficial del tipo **diccionario**:

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> otro_versiones = versiones.copy()
    >>> versiones == otro_versiones
    True


.. _python_dict_mtd_fromkeys:

fromkeys()
~~~~~~~~~~

Este método crea un nuevo **diccionario** con claves a partir de una secuencia ``seq``
y con valores asignados a ``value``.

.. todo:: TODO terminar de escribir sobre este método integrado.

::

    dict.fromkeys(seq[,value])

El nuevo **diccionario** con claves de la secuencia ``seq`` y los valores son iguales a 
``value``. El valor de ``value`` por defecto es :ref:`None <python_obj_none>`.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versionesIterador = versiones.iterkeys()
    >>> versiones.fromkeys(versionesIterador[,5.1])

.. todo:: TODO terminar de escribir un ejemplo de uso del método.


.. _python_dict_mtd_get:

get()
~~~~~

Este método devuelve el valor en base a una coincidencia de búsqueda en un diccionario 
mediante una clave, de lo contrario devuelve el objeto :ref:`None <python_obj_none>`. 

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones.get('plone')
    5.1
    >>> versiones.get('php')
    >>>


.. _python_dict_mtd_has_key:

has_key()
~~~~~~~~~

Este método devuelve el valor ``True`` si el diccionario tiene presente la clave 
enviada como argumento. D.has_key(k) -> True if D has a key k, else False

.. todo:: TODO traducir frases del párrafo anterior.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones.has_key('plone')
    True


.. _python_dict_mtd_items:

items()
~~~~~~~

Este método devuelve una lista de pares de diccionarios (clave, valor), como 2 tuplas:

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones.items()
    [('zope', 2.13), ('python', 2.7), ('plone', 5.1)]


.. _python_dict_mtd_iteritems:

iteritems()
~~~~~~~~~~~

Este método devuelve un iterador sobre los elementos (clave, valor) del diccionario.
Lanza una excepción :ref:`StopIteration <python_exception_stopiteration>` si llega al 
final de la posición del **diccionario**.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> print versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> versiones.iteritems()
    <dictionary-itemiterator object at 0x7fab9dd4bc58>
    >>> for clave,valor in versiones.iteritems():
    ...     print clave,valor
    ... 
    zope 2.13
    python 2.7
    plone 5.1
    >>> versionesIterador = versiones.iteritems()
    >>> print versionesIterador.next()
    ('zope', 2.13)
    >>> print versionesIterador.next()
    ('python', 2.7)
    >>> print versionesIterador.next()
    ('plone', 5.1)
    >>> print versionesIterador.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration


.. _python_dict_mtd_iterkeys:

iterkeys()
~~~~~~~~~~

Este método devuelve un iterador sobre las claves del diccionario. Lanza una 
excepción :ref:`StopIteration <python_exception_stopiteration>` si llega al final de 
la posición del **diccionario**.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> print versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> versiones.iterkeys()
    <dictionary-keyiterator object at 0x7fab9dd4bcb0>
    >>> for clave in versiones.iterkeys():
    ...     print clave
    ... 
    zope
    python
    plone
    >>> versionesIterador = versiones.iterkeys()
    >>> print versionesIterador.next()
    zope
    >>> print versionesIterador.next()
    python
    >>> print versionesIterador.next()
    plone
    >>> print versionesIterador.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration


.. _python_dict_mtd_itervalues:

itervalues()
~~~~~~~~~~~~

Este método devuelve un iterador sobre los valores del diccionario. Lanza una 
excepción :ref:`StopIteration <python_exception_stopiteration>` si llega al final de 
la posición del **diccionario**.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> print versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> versiones.itervalues()
    <dictionary-valueiterator object at 0x7fab9dd4bc58>
    >>> for valor in versiones.itervalues():
    ...     print valor
    ... 
    2.13
    2.7
    5.1
    >>> versionesIterador = versiones.itervalues()
    >>> print versionesIterador.next()
    2.13
    >>> print versionesIterador.next()
    2.7
    >>> print versionesIterador.next()
    5.1
    >>> print versionesIterador.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration


.. _python_dict_mtd_keys:

keys()
~~~~~~

Este método devuelve una lista de las claves del diccionario:

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones.keys()
    ['zope', 'python', 'plone']


.. _python_dict_mtd_pop:

pop()
~~~~~

Este método remueve específicamente una clave de **diccionario** y devuelve valor 
correspondiente. Lanza una excepción :ref:`KeyError <python_exception_keyerror>` 
si la **clave** no es encontrada.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> versiones.pop('zope')
    2.13
    >>> versiones
    {'python': 2.7, 'plone': 5.1}
    >>> versiones.pop('django')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'django'


.. _python_dict_mtd_popitem:

popitem()
~~~~~~~~~

Este método remueve y devuelve algún par (clave, valor) del **diccionario** como 
una 2 tuplas. Lanza una excepción :ref:`KeyError <python_exception_keyerror>` si 
el **diccionario** esta vació.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> versiones.popitem()
    ('zope', 2.13)
    >>> versiones
    {'python': 2.7, 'plone': 5.1}
    >>> versiones.popitem()
    ('python', 2.7)
    >>> versiones
    {'plone': 5.1}
    >>> versiones.popitem()
    ('plone', 5.1)
    >>> versiones
    {}
    >>> versiones.popitem()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'popitem(): dictionary is empty'


.. _python_dict_mtd_setdefault:

setdefault()
~~~~~~~~~~~~

Este método es similar a :ref:`get(key, default) <python_dict_mtd_get>`, pero además 
asigna la clave ``key`` al valor por ``default`` si no se encuentra en el diccionario.

::

    D.setdefault(key[,default])

Este método devuelve el valor producido por el método integrado 
:ref:`get() <python_dict_mtd_get>`, también define ``default`` para la clave del 
**diccionario** si la clave no esta en el diccionario.

.. todo:: TODO terminar de escribir la explicación del del método.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> versiones.setdefault('zope')
    2.13
    >>> versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}

.. todo:: TODO terminar de escribir un ejemplo de uso del método.


.. _python_dict_mtd_update:

update()
~~~~~~~~

Este método actualiza un **diccionario** desde un diccionario/iterable E y F. Si E 
esta presenta y tiene un método ``.keys()``, hace: ``for key in E: D[key] = E[key]``. 
Si E esta presenta y carece del método ``.keys()``, hace: ``for (key, value) in E: D[key] = value``.
En otro caso, esto es lo seguido por: ``for key in F: D[k] = F[key]``.

::

    D.update([E, ]**F) -> None.

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_values:

values()
~~~~~~~~

Este método devuelve una lista de los valores del diccionario:

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones.values()
    [2.13, 2.7, 5.1]


.. _python_dict_mtd_viewitems:

viewitems()
~~~~~~~~~~~

Este método devuelve un objeto como un conjunto mutable proveyendo una vista en los 
elementos del diccionario:

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones.viewkeys()
    dict_keys(['zope', 'python', 'plone'])
    >>> for clave,valor in versiones.iteritems():
    ...     print clave,valor
    ... 
    zope 2.13
    python 2.7
    plone 5.1


.. _python_dict_mtd_viewkeys:

viewkeys()
~~~~~~~~~~

Este método devuelve un objeto proveyendo una vista de las claves del **diccionario**.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones.viewkeys()
    dict_keys(['zope', 'python', 'plone'])
    >>> for clave in versiones.viewkeys():
    ...     print clave
    ... 
    zope
    python
    plone


.. _python_dict_mtd_viewvalues:

viewvalues()
~~~~~~~~~~~~

Este método devuelve un objeto proveyendo una vista de los valores del **diccionario**.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones.viewvalues()
    dict_values([2.13, 2.7, 5.1])
    >>> for valor in versiones.viewvalues():
    ...     print valor
    ... 
    2.13
    2.7
    5.1


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

**Ejemplo de definición de un diccionario**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :lines: 8-16

**Ejemplo de operaciones con tipo diccionario con funciones propias**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :lines: 22-24

**Ejemplo de iteración avanzada sobre diccionarios con función iteritems**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :lines: 29-30

**Ejemplo real de usar tipo diccionario**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :lines: 33-50


----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los **diccionarios** 
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

::

    >>> help(dict)


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_diccionarios.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_diccionarios.py`, abra una consola de comando, 
    acceda al directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    ::

        python tipo_diccionarios.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
