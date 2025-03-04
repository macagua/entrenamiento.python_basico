.. _python_modulo_bpython:

Interprete bpython
------------------

Alternativamente puedes usar el paquete `bpython`_ que mejora aun más la experiencia
de trabajo con el paquete :ref:`ipython <python_modulo_ipython>`.

Para mayor información visite su página principal de `interprete bpython`_ y si necesita
instalar este programa ejecute el siguiente comando, el cual a continuación se presentan
el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          pip install bpython

   .. group-tab:: Windows

      .. code-block:: console

          pip install bpython


Luego sustituya el comando ``python`` por ``bpython`` correspondiente a tu sistema
operativo de la siguiente forma:


.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          bpython

   .. group-tab:: Windows

      .. code-block:: console

          bpython


Dentro de interprete Python puede apreciar que ofrece otra forma de presentar
la documentación y la estructura del lenguaje, con los siguientes comandos de ejemplos:

.. code-block:: console

    >>> print('Hola Mundo')

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: console
    :class: no-copy

    Hola Mundo

.. code-block:: console
    :class: no-copy

    >>> for item in range(
    ┌───────────────────────────────────────────────────────────────────────────────┐
    │ range: (stop)                                                                 │
    │ range(stop) -> range object                                                   │
    │ range(start, stop[, step]) -> range object                                    │
    │                                                                               │
    │ Return an object that produces a sequence of integers from start (inclusive)  │
    │ to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.     │
    │ start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.      │
    │ These are exactly the valid indices for a list of 4 elements.                 │
    │ When step is given, it specifies the increment (or decrement).                │
    └───────────────────────────────────────────────────────────────────────────────┘

Y para cerrar la sesión con el ``bpython`` ejecute el siguiente comando:

.. code-block:: pycon

    >>> exit()


Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    (None,)

Asi pudo salir de la sesión del interprete interactivo ``bpython``.

De esta forma, ha aprendió nociones básicas con el interprete interactivo ``bpython``.


----


Como puede apreciar este tutorial no le enseña a programar sino a simplemente
aprender a conocer como manejarse en el modo interactivo usando el paquete
``bpython``, con el fin de conocer a través de la introspección del lenguaje,
las librerías estándar y módulos propios escritos en Python que
tienes instalado en tu sistema.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`bpython`: https://pypi.org/project/bpython/
.. _`interprete bpython`: https://bpython-interpreter.org/
