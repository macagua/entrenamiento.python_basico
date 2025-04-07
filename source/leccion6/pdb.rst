.. _python_modulo_pdb:

Módulo pdb
----------

En este tutorial se exploran herramientas que ayudan a entender tu
código: depuración para encontrar y corregir *bugs* (errores).

El depurador Python, :mod:`pdb`, te permite inspeccionar tu código
de forma interactiva.

Te permite:

-  Ver el código fuente.

-  Ir hacia arriba y hacia abajo del punto donde se ha producido
   un error.

-  Inspeccionar valores de variables.

-  Modificar valores de variables.

-  Establecer ``breakpoints`` (punto de parada del proceso).

.. topic:: **print**

    Sí, las declaraciones :ref:`print <python_sent_print>` sirven como herramienta de depuración.
    Sin embargo, para inspeccionar en tiempo de ejecución es más
    eficiente usar el depurador.


Invocando al depurador
......................

Formas de lanzar el depurador:

#. Postmortem, lanza el depurador después de que se hayan producido
   errores.

#. Lanza el módulo con el depurador.

#. Llama al depurador desde dentro del módulo.


Postmortem
~~~~~~~~~~

**Situación**: Estás trabajando en el interprete :ref:`IPython <python_modulo_ipython>`
y obtienes un error (:ref:`traceback <python_modulo_traceback>`).

En este caso esta depurando el módulo :download:`index_error.py <../../recursos/leccion6/index_error.py>`.

Entonces ejecute el interprete :ref:`IPython <python_modulo_ipython>`, con el siguiente comando:

.. code-block:: console

    ipython

Al entrar al interprete :ref:`IPython <python_modulo_ipython>`, escribe :command:`%run index_error.py`

.. code-block:: pycon

    In [1]: %run index_error.py
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    File /home/macagua/python/entrenamiento/index_error.py:10
         6     print(lst[len(lst)])
         9 if __name__ == "__main__":
    ---> 10     index_error()

    File /home/macagua/python/entrenamiento/index_error.py:6, in index_error()
          4 def index_error():
          5     lst = list("foobar")
    ----> 6     print(lst[len(lst)])

    IndexError: list index out of range

Cuando lo ejecutes verás como se lanza una excepción :ref:`IndexError <python_exception_indexerror>`.
Entonces ejecute el comando :command:`%debug` y entrarás en el depurador.

.. code-block:: pycon

    In [2]: %debug
    > /home/macagua/python/entrenamiento/index_error.py(6)index_error()
          4 def index_error():
          5     lst = list("foobar")
    ----> 6     print(lst[len(lst)])
          7
          8

    ipdb> list
          1 """Small snippet to raise an IndexError."""
          2
          3
          4 def index_error():
          5     lst = list("foobar")
    ----> 6     print(lst[len(lst)])
          7
          8
          9 if __name__ == "__main__":
          10     index_error()

    ipdb> len(lst)
    6
    ipdb> print(lst[len(lst)-1])
    r
    ipdb> quit

    In [3]:

.. topic:: Depuración post-mortem sin IPython

   En algunas situaciones no podrás usar :ref:`IPython <python_modulo_ipython>`, por ejemplo
   para depurar un `script` que ha sido llamado desde la línea de comandos. En este caso,
   puedes ejecutar el `script` de la siguiente forma :command:`python3 -m pdb script.py`:

   .. sourcecode:: console

      python3 -m pdb index_error.py

   Este comando anterior muestra lo siguiente:

   .. code-block:: pycon

      > /home/macagua/python/entrenamiento/index_error.py(1)<module>()
      -> """Small snippet to raise an IndexError."""
      (Pdb) continue
      Traceback (most recent call last):
        File "/usr/lib/python3.11/pdb.py", line 1774, in main
          pdb._run(target)
        File "/usr/lib/python3.11/pdb.py", line 1652, in _run
          self.run(target.code)
        File "/usr/lib/python3.11/bdb.py", line 597, in run
          exec(cmd, globals, locals)
        File "<string>", line 1, in <module>
        File "/home/macagua/python/entrenamiento/index_error.py", line 10, in <module>
          index_error()
        File "/home/macagua/python/entrenamiento/index_error.py", line 6, in index_error
          print(lst[len(lst)])
                ~~~^^^^^^^^^^
      IndexError: list index out of range
      Uncaught exception. Entering post mortem debugging
      Running 'cont' or 'step' will restart the program
      > /home/macagua/python/entrenamiento/index_error.py(6)index_error()
      -> print(lst[len(lst)])
      (Pdb)

De esta forma, puedes ejecutar postmortem la depuración del código del módulo.


