.. -*- coding: utf-8 -*-


.. _python_variable_constante:

Variables y constantes
----------------------


.. _python_variable:

Variables
.........

Es un nombre que se refiere a un objeto que reside en la memoria. El objeto puede ser 
de alguno de los tipos vistos (número o cadena de texto), o alguno de los otros tipos 
existentes en Python.

Cada variable debe tener un nombre único llamado identificador. Eso es muy de ayuda 
pensar las variables como contenedores que contienen data el cual puede ser cambiado 
después a través de técnicas de programación.


.. _python_alcance_variables:

Alcance de las variables
~~~~~~~~~~~~~~~~~~~~~~~~

Las variables en Python son locales por defecto. Esto quiere decir que las variables 
definidas y utilizadas en el bloque de código de una :ref:`función <python_funciones>`, 
sólo tienen existencia dentro de la misma, y no interfieren con otras variables del 
resto del código.

A su vez, las variables existentes fuera de una :ref:`función <python_funciones>`, no 
son visibles dentro de la misma.

En caso de que sea conveniente o necesario, una variable local puede convertirse en 
una variable global declarándola explícitamente como tal con la sentencia 
:ref:`global <python_sent_global>`.


Ejemplos de variables
~~~~~~~~~~~~~~~~~~~~~

A continuación, se presentan algunos ejemplos del uso de *variables*:

**Ejemplo de asignar valor a variable**

A continuación, se creará un par de variables a modo de ejemplo. Una de tipo 
:ref:`cadenas de caracteres <python_str>` y una de tipo 
:ref:`entero <python_num_entero>`:

::

    >>> c = "Hola Mundo" # cadenas de caracteres
    >>> type(c) # comprobar tipo de dato
    <type 'str'>
    >>> e = 23 # número entero
    >>> type(e) # comprobar tipo de dato
    <type 'int'>

Como puede ver en Python, a diferencia de muchos otros lenguajes, no se declara el 
tipo de la variable al crearla. En *Java*, por ejemplo, definir una variable seria 
así:

.. sourcecode:: java

    String c = "Hola Mundo";
    int e = 23;

También nos ha servido el pequeño ejemplo para presentar los comentarios en linea en 
Python: cadenas de caracteres que comienzan con el carácter ``#`` y que Python ignora 
totalmente. Hay más tipos de :ref:`comentarios <python_str_comentarios>`, de los 
cuales se tratarán más adelante.

----

**Ejemplo de cambiar valor a variable**

A continuación, se cambiará el valor para una variable de tipo 
:ref:`cadenas de caracteres <python_str>` a modo de ejemplo: 

::

    >>> c = "Hola Plone" # cadenas de caracteres
    >>> c
    'Hola Plone'

----

**Ejemplo de asignar múltiples valores a a múltiples variables**

A continuación, se creará múltiples variables (:ref:`entero <python_num_entero>`, 
:ref:`coma flotante <python_num_float>`, :ref:`cadenas de caracteres <python_str>`) 
asignando múltiples valores:

::

    >>> a, b, c = 5, 3.2, "Hello"
    >>> print a
    5
    >>> print b
    3.2
    >>> print c
    'Hello'

Si usted quiere asignar el mismo valor a múltiples variables al mismo tiempo, usted 
puede hacer lo siguiente:

::

    >>> x = y = z = True
    >>> print x
    True
    >>> print y
    True
    >>> print z
    True

El segundo programa asigna el mismo valor booleano a todas las tres variables ``x``, 
``y``, ``z``.



----

.. _python_constante:

Constantes
..........

Una constante es un tipo de variable la cual no puede ser cambiada. Eso es muy de 
ayuda pensar las constantes como contenedores que contienen información el cual no 
puede ser cambiado después.

En Python, las constantes son usualmente declaradas y asignadas en un módulo. Aquí, 
el módulo significa un nuevo archivo que contiene variables, funciones, etc; el cual 
es importada en el archivo principal. Dentro del módulo, las constantes son escritas 
en letras MAYÚSCULAS y separadas las palabras con el carácter *underscore* ``_``.


Constantes integradas
~~~~~~~~~~~~~~~~~~~~~

Un pequeño número de constantes vive en el espacio de nombres incorporado. Son:

``False``
    El valor falso del tipo :ref:`booleano <python_booleanos>`.

``True``
    El valor verdadero del tipo :ref:`booleano <python_booleanos>`.

``None``
    El valor único de objeto :ref:`types.NoneType <python_objeto_none>`. ``None`` 
    se utiliza con frecuencia para representar la ausencia de un valor, como cuando 
    los argumentos predeterminados no se pasan a una función.

``NotImplemented``
    Valor especial que puede ser devuelto por los métodos especiales de "comparación 
    rica" (``__eq__()``, ``__lt__()`` y amigos), para indicar que la comparación no 
    se implementa con respecto al otro tipo.

