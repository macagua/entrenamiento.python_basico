.. -*- coding: utf-8 -*-


.. _python_variable_constante:

Variables y constantes
----------------------


.. _python_variable:

Variables
.........

Es un nombre que se refiere a un objeto que reside en la memoria. 
El objeto puede ser de alguno de los tipos vistos (número o cadena 
de texto), o alguno de los otros tipos existentes en Python.

Cada variable debe tener un nombre único llamado identificador. Eso es muy 
de ayuda pensar las variables como contenedores que contienen data el cual 
puede ser cambiado después a través de técnicas de programación.


Ejemplos de variables
~~~~~~~~~~~~~~~~~~~~~

A continuación, se presentan algunos ejemplos del uso de *variables*:

**Ejemplo de asignar valor a variable**

A continuación, se creará un par de variables a modo de ejemplo. Una 
de tipo :ref:`cadenas de caracteres <python_cadenas>` y una de tipo 
:ref:`entero <python_num_entero>`:

::

	>>> c = "Hola Mundo" # cadenas de caracteres
	>>> type(c) # comprobar tipo de dato
	<type 'str'>
	>>> e = 23 # número entero
	>>> type(e) # comprobar tipo de dato
	<type 'int'>
	>>> 

Como puede ver en Python, a diferencia de muchos otros lenguajes, no se
declara el tipo de la variable al crearla. En *Java*, por ejemplo,
definir una variable seria así:

.. sourcecode:: java

    String c = "Hola Mundo";
    int e = 23;

También nos ha servido el pequeño ejemplo para presentar los
comentarios en linea en Python: cadenas de caracteres que comienzan con el
carácter ``#`` y que Python ignora totalmente. Hay más tipos de 
:ref:`comentarios <python_cadenas_comentarios>`, de los cuales se 
tratarán más adelante.

----

**Ejemplo de cambiar valor a variable**

A continuación, se cambiará el valor para una variable de tipo 
:ref:`cadenas de caracteres <python_cadenas>` a modo de ejemplo: 

::

	>>> c = "Hola Python" # cadenas de caracteres
	>>> c
	'Hola Python'
	>>>

----

**Ejemplo de asignar múltiples valores a a múltiples variables**

A continuación, se creará múltiples variables (:ref:`entero <python_num_entero>`, 
:ref:`coma flotante <python_coma_flotante>`, :ref:`cadenas de caracteres <python_cadenas>`) 
asignando múltiples valores:

::

	>>> a, b, c = 5, 3.2, "Hello"
	>>> print a
	5
	>>> print b
	3.2
	>>> print c
	'Hello'
	>>> 

Si usted quiere asignar el mismo valor a múltiples variables al mismo tiempo, 
usted puede hacer lo siguiente:

::

	>>> x = y = z = True
	>>> print x
	True
	>>> print y
	True
	>>> print z
	True
	>>> 

El segundo programa asigna el mismo valor booleano a todas las tres variables ``x``, 
``y``, ``z``.

----

.. _python_constante:

Constantes
..........

Una constante es un tipo de variable la cual no puede ser cambiada. Eso es muy 
de ayuda pensar las constantes como contenedores que contienen información el 
cual no puede ser cambiado después.

En Python, las constantes son usualmente declaradas y asignadas en un módulo. 
Aquí, el módulo significa un nuevo archivo que contiene variables, funciones, 
etc; el cual es importada en el archivo principal. Dentro del módulo, las 
constantes son escritas en letras MAYÚSCULAS y separadas las palabras con el 
carácter *underscore* ``_``.


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
	Valor especial que puede ser devuelto por los métodos especiales de 
	"comparación rica" (``__eq__()``, ``__lt__()`` y amigos), para indicar que 
	la comparación no se implementa con respecto al otro tipo.

``Ellipsis``
	Valor especial utilizado junto con la sintaxis de corte ampliada. Véase también el 
	objeto :ref:`elipsis <python_objeto_ellipsis>`.

