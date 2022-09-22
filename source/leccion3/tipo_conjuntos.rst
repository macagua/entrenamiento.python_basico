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

Este método agrega un elemento a un **conjunto mutable**. Esto no tiene efecto si el
elemento ya esta presente.

.. code-block:: pycon

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> print(set_mutable1)
    set([1, 2, 3, 4, 5, 7, 11])
    >>> set_mutable1.add(22)
    >>> print(set_mutable1)
    set([1, 2, 3, 4, 5, 7, 11, 22])


.. _python_set_mtd_clear:

clear()
~~~~~~~

Este método remueve todos los elementos desde este **conjunto mutable**.

.. code-block:: pycon

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> print(set_mutable1)
    set([1, 2, 3, 4, 5, 7, 11])
    >>> set_mutable1.clear()
    >>> print(set_mutable1)
    set([])


.. _python_set_mtd_copy:

copy()
~~~~~~

Este método devuelve una copia superficial del tipo **conjunto mutable** o
**conjunto inmutable**:

.. code-block:: pycon

    >>> set_mutable = set([4.0, "Carro", True])
    >>> otro_set_mutable = set_mutable.copy()
    >>> set_mutable == otro_set_mutable
    True


.. _python_set_mtd_difference:

difference()
~~~~~~~~~~~~

Este método devuelve la diferencia entre dos **conjunto mutable** o **conjunto inmutable**:
todos los elementos que están en el primero, pero no en el argumento.

.. code-block:: pycon

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> print(set_mutable1)
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print(set_mutable2)
    set([2, 4, 5, 8, 9, 11])
    >>> print(set_mutable1).difference(set_mutable2)
    set([1, 3, 7])
    >>> print(set_mutable2.difference(set_mutable1))
    set([8, 9])


.. _python_set_mtd_difference_update:

difference_update()
~~~~~~~~~~~~~~~~~~~

Este método actualiza un tipo **conjunto mutable** llamando al método
``difference_update()`` con la diferencia de los conjuntos.

.. code-block:: pycon

    >>> proyecto1 = {"python", "Zope", "ZODB3", "zope.pagetemplate"}
    >>> proyecto1
    set(['python', 'zope.pagetemplate', 'Zope', 'ZODB3'])
    >>> proyecto2 = {"python", "Plone", "plone.volto"}
    >>> proyecto2
    set(['python', 'plone.volto', 'Plone'])
    >>> proyecto1.difference_update(proyecto2)
    >>> proyecto1
    set(['zope.pagetemplate', 'Zope', 'ZODB3'])

Si ``proyecto1`` y ``proyecto2`` son dos conjuntos. La diferencia del conjunto
``proyecto1`` y conjunto ``proyecto2`` es un conjunto de elementos que existen
solamente en el conjunto ``proyecto1`` pero no en el conjunto ``proyecto2``.


.. _python_set_mtd_discard:

discard()
~~~~~~~~~

Este método remueve un elemento desde un **conjunto mutable** si esta presente.


.. code-block:: pycon

    >>> paquetes = {"python", "zope", "plone", "django"}
    >>> paquetes
    set(['python', 'zope', 'plone', 'django'])
    >>> paquetes.discard("django")
    >>> paquetes
    set(['python', 'zope', 'plone'])

El **conjunto mutable** permanece sin cambio si el elemento pasado como argumento
al método ``discard()`` no existe.

.. code-block:: pycon

    >>> paquetes = {"python", "zope", "plone", "django"}
    >>> paquetes.discard("php")
    >>> paquetes
    set(['python', 'zope', 'plone'])


.. _python_set_mtd_intersection:

intersection()
~~~~~~~~~~~~~~

Este método devuelve la intersección entre los **conjuntos mutables** o **conjuntos
inmutables**: todos los elementos que están en ambos.

.. code-block:: pycon

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> print(set_mutable1)
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print(set_mutable2)
    set([2, 4, 5, 8, 9, 11])
    >>> print(set_mutable1).intersection(set_mutable2)
    set([2, 11, 4, 5])
    >>> print(set_mutable2.intersection(set_mutable1))
    set([2, 11, 4, 5])


.. _python_set_mtd_intersection_update:

intersection_update()
~~~~~~~~~~~~~~~~~~~~~

Este método actualiza un **conjunto mutable** con la intersección de ese mismo y otro
**conjunto mutable**.

El método ``intersection_update()`` le permite arbitrariamente varios numero de
argumentos (conjuntos).

.. code-block:: pycon

    >>> proyecto1 = {"python", "Zope", "zope.pagetemplate"}
    >>> proyecto1
    set(['python', 'zope.pagetemplate', 'Zope'])
    >>> proyecto2 = {"python", "Plone", "plone.volto", "plone.restapi"}
    >>> proyecto2
    set(['python', 'plone.restapi', 'plone.volto', 'Plone'])
    >>> proyecto3 = {"python", "django", "django-filter"}
    >>> proyecto3
    set(['python', 'django-filter', 'django'])
    >>> proyecto3.intersection_update(proyecto1, proyecto2)
    >>> proyecto3
    set(['python'])

