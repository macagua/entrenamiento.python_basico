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

    >>> versiones_plone = dict(python=2.7, zope=2, plone=5.1)
    >>> print versiones_plone
    {'zope': 2, 'python': 2.7, 'plone': 5.1}
    >>> versiones_plone.clear()
    >>> print versiones_plone
    {}


.. _python_dict_mtd_copy:

copy()
~~~~~~

Esta método devuelve una copia (a shallow copy) del tipo **diccionario**:

::

    >>> versiones_plone = dict(python=2.7, zope=2, plone=5.1)
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

Esta método 
D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

::

    >>>

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_has_key:

has_key()
~~~~~~~~~

Esta método 
D.has_key(k) -> True if D has a key k, else False

::

    >>>

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_items:

items()
~~~~~~~

Esta método 
D.items() -> list of D's (key, value) pairs, as 2-tuples

::

    >>>

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_iteritems:

iteritems()
~~~~~~~~~~~

Esta método 
D.iteritems() -> an iterator over the (key, value) items of D

::

    >>>

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_iterkeys:

iterkeys()
~~~~~~~~~~

Esta método 
D.iterkeys() -> an iterator over the keys of D

::

    >>>

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_itervalues:

itervalues()
~~~~~~~~~~

Esta método 
D.itervalues() -> an iterator over the values of D

::

    >>>

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_keys:

keys()
~~~~~~

Esta método 
D.keys() -> list of D's keys

::

    >>>

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_pop:

pop()
~~~~~

Esta método remueve y devuelve un elemento de **diccionario** arbitrariamente. 
Lanza una excepción :ref:`KeyError <python_exception_keyerror>` si el **conjunto 
mutable** es vacío.

D.pop(k[,d]) -> v, remove specified key and return the corresponding value. If key is not found, d is returned if given, otherwise KeyError is raised

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_popitem:

popitem()
~~~~~~~~~

Esta método 
D.popitem() -> (k, v), remove and return some (key, value) pair as a 2-tuple; but raise KeyError if D is empty.

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_setdefault:

setdefault()
~~~~~~~~~~~~

Esta método 
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D.

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_update:

update()
~~~~~~~~

Esta método actualiza un **diccionario** desde un diccionario/iterable E y F.
D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k in F: D[k] = F[k]

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_values:

values()
~~~~~~~~

Esta método 
D.values() -> list of D's values

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_viewitems:

viewitems()
~~~~~~~~~~~

Esta método 
D.viewitems() -> a set-like object providing a view on D's items

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_viewkeys:

viewkeys()
~~~~~~~~~~

Esta método 
D.viewkeys() -> a set-like object providing a view on D's keys

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_dict_mtd_viewvalues:

viewvalues()
~~~~~~~~~~~~

Esta método 
D.viewvalues() -> an object providing a view on D's values

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


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