Ejecución paso a paso
~~~~~~~~~~~~~~~~~~~~~

**Situación**: Crees que existe un error en un módulo pero no estás seguro donde.

Por ejemplo, esta intentado depurar :download:`wiener_filtering.py <../../recursos/leccion6/wiener_filtering.py>`.
A pesar de que el código se ejecuta, observa que el filtrado no se
está haciendo correctamente.

* Ejecuta el `script` en :ref:`IPython <python_modulo_ipython>` con el depurador usando :command:`%run -d wiener_filtering.py`:

  .. code-block:: pycon

    In [1]: %run -d wiener_filtering.py
    *** Blank or comment
    *** Blank or comment
    *** Blank or comment
    Breakpoint 1 at /home/macagua/python/entrenamiento/wiener_filtering.py:4
    NOTE: Enter 'c' at the ipdb>  prompt to start your script.
    > <string>(1)<module>()

* Coloca un ``breakpoint`` en la línea 34 usando ``b 34``:

  .. code-block:: pycon

    ipdb> n
    > /home/macagua/python/entrenamiento/wiener_filtering.py(4)<module>()
          3
    1---> 4 import numpy as np
          5 import scipy as sp

    ipdb> b 34
    Breakpoint 2 at /home/macagua/python/entrenamiento/wiener_filtering.py:34

