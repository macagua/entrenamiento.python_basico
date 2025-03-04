.. _python_listas_comprension:

Listas de comprensión
---------------------

La listas de comprensión, del inglés *list comprehensions*, es una funcionalidad
que le permite crear listas avanzadas en una misma línea de código.

La forma general de la definición de una lista por comprensión es:

::

    [expresion for item in iterable]

Opcionalmente, se puede incluir un condicional en la expresión:

::

    [expresion for item in iterable if condicion]

``expresion`` puede ser cualquier expresión computable en Python, generalmente
involucrando un ``item`` del iterable llamado ``iterable`` puede ser cualquier
objeto iterable, como una secuencia (:ref:`lista <python_list>` o
:ref:`cadena de caracteres <python_str>`), la función la función
:ref:`range() <python_fun_range>`, etc.

La salida siempre es un tipo de :ref:`lista <python_list>` Python.


Ejemplo 1
.........

Si requiere crear una :ref:`lista <python_list>` de 4 elementos y cada elemento calcularle la potencia
de 2, usando el método tradicional, eso seria así:

.. code-block:: pycon

    >>> lista = []
    >>> for i in range(4):
    ...     lista.append(i**2)
    ...
    >>> print(lista)
    [0, 1, 4, 9]

Entonces el ejemplo anterior usando listas de comprensión, eso seria así:

.. code-block:: pycon

    >>> [i**2 for i in range(4)]
    [0, 1, 4, 9]


Ejemplo 2
.........

A continuación se crear una :ref:`lista <python_list>` con las letras de una palabra, usando el método
tradicional, eso seria así:

.. code-block:: pycon

    >>> lista = []
    >>> for letra in "casa":
    ...     lista.append(letra)
    ...
    >>> print(lista)
    ['c', 'a', 's', 'a']


Entonces el ejemplo anterior usando listas de comprensión, eso seria así:

.. code-block:: pycon

    >>> lista = [letra for letra in "casa"]
    >>> print(lista)
    ['c', 'a', 's', 'a']

Como puede detallar en el ejemplo anterior, gracias a la listas de comprensión
usted puede indicar directamente cada elemento que va a formar la :ref:`lista <python_list>`, en este
caso cada letra, a la vez que definimos el :ref:`bucle for <python_bucle_for>`,
entonces la :ref:`lista <python_list>` está formada por cada letra que recorremos en el bucle :ref:`for <python_bucle_for>`.


Ejemplo 3
.........

A continuación se crear una :ref:`lista <python_list>` con las potencias de 2 de los primeros 10
:ref:`números <python_int>`, usando el método tradicional, eso seria así:

.. code-block:: pycon

    >>> lista = []
    >>> for numero in range(0, 11):
    ...     lista.append(numero**2)
    ...
    >>> print(lista)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Entonces el ejemplo anterior usando listas de comprensión, eso seria así:

.. code-block:: pycon

    >>> lista = [numero**2 for numero in range(0, 11)]
    >>> print(lista)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

De este código anterior usted puede aprender que es posible modificar al vuelo
los elementos los cuales van a formar la :ref:`lista <python_list>`.


Ejemplo 4
.........

A continuación se crear una :ref:`lista <python_list>` con los todos los múltiples de 2 entre 0 y 10,
usando el método tradicional, eso seria así:

.. code-block:: pycon

    >>> lista = []
    >>> for numero in range(0, 11):
    ...     lista.append(numero**2)
    ...
    >>> print(lista)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


También, si añade al código anterior, los :ref:`números <python_int>` del 0 al 10 cuando su módulo de
2 sea 0 usando el método tradicional, eso seria así:

.. code-block:: pycon

    >>> lista = []
    >>> for numero in range(0, 11):
    ...     if numero % 2 == 0:
    ...         lista.append(numero)
    ...
    >>> print(lista)
    [0, 2, 4, 6, 8, 10]

