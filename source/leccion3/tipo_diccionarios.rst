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

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
    >>> versiones['zope']
    2.13


.. _python_dict_opers_setv:

Asignar valor a clave
~~~~~~~~~~~~~~~~~~~~~

Esta operación le permite asignar el valor especifico del *diccionario* mediante su 
clave.

::

    >>> versiones = {'python': 2.7, 'zope': 2.13, 'plone': None}
    >>> versiones['plone']
    >>> versiones['plone'] = 5.1
    >>> versiones
    {'python': 2.7, 'zope': 2.13, 'plone': 5.1}
    >>> versiones['plone']
    5.1


.. _python_dict_opers_in:

Iteración in
~~~~~~~~~~~~

Este operador es el mismo operador integrado :ref:`in <python_opers_in>` en el 
interprete Python pero aplicada al uso de la secuencia de tipo **diccionario**.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
    >>> print versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1, 'django': 2.1}
    >>> 'plone' in versiones
    True
    >>> 'flask' in versiones
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

Este método crea un nuevo **diccionario** con *claves* a partir de un tipo de dato 
*secuencia*. El valor de ``value`` por defecto es el tipo :ref:`None <python_obj_none>`.

::

    >>> secuencia = ('python', 'zope', 'plone')
    >>> versiones = dict.fromkeys(secuencia)
    >>> print "Nuevo Diccionario : %s" %  str(versiones)
    Nuevo Diccionario : {'python': None, 'zope': None, 'plone': None}

En el ejemplo anterior inicializa los valores de cada clave a ``None``, mas puede 
inicializar un *valor* común por defecto para cada *clave*:

::

    >>> versiones = dict.fromkeys(secuencia, 0.1)
    >>> print "Nuevo Diccionario : %s" %  str(versiones)
    Nuevo Diccionario : {'python': 0.1, 'zope': 0.1, 'plone': 0.1}


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
enviada como argumento.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones.has_key('plone')
    True
    >>> versiones.has_key('django')
    False


.. _python_dict_mtd_items:

items()
~~~~~~~

Este método devuelve una lista de pares de diccionarios (clave, valor), como 2 tuplas.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones.items()
    [('zope', 2.13), ('python', 2.7), ('plone', 5.1)]


.. _python_dict_mtd_iteritems:

iteritems()
~~~~~~~~~~~

Este método devuelve un :ref:`iterador <python_iter>` sobre los elementos (clave, valor) 
del diccionario. Lanza una excepción :ref:`StopIteration <python_exception_stopiteration>` 
si llega al final de la posición del **diccionario**.

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

Este método devuelve un :ref:`iterador <python_iter>` sobre las claves del diccionario. 
Lanza una excepción :ref:`StopIteration <python_exception_stopiteration>` si llega al 
final de la posición del **diccionario**.

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

Este método devuelve un :ref:`iterador <python_iter>` sobre los valores del diccionario. 
Lanza una excepción :ref:`StopIteration <python_exception_stopiteration>` si llega al 
final de la posición del **diccionario**.

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

Este método es similar a :ref:`get(key, default_value) <python_dict_mtd_get>`, pero además 
asigna la clave ``key`` al valor por ``default_value`` para la clave si esta no se encuentra 
en el **diccionario**.

::

    D.setdefault(key[,default_value])

