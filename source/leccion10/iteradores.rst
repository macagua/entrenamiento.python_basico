.. -*- coding: utf-8 -*-


.. _python_iteradores:

Iteradores
----------

.. todo::
    TODO escribir esta sección.

Entendiendo Iteradores
......................

.. sidebar:: Simplicidad

   La duplicación del esfuerzo es un derroche y reemplazar
   varios de los enfoques propios con una característica 
   estándar, normalmente, deriva en hacer las cosas más 
   legibles además de más interoperable.

      *Guido van Rossum* --- `Añadiendo tipado estático opcional a Python` (`Adding Optional Static Typing to Python`_)

.. _`Adding Optional Static Typing to Python`: https://www.artima.com/weblogs/viewpost.jsp?thread=86641


Un iterador es un objeto adherido al 'protocolo de iterador'
(`iterator protocol`_) --- básicamente esto significa que tiene
un método `next <iterator.next>` ('next' por siguiente), el cual,
cuando se le llama, devuelve la siguiente 'pieza' (o 'item') en la
secuencia y, cuando no queda nada para ser devuelto, lanza la excepción 
:ref:`StopIteration <python_exception_stopiteration>`.

.. _`iterator protocol`: https://docs.python.org/dev/library/stdtypes.html#iterator-types


::

  >>> nums = [1,2,3]
  >>> iter(nums)
  <listiterator object at 0xb712ebec>
  >>> nums.__iter__()
  <listiterator object at 0xb712eb0c>
  >>> nums.__reversed__()
  <listreverseiterator object at 0xb712ebec>


Usando 'iter' y 'next'
......................

Cuando se usa en un bucle, finalmente se llama a :ref:`StopIteration <python_exception_stopiteration>` y se provoca la finalización del bucle. Pero si se llama de forma explícita puede ver que, una vez que el iterador está ‘agotado’, al llamarlo nuevamente verá que se lanza la excepción comentada anteriormente.

::
  
  >>> it = iter(nums)
  >>> it.next()
  1
  >>> it.next()
  2
  >>> it.next()
  3
  >>> it.next()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  StopIteration

::

  >>> f = open('/etc/fstab')
  >>> f is f.__iter__()
  True

Iteradores y Diccionarios
.........................

.. todo::
    TODO escribir esta sección.

Otros Iteradores
................

.. todo::
    TODO escribir esta sección.

Ejercicios
..........

.. todo::
    TODO escribir esta sección.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion10>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
