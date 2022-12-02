.. -*- coding: utf-8 -*-


.. _python_modulo_bpython:

Interprete bpython
------------------

Alternativamente puedes usar el paquete `bpython`_ que mejora aun más la experiencia
de trabajo con el paquete :ref:`ipython <python_modulo_ipython>`.

Para mayor información visite su página principal de `interprete bpython`_ y si necesita
instalar este programa ejecute el siguiente comando:

.. code-block:: console

    $ pip install bpython

Luego sustituya el comando ``python`` por ``bpython`` de la siguiente forma:

.. code-block:: console

    $ bpython


Dentro de interprete Python puede apreciar que ofrece otra forma de presentar
la documentación y la estructura del lenguaje, con los siguientes comandos de ejemplos:

.. code-block:: console

    >>> print('Hola Mundo')
    Hola Mundo
    >>> for item in range(
    ┌──────────────────────────────────────────────────────────────────────────────────────┐
    │ range: (stop)                                                                 │
    │ range(stop) -> range object                                                   │
    │ range(start, stop[, step]) -> range object                                    │
    │                                                                               │
    │ Return an object that produces a sequence of integers from start (inclusive)  │
    │ to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.     │
    │ start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.      │
    │ These are exactly the valid indices for a list of 4 elements.                 │
    │ When step is given, it specifies the increment (or decrement).                │
    └──────────────────────────────────────────────────────────────────────────────────────┘


Como puede apreciar este tutorial no le enseña a programar sino a simplemente
aprender a conocer como manejarse en el modo interactivo usando el paquete
``bpython``, con el fin de conocer a través de la introspección del lenguaje,
las librerías estándar y módulos propios escritos en Python que
tienes instalado en tu sistema.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.

.. _`bpython`: https://pypi.org/project/bpython/
.. _`interprete bpython`: https://bpython-interpreter.org/
