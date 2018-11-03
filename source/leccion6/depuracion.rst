.. -*- coding: utf-8 -*-


.. _python_pdb:

Depuración con pdb
------------------

En este tutorial se exploran herramientas que ayudan a entender tu
código: depuración para encontrar y corregir *bugs* (errores).

El depurador python, ``pdb``:
`https://docs.python.org/2/library/pdb.html <https://docs.python.org/2/library/pdb.html>`_,
te permite inspeccionar tu código de forma interactiva.

Te permite:

-  Ver el código fuente.

-  Ir hacia arriba y hacia abajo del punto donde se ha producido
   un error.

-  Inspeccionar valores de variables.

-  Modificar valores de variables.

-  Establecer ``breakpoints`` (punto de parada del proceso).

.. topic:: **print**

    Sí, las declaraciones ``print`` sirven como herramienta de depuración. 
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

**Situación**: Estás trabajando en ``ipython`` y obtienes un error (`traceback`).

En este caso estamos depurando el fichero :download:`index_error.py <../../recursos/leccion6/index_error.py>`. Cuando lo ejecutes verás como se lanza una excepción :ref:`IndexError <python_exception_indexerror>`. Escribe ``%debug`` y entrarás en el depurador.

.. sourcecode:: ipython

    In [1]: %run index_error.py
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    /home/macagua/entrenamiento.python_basico/recursos/leccion6/index_error.py in <module>()
          6 
          7 if __name__ == '__main__':
    ----> 8     index_error()
          9 

    /home/macagua/entrenamiento.python_basico/recursos/leccion6/index_error.py in index_error()
          3 def index_error():
          4     lst = list('foobar')
    ----> 5     print lst[len(lst)]
          6 
          7 if __name__ == '__main__':

    IndexError: list index out of range

    In [2]: %debug
    > /home/macagua/entrenamiento.python_basico/recursos/leccion6/index_error.py(5)index_error()
          4     lst = list('foobar')
    ----> 5     print lst[len(lst)]
          6 

    ipdb> list
          1 """Small snippet to raise an IndexError."""
          2 
          3 def index_error():
          4     lst = list('foobar')
    ----> 5     print lst[len(lst)]
          6 
          7 if __name__ == '__main__':
          8     index_error()
          9 

    ipdb> len(lst)
    6
    ipdb> print lst[len(lst)-1]
    r
    ipdb> quit

    In [3]: 

.. topic:: Depuración post-mortem sin ipython

   En algunas situaciones no podrás usar IPython, por ejemplo para depurar
   un `script` que ha sido llamado desde la línea de comandos. En este caso,
   puedes ejecutar el `script` de la siguiente forma 
   ``python -m pdb script.py``::

    $ python -m pdb index_error.py
    > /home/macagua/entrenamiento.python_basico/recursos/leccion6/index_error.py(1)<module>()
    -> """Small snippet to raise an IndexError."""
    (Pdb) continue
    Traceback (most recent call last):
    File "/usr/lib/python2.7/pdb.py", line 1296, in main
        pdb._runscript(mainpyfile)
    File "/usr/lib/python2.7/pdb.py", line 1215, in _runscript
        self.run(statement)
    File "/usr/lib/python2.7/bdb.py", line 372, in run
        exec cmd in globals, locals
    File "<string>", line 1, in <module>
    File "index_error.py", line 8, in <module>
        index_error()
    File "index_error.py", line 5, in index_error
        print lst[len(lst)]
    IndexError: list index out of range
    Uncaught exception. Entering post mortem debugging
    Running 'cont' or 'step' will restart the program
    > /home/macagua/entrenamiento.python_basico/recursos/leccion6/index_error.py(5)index_error()
    -> print lst[len(lst)]
    (Pdb) 


Ejecución paso a paso
~~~~~~~~~~~~~~~~~~~~~

**Situación**: Crees que existe un error en un módulo pero no estás seguro donde.

Por ejemplo, estamos intentado depurar :download:`wiener_filtering.py <../../recursos/leccion6/wiener_filtering.py>`.
A pesar de que el código se ejecuta, observamos que el filtrado no se
está haciendo correctamente.

* Ejecuta el `script` en IPython con el depurador usando ``%run -d wiener_filtering.py``:

  .. sourcecode:: ipython

    In [1]: %run -d wiener_filtering.py
    *** Blank or comment
    *** Blank or comment
    *** Blank or comment
    Breakpoint 1 at /home/macagua/entrenamiento.python_basico/recursos/leccion6/wiener_filtering.py:4
    NOTE: Enter 'c' at the ipdb>  prompt to start your script.
    > <string>(1)<module>()

