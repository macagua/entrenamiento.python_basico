.. -*- coding: utf-8 -*-

Bucles WHILE
============

En Python tenemos una palabra reservada llamada “\ **while**\ ” que nos
permite ejecutar ciclos, o bien secuencias periódicas que nos permiten
ejecutar código múltiples veces.

El ciclo ``while`` nos permite realizar múltiples iteraciones basándonos en
el resultado de una expresión lógica que puede tener como resultado un
valor verdadero o falso (true o false).

Tipos de Bucles 'while'
-----------------------

Bucles 'while' controlado por Conteo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 7-17

En este ejemplo tenemos un contador con un valor inicial de cero, cada
iteración del ``while`` manipula esta variable de manera que
incremente su valor en 1, por lo que después de su primera iteración el
contador tendrá un valor de 1, luego 2, y así sucesivamente.
Eventualmente cuando el contador llegue a tener un valor de 10, la
condición del ciclo ``numero <= 10`` sera falsa, por lo que el ciclo
terminará arrojando el siguiente resultado.

Bucles 'while' controlado por Evento
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 19-36

Sentencias utilitarias
----------------------

Usando la sentencia 'break'
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 40-48

Adicionalmente existe una forma alternativa de interrumpir
o cortar los ciclos utilizando la palabra reservada ``break``.
Esta nos permite salir del ciclo incluso si la expresión evaluada 
en ``while`` (o en otro ciclo como ``for``) permanece siendo
verdadera. Para comprender mejor usaremos el mismo ejemplo
anterior pero interrumpiremos el ciclo usando ``break``.

Usando la sentencia 'continue'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 50-58

La sentencia ``continue`` hace que pase de nuevo al principio del bucle aunque no se haya terminado de ejecutar el ciclo anterior.

Ejemplos
--------

Ejemplo de fibonacci
^^^^^^^^^^^^^^^^^^^^

Ejemplo de la `Sucesión de Fibonacci`_ con bucle ``while``:

.. literalinclude:: ../../recursos/leccion4/fibonacci.py
    :linenos:
    :language: python

Ejemplo de bucle while
^^^^^^^^^^^^^^^^^^^^^^

Ejemplo de completo de bucles ``while``:

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python

Vídeo tutorial
--------------

- `Tutorial Python 11 - Bucles`_.


Referencia
----------

- `Introducción a Bucles 'while'`_.

- `Ciclo while en Python`_.
 
.. _`Introducción a Bucles 'while'`: http://docs.python.org.ar/tutorial/2/introduction.html#primeros-pasos-hacia-la-programacion
.. _`Sucesión de Fibonacci`: https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci
.. _`Tutorial Python 11 - Bucles`: https://www.youtube.com/watch?v=IyI2ZuOq_xQ
.. _`Ciclo while en Python`: http://codigoprogramacion.com/cursos/tutoriales-python/ciclo-while-en-python.html