Entonces el ejemplo anterior donde crear una :ref:`lista <python_list>` con los todos los múltiples de
2 entre 0 y 10, usando listas de comprensión, eso seria así:

.. code-block:: pycon

    >>> lista = [numero for numero in range(0, 11) if numero % 2 == 0]
    >>> print(lista)
    [0, 2, 4, 6, 8, 10]

Para el ejemplo anterior donde crear una :ref:`lista <python_list>` con los todos los múltiples de 2
entre 0 y 10 cuando su módulo de 2 sea 0, usando listas de comprensión, eso seria
así:

.. code-block:: pycon

    >>> [numero for numero in range(0, 11) if numero % 2 == 0]
    [0, 2, 4, 6, 8, 10]

En este caso puede observar que incluso puede marcar una condición justo al final
para añadir o no el elemento en la :ref:`lista <python_list>`.


Ejemplo 5
.........

A continuación se crear una lista de pares a partir de otra :ref:`lista <python_list>` creada con las
potencias de 2 de los primeros 10 :ref:`números <python_int>`, usando el método tradicional, eso seria
así:

.. code-block:: pycon

    >>> lista = []
    >>> for numero in range(0, 11):
    ...     lista.append(numero**2)
    ...
    >>> pares = []
    >>> for numero in lista:
    ...     if numero % 2 == 0:
    ...         pares.append(numero)
    ...
    >>> print(pares)
    [0, 4, 16, 36, 64, 100]

Entonces el ejemplo anterior usando listas de comprensión, eso seria así:

.. code-block:: pycon

    >>> lista = [
    ...     numero for numero in [numero**2 for numero in range(0, 11)] if numero % 2 == 0
    ... ]
    >>> print(lista)
    [0, 4, 16, 36, 64, 100]

Crear :ref:`listas <python_list>` a partir de :ref:`listas <python_list>` anidadas le permite llevar la listas de comprensión
al siguiente nivel y además no hay un límite.


Usando Listas de comprensión con Archivos
.........................................

Aquí hay un posible programa que usa listas de comprensión para manipular archivos en Python 3:

.. literalinclude:: ../../recursos/leccion10/listas_comprension_archivo.py
    :language: python
    :linenos:
    :lines: 1-21

Archivo de texto a leer y manipular:

.. literalinclude:: ../../recursos/leccion10/listas_comprension_archivo.txt
    :language: text
    :linenos:
    :lines: 1-4


Este programa usa listas de comprensión para transformar cada línea del archivo de texto según
una expresión. Puedes cambiar la expresión según lo que quieras hacer con el archivo. Por ejemplo,
puedes filtrar las líneas que contienen una palabra específica, o añadir algún prefijo o sufijo a
cada línea.

Asi queda el archivo manipulado:

.. code-block:: text

    LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT, SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA.

    UT ENIM AD MINIM VENIAM, QUIS NOSTRUD EXERCITATION ULLAMCO LABORIS NISI UT ALIQUIP EX EA COMMODO CONSEQUAT.

    DUIS AUTE IRURE DOLOR IN REPREHENDERIT IN VOLUPTATE VELIT ESSE CILLUM DOLORE EU FUGIAT NULLA PARIATUR.

    EXCEPTEUR SINT OCCAECAT CUPIDATAT NON PROIDENT, SUNT IN CULPA QUI OFFICIA DESERUNT MOLLIT ANIM ID EST LABORUM.



----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces: :download:`listas_comprension_archivo.py <../../recursos/leccion10/listas_comprension_archivo.py>`
    y :download:`listas_comprension_archivo.txt <../../recursos/leccion10/listas_comprension_archivo.txt>`.


.. tip::
    Para ejecutar el código :file:`listas_comprension_archivo.py` y :file:`listas_comprension_archivo.txt`, abra una
    consola de comando, acceda al directorio donde se encuentra ambos programas:

    ::

        leccion10/
        ├── listas_comprension_archivo.py
        └── listas_comprension_archivo.txt

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        python3 listas_comprension_archivo.py

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion10>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
