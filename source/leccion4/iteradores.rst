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

::

    >>> archivo = open('/etc/hostname')
    >>> archivo
    <open file '/etc/hostname', mode 'r' at 0x7fa44ba379c0>
    >>> archivo.__iter__()
    <open file '/etc/hostname', mode 'r' at 0x7fa44ba379c0>
    >>> iter(archivo)
    <open file '/etc/hostname', mode 'r' at 0x7fa44ba379c0>
    >>> archivo is archivo.__iter__()
    True
    >>> linea = archivo.__iter__()
    >>> linea.next()
    'laptop\n'
    >>> linea.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo, el método especial ``__iter__()``, hace lo mismo que la función integrada 
:ref:`iter(archivo) <python_fun_iter>`.


Iteradores y secuencias
.......................

Los *iteradores* se usan con los tipos de secuencias estándar. A continuación, 
se describen algunos ejemplos:

**Iterar sobre la secuencia inmutable cadena de caracter**

A continuación, un ejemplo del uso de los iteradores con la secuencia *inmutable* de 
tipo :ref:`cadena de caracteres <python_str>` ``ASCII``:

::

    >>> frase = 'Hola Mundo'
    >>> letra = iter(frase)
    >>> letra.next()
    'H'
    >>> letra.next()
    'o'
    >>> letra.next()
    'l'
    >>> letra.next()
    'a'
    >>> letra.next()
    ' '
    >>> letra.next()
    'M'
    >>> letra.next()
    'u'
    >>> letra.next()
    'n'
    >>> letra.next()
    'd'
    >>> letra.next()
    'o'
    >>> letra.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior, cuando se itera en la secuencia ``frase``, al 
llegar al final mediante el iterador ``letra`` se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la 
iteración.

**Iterar sobre la secuencia inmutable cadena Unicode**

A continuación, un ejemplo del uso de los iteradores con la secuencia *inmutable* de 
tipo :ref:`cadena de caracteres <python_unicode_cls>` ``Unicode``:

::

    >>> frase = u'Jekechitü'
    >>> letra = iter(frase)
    >>> letra.next()
    u'J'
    >>> letra.next()
    u'e'
    >>> letra.next()
    u'k'
    >>> letra.next()
    u'e'
    >>> letra.next()
    u'c'
    >>> letra.next()
    u'h'
    >>> letra.next()
    u'i'
    >>> letra.next()
    u't'
    >>> letra.next()
    u'\xfc'
    >>> letra.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior, cuando se itera en la secuencia ``frase``, al 
llegar al final mediante el iterador ``letra`` se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la 
iteración.

**Iterar sobre la secuencia inmutable tupla**

A continuación, un ejemplo del uso de los iteradores con la secuencia *inmutable* de 
tipo :ref:`tupla <python_tuple>`:

::

    >>> valores = ("Python", True, "Zope", 5)
    >>> valores
    ('Python', True, "Zope", 5)
    >>> valores.__iter__()
    <tupleiterator object at 0x7fa44b9fa450>
    >>> valor = valores.__iter__()
    >>> valor.next()
    'Python'
    >>> valor.next()
    True
    >>> valor.next()
    'Zope'
    >>> valor.next()
    5
    >>> valor.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration


En el ejemplo anterior, cuando se itera en la secuencia ``valores``, al llegar al 
final mediante el iterador ``valor`` se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la 
iteración.

**Iterar sobre la función inmutable xrange**

A continuación, un ejemplo del uso de los iteradores con la secuencia *inmutable* 
con la función integrada :ref:`xrange() <python_fun_xrange>`:

::

    >>> lista = iter(xrange(5))
    >>> lista
    <rangeiterator object at 0x7fa44b9fb7b0>
    >>> lista.next()
    0
    >>> lista.next()
    1
    >>> lista.next()
    2
    >>> lista.next()
    3
    >>> lista.next()
    4
    >>> lista.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior, cuando se itera en la secuencia ``lista``, al llegar 
al final se llama a la excepción :ref:`StopIteration <python_exception_stopiteration>` 
y se causa el detener la iteración.

**Iterar sobre la secuencia mutable lista**

A continuación, un ejemplo del uso de los iteradores con la secuencia *mutable* de 
tipo :ref:`lista <python_list>`:

::

    >>> versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
    >>> iter(versiones_plone)
    <listiterator object at 0x7fa44b9fa450>
    >>> version = iter(versiones_plone)
    >>> version
    <listiterator object at 0x7fa44b9fa550>
    >>> version.next()
    2.1
    >>> version.next()
    2.5
    >>> version.next()
    3.6
    >>> version.next()
    4
    >>> version.next()
    5
    >>> version.next()
    6
    >>> version.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al 
llegar al final mediante el iterador ``version`` se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la 
iteración.