La intersección de dos o mas conjuntos es el conjunto de elemento el cual es común a
todos los conjuntos.


.. _python_set_mtd_isdisjoint:

isdisjoint()
~~~~~~~~~~~~

Este método devuelve el valor ``True`` si no hay elementos comunes entre los
**conjuntos mutables** o **conjuntos inmutables**.

.. code-block:: pycon

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> print(set_mutable1)
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print(set_mutable2)
    set([2, 4, 5, 8, 9, 11])
    >>> print(set_mutable1).isdisjoint(set_mutable2)


.. _python_set_mtd_issubset:

issubset()
~~~~~~~~~~

Este método devuelve el valor ``True`` si el **conjunto mutable** es un *subconjunto* del
**conjunto mutable** o del **conjunto inmutable** argumento.

.. code-block:: pycon

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> set_mutable3 = set([11, 5, 2, 4])
    >>> print(set_mutable1)
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print(set_mutable2)
    set([2, 4, 5, 8, 9, 11])
    >>> print(set_mutable3)
    set([2, 11, 4, 5])
    >>> print(set_mutable2.issubset(set_mutable1))
    False
    >>> print(set_mutable3.issubset(set_mutable1))
    True


.. _python_set_mtd_issuperset:

issuperset()
~~~~~~~~~~~~

Este método devuelve el valor ``True`` si el **conjunto mutable** o el **conjunto inmutable**
es un *superset* del **conjunto mutable** argumento.

.. code-block:: pycon

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> set_mutable3 = set([11, 5, 2, 4])
    >>> print(set_mutable1)
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print(set_mutable2)
    set([2, 4, 5, 8, 9, 11])
    >>> print(set_mutable3)
    set([2, 11, 4, 5])
    >>> print(set_mutable1).issuperset(set_mutable2)
    False
    >>> print(set_mutable1).issuperset(set_mutable3)
    True


.. _python_set_mtd_pop:

pop()
~~~~~

Este método remueve arbitrariamente y devuelve un elemento de **conjunto mutable**.
El método ``pop()`` no toma ningún argumento. Si el **conjunto mutable** esta vacío
se lanza una excepción :ref:`KeyError <python_exception_keyerror>`.

.. code-block:: pycon

    >>> paquetes = {"python", "zope", "plone", "django"}
    >>> paquetes
    set(['python', 'zope', 'plone', 'django'])
    >>> print("Valor aleatorio devuelto es:", paquetes.pop())
    Valor aleatorio devuelto es: python
    >>> paquetes
    set(['zope', 'plone', 'django'])
    >>> print("Valor aleatorio devuelto es:", paquetes.pop())
    Valor aleatorio devuelto es: zope
    >>> paquetes
    set(['plone', 'django'])
    >>> print("Valor aleatorio devuelto es:", paquetes.pop())
    Valor aleatorio devuelto es: plone
    >>> paquetes
    set(['django'])
    >>> print("Valor aleatorio devuelto es:", paquetes.pop())
    Valor aleatorio devuelto es: django
    >>> print("Valor aleatorio devuelto es:", paquetes.pop())
    Valor aleatorio devuelto es:
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'pop from an empty set'

Tenga en cuenta que usted podría obtener diferente salida devueltas usando el método
``pop()`` por que remueve aleatoriamente un elemento.


.. _python_set_mtd_remove:

remove()
~~~~~~~~

Este método busca y remueve un elemento de un **conjunto mutable**, si debe ser un
miembro.

.. code-block:: pycon

    >>> paquetes = {"python", "zope", "plone", "django"}
    >>> paquetes
    set(['python', 'zope', 'plone', 'django'])
    >>> paquetes.remove("django")
    >>> paquetes
    set(['python', 'zope', 'plone'])

Si el elemento no es existe en el **conjunto mutable**, lanza una excepción
:ref:`KeyError <python_exception_keyerror>`. Usted puede usar el método
:ref:`discard() <python_set_mtd_discard>` si usted no quiere este error. El
**conjunto mutable** permanece sin cambio si el elemento pasado al método ``discard()``
no existe.

Un conjunto es una colección desordenada de elementos. Si usted quiere remover
arbitrariamente elemento un conjunto, usted puede usar el método
:ref:`pop() <python_set_mtd_pop>`.


.. _python_set_mtd_symmetric_difference:

symmetric_difference()
~~~~~~~~~~~~~~~~~~~~~~

Este método devuelve todos los elementos que están en un **conjunto mutable** e
**conjunto inmutable** u otro, pero no en ambos.

