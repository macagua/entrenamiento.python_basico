.. -*- coding: utf-8 -*-

LECCIÓN 9: ITERADORES
=====================

Entendiendo Iteradores
----------------------

.. sidebar:: Simplicidad

   La duplicación del esfuerzo es un derroche y reemplazar
   varios de los enfoques propios con una característica estándar,
   normalmente, deriva en hacer las cosas más legibles además de más
   interoperable.

                 *Guido van Rossum* --- `Añadiendo tipado estático opcional a Python` (`Adding Optional Static Typing to Python`_)

.. _`Adding Optional Static Typing to Python`:
   http://www.artima.com/weblogs/viewpost.jsp?thread=86641


Un iterador es un objeto adherido al 'protocolo de iterador' (`iterator protocol`_)
--- básicamente esto significa que tiene un método `next <iterator.next>` ('next' por siguiente),
el cual, cuando se le llama, devuelve la siguiente 'pieza' (o 'item') en la secuencia y, cuando
no queda nada para ser devuelto, lanza la excepción 
`StopIteration <exceptions.StopIteration>`.

.. _`iterator protocol`: http://docs.python.org/dev/library/stdtypes.html#iterator-types


::

  >>> nums = [1,2,3]
  >>> iter(nums)
  <listiterator object at 0xb712ebec>
  >>> nums.__iter__()
  <listiterator object at 0xb712eb0c>
  >>> nums.__reversed__()
  <listreverseiterator object at 0xb712ebec>

Usando 'iter' y 'next'
----------------------

Cuando se usa en un bucle, finalmente se llama a StopIteration y se provoca la finalización del bucle. Pero si se invoca de forma explícita podemos ver que, una vez que el iterador está ‘agotado’, al invocarlo nuevamente veremos que se lanza la excepción comentada anteriormente.

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

- Iteradores y Diccionarios.

- Otros Iteradores.

- Ejercicio 1.

Vídeo tutorial
--------------

 - `Tutorial Python 25 - Comprensión de Listas`_.

 - `Tutorial Python 26 - Generadores`_.

 - `Tutorial Python 27 - Decoradores`_.
 
.. _Tutorial Python 25 - Comprensión de Listas: https://www.youtube.com/watch?v=87s8XQbUv1k
.. _Tutorial Python 26 - Generadores: https://www.youtube.com/watch?v=tvHbC_OZV14
.. _Tutorial Python 27 - Decoradores: https://www.youtube.com/watch?v=TaIWx9paNIA
