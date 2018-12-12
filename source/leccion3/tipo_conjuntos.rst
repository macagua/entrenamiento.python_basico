.. -*- coding: utf-8 -*-


.. _python_set:

Tipo conjuntos
--------------

Un conjunto, es una colección no ordenada y sin elementos repetidos. Los usos básicos 
de éstos incluyen verificación de pertenencia y eliminación de entradas duplicadas.

+---------------+-----------+-------------------------+-------------------------------------+
| **Clase**     | **Tipo**  | **Notas**               | **Ejemplo**                         |
+---------------+-----------+-------------------------+-------------------------------------+
| ``set``       | Conjuntos | Mutable, sin orden, no  | ``set([4.0, 'Carro', True])``       |
|               |           | contiene duplicados.    |                                     |
+---------------+-----------+-------------------------+-------------------------------------+
| ``frozenset`` | Conjuntos | Inmutable, sin orden,   | ``frozenset([4.0, 'Carro', True])`` |
|               |           | no contiene duplicados. |                                     |
+---------------+-----------+-------------------------+-------------------------------------+


.. _python_set_mtds:

Métodos
.......

Los objetos de tipo **conjunto mutable** y **conjunto inmutable** integra una serie de 
métodos integrados a continuación:


.. _python_set_mtd_add:

add()
~~~~~

Esta método agrega un elemento a un **conjunto mutable**. Esto no tiene efecto si el 
elemento ya esta presente.

::

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> print set_mutable1
    set([1, 2, 3, 4, 5, 7, 11])
    >>> set_mutable1.add(22)
    >>> print set_mutable1
    set([1, 2, 3, 4, 5, 7, 11, 22])


.. _python_set_mtd_clear:

clear()
~~~~~~~

Esta método remueve todos los elementos desde este **conjunto mutable**.

::

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> print set_mutable1
    set([1, 2, 3, 4, 5, 7, 11])
    >>> set_mutable1.clear()
    >>> print set_mutable1
    set([])


.. _python_set_mtd_copy:

copy()
~~~~~~

Esta método devuelve una copia (a shallow copy) del tipo **conjunto mutable** o 
**conjunto inmutable**:

::

    >>> set_mutable = set([4.0, 'Carro', True])
    >>> otro_set_mutable = set_mutable.copy()
    >>> set_mutable == otro_set_mutable
    True


.. _python_set_mtd_difference:

difference()
~~~~~~~~~~~~

Esta método devuelve la diferencia entre dos **conjunto mutable** o **conjunto inmutable**: 
todos los elementos que están en el primero, pero no en el argumento.

::

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> print set_mutable1
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print set_mutable2
    set([2, 4, 5, 8, 9, 11])
    >>> print set_mutable1.difference(set_mutable2)
    set([1, 3, 7])
    >>> print set_mutable2.difference(set_mutable1)
    set([8, 9])


.. _python_set_mtd_difference_update:

difference_update()
~~~~~~~~~~~~~~~~~~~

Esta método remueve todos los elementos de otro **conjunto mutable** desde este 
**conjunto mutable**.

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_set_mtd_discard:

discard()
~~~~~~~~~

Esta método remueve un elemento desde un **conjunto mutable** si ese es un miembro. 
Si el elemento no es miembro, no hacer nada.


::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_set_mtd_intersection:

intersection()
~~~~~~~~~~~~~~

Esta método devuelve la intersección entre los **conjuntos mutables** o **conjuntos 
inmutables**: todos los elementos que están en ambos.

::

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> print set_mutable1
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print set_mutable2
    set([2, 4, 5, 8, 9, 11])
    >>> print set_mutable1.intersection(set_mutable2)
    set([2, 11, 4, 5])
    >>> print set_mutable2.intersection(set_mutable1)
    set([2, 11, 4, 5])


.. _python_set_mtd_intersection_update:

intersection_update()
~~~~~~~~~~~~~~~~~~~~~

Esta método actualiza un **conjunto mutable** con la intersección de ese mismo y otro.

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.



.. _python_set_mtd_isdisjoint:

isdisjoint()
~~~~~~~~~~~~

Esta método devuelve el valor ``True`` si no hay elementos comunes entre los 
**conjuntos mutables** o **conjuntos inmutables**.

::

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> print set_mutable1
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print set_mutable2
    set([2, 4, 5, 8, 9, 11])
    >>> print set_mutable1.isdisjoint(set_mutable2)


.. _python_set_mtd_issubset:

issubset()
~~~~~~~~~~

Esta método devuelve el valor ``True`` si el **conjunto mutable** es un *subconjunto* del 
**conjunto mutable** o del **conjunto inmutable** argumento.

