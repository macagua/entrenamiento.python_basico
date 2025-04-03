.. _python_modulo_ipdb:

Módulo ipdb
-----------

Depurando interactivamente en la consola

El módulo `ipdb <https://pypi.org/project/ipdb>`_ exporta funciones para acceder al :ref:`IPython <python_modulo_ipython>`,
que cuenta con completado de tabulación, resaltado de sintaxis, mejores trazas, mejor introspección con la misma interfaz
que el módulo :ref:`pdb <python_modulo_pdb>` para depurar tu código fuente de forma interactiva.

Si necesita instalar este módulo, ejecute el siguiente comando:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          pip3 install ipdb

   .. group-tab:: Windows

      .. code-block:: console

          pip3 install ipdb

Puede probar si la instalación se realizo correctamente, ejecutando el siguiente
comando correspondiente a tu sistema operativo:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          python3 -c "import ipdb ; print(ipdb.__package__)"

   .. group-tab:: Windows

      .. code-block:: console

          python3 -c "import ipdb ; print(ipdb.__package__)"

Si muestra el nombre del paquete ``ipdb`` en la terminal, tiene correctamente
instalada la módulo. Con esto, ya tiene todo listo para continuar.


Invocando al depurador
......................

Formas de lanzar el depurador:

#. Postmortem, lanza el depurador después de que se hayan producido
   errores.

#. Lanza el módulo con el depurador.

#. Lanza al depurador desde dentro del módulo.


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
   puedes ejecutar el `script` de la siguiente forma :command:`python3 -m ipdb script.py`:

   .. sourcecode:: console

      python3 -m ipdb index_error.py

   Este comando anterior muestra lo siguiente:

   .. code-block:: pycon

       > /home/macagua/python/entrenamiento/index_error.py(1)<module>()
       ----> 1 """Small snippet to raise an IndexError."""
             2
             3

       ipdb> continue
       Traceback (most recent call last):
          File "/usr/lib/python3.11/ipdb/__main__.py", line 318, in main
            pdb._run(stdlib_pdb._ScriptTarget(mainpyfile))
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
                5     lst = list("foobar")
          ----> 6     print(lst[len(lst)])
                7

          ipdb>

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
    NOTE: Enter 'c' at the ipdb>  prompt to continue execution.
    > /home/macagua/python/entrenamiento/wiener_filtering.py(1)<module>()
    ----> 1 """Wiener filtering a noisy Lena: this module is buggy"""
          2
          3 import numpy as np
          4 import scipy as sp
          5 import pylab as pl


* Coloca un ``breakpoint`` en la línea 34 usando ``b 34``:

  .. code-block:: pycon

    ipdb> n
    > /home/macagua/python/entrenamiento/wiener_filtering.py(3)<module>()
          1 """Wiener filtering a noisy Lena: this module is buggy"""
          2
    ----> 3 import numpy as np
          4 import scipy as sp
          5 import pylab as pl

    ipdb> b 34
    Breakpoint 1 at /home/macagua/python/entrenamiento/wiener_filtering.py:34

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

    import ipdb

    ipdb.set_trace()

A continuación, se muestra un ejemplo del uso de la función ``set_trace()``:

.. literalinclude:: ../../recursos/leccion6/funcion_ipdb.py
    :language: python
    :linenos:
    :lines: 1-13

.. tip::
    Para ejecutar el código fuente de esta práctica debe invocar al módulo :file:`funcion_ipdb.py`,
    abra una consola de comando, acceda al directorio donde se encuentra el módulo :file:`funcion_ipdb.py`
    y ejecute el siguiente comando:

.. code-block:: console

    python3 funcion_ipdb.py

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console
    :class: no-copy

    > /home/macagua/python/entrenamiento/funcion_ipdb.py(6)calculo()
          5     ipdb.set_trace()
    ----> 6     if args[0]:
          7         print(args[0])

    ipdb> c
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


.. _python_modulo_ipdb_comandos:

Comandos del depurador interactivo
..................................

A continuación se muestra una tabla con los comandos más comunes
de depuración y sus descripciones:

.. tip::
    Consulte los :ref:`comandos del pdb <python_modulo_pdb_comandos>`.

============================= ======================================================================
``exceptions``                Listar o modificar la excepción actual en una cadena de excepciones
``pdef``                      Imprime la firma de llamada de cualquier objeto invocable.
``pdoc``                      Imprime la cadena de documentación de un objeto.
``pfile``                     Imprime el archivo donde se define un objeto.
``pinfo``                     Proporciona información detallada sobre un objeto.
``pinfo2``                    Proporciona información extra detallada sobre un objeto.
``psource``                   Imprime el código fuente de un objeto.
``retval``, ``rv``            Imprime el valor de retorno de la última función llamada.
``s(tep)``                    Ejecuta la línea actual, deteniéndose en la primera ocasión posible.
``skip_hidden``               Cambia si se deben omitir o no los marcos con el atributo ``__tracebackhide__``.
``skip_predicates``           La opción global de omitir (o no) los fotogramas ocultos se establece con ``skip_hidden``
============================= ======================================================================

.. warning:: **Los comandos de depuración no son código Python**

    No puedes nombrar a las variables de la forma que quieras. Por ejemplo,
    si esta dentro del depurador no podrá sobrescribir a las variables con el
    mismo y, por tanto, **habrá que usar diferentes nombres para las
    variables cuando este tecleando código en el depurador**.


.. _python_modulo_ipdb_ayuda:

Ayuda del depurador interactivo
...............................

Teclea ``h`` o ``help`` para acceder a la ayuda interactiva:

.. sourcecode:: pycon

    ipdb> help

    Documented commands (type help <topic>):
    ========================================
    EOF    commands   enable      ll        pp       s                until
    a      condition  exceptions  longlist  psource  skip_hidden      up
    alias  cont       exit        n         q        skip_predicates  w
    args   context    h           next      quit     source           whatis
    b      continue   help        p         r        step             where
    break  d          ignore      pdef      restart  tbreak
    bt     debug      j           pdoc      return   u
    c      disable    jump        pfile     retval   unalias
    cl     display    l           pinfo     run      undisplay
    clear  down       list        pinfo2    rv       unt

    Miscellaneous help topics:
    ==========================
    exec  pdb

    Undocumented commands:
    ======================
    interact


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`index_error.py <../../recursos/leccion6/index_error.py>`.

    - :download:`wiener_filtering.py <../../recursos/leccion6/wiener_filtering.py>`.

    Adicional se incluye otro código de ejemplo muy simple
    :download:`funcion_ipdb.py <../../recursos/leccion6/funcion_ipdb.py>`
    usando la función ``set_trace()`` del módulo ``ipdb``.


.. tip::
    Para ejecutar el código :file:`index_error.py`, :file:`wiener_filtering.py`
    y :file:`funcion_ipdb.py`, abra una consola de comando, acceda al directorio
    donde se encuentra ambos programas:

    .. code-block:: console
      :class: no-copy

      depuracion/
      ├── index_error.py
      ├── wiener_filtering.py
      └── funcion_ipdb.py

    Si tiene la estructura de archivo previa, entonces ejecute por separado cada comando:

    .. code-block:: console

        ipdb3 index_error.py

    .. code-block:: console

        python3 -m ipdb wiener_filtering.py

    .. code-block:: console

        python3 funcion_ipdb.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion6>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