.. code-block:: pycon

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> print(set_mutable1)
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print(set_mutable2)
    set([2, 4, 5, 8, 9, 11])
    >>> print(set_mutable1).symmetric_difference(set_mutable2)
    set([1, 3, 7, 8, 9])


.. _python_set_mtd_symmetric_difference_update:

symmetric_difference_update()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Este método actualiza un **conjunto mutable** llamando al método
``symmetric_difference_update()`` con los conjuntos de diferencia simétrica.

La diferencia simétrica de dos conjuntos es el conjunto de elementos que están en
cualquiera de los conjuntos pero no en ambos.

.. code-block:: pycon

    >>> proyecto1 = {"python", "plone", "django"}
    >>> proyecto1
    set(['python', 'plone', 'django'])
    >>> proyecto2 = {"django", "zope", "pyramid"}
    >>> proyecto2
    set(['zope', 'pyramid', 'django'])
    >>> proyecto1.symmetric_difference_update(proyecto2)
    >>> proyecto1
    set(['python', 'zope', 'pyramid', 'plone'])

El método ``symmetric_difference_update()`` toma un argumento simple de un tipo
**conjunto mutable**.

.. _python_set_mtd_union:

union()
~~~~~~~

Este método devuelve un **conjunto mutable** y **conjunto inmutable** con todos los
elementos que están en alguno de los **conjuntos mutables** y **conjuntos inmutables**.

.. code-block:: pycon

    >>> set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
    >>> set_mutable2 = set([11, 5, 9, 2, 4, 8])
    >>> print(set_mutable1)
    set([1, 2, 3, 4, 5, 7, 11])
    >>> print(set_mutable2)
    set([2, 4, 5, 8, 9, 11])
    >>> print(set_mutable1).union(set_mutable2)
    set([1, 2, 3, 4, 5, 7, 8, 9, 11])


.. _python_set_mtd_update:

update()
~~~~~~~~

Este método agrega elementos desde un **conjunto mutable** (pasando como un argumento)
un tipo :ref:`tupla <python_tuple>`, un tipo :ref:`lista <python_list>`, un tipo
:ref:`diccionario <python_dict>` o un tipo **conjunto mutable** llamado con el método
``update()``.

A continuación un ejemplo de agregar nuevos elementos un tipo **conjunto mutable**
usando otro tipo **conjunto mutable**:

.. code-block:: pycon

    >>> version_plone_dev = set([5.1, 6])
    >>> version_plone_dev
    set([5.1, 6])
    >>> versiones_plone = set([2.1, 2.5, 3.6, 4])
    >>> versiones_plone
    set([2.5, 3.6, 2.1, 4])
    >>> versiones_plone.update(version_plone_dev)
    >>> versiones_plone
    set([2.5, 3.6, 4, 6, 5.1, 2.1])

A continuación un ejemplo de agregar nuevos elementos un tipo **conjunto mutable**
usando otro tipo :ref:`cadena de caracteres <python_str>`:

.. code-block:: pycon

    >>> cadena = "abc"
    >>> cadena
    'abc'
    >>> conjunto = {1, 2}
    >>> conjunto.update(cadena)
    >>> conjunto
    set(['a', 1, 2, 'b', 'c'])

A continuación un ejemplo de agregar nuevos elementos un tipo **conjunto mutable**
usando otro tipo :ref:`diccionario <python_dict>`:

.. code-block:: pycon

    >>> diccionario = {"key": 1, 2: "lock"}
    >>> diccionario.viewitems()
    dict_items([(2, 'lock'), ('key', 1)])
    >>> conjunto = {"a", "b"}
    >>> conjunto.update(diccionario)
    >>> conjunto
    set(['a', 2, 'b', 'key'])


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
    :lines: 7-29


Conjuntos frozenset
~~~~~~~~~~~~~~~~~~~

A continuación, se presentan un ejemplo de conjuntos ``frozenset``:

.. code-block:: pycon

    >>> versiones_plone = frozenset([6, 2.1, 2.5, 3.6, 4, 5, 4, 2.5])
    >>> print(versiones_plone, type(versiones_plone))
    frozenset([2.5, 4, 5, 6, 2.1, 3.6]) <type 'frozenset'>

Los elementos de un set son únicos (sin repeticiones dentro del ``set``), y deben
ser objetos inmutables: números, cadenas de caracteres, tuplas y sets inmutables,
pero no listas ni sets mutables.


Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los **conjuntos set**
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

.. code-block:: pycon

    >>> help(set)

Usted puede consultar toda la documentación disponible sobre los **conjuntos frozenset**
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

.. code-block:: pycon

    >>> help(frozenset)

Para salir de esa ayuda presione la tecla :keys:`q`.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion3/tipo_conjuntos.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_conjuntos.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    .. code-block:: console

        python3 tipo_conjuntos.py


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
