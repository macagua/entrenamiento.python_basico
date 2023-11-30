.. -*- coding: utf-8 -*-


.. _python_iter:

Iteradores
----------

Para entender los la filosofía de los *Iteradores*, busca la *simplicidad* de las
operaciones, evitando la duplicación del esfuerzo, el cual es un derroche y busca
reemplazar varios de los enfoques propios con una característica estándar, normalmente,
deriva en hacer las cosas más legibles además de más interoperable.

  *Guido van Rossum* --- `Añadiendo tipado estático opcional a Python`
  (`Adding Optional Static Typing to Python <https://www.artima.com/weblogs/viewpost.jsp?thread=86641>`_).

Un iterador es un objeto adherido al `iterator protocol`_, básicamente esto significa
que tiene una función :ref:`next() <python_fun_next>`, es decir, cuando se le llama,
devuelve la siguiente elemento en la secuencia, cuando no queda nada para ser devuelto,
lanza la excepción :ref:`StopIteration <python_exception_stopiteration>` y se causa el
detener la iteración. Pero si se llama de forma explícita puede ver que, una vez que el
iterador esté *agotado*, al llamarlo nuevamente verá que se lanza la excepción comentada
anteriormente.

A continuación el uso de iteradores usando del método especial ``__iter__()`` incluido
en el *objeto integrado* :ref:`file <python_cls_file>`:

.. code-block:: pycon

    >>> archivo = open("/etc/issue")
    >>> archivo
    <_io.TextIOWrapper name='/etc/issue' mode='r' encoding='UTF-8'>
    >>> archivo.__iter__()
    <_io.TextIOWrapper name='/etc/issue' mode='r' encoding='UTF-8'>
    >>> iter(archivo)
    <_io.TextIOWrapper name='/etc/issue' mode='r' encoding='UTF-8'>
    >>> archivo_iter = iter(archivo)
    >>> archivo is archivo.__iter__()
    True
    >>> print(next(archivo_iter))
    Ubuntu 20.04.5 LTS \n \l

    >>> print(next(archivo_iter))


    >>> print(next(archivo_iter))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

.. note::
  En el ejemplo, el método especial ``__iter__()``, hace lo mismo que la
  función integrada :ref:`iter(archivo) <python_fun_iter>`.


Iteradores y secuencias
.......................

Los *iteradores* se usan con los tipos de secuencias estándar. A continuación,
se describen algunos ejemplos:

**Iterar sobre la secuencia inmutable cadena de carácter**

A continuación, un ejemplo del uso de los iteradores con la secuencia *inmutable* de
tipo :ref:`cadena de caracteres <python_str>` ``ASCII``:

.. code-block:: pycon

    >>> frase = "Hola Mundo"
    >>> letra = iter(frase)
    >>> print(next(letra))
    H
    >>> print(next(letra))
    o
    >>> print(next(letra))
    l
    >>> print(next(letra))
    a
    >>> print(next(letra))

    >>> print(next(letra))
    M
    >>> print(next(letra))
    u
    >>> print(next(letra))
    n
    >>> print(next(letra))
    d
    >>> print(next(letra))
    o
    >>> print(next(letra))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

.. note::
  En el ejemplo anterior, cuando se itera en la secuencia ``frase``, al
  llegar al final mediante el iterador ``letra`` se llama a la excepción
  :ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la
  iteración.

**Iterar sobre la secuencia inmutable tupla**

A continuación, un ejemplo del uso de los iteradores con la secuencia *inmutable* de
tipo :ref:`tupla <python_tuple>`:

.. code-block:: pycon

    >>> valores = ("Python", True, "Zope", 5)
    >>> valores
    ('Python', True, "Zope", 5)
    >>> valores.__iter__()
    <tupleiterator object at 0x7fa44b9fa450>
    >>> valor = valores.__iter__()
    >>> print(next(valor))
    'Python'
    >>> print(next(valor))
    True
    >>> print(next(valor))
    'Zope'
    >>> print(next(valor))
    5
    >>> print(next(valor))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

