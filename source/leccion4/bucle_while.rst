.. -*- coding: utf-8 -*-


.. _python_bucle_while:

Bucle while
-----------

En Python tiene una palabra reservada llamada ``while`` que nos permite ejecutar 
ciclos, o bien secuencias periódicas que nos permiten ejecutar código múltiples 
veces.

El ciclo ``while`` nos permite realizar múltiples iteraciones basándonos en el 
resultado de una expresión lógica que puede tener como resultado un valor ``True`` 
o ``False``.


Tipos de Bucle 'while'
.......................

A continuación, se presentan algunos ejemplos del uso del bucle ``while``:


Bucle 'while' controlado por Conteo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``while`` controlado por 
conteo:

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 12-17

En este ejemplo tiene un contador con un valor inicial de cero, cada iteración del 
``while`` manipula esta variable de manera que incremente su valor en 1, por lo que 
después de su primera iteración el contador tendrá un valor de 1, luego 2, y así 
sucesivamente. 

Eventualmente cuando el contador llegue a tener un valor de 10, la condición del ciclo 
``numero <= 10`` sera ``False``, por lo que el ciclo terminará arrojando el siguiente 
resultado.


Bucle 'while' controlado por Evento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``while`` controlado 
por Evento:

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 27-37

En este casi el evento que se dispara cuando el usuario ingresa el valor ``-1``, 
causando que el bucle ``while`` se interrumpo o no se inicie.


Bucle 'while' con 'else'
~~~~~~~~~~~~~~~~~~~~~~~~

Al igual que la sentencia :ref:`if <python_sent_if>`, la estructura ``while`` también 
puede combinarse con una sentencia :ref:`else <python_sent_else>`).

El nombre de la sentencia :ref:`else <python_sent_else>` es equivocada, ya que el bloque 
``else`` se ejecutará en todos los casos, es decir, cuando la expresión condicional del 
``while`` sea ``False``, (a comparación de la :ref:`sentencia if <python_sent_if>`).

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 47-57

La sentencia ``else`` tiene la ventaja de mantener el mismo nombre y la misma sintaxis 
que en las demás estructuras de control.


Sentencias utilitarias
......................

A continuación, se presentan algunos ejemplos del uso de sentencias utilitarias 
usadas en el bucle ``while``:


.. _python_sent_break:

Sentencia break
~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``while`` controlado la 
sentencia ``break``:

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 64-70

Adicionalmente existe una forma alternativa de interrumpir o cortar los ciclos utilizando 
la palabra reservada ``break``.

Esta nos permite salir del ciclo incluso si la expresión evaluada en ``while`` (o en 
otro ciclo como ``for``) permanece siendo ``True``. Para comprender mejor use el mismo 
ejemplo anterior pero se interrumpe el ciclo usando la sentencia ``break``.


.. _python_sent_continue:

Sentencia continue
~~~~~~~~~~~~~~~~~~

A continuación, se presenta un ejemplo del uso del bucle ``while`` controlado la 
sentencia ``continue``:

.. literalinclude:: ../../recursos/leccion4/bucle_while.py
    :linenos:
    :language: python
    :lines: 77-83

La sentencia ``continue`` hace que pase de nuevo al principio del bucle aunque no 
se haya terminado de ejecutar el ciclo anterior.


Ejemplos
........


Sucesión de Fibonacci
~~~~~~~~~~~~~~~~~~~~~

Ejemplo de la `Sucesión de Fibonacci <https://es.wikipedia.org/wiki/Sucesión_de_Fibonacci>`_ 
con bucle ``while``:

.. literalinclude:: ../../recursos/leccion4/fibonacci.py
    :linenos:
    :language: python
    :lines: 6-9


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion4/bucle_while.py>`.


.. tip::
    Para ejecutar el código :file:`bucle_while.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando:

    ::

        python bucle_while.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion4>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
