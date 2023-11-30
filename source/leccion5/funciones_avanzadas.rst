.. -*- coding: utf-8 -*-


.. _python_fun_avanzadas:

Funciones avanzadas
-------------------

En Python hay varias funciones avanzadas que se describen a continuación:


.. _python_fun_predicado:

Funciones de predicado
......................

Las funciones de predicado no es más que una función la cual dice si algo es ``True``
o ``False``, es decir, es una función que devuelve un tipo de datos
:ref:`booleano <python_bool>`.

.. comments:

    .. todo::
        TODO terminar de escribir la sección Funciones de predicado.


.. comments:

    Objetos de función
    ..................

    .. todo::
        TODO escribir la sección Objetos de función.


.. _python_fun_anonimas:

Funciones anónimas
..................

Una función anónima, como su nombre indica es una función sin nombre. Es decir, es
posible ejecutar una función sin referenciar un nombre, en Python puede ejecutar
una función sin definirla con ``def``.

De hecho son similares pero con una diferencia fundamental, **el contenido de una
función anónima debe ser una única expresión en lugar de un bloque de acciones**.

Las funciones anónimas se implementan en Python con las funciones o expresiones
:ref:`lambda <python_expresion_lambda>`, esta es unas de las funcionalidades más
potentes de Python, pero a la vez es la más confusas para los principiantes.

Más allá del sentido de función que usted tiene hasta el momento, con su nombre y
sus acciones internas, una función en su sentido más trivial significa realizar algo
sobre algo. Por tanto se podría decir que, mientras las funciones anónimas
``lambda`` sirven para realizar funciones simples, las funciones definidas con
``def`` sirven para manejar tareas más extensas.


.. _python_expresion_lambda:

Expresión lambda
................

Si deconstruye una función sencilla, puede llegar a una función ``lambda``. Por ejemplo
la siguiente función es para doblar un valor de un número:

.. code-block:: pycon

    >>> def doblar(numero):
    ...     resultado = numero * 2
    ...     return resultado
    ...

    >>> doblar(2)
    4
    >>> type(doblar)
    <type 'function'>


Si el código fuente anterior se simplifica se verá, de la siguiente forma:

.. code-block:: pycon

    >>> def doblar(numero):
    ...     return numero * 2
    ...

    >>> doblar(2)
    4
    >>> type(doblar)
    <type 'function'>


Usted puede todavía simplificar más, escribirlo todo en una sola línea, de la
siguiente forma:

.. code-block:: pycon

    >>> def doblar(numero):
    ...     return numero * 2
    ...

    >>> doblar(2)
    4
    >>> type(doblar)
    <type 'function'>
    >>> lambda numero: numero * 2
    <function <lambda> at 0x7f1023944e60>


Esta notación simple es la que una función ``lambda`` intenta replicar, observe,
a continuación se va a convertir la función en una función anónima:

.. code-block:: pycon

    >>> lambda numero: numero * 2
    <function <lambda> at 0x7f1023944e60>

En este ejemplo tiene una función anónima con una entrada que recibe ``numero``,
y una salida que devuelve ``numero * 2``.

Lo único que necesita hacer para utilizarla es guardarla en una variable y utilizarla
tal como haría con una función normal:

.. code-block:: pycon

    >>> doblar = lambda numero: numero * 2
    >>> doblar(2)
    4
    >>> type(doblar)
    <type 'function'>


Con la flexibilidad de Python usted puede implementar infinitas funciones simples.
Usted puede encontrar más ejemplos de funciones anónimas usando ``lambda`` en la
sección :ref:`ejemplos de funciones avanzadas <python_fun_avanzadas_ejs>`.

Usted puede explotar al máximo la función lambda utilizándola en conjunto con otras
funciones como :ref:`filter() <python_fun_filter>` y :ref:`map() <python_fun_map>`.


.. _python_fun_avanzadas_ejs:

Ejemplos de funciones avanzadas
...............................

A continuación, se presentan algunos ejemplos de su uso:


**Función lambda - operaciones aritméticas**

A continuación, se presenta un ejemplo para comprobar si un número es impar:

.. code-block:: pycon

    >>> impar = lambda numero: numero % 2 != 0
    >>> impar(5)
    True


**Función lambda - operaciones de cadena**

A continuación, se presenta un ejemplo para darle la vuelta a una :ref:`cadena <python_str>` rebanándola
en sentido inverso:

.. code-block:: pycon

    >>> revertir = lambda cadena: cadena[::-1]
    >>> revertir("Plone")
    'enolP'
    >>> revertir("enolP")
    'Plone'


**Función lambda - varios parámetros**

A continuación, se presenta un ejemplo para varios parámetros, por ejemplo para
sumar dos :ref:`números <python_int>`:

.. code-block:: pycon

    >>> sumar = lambda x, y: x + y
    >>> sumar(5, 2)
    7


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion5>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