::

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> set_mutable3 = set([11, 5, 2, 4])
    >>> print set_mutable1
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print set_mutable2
    set([2, 4, 5, 8, 9, 11])
    >>> print set_mutable3
    set([2, 11, 4, 5])
    >>> print set_mutable2.issubset(set_mutable1)
    False
    >>> print set_mutable3.issubset(set_mutable1)
    True


.. _python_set_mtd_issuperset:

issuperset()
~~~~~~~~~~~~

Esta método devuelve el valor ``True`` si el **conjunto mutable** o el **conjunto inmutable** 
es un *superset* del **conjunto mutable** argumento.

::

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> set_mutable3 = set([11, 5, 2, 4])
    >>> print set_mutable1
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print set_mutable2
    set([2, 4, 5, 8, 9, 11])
    >>> print set_mutable3
    set([2, 11, 4, 5])
    >>> print set_mutable1.issuperset(set_mutable2)
    False
    >>> print set_mutable1.issuperset(set_mutable3)
    True


.. _python_set_mtd_pop:

pop()
~~~~~

Esta método remueve y devuelve un elemento de **conjunto mutable** arbitrariamente. 
Lanza una excepción :ref:`KeyError <python_exception_keyerror>` si el **conjunto 
mutable** es vacío.

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_set_mtd_remove:

remove()
~~~~~~~~

Esta método remueve un elemento de un **conjunto mutable**, si debe ser un miembro. 
Si el elemento no es miembro, lanza una excepción :ref:`KeyError <python_exception_keyerror>`.

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_set_mtd_symmetric_difference:

symmetric_difference()
~~~~~~~~~~~~~~~~~~~~~~

Esta método devuelve todos los elementos que están en un **conjunto mutable** e 
**conjunto inmutable** u otro, pero no en ambos.

::

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> print set_mutable1
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print set_mutable2
    set([2, 4, 5, 8, 9, 11])
    >>> print set_mutable1.symmetric_difference(set_mutable2)
    set([1, 3, 7, 8, 9])


.. _python_set_mtd_symmetric_difference_update:

symmetric_difference_update()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Esta método actualiza un **conjunto mutable** con diferencia simétrica de ese mismo 
y otro.

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_set_mtd_union:

union()
~~~~~~~

Esta método devuelve un **conjunto mutable** y **conjunto inmutable** con todos los 
elementos que están en alguno de los **conjuntos mutables** y **conjuntos inmutables**.

::

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> print set_mutable1
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print set_mutable2
    set([2, 4, 5, 8, 9, 11])
    >>> print set_mutable1.union(set_mutable2)
    set([1, 2, 3, 4, 5, 7, 8, 9, 11])


.. _python_set_mtd_update:

update()
~~~~~~~~

Esta método actualiza un **conjunto mutable** con la unión de si mismo y otros.

::

    >>> 

.. todo:: TODO terminar de escribir sobre este método integrado.


.. _python_set_convertir:

Convertir a conjuntos
.....................

Para convertir a *tipos conjuntos* debe usar las funciones :ref:`set() <python_fun_set>` 
y :ref:`frozenset() <python_fun_frozenset>`, las cuales 
:ref:`están integradas <python_fun_builtins>` en el interprete Python.

.. tip:: 
    Para más información consulte las funciones integradas para 
    :ref:`operaciones de secuencias <python_fun_builtins_secuencias>`.


.. _python_set_ejs:

Ejemplos
........


Conjuntos set
~~~~~~~~~~~~~

A continuación, se presentan un ejemplo de conjuntos ``set``:

.. literalinclude:: ../../recursos/leccion3/tipo_conjuntos.py
    :language: python
    :lines: 9-38


Conjuntos frozenset
~~~~~~~~~~~~~~~~~~~

A continuación, se presentan un ejemplo de conjuntos ``frozenset``:

::

    >>> inmutable = frozenset([1, 2, 3, 2, 1, 4, 5, 3])
    >>> print inmutable, type(inmutable)
    frozenset([1, 2, 3, 4, 5]) <type 'frozenset'>

Los elementos de un set son únicos (sin repeticiones dentro del ``set``), y deben 
ser objetos inmutables: números, cadenas de caracteres, tuplas y sets inmutables, 
pero no listas ni sets mutables.


----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los **conjuntos set** 
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

::

    >>> help(set)

Usted puede consultar toda la documentación disponible sobre los **conjuntos frozenset** 
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

::

    >>> help(frozenset)

Para salir de esa ayuda presione la tecla ``q``.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_conjuntos.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_conjuntos.py`, abra una consola de comando, 
    acceda al directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    ::

        python tipo_conjuntos.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