Usted puede devolver un objeto iterador en orden inverso sobre una secuencia *mutable* de 
tipo :ref:`lista <python_list>` usando su función integrada ``__reversed__()``.

::

    >>> versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
    >>> versiones_plone.__reversed__()
    <listreverseiterator object at 0xb712ebec>
    >>> version = versiones_plone.__reversed__()
    >>> version.next()
    6
    >>> version.next()
    5
    >>> version.next()
    4
    >>> version.next()
    3.6
    >>> version.next()
    2.5
    >>> version.next()
    2.1
    >>> version.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al 
llegar al final mediante el iterador ``version`` se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la 
iteración.

También puede acceder al uso del método especial ``__iter__()`` incluido en la 
secuencia *mutable* del tipo integrado :ref:`lista <python_list>`:

::

    >>> versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
    >>> versiones_plone.__iter__()
    <listiterator object at 0x7fa44b9fa510>

**Iterar sobre la función mutable range**

A continuación, un ejemplo del uso de los iteradores con la secuencia *mutable* 
de la función integrada :ref:`range() <python_fun_range>`:

::

    >>> lista = iter(range(5))
    >>> lista
    <listiterator object at 0x7fa44b9fa490>
    >>> lista.next()
    0
    >>> lista.next()
    1
    >>> lista.next()
    2
    >>> lista.next()
    3
    >>> lista.next()
    4
    >>> lista.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

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

::

    >>> versiones_plone = set([2.1, 2.5, 3.6, 4, 5, 6, 4])
    >>> version = iter(versiones_plone)
    >>> version
    <setiterator object at 0x7fac9c7c7a50>
    >>> version.next()
    2.5
    >>> version.next()
    4
    >>> version.next()
    5
    >>> version.next()
    6
    >>> version.next()
    2.1
    >>> version.next()
    3.6
    >>> version.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al 
llegar al final mediante el iterador ``version`` se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la 
iteración.

**Iterar sobre el conjunto inmutable**

A continuación, un ejemplo del uso de los iteradores con el conjunto *inmutable* de 
tipo :ref:`conjuntos <python_set>`:

::

    >>> versiones_plone = frozenset([6, 2.1, 2.5, 3.6, 4, 5, 4, 2.5])
    >>> version = iter(versiones_plone)
    >>> version
    <setiterator object at 0x7fac9c7c7cd0>
    >>> version.next()
    2.5
    >>> version.next()
    4
    >>> version.next()
    5
    >>> version.next()
    6
    >>> version.next()
    2.1
    >>> version.next()
    3.6
    >>> version.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

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

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> paquete = iter(versiones_plone)
    >>> paquete
    <dictionary-keyiterator object at 0x7fa44b9e99f0>
    >>> paquete.next()
    'zope'
    >>> paquete.next()
    'python'
    >>> paquete.next()
    'plone'
    >>> paquete.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al 
llegar al final mediante el iterador ``paquete`` se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la 
iteración.

**Iterar sobre los valores del diccionario**

A continuación, un ejemplo del uso de los iteradores con la secuencia de *mapeo*, 
tipo :ref:`diccionario <python_dict>` para mostrar el valor de una clave usando el 
método integrado :ref:`itervalues() <python_dict_mtd_itervalues>`:

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> version = iter(versiones_plone.itervalues())
    >>> version
    <dictionary-valueiterator object at 0x7fa44b9e9c00>
    >>> version.next()
    2.13
    >>> version.next()
    2.7
    >>> version.next()
    5.1
    >>> version.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al 
llegar al final mediante el iterador ``version`` se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la 
iteración.

**Iterar sobre los elementos del diccionario**

A continuación, un ejemplo del uso de los iteradores con la secuencia de *mapeo*, 
tipo :ref:`diccionario <python_dict>` para mostrar el par clave/valor usando el 
método integrado :ref:`iteritems() <python_dict_mtd_iteritems>`:

::

    >>> versiones_plone = dict(python=2.7, zope=2.13, plone=5.1)
    >>> paquete = iter(versiones_plone.iteritems())
    >>> paquete
    <dictionary-itemiterator object at 0x7fa44b9e9b50>
    >>> paquete.next()
    ('zope', 2.13)
    >>> paquete.next()
    ('python', 2.7)
    >>> paquete.next()
    ('plone', 5.1)
    >>> paquete.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

En el ejemplo anterior, cuando se itera en la secuencia ``versiones_plone``, al 
llegar al final mediante el iterador ``paquete`` se llama a la excepción 
:ref:`StopIteration <python_exception_stopiteration>` y se causa el detener la 
iteración.

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion10>` 
    del entrenamiento para ampliar su conocimiento en esta temática.

.. _`iterator protocol`: https://docs.python.org/dev/library/stdtypes.html#iterator-types
