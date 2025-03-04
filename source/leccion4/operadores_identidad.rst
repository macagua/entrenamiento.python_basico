.. _python_opers_identidad:

Operadores de identidad
-----------------------

El operador de identidad ``is`` indica si dos variables hacen referencia al mismo objeto.
Esto implica que si dos variables distintas tienen el mismo ``id()``, el resultado de
aplicar el operador ``is`` sobre ellas será ``True``.


.. _python_opers_is:

Operador is
...........

El operador ``is``, significa, que prueba identidad: ambos lados de la expresión
condicional debe ser el mismo objecto:

.. code-block:: pycon

    >>> a, b = 10, 10.0
    >>> print(a is b)
    False
    >>> a, b = 10, 10
    >>> print(a is b)
    True

Esto es debido a que Python reutiliza el mismo objeto que almacena el valor ``10``
para ambas variables. De hecho, si usamos la función ``id()``, podemos ver que el
objeto es el mismo.

.. code-block:: pycon

    >>> a, b = 1, 1.0
    >>> id(a)
    9801248
    >>> id(b)
    140676746660560
    >>> id(a) == id(b)
    False
    >>> a, b = 1, 1
    >>> id(a)
    9807616
    >>> id(b)
    9807616
    >>> id(a) == id(b)
    True


.. _python_opers_isnot:

Operador is not
...............

El operador ``is not``, es la negación el contrario de operador :ref:`is <python_opers_is>`, devuelve
``False`` si no hacen referencia a el mismo objeto.

.. code-block:: pycon

    >>> c = 4
    >>> d = [1, 2, 3]
    >>> print(c is not d)
    True
    >>> c = 1
    >>> print(c is not d)
    False

En el ejemplo anterior, si ``b`` es una :ref:`lista <python_list>`, este prueba que ``4`` y ``1`` sean
elementos de la :ref:`lista <python_list>` ``b``.


Ejemplos
........

A continuación, se presentan algunos ejemplos de su uso:


**Operador de identidad is**:

.. literalinclude:: ../../recursos/leccion4/operadores_identidad.py
    :language: python
    :linenos:
    :lines: 7-15

El código anterior muestra el siguiente resultado:

.. code-block:: console

    Operador is
    ===========
    True
    200 su id es 9807616
    200 su id es 9807616
    False
    200 su id es 9807616
    200.0 su id es 139992306955312


**Operador de identidad is not**:

.. literalinclude:: ../../recursos/leccion4/operadores_identidad.py
    :language: python
    :linenos:
    :lines: 22-38

El código anterior muestra el siguiente resultado:

.. code-block:: console

    Operador is not
    ===============
    Python crea dos objetos diferentes, uno para cada lista. Las listas son mutables.
    True
    [1, 2, 3] su id es 140508292871232
    [1, 2, 3] su id es 140508290502400
    Python reutiliza el objeto que almacena 5 por lo que ambas variables apuntan a el mismo.
    False
    200 su id es 10875752
    200 su id es 10875752

----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic
    :download:`aquí <../../recursos/leccion4/operadores_identidad.py>`.


.. tip::
    Para ejecutar el código :file:`operadores_identidad.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    .. code-block:: console

        python3 operadores_identidad.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion4>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
