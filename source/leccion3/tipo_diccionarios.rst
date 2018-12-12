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
Mapeos son objetos mutable. El *diccionario* es el único tipo de mapeo estándar 
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

Un diccionario puede almacenar los diveros tipos de datos integrados en Python usando 
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

Esta método remueve todos los elementos desde el **diccionario**.

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> print versiones_plone
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> versiones_plone.clear()
    >>> print versiones_plone
    {}


.. _python_dict_mtd_copy:

copy()
~~~~~~

Esta método devuelve una copia (a shallow copy) del tipo **diccionario**:

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> otro_versiones_plone = versiones_plone.copy()
    >>> versiones_plone == otro_versiones_plone
    True


.. _python_dict_mtd_fromkeys:

fromkeys()
~~~~~~~~~~

Esta método 
dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
v defaults to None.

::

    >>>

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_get:

get()
~~~~~

Esta método devuelve el valor en base a una coincidencia de búsqueda en un diccionario 
mediante una clave, de lo contrario devuelve el objeto :ref:`None <python_obj_none>`. 

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone.get('plone')
    5.1
    >>> versiones_plone.get('php')
    >>>


.. _python_dict_mtd_has_key:

has_key()
~~~~~~~~~

Esta método devuelve el valor ``True`` si el diccionario tiene presente la clave enviada como argumento. 
D.has_key(k) -> True if D has a key k, else False

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone.has_key('plone')
    True


.. _python_dict_mtd_items:

items()
~~~~~~~

Esta método devuelve una lista de pares de diccionarios (clave, valor), como 2 tuplas:

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone.items()
    [('zope', 2.13), ('python', 2.7), ('plone', 5.1)]


.. _python_dict_mtd_iteritems:

iteritems()
~~~~~~~~~~~

Esta método devuelve un iterador sobre los elementos (clave, valor) del diccionario:

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone.iteritems()
    <dictionary-itemiterator object at 0x7fab9dd4bc58>

.. todo:: TODO terminar de escribir un ejemplo de uso del método.


.. _python_dict_mtd_iterkeys:

iterkeys()
~~~~~~~~~~

Esta método devuelve un iterador sobre las claves (keys) del diccionario:

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone.iterkeys()
    <dictionary-keyiterator object at 0x7fab9dd4bcb0>

.. todo:: TODO terminar de escribir un ejemplo de uso del método.


.. _python_dict_mtd_itervalues:

itervalues()
~~~~~~~~~~~~

Esta método devuelve un iterador sobre los valores (values) del diccionario:

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone.itervalues()
    <dictionary-valueiterator object at 0x7fab9dd4bc58>

.. todo:: TODO terminar de escribir un ejemplo de uso del método.


.. _python_dict_mtd_keys:

keys()
~~~~~~

Esta método devuelve una lista de las claves (keys) del diccionario:

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone.keys()
    ['zope', 'python', 'plone']


.. _python_dict_mtd_pop:

pop()
~~~~~

Esta método remueve específicamente una clave de **diccionario** y devuelve valor correspondiente.  
Lanza una excepción :ref:`KeyError <python_exception_keyerror>` si la **clave** no es encontrada.

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> versiones_plone.pop('zope')
    2.13
    >>> versiones_plone
    {'python': 2.7, 'plone': 5.1}
    >>> versiones_plone.pop('django')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'django'


.. _python_dict_mtd_popitem:

popitem()
~~~~~~~~~

Esta método remueve y devuelve algún par (clave, valor) del **diccionario** como una 2-tuple.
Lanza una excepción :ref:`KeyError <python_exception_keyerror>` si el **diccionario** esta vació.

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> versiones_plone.popitem()
    ('zope', 2.13)
    >>> versiones_plone
    {'python': 2.7, 'plone': 5.1}
    >>> versiones_plone.popitem()
    ('python', 2.7)
    >>> versiones_plone
    {'plone': 5.1}
    >>> versiones_plone.popitem()
    ('plone', 5.1)
    >>> versiones_plone
    {}
    >>> versiones_plone.popitem()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'popitem(): dictionary is empty'


.. _python_dict_mtd_setdefault:

setdefault()
~~~~~~~~~~~~

Esta método devuelve el valor producido por el método integrado ``get()``, también 
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D.

.. todo:: TODO terminar de escribir la explicación del del método.

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> versiones_plone.setdefault('zope')
    2.13
    >>> versiones_plone
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}

.. todo:: TODO terminar de escribir un ejemplo de uso del método.


.. _python_dict_mtd_update:

update()
~~~~~~~~

Esta método actualiza un **diccionario** desde un diccionario/iterable E y F.
Si E esta presenta y tiene un método ``.keys()``, hace:     for k in E: D[k] = E[k]
Si E esta presenta y lacks método ``.keys()``, hace:     for (k, v) in E: D[k] = v
En otro caso, esto es lo seguido por: for k in F: D[k] = F[k]

D.update([E, ]**F) -> None.

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_values:

values()
~~~~~~~~

Esta método devuelve una lista de los valores (values) del diccionario:

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone.values()
    [2.13, 2.7, 5.1]


.. _python_dict_mtd_viewitems:

viewitems()
~~~~~~~~~~~

Esta método devuelve un objeto como un conjunto mutable proveyendo una vista en los 
elementos del diccionario:

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone.viewitems()
    dict_items([('zope', 2.13), ('python', 2.7), ('plone', 5.1)])

.. todo:: TODO terminar de escribir un ejemplo de uso del método.


.. _python_dict_mtd_viewkeys:

viewkeys()
~~~~~~~~~~

Esta método 
D.viewkeys() -> a set-like object providing a view on D's keys

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone.viewkeys()
    dict_keys(['zope', 'python', 'plone'])

.. todo:: TODO terminar de escribir un ejemplo de uso del método.


.. _python_dict_mtd_viewvalues:

viewvalues()
~~~~~~~~~~~~

Esta método 
D.viewvalues() -> an object providing a view on D's values

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_plone.viewvalues()
    dict_values([2.13, 2.7, 5.1])

.. todo:: TODO terminar de escribir un ejemplo de uso del método.


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