A continuación un ejemplo de como trabaja el método ``setdefault()`` cuando la clave 
esta en el diccionario:

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> zope = versiones.setdefault('zope')
    >>> print 'Versiones instaladas:', versiones
    Versiones instaladas: {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> print 'Versión de Zope:', zope
    Versión de Zope: 2.13

A continuación un ejemplo de como trabaja el método ``setdefault()`` la clave no esta 
en el diccionario:

::

    >>> paquetes = {'python': 2.7, 'zope': 2.13}
    >>> print paquetes
    {'python': 2.7, 'zope': 2.13}
    >>> plone = paquetes.setdefault('plone')
    >>> print 'paquetes: ', paquetes
    paquetes:  {'python': 2.7, 'zope': 2.13, 'plone': None}
    >>> print 'plone: ', plone
    plone:  None

Si el valor no es proveído, el valor ``default_value`` será el tipo objeto integrado
:ref:`None <python_obj_none>`. 

A continuación un ejemplo de como trabaja el método ``setdefault()`` la clave no esta 
en el diccionario pero esta vez el ``default_value`` es proveído:

::

    >>> pkgs = {'python': 2.7, 'zope': 2.13, 'plone': None}
    >>> print pkgs
    {'python': 2.7, 'zope': 2.13, 'plone': None}
    >>> django = paquetes.setdefault('django', 2.1)
    >>> print 'paquetes =', pkgs
    paquetes = {'python': 2.7, 'zope': 2.13, 'plone': None}
    >>> print 'django =', django
    django = 2.1

A continuación otro ejemplo en donde puedes agrupar N :ref:`tuplas <python_tuple>` 
por el valor el cual se repite más y construir un diccionario que cuyas claves son 
los valores mas repetidos y cuyos valores este agrupados en tipo 
:ref:`listas <python_list>`:

::

    >>> PKGS = (('zope', 'Zope2'),
    ...        ('zope', 'pytz'),
    ...        ('plone', 'Plone'),
    ...        ('plone', 'diazo'),
    ...        ('plone', 'z3c.form'),)
    >>> 
    >>> paquetes = {}
    >>> for clave, valor in PKGS:
    ...     if paquetes.has_key(clave):
    ...         paquetes[clave].append(valor)
    ...     else:
    ...         paquetes[clave] = [valor]
    ... 
    >>> print paquetes
    {'zope': ['Zope2', 'pytz'], 'plone': ['Plone', 'diazo', 'z3c.form']}

En el tipo tupla ``PKGS`` los elementos mas repetidos son ``'zope'`` y ``'plone'`` 
estos se convierten en clave del diccionario ``paquetes`` y los otros elementos se 
agrepan en listas como sus respectivos valores. 

A continuación un mejor aprovechamiento implementando el método ``setdefault()``:

::

    >>> PKGS = (('zope', 'Zope2'),
    ...        ('zope', 'pytz'),
    ...        ('plone', 'Plone'),
    ...        ('plone', 'diazo'),
    ...        ('plone', 'z3c.form'),)
    >>> paquetes = {}
    >>> for clave, valor in PKGS:
    ...     paquetes.setdefault(clave, []).append(valor)
    ... 
    >>> print paquetes
    {'zope': ['Zope2', 'pytz'], 'plone': ['Plone', 'diazo', 'z3c.form']}

En el ejemplo anterior puede ver que el aprovechamiento del método ``setdefault()`` 
a comparación de no usar el respectivo método.


.. _python_dict_mtd_update:

update()
~~~~~~~~

Este método actualiza un **diccionario** agregando los pares clave-valores en un 
segundo diccionario. Este método no devuelve nada.

El método ``update()`` toma un diccionario o un objeto iterable de pares clave/valor 
(generalmente tuplas). Si se llama a ``update()`` sin pasar parámetros, el diccionario 
permanece sin cambios.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
    >>> print versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}
    >>> versiones_adicional = dict(django=2.1)
    >>> print versiones_adicional
    {'django': 2.1}
    >>> versiones.update(versiones_adicional)

Como puede apreciar este método no devuelve nada, más si muestra de nuevo el diccionario 
``versiones`` puede ver que este fue actualizado con el otro diccionario 
``versiones_adicional``.

::

    >>> print versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1, 'django': 2.1}


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


.. _python_dict_fun:

Funciones
.........

Los objetos de tipo **diccionario** tienen disponibles una serie de *funciones* 
integradas en el interprete Python para su tratamiento, a continuación algunas 
de estas:

.. _python_dict_fun_cmp:

cmp()
~~~~~

Esta función es la misma función integrada :ref:`cmp() <python_fun_cmp>` en el 
interprete Python pero aplicada al uso de la secuencia de tipo **diccionario**.

::

    >>> versiones_proyecto1 = dict(python=2.7, zope=2.13, plone=5.1)
    >>> versiones_proyecto2 = dict(django=2.1, django-filter=1.1.0)
    >>> print cmp(versiones_proyecto1, versiones_proyecto2)
    1

La función ``cmp()`` es usado en Python para comparar valores y claves de dos 
diccionarios. Si la función devuelve el valor ``0`` si ambos diccionarios son 
igual, devuelve el valor ``1`` si el primer diccionario es mayor que el segundo 
diccionario y devuelve el valor ``-1`` si el primer diccionario es menor que el 
segundo diccionario.


.. _python_dict_fun_len:

len()
~~~~~

Esta función es la misma función integrada :ref:`len() <python_fun_len>` en el 
interprete Python pero aplicada al uso de la secuencia de tipo **diccionario**.

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1)
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

::

    >>> versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
    >>> print versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1, 'django': 2.1}
    >>> del versiones['django']
    >>> print versiones
    {'zope': 2.13, 'python': 2.7, 'plone': 5.1}

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

**Ejemplo de definir un diccionario**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :lines: 4-12

**Ejemplo de operaciones con tipo diccionario con funciones propias**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :lines: 18-20

**Ejemplo de iteración avanzada sobre diccionarios con función iteritems**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :lines: 25-26

**Ejemplo real de usar tipo diccionario**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :lines: 29-46


Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los **diccionarios** 
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

::

    >>> help(dict)


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_diccionarios.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_diccionarios.py`, abra una consola de comando, 
    acceda al directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    ::

        python tipo_diccionarios.py


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