``Ellipsis``
    Valor especial utilizado junto con la sintaxis de corte ampliada. Véase también 
    el objeto :ref:`elipsis <python_objeto_ellipsis>`.

``__debug__``
    Esta constante es ``True`` si Python no se inició con una opción ``-O``. Véase 
    también la sentencia :ref:`assert <python_sent_assert>`.

.. note:: 
    Los nombres ``None`` y ``__debug__`` no se pueden reasignar (asignaciones a ellos, 
    incluso como un nombre de atributo, causa una excepción 
    :ref:`SyntaxError <python_exception_syntaxerror>`), por lo que pueden considerarse 
    constantes "verdaderas".


Ejemplo de constantes
~~~~~~~~~~~~~~~~~~~~~

A continuación, se presentan algunos ejemplos del uso de *constantes*:

**Ejemplo de constantes desde un módulo externo**

Crear un archivo ``constantes.py`` con el siguiente contenido:

.. literalinclude:: ../../recursos/leccion3/constantes.py
    :linenos:
    :language: python
    :lines: 5-9

Crear un archivo ``main.py``

.. literalinclude:: ../../recursos/leccion3/main.py
    :linenos:
    :language: python
    :lines: 4-9

Cuando usted ejecuta el programa, la salida será:

::

    scp -v -P 3307 root@127.0.0.1:/root/webapp/db.sql /srv/backup

En el programa anterior, existe un archivo de módulo ``constantes.py``. Entonces 
en este se asignan los valores de constantes ``IP_DB_SERVER``, ``PORT_DB_SERVER``, 
``USER_DB_SERVER``, ``PASSWORD_DB_SERVER`` y ``DB_NAME``. Ademas, existe el archivo 
de módulo ``main.py`` el cual importa el módulo ``constantes``. Finalmente, se 
imprime una linea de conexión del comando ``scp`` de Linux usando la función 
integrada en la librería estándar Python llamada :ref:`format() <python_fun_format>`.

.. note:: 
    En realidad, no se usa las constantes en Python. El módulo ``globals`` o 
    ``constants`` es usado a lo largo de los programas de Python.

----


.. _python_palabras_reservadas:

Palabras reservadas
...................

Existen ciertas palabras que tienen significado especial para el intérprete de Python. 
Estas no pueden utilizarse para ningún otro fin (como ser nombrar valores) excepto 
para el que han sido creadas. Estas son:

- :ref:`and <python_opers_logicos>`.

- ``as``.

- :ref:`assert <python_sent_assert>`.

- :ref:`break <python_sent_break>`.

- :ref:`class <python_clases>`.

- :ref:`continue <python_sent_continue>`.

- :ref:`def <python_sent_def>`.

- :ref:`del <python_sent_del>`.

- :ref:`elif <python_sent_elif>`.

- :ref:`else <python_sent_else>`.

- :ref:`except <python_sent_try_except>`.

- ``exec``.

- :ref:`finally <python_sent_finally>`.

- :ref:`for <python_bucle_for>`.

- :ref:`from <python_sent_from>`.

- :ref:`global <python_sent_global>`.

- :ref:`if <python_sent_if>`.

- :ref:`import <python_sent_import>`.

- :ref:`in <python_opers_in>`.

- :ref:`is <python_opers_is>`.

- :ref:`lambda <python_fun_lambda>`.

- :ref:`not <python_opers_logicos>`.

- :ref:`or <python_opers_logicos>`.

- :ref:`pass <python_sent_pass>`.

- :ref:`print <python_salida>`.

- :ref:`raise <python_sent_raise>`.

- :ref:`return <python_sent_return>`.

- :ref:`try <python_sent_try_except>`.

- :ref:`while <python_bucle_while>`.

- :ref:`with <python_sent_with>`.

- ``yield``.


.. note:: Para Python 2.7 son un total de 31 palabras reservadas.


Puede verificar si una palabra esta reservada utilizando el módulo integrado 
``keyword``, de la siguiente forma:

::

    >>> import keyword
    >>> keyword.iskeyword('as')
    True
    >>> keyword.iskeyword('x')
    False

Para obtener una lista de todas las palabras reservadas

::

    >>> import keyword
    >>> keyword.kwlist
    ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 
    'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 
    'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 
    'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 
    'with', 'yield']


----


Reglas y convención de nombres
..............................

Algunas reglas y convenciones de nombres para las :ref:`variables <python_variable>` 
y :ref:`constantes <python_constante>`:

- Nunca use símbolos especiales como !, @, #, $, %, etc.

- El primer carácter no puede ser un número o dígito.

- Las constantes son colocadas dentro de módulos Python y significa 
  que no puede ser cambiado.

