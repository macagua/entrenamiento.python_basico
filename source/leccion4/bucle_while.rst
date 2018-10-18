.. -*- coding: utf-8 -*-


.. _python_bucle_while:

Bucle while
-----------

En Python tenemos una palabra reservada llamada ``while`` que nos
permite ejecutar ciclos, o bien secuencias periódicas que nos permiten
ejecutar código múltiples veces.

El ciclo ``while`` nos permite realizar múltiples iteraciones basándonos en
el resultado de una expresión lógica que puede tener como resultado un
valor ``true`` o ``false`` (verdadero o  falso).


Tipos de Bucle 'while'
.......................

A continuación, se presentan algunos ejemplos del uso del bucle ``while``:


Bucle 'while' controlado por Conteo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``while`` controlado por Conteo:

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 8-19

En este ejemplo tenemos un contador con un valor inicial de cero, cada
iteración del ``while`` manipula esta variable de manera que
incremente su valor en 1, por lo que después de su primera iteración el
contador tendrá un valor de 1, luego 2, y así sucesivamente.
Eventualmente cuando el contador llegue a tener un valor de 10, la
condición del ciclo ``numero <= 10`` sera falsa, por lo que el ciclo
terminará arrojando el siguiente resultado.


Bucle 'while' controlado por Evento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``while`` controlado por Evento:

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 23-41

En este casi el evento que se dispara cuando el usuario ingresa el valor ``-1``, 
causando que el bucle ``while`` se interrumpo o no se inicie.


Sentencias utilitarias
......................

A continuación, se presentan algunos ejemplos del uso de sentencias utilitarias usadas en 
el bucle ``while``:


Usando la sentencia 'break'
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``while`` controlado la sentencia 
``break``:

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 45-53

Adicionalmente existe una forma alternativa de interrumpir
o cortar los ciclos utilizando la palabra reservada ``break``.
Esta nos permite salir del ciclo incluso si la expresión evaluada 
en ``while`` (o en otro ciclo como ``for``) permanece siendo
verdadera. Para comprender mejor usaremos el mismo ejemplo
anterior pero interrumpiremos el ciclo usando ``break``.


Usando la sentencia 'continue'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``while`` controlado la sentencia 
``continue``:

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 57-65

La sentencia ``continue`` hace que pase de nuevo al principio del 
bucle aunque no se haya terminado de ejecutar el ciclo anterior.


Ejemplos
........

Sucesión de Fibonacci
~~~~~~~~~~~~~~~~~~~~~

Ejemplo de la `Sucesión de Fibonacci`_ con bucle ``while``:

.. literalinclude:: ../../recursos/leccion4/fibonacci.py
    :linenos:
    :language: python
    :lines: 8-11


.. seealso:: Ver el vídeo `Tutorial Python 11 - Bucles`_.


Referencia
..........

- `Introducción a Bucles 'while'`_.

- `Ciclo while en Python`_.
 
.. _`Introducción a Bucles 'while'`: http://docs.python.org.ar/tutorial/2/introduction.html#primeros-pasos-hacia-la-programacion
.. _`Sucesión de Fibonacci`: https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci
.. _`Tutorial Python 11 - Bucles`: https://www.youtube.com/watch?v=IyI2ZuOq_xQ
.. _`Ciclo while en Python`: http://codigoprogramacion.com/cursos/tutoriales-python/ciclo-while-en-python.html