* Coloca un *breakpoint* en la línea 34 usando ``b 34``:

  .. sourcecode:: ipython

    ipdb> n
    > /home/macagua/entrenamiento.python_basico/recursos/leccion6/wiener_filtering.py(4)<module>()
          3 
    1---> 4 import numpy as np
          5 import scipy as sp

    ipdb> b 34
    Breakpoint 2 at /home/macagua/entrenamiento.python_basico/recursos/leccion6/wiener_filtering.py:34

* Continua la ejecución hasta el siguiente `breakpoint` con ``c(ont(inue))``:

  .. sourcecode:: ipython

    ipdb> c
    > /home/macagua/entrenamiento.python_basico/recursos/leccion6/wiener_filtering.py(34)iterated_wiener()
         33     """
    2--> 34     noisy_img = noisy_img
         35     denoised_img = local_mean(noisy_img, size=size)

* Da pasos hacia adelante y detrás del código con ``n(ext)`` y
  ``s(tep)``. ``next`` salta hasta la siguiente declaración en el actual
  contexto de ejecución mientras que ``step`` se moverá entre los contextos
  en ejecución, i.e. permitiendo explorar dentro de llamadas a funciones:

  .. sourcecode:: ipython

    ipdb> s
    > /home/macagua/entrenamiento.python_basico/recursos/leccion6/wiener_filtering.py(35)iterated_wiener()
    2    34     noisy_img = noisy_img
    ---> 35     denoised_img = local_mean(noisy_img, size=size)
         36     l_var = local_var(noisy_img, size=size)

    ipdb> n
    > /home/macagua/entrenamiento.python_basico/recursos/leccion6/wiener_filtering.py(36)iterated_wiener()
         35     denoised_img = local_mean(noisy_img, size=size)
    ---> 36     l_var = local_var(noisy_img, size=size)
         37     for i in range(3):


* Muévete unas pocas líneas y explora las variables locales:

  .. sourcecode:: ipython

    ipdb> n
    > /home/macagua/entrenamiento.python_basico/recursos/leccion6/wiener_filtering.py(37)iterated_wiener()
         36     l_var = local_var(noisy_img, size=size)
    ---> 37     for i in range(3):
         38         res = noisy_img - denoised_img
    ipdb> print l_var
    [[5868 5379 5316 ..., 5071 4799 5149]
     [5013  363  437 ...,  346  262 4355]
     [5379  410  344 ...,  392  604 3377]
     ..., 
     [ 435  362  308 ...,  275  198 1632]
     [ 548  392  290 ...,  248  263 1653]
     [ 466  789  736 ..., 1835 1725 1940]]
    ipdb> print l_var.min()
    0

*Oh dear*, solo vemos enteror y variación 0. Aquí está nuestro error,
estamos haciendo aritmética con enteros.

.. topic:: Lanzando excepciones en errores numéricos

    Cuando ejecutamos el fichero :download:`wiener_filtering.py <../../recursos/leccion6/wiener_filtering.py>`, 
    se lanzarán los siguientes avisos:

    .. sourcecode:: ipython

        In [2]: %run wiener_filtering.py
        wiener_filtering.py:40: RuntimeWarning: divide by zero encountered in divide
            noise_level = (1 - noise/l_var )

    Podemos convertir estos avisos a excepciones, lo que nos permitiría
    hacer una depuración post-mortem sobre ellos y encontrar el problema
    de manera más rápida:

    .. sourcecode:: ipython

        In [3]: np.seterr(all='raise')
        Out[3]: {'divide': 'print', 'invalid': 'print', 'over': 'print', 'under': 'ignore'}
        In [4]: %run wiener_filtering.py
        ---------------------------------------------------------------------------
        FloatingPointError                        Traceback (most recent call last)
        /home/macagua/venv/lib/python2.7/site-packages/IPython/utils/py3compat.pyc in execfile(fname, *where)
            176             else:
            177                 filename = fname
        --> 178             __builtin__.execfile(filename, *where)

        /home/macagua/entrenamiento.python_basico/recursos/leccion6/wiener_filtering.py in <module>()
             55 pl.matshow(noisy_lena[cut], cmap=pl.cm.gray)
             56 
        ---> 57 denoised_lena = iterated_wiener(noisy_lena)
             58 pl.matshow(denoised_lena[cut], cmap=pl.cm.gray)
             59 

        /home/macagua/entrenamiento.python_basico/recursos/leccion6/wiener_filtering.py in iterated_wiener(noisy_img, size)
             38         res = noisy_img - denoised_img
             39         noise = (res**2).sum()/res.size
        ---> 40         noise_level = (1 - noise/l_var )
             41         noise_level[noise_level<0] = 0
             42         denoised_img += noise_level*res
        FloatingPointError: divide by zero encountered in divide


Otras formas de comenzar una depuración
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Lanzar una excepción "break point" a lo pobre**

  Si encuentras tedioso el tener que anotar el número de línea para colocar
  un *break point*, puedes lanzar una excepción en el punto que quieres 
  inspeccionar y usar la 'magia' ``%debug`` de ``ipython``. Destacar que en este
  caso no puedes moverte por el código y continuar después la ejecución.

* **Depurando fallos de pruebas usando nosetests**

  Podemos ejecutar ``nosetests --pdb`` para saltar a la depuración
  post-mortem de excepciones y ``nosetests --pdb-failure`` para inspeccionar
  los fallos de pruebas usando el depurador.

  Además, puedes usar la interfaz IPython para el depurador en **nose**
  usando el plugin  de **nose**
  `ipdbplugin <https://pypi.org/project/ipdbplugin>`_. Podremos, entonces,
  pasar las opciones ``--ipdb`` y ``--ipdb-failure`` a los *nosetests*.

* **Llamando explícitamente al depurador**

  Inserta la siguiente línea donde quieres que salte el depurador::

    import pdb; pdb.set_trace()

.. warning::

    Cuandos e ejecutan ``nosetests``, se captura la salida y parecerá
    que el depurador no está funcionando. Para evitar esto simplemente ejecuta
    los ``nosetests`` con la etiqueta ``-s``.


.. topic:: Depuradores gráficos y alternativas

    * Quizá encuentres más conveniente usar un depurador gráfico como  
      `winpdb <https://pypi.org/project/winpdb/>`_. para inspeccionar saltas a través del 
      código e inspeccionar las variables

    * De forma alternativa, `pudb <https://pypi.org/project/pudb>`_ es un 
      buen depurador semi-gráfico con una interfaz de texto en la consola.

    * También, estaría bien echarle un ojo al proyecto 
      `pydbgr <https://code.google.com/archive/p/pydbgr>`_

Comandos del depurador e interacciones
......................................

============ ======================================================================
``l(list)``   Lista el código en la posición actual
``u(p)``      Paso arriba de la llamada a la pila (*call stack*)
``d(own)``    Paso abajo de la llamada a la pila ((*call stack*)
``n(ext)``    Ejecuta la siguiente línea (no va hacia abajo en funciones nuevas)
``s(tep)``    Ejecuta la siguiente declaración (va hacia abajo en las nuevas funciones)
``bt``        Muestra el *call stack*
``a``         Muestra las variables locales
``!command``  Ejecuta el comando **Python** proporcionado (en oposición a comandos pdb)
============ ======================================================================

.. warning:: **Los comandos de depuración no son código Python**

    No puedes nombrar a las variables de la forma que quieras. Por ejemplo,
    si estamos dentro del depurador no podremos sobrescribir a las variables 
    con el mismo y, por tanto, **habrá que usar diferentes nombres para las
    variables cuando estemos tecleando código en el depurador**.

Obteniendo ayuda dentro del depurador
.....................................

Teclea ``h`` o ``help`` para acceder a la ayuda interactiva:

.. sourcecode:: pycon

    ipdb> help

    Documented commands (type help <topic>):
    ========================================
    EOF    bt         cont      enable  jump  pdef   r        tbreak   w
    a      c          continue  exit    l     pdoc   restart  u        whatis
    alias  cl         d         h       list  pinfo  return   unalias  where
    args   clear      debug     help    n     pp     run      unt
    b      commands   disable   ignore  next  q      s        until
    break  condition  down      j       p     quit   step     up

    Miscellaneous help topics:
    ==========================
    exec  pdb

    Undocumented commands:
    ======================
    retval  rv

.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los 
    siguientes enlaces: :download:`index_error.py <../../recursos/leccion6/index_error.py>` 
    y :download:`wiener_filtering.py <../../recursos/leccion6/wiener_filtering.py>`. 
    Adicional se incluye otro código de ejemplo muy simple 
    :download:`funcion_a_depurar.py <../../recursos/leccion6/funcion_a_depurar.py>` 
    usando la función ``set_trace()`` del paquete ``pdb``.


.. tip::
    Para ejecutar el código :file:`index_error.py`, :file:`wiener_filtering.py` 
    y :file:`funcion_a_depurar.py`, abra una consola de comando, acceda al directorio 
    donde se encuentra ambos programas: ::

      leccion6/
      ├── index_error.py
      ├── wiener_filtering.py
      └── funcion_a_depurar.py

    Si tiene la estructura de archivo previa, entonces ejecute por separado cada comando: ::

        python2 index_error.py
        python2 wiener_filtering.py
        python2 funcion_a_depurar.py


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion6>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