* Continua la ejecución hasta el siguiente ``breakpoint`` con ``c(ont(inue))``:

  .. code-block:: pycon

    ipdb> c
    > /home/macagua/python/entrenamiento/wiener_filtering.py(34)iterated_wiener()
         33     """
    2--> 34     noisy_img = noisy_img
         35     denoised_img = local_mean(noisy_img, size=size)

* Da pasos hacia adelante y detrás del código con ``n(ext)`` y
  ``s(tep)``. ``next`` salta hasta la siguiente declaración en el actual
  contexto de ejecución mientras que ``step`` se moverá entre los contextos
  en ejecución, i.e. permitiendo explorar dentro de llamadas a funciones:

  .. code-block:: pycon

    ipdb> s
    > /home/macagua/python/entrenamiento/wiener_filtering.py(35)iterated_wiener()
    2    34     noisy_img = noisy_img
    ---> 35     denoised_img = local_mean(noisy_img, size=size)
         36     l_var = local_var(noisy_img, size=size)

    ipdb> n
    > /home/macagua/python/entrenamiento/wiener_filtering.py(36)iterated_wiener()
         35     denoised_img = local_mean(noisy_img, size=size)
    ---> 36     l_var = local_var(noisy_img, size=size)
         37     for i in range(3):


* Muévete unas pocas líneas y explora las variables locales:

  .. code-block:: pycon

    ipdb> n
    > /home/macagua/python/entrenamiento/wiener_filtering.py(37)iterated_wiener()
         36     l_var = local_var(noisy_img, size=size)
    ---> 37     for i in range(3):
         38         res = noisy_img - denoised_img
    ipdb> print(l_var)
    [[5868 5379 5316 ..., 5071 4799 5149]
     [5013  363  437 ...,  346  262 4355]
     [5379  410  344 ...,  392  604 3377]
     ...,
     [ 435  362  308 ...,  275  198 1632]
     [ 548  392  290 ...,  248  263 1653]
     [ 466  789  736 ..., 1835 1725 1940]]
    ipdb> print(l_var.min())
    0

*Oh estimado(a)*, solo ve entero y variación 0. Aquí está nuestro error,
estamos haciendo aritmética con enteros.

.. topic:: Lanzando excepciones en errores numéricos

    Cuando ejecuta el archivo :download:`wiener_filtering.py <../../recursos/leccion6/wiener_filtering.py>`,
    se lanzarán los siguientes avisos:

    .. code-block:: pycon
      :class: no-copy

        In [2]: %run wiener_filtering.py
        wiener_filtering.py:40: RuntimeWarning: divide by zero encountered in divide
            noise_level = (1 - noise/l_var )

    Puede convertir estos avisos a excepciones, lo que le permitiría
    hacer una depuración post-mortem sobre ellos y encontrar el problema
    de manera más rápida:

    .. code-block:: pycon
      :class: no-copy

        In [3]: np.seterr(all='raise')
        Out[3]: {'divide': 'print', 'invalid': 'print', 'over': 'print', 'under': 'ignore'}
        In [4]: %run wiener_filtering.py
        ---------------------------------------------------------------------------
        FloatingPointError                        Traceback (most recent call last)
        /home/macagua/venv/lib/python3.11/site-packages/IPython/utils/py3compat.pyc
        in execfile(fname, *where)
            176             else:
            177                 filename = fname
        --> 178             __builtin__.execfile(filename, *where)

        /home/macagua/python/entrenamiento/wiener_filtering.py in <module>()
             55 pl.matshow(noisy_lena[cut], cmap=pl.cm.gray)
             56
        ---> 57 denoised_lena = iterated_wiener(noisy_lena)
             58 pl.matshow(denoised_lena[cut], cmap=pl.cm.gray)
             59

        /home/macagua/python/entrenamiento/wiener_filtering.py in
        iterated_wiener(noisy_img, size)
             38         res = noisy_img - denoised_img
             39         noise = (res**2).sum()/res.size
        ---> 40         noise_level = (1 - noise/l_var )
             41         noise_level[noise_level<0] = 0
             42         denoised_img += noise_level*res
        FloatingPointError: divide by zero encountered in divide

De esta forma, puedes ejecutar paso a paso la depuración del código del módulo.


Lanza al depurador desde adentro
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Puedes llamar explícitamente al depurador desde adentro. Inserta la siguiente línea
donde quieres que salte el depurador:

.. code-block:: python
    :linenos:

    import pdb

    pdb.set_trace()

A continuación, se muestra un ejemplo del uso de la función ``set_trace()``:

.. literalinclude:: ../../recursos/leccion6/funcion_a_depurar.py
    :language: python
    :linenos:
    :lines: 1-13

.. tip::
    Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`funcion_a_depurar.py`,
    abra una consola de comando, acceda al directorio donde se encuentra el módulo :file:`funcion_a_depurar.py`
    y ejecute el siguiente comando:

.. code-block:: console

    python3 funcion_a_depurar.py

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console
    :class: no-copy

    > /home/macagua/python/entrenamiento/funcion_a_depurar.py(6)calculo()
    -> if args[0]:
    (Pdb) c
    12
    14522590


De esta forma, puedes depurar el código de la función ``calculo`` desde adentro del módulo.


Formas alternativas para depurar
................................

Existen otras formas de comenzar una depuración, a continuación se describen:

* **Lanzar una excepción "break point" a lo pobre**

  Si encuentras tedioso el tener que anotar el número de línea para colocar
  un *break point*, puedes lanzar una excepción en el punto que quieres
  inspeccionar y usar la *'magia'* ``%debug`` del interprete :ref:`IPython <python_modulo_ipython>`.
  Destacar que en este caso no puedes moverte por el código y continuar después la ejecución.

* **Depurando fallos de pruebas usando pytest**

  Puede ejecutar pruebas usando `pytest <https://docs.pytest.org/en/stable/>`_ con el comando
  :command:`pytest --pdb` este invocará al depurador de Python en cada fallo (o una excepción
  :ref:`KeyboardInterrupt <python_exception_keyboardinterrupterror>` se dispara al momento que
  el programador presiona el comando :keys:`Ctrl+C` o :keys:`Ctrl+Z` en su teclado, cuando está
  presente en una línea de comandos (en Windows) o en una terminal(en iOS/Linux)). Ademas con el
  comando :command:`pytest --trace`  puedes permite entrar en el prompt :ref:`pdb <python_modulo_pdb>`
  inmediatamente al inicio de cada prueba.

* **Depurando interactivamente en la consola**

  Consulte el módulo :ref:`ipdb <python_modulo_ipdb>`.


.. topic:: Depuradores gráficos y alternativas

    * Quizá encuentres más conveniente usar un depurador gráfico como
      `winpdb <https://pypi.org/project/winpdb/>`_. para inspeccionar saltas a través del
      código e inspeccionar las variables

    * De forma alternativa, `pudb <https://pypi.org/project/pudb>`_ es un
      buen depurador semi-gráfico con una interfaz de texto en la consola.


.. _python_modulo_pdb_comandos:

Comandos del depurador
......................

A continuación se muestra una tabla con los comandos más comunes
de depuración y sus descripciones:

============================= ======================================================================
``EOF``                       Maneja la recepción de EOF como un comando
``alias <nombre> <comando>``  Crea un alias para el comando
``a``, ``args``               Imprime la lista de argumentos de la función actual
``b``, ``break``              Establece un *breakpoint* en la línea actual
``bt``                        Muestra el *call stack*
``cl``, ``clear``             Limpia todos los *breakpoints*
``cl <n>``                    Limpia el *breakpoint* número ``n``
``!command``                  Ejecuta el comando **Python** proporcionado (en oposición a comandos ``pdb``)
``commands <n>``              Muestra los comandos del *breakpoint* número ``n``
``commands <n> <comando>``    Añade un comando al *breakpoint* número ``n``
``condition <n> <c>``         Establece la condición ``c`` para el *breakpoint* número ``n``
``c``, ``cont``, ``continue`` Continua la ejecución hasta el siguiente *breakpoint*
``debug``                     Introduce un depurador recursivo que recorre el argumento de código (que es una expresión o sentencia arbitraria a ejecutar en el entorno actual).
``disable <n>``               Desactiva el *breakpoint* número ``n``
``display <objeto>``          Muestra el valor del objeto dado
``d``, ``down``               Paso abajo de la llamada a la pila (*call stack*)
``enable <n>``                Activa el *breakpoint* número ``n``
``exec``                      Ejecuta la sentencia (de una línea) en el contexto del marco de pila actual
``exit``                      Salir del depurador
``h``, ``help``               Muestra la ayuda de los comandos
``h <command>``               Muestra la ayuda del comando ``command``
``ignore <n> <c>``            Ignora el *breakpoint* número ``n`` si la condición ``c`` es verdadera
``interact``                  Ejecuta el comando ``pdb`` en el contexto de la función actual
``j``, ``jump``               Salta a la línea especificada (no se puede usar en el contexto de una función)
``l``, ``list``               Lista el código en la posición actual
``ll``, ``longlist``          Lista el código en la posición actual (más líneas)
``n``, ``next``               Ejecuta la siguiente línea (no va hacia abajo en funciones nuevas)
``p``, ``print``              Imprime el valor de una variable
``pp``                        Imprime el valor de una variable (con formato)
``q``, ``quit``               Salir del depurador
``restart``                   Reiniciar el programa python depurado
``r``, ``return``             Regresa de la función actual
``run``                       Iniciar el programa python depurado
``rv``, ``retval``            Imprime el valor de retorno del último retorno de una función
``source``                    Intenta obtener el código fuente del objeto dado y mostrarlo
``s``, ``step``               Ejecuta la siguiente línea (va hacia abajo en las nuevas funciones)
``tbreak``                    Establece un *breakpoint* temporal
``unalias <nombre>``          Elimina el alias
``undisplay <n>``             Elimina el *display* número ``n``
``unt``, ``until``            Sin argumento, continúa la ejecución hasta alcanzar la línea con un número mayor que el actual.
``u``, ``up``                 Paso arriba de la llamada a la pila (*call stack*)
``whatis <objeto>``           Muestra el tipo del objeto dado
``w``, ``where``              Muestra la traza de la pila actual
============================= ======================================================================

.. warning:: **Los comandos de depuración no son código Python**

    No puedes nombrar a las variables de la forma que quieras. Por ejemplo,
    si esta dentro del depurador no podrá sobrescribir a las variables con el
    mismo y, por tanto, **habrá que usar diferentes nombres para las
    variables cuando este tecleando código en el depurador**.


.. _python_modulo_pdb_ayuda:

Ayuda del depurador
...................

Teclea ``h`` o ``help`` para acceder a la ayuda interactiva:

.. sourcecode:: pycon

    (Pdb) help

    Documented commands (type help <topic>):
    ========================================
    EOF    c          d        h         list      q        rv       undisplay
    a      cl         debug    help      ll        quit     s        unt
    alias  clear      disable  ignore    longlist  r        source   until
    args   commands   display  interact  n         restart  step     up
    b      condition  down     j         next      return   tbreak   w
    break  cont       enable   jump      p         retval   u        whatis
    bt     continue   exit     l         pp        run      unalias  where

    Miscellaneous help topics:
    ==========================
    exec  pdb

----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`funcion_a_depurar.py <../../recursos/leccion6/funcion_a_depurar.py>`.

    - :download:`index_error.py <../../recursos/leccion6/index_error.py>`.

    - :download:`wiener_filtering.py <../../recursos/leccion6/wiener_filtering.py>`.


.. tip::
    Para ejecutar el código :file:`funcion_a_depurar.py`, :file:`index_error.py`
    y :file:`wiener_filtering.py`, abra una consola de comando, acceda al directorio
    donde se encuentra ambos programas:

    .. code-block:: console
      :class: no-copy

      depuracion/
      ├── funcion_a_depurar.py
      ├── index_error.py
      └── wiener_filtering.py

    Si tiene la estructura de archivo previa, entonces ejecute por separado cada comando:

    .. code-block:: console

        python3 funcion_a_depurar.py

    .. code-block:: console

        pdb3 index_error.py

    .. code-block:: console

        python3 -m pdb wiener_filtering.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion6>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