- Los nombres de constante y variable debería tener la combinación de letras en 
  minúsculas (de *a* a la *z*) o MAYÚSCULAS (de la *A* a la *Z*) o dígitos (del 
  *0* al *9*) o un ``underscore`` (_). Por ejemplo:

    - snake_case

    - MACRO_CASE

    - camelCase

    - CapWords

- Los nombres que comienzan con guión bajo (simple ``_`` o doble ``__``) se reservan para 
  variables con significado especial

- No pueden usarse como identificadores, las :ref:`palabras reservadas <python_palabras_reservadas>` .


----


.. _python_sent_del:

Sentencia del
.............

La sentencia ``del`` se define recursivamente muy similar a la forma en el cual se 
define la asignación. A continuación unos ejemplos donde se inicializan variables:

::

    >>> cadena, numero, lista = "Hola Plone", 123456, [7,8,9,0]
    >>> tupla = (11, "Chao Plone", True, None)
    >>> diccionario = {"nombres":"Leonardo Jose","apellidos":"Caballero Garcia"}

Luego de inicializar las variables del código anterior, usted puede usar la función 
:ref:`vars() <python_fun_vars>` para obtener un diccionario conteniendo ámbito 
actual de las variables, ejecutando:

::

    >>> vars()
    {'tupla': (11, 'Chao Plone', True, None), 
    '__builtins__': <module '__builtin__' (built-in)>, 
    'numero': 123456, '__package__': None, 'cadena': 'Hola Plone', 
    'diccionario': {'apellidos': 'Caballero Garcia', 'nombres': 'Leonardo Jose'}, 
    '__name__': '__main__', 'lista': [7, 8, 9, 0], '__doc__': None}


Si desea eliminar la referencia a la variable ``cadena``, ejecuta:

::

    >>> del cadena
    >>> vars()
    {'tupla': (11, 'Chao Plone', True, None), 
    '__builtins__': <module '__builtin__' (built-in)>, 
    'numero': 123456, '__package__': None, 
    'diccionario': {'apellidos': 'Caballero Garcia', 
    'nombres': 'Leonardo Jose'}, '__name__': '__main__', 
    'lista': [7, 8, 9, 0], '__doc__': None}

Como pudo ver en el ejemplo anterior que elimino la referencia a la variable ``cadena``,
incluso al volver a la función :ref:`vars() <python_fun_vars>` ya no sale en el 
ámbito de variables disponibles.

La eliminación de una lista de objetivos elimina recursivamente cada objetivo, de 
izquierda a derecha.

::

    >>> del numero, lista, tupla, diccionario
    >>> vars()
    {'__builtins__': <module '__builtin__' (built-in)>, 
    '__package__': None, '__name__': '__main__', '__doc__': None}

Como pudo ver en el ejemplo anterior que elimino las referencias a las variables ``numero``, 
``lista``, ``tupla``, ``diccionario`` que incluso al volver a la función 
:ref:`vars() <python_fun_vars>` ya no están en el ámbito de variables disponibles.

La eliminación de un nombre elimina el enlace de ese nombre del espacio de nombres 
*local* o *global*, dependiendo de si el nombre aparece en una sentencia 
":ref:`global <python_sent_global>`" en el mismo bloque de código. Si el nombre 
no está vinculado, se generará una excepción ":ref:`NameError <python_exception_nameerror>`".

.. tip::

    Es ilegal eliminar un nombre del espacio de nombres *local* si aparece como una 
    variable libre en un bloque anidado.

La eliminación de las referencias de atributos, suscripciones y segmentaciones se pasa 
al objeto primario involucrado; la eliminación de un corte es en general equivalente a 
la asignación de un corte vacío del tipo correcto (pero incluso esto está determinado 
por el objeto cortado).


.. _python_sent_global:

Sentencia global
................

La sentencia ``global`` es una declaración que se mantiene para todo el bloque de 
código actual. Eso significa que los identificadores listados son interpretados como 
globales. Eso podría ser imposible asignar a una variable global sin la sentencia 
``global``, aunque las variables libres pueden referirse a globales sin ser declaradas 
globales.

::

    >>> variable1 = "variable original"
    >>> def variable_global():
    ...     global variable1
    ...     variable1 = "variable global modificada"
    ... 
    >>> print variable1
    variable original
    >>> variable_global()
    >>> print variable1
    variable global modificada

Como se puede ver, después de llamar a la función ``variable_global()``, la variable 
``variable1`` queda modificada. En general, este procedimiento debe utilizarse con 
precaución.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los 
    siguientes enlaces: :download:`constantes.py <../../recursos/leccion3/constantes.py>` 
    y :download:`main.py <../../recursos/leccion3/main.py>`.


.. tip::
    Para ejecutar el código :file:`constantes.py` y :file:`main.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra ambos programas:

    ::

        leccion3/
        ├── constantes.py
        └── main.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    ::

        python constantes.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