.. note::
  En el ejemplo anterior, cuando se itera en la secuencia ``valores``, al llegar al
  final mediante el iterador ``valor`` se llama a la excepción
  :ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la
  iteración.

**Iterar sobre la función inmutable range**

A continuación, un ejemplo del uso de los iteradores con la secuencia *inmutable*
con la función integrada :ref:`range() <python_fun_range>`:

.. code-block:: pycon

    >>> lista = iter(range(5))
    >>> lista
    <range_iterator object at 0x7f792c5c0180>
    >>> print(next(lista))
    0
    >>> print(next(lista))
    1
    >>> print(next(lista))
    2
    >>> print(next(lista))
    3
    >>> print(next(lista))
    4
    >>> print(next(lista))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

.. note::
  En el ejemplo anterior, cuando se itera en la secuencia ``lista``, al llegar
  al final se llama a la excepción :ref:`StopIteration <python_exception_stopiteration>`
  y se causa el detener la iteración.

**Iterar sobre la secuencia mutable lista**

A continuación, un ejemplo del uso de los iteradores con la secuencia *mutable* de
tipo :ref:`lista <python_list>`:

.. code-block:: pycon

    >>> versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
    >>> iter(versiones_plone)
    <list_iterator object at 0x7f792c5ebcd0>
    >>> version = iter(versiones_plone)
    >>> version
    <list_iterator object at 0x7f792c5c0280>
    >>> print(next(version))
    2.1
    >>> print(next(version))
    2.5
    >>> print(next(version))
    3.6
    >>> print(next(version))
    4
    >>> print(next(version))
    5
    >>> print(next(version))
    6
    >>> print(next(version))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

.. note::
  En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al
  llegar al final mediante el iterador ``version`` se llama a la excepción
  :ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la
  iteración.

Usted puede devolver un objeto iterador en orden inverso sobre una secuencia *mutable* de
tipo :ref:`lista <python_list>` usando su función integrada ``__reversed__()``.

.. code-block:: pycon

    >>> versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
    >>> versiones_plone.__reversed__()
    <list_reverseiterator object at 0x7f792c5ebe20>
    >>> version = versiones_plone.__reversed__()
    >>> print(next(version))
    6
    >>> print(next(version))
    5
    >>> print(next(version))
    4
    >>> print(next(version))
    3.6
    >>> print(next(version))
    2.5
    >>> print(next(version))
    2.1
    >>> print(next(version))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

.. note::
  En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al
  llegar al final mediante el iterador ``version`` se llama a la excepción
  :ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la
  iteración.

También puede acceder al uso del método especial ``__iter__()`` incluido en la
secuencia *mutable* del tipo integrado :ref:`lista <python_list>`:

.. code-block:: pycon

    >>> versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
    >>> versiones_plone.__iter__()
    <list_iterator object at 0x7f792c5ebdf0>

**Iterar sobre la función mutable range**

A continuación, un ejemplo del uso de los iteradores con la secuencia *mutable*
de la función integrada :ref:`range() <python_fun_range>`:

.. code-block:: pycon

    >>> lista = iter(range(5))
    >>> lista
    <range_iterator object at 0x7f792c5ebf00>
    >>> print(next(lista))
    0
    >>> print(next(lista))
    1
    >>> print(next(lista))
    2
    >>> print(next(lista))
    3
    >>> print(next(lista))
    4
    >>> print(next(lista))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

.. note::
  En el ejemplo anterior, cuando se itera en la secuencia ``lista``, al llegar
  al final se llama a la excepción :ref:`StopIteration <python_exception_stopiteration>`
  y se causa el detener la iteración.


Iteradores y conjuntos
......................

Los *iteradores* se usan con los tipos de conjuntos estándar. A continuación,
se describen algunos ejemplos:

**Iterar sobre el conjunto mutable**

A continuación, un ejemplo del uso de los iteradores con el conjunto *mutable* de
tipo :ref:`conjuntos <python_set>`:

.. code-block:: pycon

    >>> versiones_plone = set([2.1, 2.5, 3.6, 4, 5, 6, 4])
    >>> version = iter(versiones_plone)
    >>> version
    <set_iterator object at 0x7f792c5985c0>
    >>> print(next(version))
    2.5
    >>> print(next(version))
    4
    >>> print(next(version))
    5
    >>> print(next(version))
    6
    >>> print(next(version))
    2.1
    >>> print(next(version))
    3.6
    >>> print(next(version))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

.. note::
  En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al
  llegar al final mediante el iterador ``version`` se llama a la excepción
  :ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la
  iteración.

**Iterar sobre el conjunto inmutable**

A continuación, un ejemplo del uso de los iteradores con el conjunto *inmutable* de
tipo :ref:`conjuntos <python_set>`:

.. code-block:: pycon

    >>> versiones_plone = frozenset([6, 2.1, 2.5, 3.6, 4, 5, 4, 2.5])
    >>> version = iter(versiones_plone)
    >>> version
    <set_iterator object at 0x7f792c598500>
    >>> print(next(version))
    2.1
    >>> print(next(version))
    3.6
    >>> print(next(version))
    2.5
    >>> print(next(version))
    4
    >>> print(next(version))
    6
    >>> print(next(version))
    5
    >>> print(next(version))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

.. note::
  En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al
  llegar al final mediante el iterador ``version`` se llama a la excepción
  :ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la
  iteración.


Iteradores y mapeos
...................

Los *iteradores* se usan con los tipos de secuencias estándar. A continuación,
se describen algunos ejemplos:

**Iterar sobre las claves del diccionario**

A continuación, un ejemplo del uso de los iteradores con la secuencia de *mapeo*,
tipo :ref:`diccionario <python_dict>`, por defecto muestra la clave de la secuencia:

.. code-block:: pycon

    >>> versiones_plone = dict(python=3.11, zope=5.2, plone=6.0)
    >>> paquete = iter(versiones_plone)
    >>> paquete
    <dict_keyiterator object at 0x7f792c68ff40>
    >>> print(next(paquete))
    zope
    >>> print(next(paquete))
    python
    >>> print(next(paquete))
    plone
    >>> print(next(paquete))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

.. note::
  En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al
  llegar al final mediante el iterador ``paquete`` se llama a la excepción
  :ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la
  iteración.

**Iterar sobre los valores del diccionario**

A continuación, un ejemplo del uso de los iteradores con la secuencia de *mapeo*,
tipo :ref:`diccionario <python_dict>` para mostrar el valor de una clave usando el
método integrado :ref:`values() <python_dict_mtd_values>`:

.. code-block:: pycon

    >>> versiones_plone = dict(python=3.11, zope=5.2, plone=6.0)
    >>> version = iter(versiones_plone.values())
    >>> version
    <dict_valueiterator object at 0x7f792c59ee50>
    >>> print(next(version))
    5.2
    >>> print(next(version))
    3.11
    >>> print(next(version))
    6.0
    >>> print(next(version))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

.. note::
  En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al
  llegar al final mediante el iterador ``version`` se llama a la excepción
  :ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la
  iteración.

**Iterar sobre los elementos del diccionario**

A continuación, un ejemplo del uso de los iteradores con la secuencia de *mapeo*,
tipo :ref:`diccionario <python_dict>` para mostrar el par clave/valor usando el
método integrado :ref:`items() <python_dict_mtd_items>`:

.. code-block:: pycon

    >>> versiones_plone = dict(python=3.11, zope=5.2, plone=6.0)
    >>> paquete = iter(versiones_plone.items())
    >>> paquete
    <dict_itemiterator object at 0x7f792c59ee50>
    >>> print(next(paquete))
    ('python', 3.11)
    >>> print(next(paquete))
    ('zope', 5.2)
    >>> print(next(paquete))
    ('plone', 6.0)
    >>> print(next(paquete))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

.. note::
  En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al
  llegar al final mediante el iterador ``paquete`` se llama a la excepción
  :ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la
  iteración.

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion10>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::

.. _`iterator protocol`: https://docs.python.org/es/3.11/library/stdtypes.html#iterator-types
