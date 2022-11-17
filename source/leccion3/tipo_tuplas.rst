.. -*- coding: utf-8 -*-


.. _python_tuple:

Tipo tuplas
-----------

Las tuplas son objetos de tipo *secuencia*, específicamente es un tipo de dato
:ref:`lista <python_list>` inmutable. Esta no puede modificarse de ningún modo
después de su creación.

.. _python_tuple_mtds:

Métodos
.......

Son muy similares a las :ref:`listas <python_list>` y comparten varias de sus
funciones y métodos integrados, aunque su principal diferencia es que son inmutables.
El objeto de tipo *tupla* integra una serie de métodos integrados a continuación:


.. _python_tuple_mtd_count:

count()
~~~~~~~

Este método recibe un elemento como argumento, y cuenta la cantidad de veces que
aparece en la tupla.

.. code-block:: pycon

    >>> valores = ("Python", True, "Zope", 5)
    >>> print("True ->", valores.count(True))
    True -> 1
    >>> print("'Zope' ->", valores.count("Zope"))
    'Zope' -> 1
    >>> print("5 ->", valores.count(5))
    5 -> 1


.. _python_tuple_mtd_index:

index()
~~~~~~~

Comparte el mismo método :ref:`index() <python_list_mtd_index>` del tipo lista.
Este método recibe un elemento como argumento, y devuelve el índice de su primera
aparición en la tupla.

.. code-block:: pycon

    >>> valores = ("Python", True, "Zope", 5)
    >>> print(valores.index(True))
    1
    >>> print(valores.index(5))
    3

El método devuelve un excepción :ref:`ValueError <python_exception_valueerror>` si el
elemento no se encuentra en la tupla, o en el entorno definido.

.. code-block:: pycon

    >>> valores = ("Python", True, "Zope", 5)
    >>> print(valores.index(4))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: tuple.index(x): x not in tuple


Convertir a tuplas
..................

Para convertir a *tipos tuplas* debe usar la función :ref:`tuple() <python_fun_tuple>`,
la cual :ref:`está integrada <python_fun_builtins>` en el interprete Python.

.. tip::
    Para más información consulte las funciones integradas para
    :ref:`operaciones de secuencias <python_fun_builtins_secuencias>`.


.. _python_tuple_ejs:

Ejemplos
........

A continuación, se presentan algunos ejemplos de su uso:

**Definir simple de tupla**

.. literalinclude:: ../../recursos/leccion3/tipo_tuplas.py
    :language: python
    :lines: 7-7


**Definir tuplas anidadas**

.. literalinclude:: ../../recursos/leccion3/tipo_tuplas.py
    :language: python
    :lines: 10-10


**Operación asignar de valores de una tupla en variables**

.. literalinclude:: ../../recursos/leccion3/tipo_tuplas.py
    :language: python
    :lines: 13-13


**Cuidar seguimiento del número de la numeración**

Una tarea común es iterar sobre una secuencia mientras cuidas el seguimiento de la
numeración de un elemento.

Podría usar un bucle ``while`` con un contador o un bucle ``for`` usando la función
:ref:`range() <python_fun_range>` y la función :ref:`len() <python_fun_len>`:

.. code-block:: pycon

    >>> tecnologias = ("Zope", "Plone", "Pyramid")
    >>> for i in range(0, len(tecnologias)):
    ...     print(i, tecnologias[i])
    ...
    0 Zope
    1 Plone
    2 Pyramid

Pero, Python provee la palabra reservada ``enumerate`` para esto:

.. code-block:: pycon

    >>> tecnologias = ("Zope", "Plone", "Pyramid")
    >>> for contador, tecnologia in enumerate(tecnologias, start=1):
    ...     print(contador, tecnologia)
    ...
    1 Zope
    2 Plone
    3 Pyramid
    >>>


**Caso real de conexión a BD**

A continuación, un ejemplo más apegado a la realidad que busca establecer una conexión
a una BD:

.. literalinclude:: ../../recursos/leccion3/tipo_tuplas.py
    :language: python
    :lines: 18-43

Este script da como resultado el siguiente mensaje:

.. code-block:: console

    Definiendo conexión a BD MySQL
    ==============================

    Conexión típica: ('127.0.0.1', 'root', 'qwerty', 'nomina') <class 'tuple'>

    Conexión con parámetros adicionales: (('127.0.0.1', 'root', 'qwerty', 'nomina'), '3307', '10') <class 'tuple'> 

    IP de la BD: 127.0.0.1
    Usuario de la BD: root
    Contraseña de la BD: qwerty
    Nombre de la BD: nomina
    Puerto de conexión: 3307
    Tiempo de espera en conexión: 10

    Más información acerca de MySQL y Python http://mysql-python.sf.net/MySQLdb.html



Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre las **tuplas** desde la
:ref:`consola interactiva <python_interactivo>` de la siguiente forma:

.. code-block:: pycon

    >>> help(tuple)


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion3/tipo_tuplas.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_tuplas.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    .. code-block:: console

        python3 tipo_tuplas.py


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