``__debug__``
	Esta constante es ``True`` si Python no se inició con una opción ``-O``. 
	Véase también la sentencia :ref:`assert <python_sentencia_assert>`.

.. note:: 
	Los nombres ``None`` y ``__debug__`` no se pueden reasignar (asignaciones 
	a ellos, incluso como un nombre de atributo, causa una excepción 
	:ref:`SyntaxError <python_exception_syntaxerror>`), por lo que pueden 
	considerarse constantes "verdaderas".


Ejemplo de constantes
~~~~~~~~~~~~~~~~~~~~~

A continuación, se presentan algunos ejemplos del uso de *constantes*:

**Ejemplo de constantes desde un módulo externo**

Crear un archivo ``constantes.py`` con el siguiente contenido:

.. literalinclude:: ../../recursos/leccion3/constantes.py
    :linenos:
    :language: python
    :lines: 4-9

Crear un archivo ``main.py``

.. literalinclude:: ../../recursos/leccion3/main.py
    :linenos:
    :language: python
    :lines: 4-9

Cuando usted ejecuta el programa, la salida será:

::

    scp -v -P 3307 root@127.0.0.1:/root/webapp/db.sql /srv/backup

En el programa anterior, existe un archivo de módulo ``constantes.py``. Entonces en 
este se asignan los valores de constantes ``IP_DB_SERVER``, ``PORT_DB_SERVER``, 
``USER_DB_SERVER``, ``PASSWORD_DB_SERVER`` y ``DB_NAME``. Ademas, existe el archivo 
de módulo ``main.py`` el cual importa el módulo ``constantes``. Finalmente, se imprime 
una linea de conexión del comando ``scp`` de Linux usando la función integrada en la 
librería estándar Python llamada :ref:`format <python_funcion_format>`.

.. note:: 
    En realidad, no se usa las constantes en Python. El módulo ``globals`` o ``constants`` 
    es usado a lo largo de los programas de Python.

----


.. _python_palabras_reservadas:

Palabras reservadas
...................

Existen ciertas palabras que tienen significado especial para el intérprete de Python. Estas 
no pueden utilizarse para ningún otro fin (como ser nombrar valores) excepto para el que han 
sido creadas. Estas son:


- :ref:`and <python_operadores_logicos>`.

- ``as``.

- :ref:`assert <python_sentencia_assert>`.

- :ref:`break <python_sentencia_break>`.

- :ref:`class <python_clases>`.

- :ref:`continue <python_sentencia_continue>`.

- :ref:`def <python_funciones>`.

- ``del``.

- :ref:`elif <python_condicional_if>`.

- :ref:`else <python_condicional_if>`.

- :ref:`except <python_sentencia_try_except>`.

- ``exec``.

- :ref:`finally <python_sentencia_finally>`.

- :ref:`for <python_bucle_for>`.

- :ref:`from <python_sentencia_from>`.

- ``global``.

- :ref:`if <python_condicional_if>`.

- :ref:`import <python_sentencia_import>`.

- :ref:`in <python_expresiones_condicional>`.

- :ref:`is <python_expresiones_condicional>`.

- :ref:`lambda <python_funcion_lambda>`.

- :ref:`not <python_operadores_logicos>`.

- :ref:`or <python_operadores_logicos>`.

- :ref:`pass <python_sentencia_pass>`.

- :ref:`print <python_salida>`.

- :ref:`raise <python_sentencia_raise>`.

- :ref:`return <python_sentencia_return>`.

- :ref:`try <python_sentencia_try_except>`.

- :ref:`while <python_bucle_while>`.

- :ref:`with <python_sentencia_with>`.

- ``yield``.


.. note:: Para Python 2.7 son un total de 31 palabras reservadas.


Puede verificar si una palabra esta reservada utilizando el módulo integrado 
``keyword``, de la siguiente forma:

::

	>>> import keyword
	>>> keyword.iskeyword('as')
	>>> keyword.iskeyword('x')

Para obtener una lista de todas las palabras reservadas

::

	>>> import keyword
	>>> keyword.kwlist


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
