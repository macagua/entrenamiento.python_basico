.. -*- coding: utf-8 -*-


.. _python_funciones:

Funciones
---------

Una función es un bloque de código con un nombre asociado, que recibe cero o más 
argumentos como entrada, sigue una secuencia de sentencias, la cuales ejecuta una 
operación deseada y devuelve un valor y/o realiza una tarea, este bloque puede ser 
llamados cuando se necesite.

El uso de funciones es un componente muy importante del paradigma de la programación 
llamada :ref:`estructurada <python_programacion_estructurada>`, y tiene varias 
ventajas:

- **modularización**: permite segmentar un programa complejo en una serie de partes 
  o módulos más simples, facilitando así la programación y el depurado.

- **reutilización**: permite reutilizar una misma función en distintos programas.

Python dispone de una serie de :ref:`funciones integradas <python_fun_builtins>` 
al lenguaje, y también permite crear funciones definidas por el usuario para ser 
usadas en su propios programas.

.. _python_sent_def:

Sentencia def
.............

La sentencia ``def`` es una definición de función usada para crear objetos **funciones 
definidas por el usuario**.

Una definición de función es una sentencia ejecutable. Su ejecución enlaza el nombre 
de la función en el namespace local actual a un objecto función (un envoltorio 
alrededor del código ejecutable para la función). Este objeto función contiene una 
referencia al namespace local global como el namespace global para ser usado cuando 
la función es llamada.

La definición de función no ejecuta el cuerpo de la función; esto es ejecutado solamente 
cuando la función es llamada.

La sintaxis para una definición de función en Python es:

::

    def NOMBRE(LISTA_DE_PARAMETROS):
        """DOCSTRING_DE_FUNCION"""
        SENTENCIAS
        RETURN [EXPRESION]

A continuación se detallan el significado de pseudo código fuente anterior:

- ``NOMBRE``, es el nombre de la función.

- ``LISTA_DE_PARAMETROS``, es la lista de parámetros que puede recibir una 
  función.

- ``DOCSTRING_DE_FUNCION``, es la cadena de caracteres usada para 
  :ref:`documentar <python_str_docstrings_def>` la función.

- ``SENTENCIAS``, es el bloque de sentencias en código fuente Python que realizar 
  cierta operación dada.

- ``RETURN``, es la :ref:`sentencia return <python_sent_return>` en código 
  Python.

- ``EXPRESION``, es la expresión o variable que devuelve la sentencia ``return``.


Un ejemplo simple de función esta seguidamente:

::

    >>> def hola(arg):
    ...     """El docstring de la función"""
    ...     print "Hola", arg, "!"
    ... 
    >>> hola("Plone")
    Hola Plone !


.. warning:: 
    Los bloques de ``function`` deben estar indentado como otros 
    bloques estructuras de control.

La palabra reservada ``def`` se usa para definir funciones. Debe seguirle el nombre 
de la función en el ejemplo anterior ``hola()`` y la lista de parámetros formales 
entre paréntesis. Las sentencias que forman el cuerpo de la función empiezan en la 
línea siguiente, y deben estar indentado.

La primer sentencia del cuerpo de la función puede ser opcionalmente una cadenas de 
caracteres literal; esta es la cadenas de caracteres de documentación de la función, 
o ``docstrings``. (Puedes encontrar más acerca de ``docstrings`` en la sección 
:ref:`Cadenas de texto de documentación <python_str_docstrings>`).

Hay herramientas que usan las ``docstrings`` para producir automáticamente documentación 
en línea o imprimible, o para permitirle al usuario que navegue el código en forma 
interactiva; es una buena práctica incluir ``docstrings`` en el código que uno escribe, 
por lo que se debe hacer un hábito de esto.

La ejecución de la función ``hola()`` muestra la impresión de un mensaje **Hola Plone !** 
que se imprime por consola. Devolver el objeto por los valores de retorno opcionales.

La ejecución de una función introduce una nueva tabla de símbolos usada para las 
variables locales de la función. Más precisamente, todas las asignaciones de 
variables en la función almacenan el valor en la tabla de símbolos local; así mismo 
la referencia a variables primero mira la tabla de símbolos local, luego en la tabla 
de símbolos local de las funciones externas, luego la tabla de símbolos global, y 
finalmente la tabla de nombres predefinidos. Así, no se les puede asignar directamente 
un valor a las variables globales dentro de una función (a menos se las nombre en la 
sentencia :ref:`global <python_sent_global>`), aunque si pueden ser referenciadas.

Los parámetros reales (argumentos) de una función se introducen en la tabla de símbolos 
local de la función llamada cuando esta es ejecutada; así, los argumentos son pasados 
por valor (dónde el valor es siempre una referencia a un objeto, no el valor del objeto). 
Cuando una función llama a otra función, una nueva tabla de símbolos local es creada 
para esa llamada.

La definición de una función introduce el nombre de la función en la tabla de símbolos 
actual. El valor del nombre de la función tiene un tipo que es reconocido por el 
interprete como una función definida por el usuario. Este valor puede ser asignado a 
otro nombre que luego puede ser usado como una función. Esto sirve como un mecanismo 
general para renombrar.


.. _python_fun_args:

Argumentos y parámetros
.......................

Al definir una función los valores los cuales se reciben se denominan parámetros, 
pero durante la llamada los valores que se envían se denominan argumentos.


Por posición
~~~~~~~~~~~~

Cuando enviá argumentos a una función, estos se reciben por orden en los parámetros 
definidos. Se dice por tanto que son argumentos por posición:

::

    >>> def resta(a, b):
    ...     return a - b
    ... 
    >>> resta(30, 10)
    20

En el ejemplo anterior el argumento *30* es la posición *0* por consiguiente es el 
parámetro de la función *a*, seguidamente el argumento *10* es la posición *1* por 
consiguiente es el parámetro de la función *b*.


Por nombre
~~~~~~~~~~

Sin embargo es posible evadir el orden de los parámetros si indica durante la llamada 
que valor tiene cada parámetro a partir de su nombre:

::

    >>> def resta(a, b):
    ...     return a - b
    ... 
    >>> (b=30, a=10)
    -20


Llamada sin argumentos
~~~~~~~~~~~~~~~~~~~~~~

Al momento de llamar una función la cual tiene definidos unos parámetros, si no pasa 
los argumentos correctamente provocará una excepción 
:ref:`TypeError <python_exception_typeerror>`:

::

    >>> resta()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: resta() takes exactly 2 arguments (0 given)


Parámetros por defecto
~~~~~~~~~~~~~~~~~~~~~~

Para solucionar la excepción :ref:`TypeError <python_exception_typeerror>` ejecutada 
al momento de la llamada a una función sin argumentos, entonces usted puede asignar 
unos valores por defecto nulos a los parámetros, de esa forma puede hacer una 
comprobación antes de ejecutar el código de la función:

::

    >>> def resta(a=None, b=None):
    ...     if a == None or b == None:
    ...         print "Error, debes enviar dos números a la función"
    ...         return
    ...     return a - b
    ... 
    >>> resta(30, 10)
    20
    >>> resta()
    Error, debes enviar dos números a la función

Como puede ver el el código anterior, se indica el final de la función luego de la 
:ref:`sentencia print <python_sent_print>`, usando la 
:ref:`sentencia return <python_sent_return>` aunque no devuelva nada.


.. _python_fun_args_kwargs:

Argumentos indeterminados
.........................

En alguna ocasión usted no sabe previamente cuantos elementos necesita enviar a una 
función. En estos casos puede utilizar los parámetros indeterminados por posición y 
por nombre.


Por posición
~~~~~~~~~~~~

Usted debe crear una lista dinámica de argumentos, es decir, un tipo 
:ref:`tupla <python_tuple>`, definiendo el parámetro con un asterisco, para recibir 
los parámetros indeterminados por posición:

::

    >>> def indeterminados_posicion(*args):
    ...     for arg in args:
    ...         print arg
    ... 
    >>> indeterminados_posicion(5,"Hola Plone",[1,2,3,4,5])
    5
    Hola Plone
    [1, 2, 3, 4, 5]


Por nombre
~~~~~~~~~~

Para recibir un número indeterminado de parámetros por nombre (clave-valor o en 
inglés *keyword args*), usted debe crear un diccionario dinámico de argumentos 
definiendo el parámetro con dos asteriscos:

::

    >>> def indeterminados_nombre(**kwargs):
    ...     print kwargs
    ... 
    >>> indeterminados_nombre(n=5, c="Hola Plone", l=[1,2,3,4,5])
    {'c': 'Hola Plone', 'l': [1, 2, 3, 4, 5], 'n': 5}

Al recibirse como un diccionario, puede iterarlo y mostrar la clave y valor de 
cada argumento:

::

    >>> def indeterminados_nombre(**kwargs):
    ...     for kwarg in kwargs:
    ...         print kwarg, "=>", kwargs[kwarg]
    ... 
    >>> indeterminados_nombre(n=5, c="Hola Plone", l=[1,2,3,4,5])
    c => Hola Plone
    l => [1, 2, 3, 4, 5]
    n => 5


Por posición y nombre
~~~~~~~~~~~~~~~~~~~~~

Si requiere aceptar ambos tipos de parámetros simultáneamente en una función, entonces 
debe crear ambas colecciones dinámicas. Primero los argumentos indeterminados por valor 
y luego los cuales son por clave y valor:

::

    >>> def super_funcion(*args,**kwargs):
    ...     total = 0
    ...     for arg in args:
    ...         total += arg
    ...     print "sumatorio => ", total
    ...     for kwarg in kwargs:
    ...         print kwarg, "=>", kwargs[kwarg]
    ... 
    >>> super_funcion(50, -1, 1.56, 10, 20, 300, cms="Plone", edad=38)
    sumatorio =>  380.56
    edad => 38
    cms => Plone

Los nombres ``args`` y ``kwargs`` no son obligatorios, pero se suelen utilizar por 
convención.

Muchos frameworks y librerías los utilizan por lo que es una buena practica llamarlos 
así.


.. _python_sent_pass:

Sentencia pass
..............

Es una operación nula --- cuando es ejecutada, nada sucede. Eso es útil como un 
contenedor cuando una sentencia es requerida sintácticamente, pero no necesita 
código que ser ejecutado, por ejemplo:

::

    >>> # una función que no hace nada (aun)
    ... def consultar_nombre_genero(letra_genero): pass
    ... 
    >>> type(consultar_nombre_genero)
    <type 'function'>
    >>> consultar_nombre_genero("M")
    >>> 
    >>> # una clase sin ningún método (aun)
    ... class Persona: pass
    ... 
    >>> macagua = Persona
    >>> type(macagua)
    <type 'classobj'>


.. _python_sent_return:

Sentencia return
................

Las funciones pueden comunicarse con el exterior de las mismas, al proceso principal 
del programa usando la sentencia ``return``. El proceso de comunicación con el exterior 
se hace *devolviendo valores*. A continuación, un ejemplo de función usando ``return``:

.. literalinclude:: ../../recursos/leccion5/funciones.py
    :language: python
    :lines: 13-16

Esta función se llama de la siguiente forma:

::

    >>> suma(23,74)
    97

.. note:: Por defecto, las funciones retorna el valor :ref:`None <python_obj_none>`.


Retorno múltiple
~~~~~~~~~~~~~~~~

Una característica interesante, es la posibilidad de devolver valores múltiples 
separados por comas:

::

    >>> def prueba():
    ...     return "Plone CMS", 20, [1,2,3]
    ... 
    >>> prueba()
    ('Plone CMS', 20, [1, 2, 3])

En el código anterior los valores múltiples se tratan en conjunto como una 
:ref:`tupla <python_tuple>` inmutable y se pueden reasignar a distintas variables:

::

    >>> def prueba():
    ...     return "Plone CMS", 20, [1,2,3]
    ... 
    >>> prueba()
    ('Plone CMS', 20, [1, 2, 3])
    >>> cadena, numero, lista = prueba()
    >>> print cadena, type(cadena)
    Plone CMS <type 'str'>
    >>> print numero, type(numero)
    20 <type 'int'>
    >>> print lista, type(lista)
    [1, 2, 3] <type 'list'>

En el código anterior puede observa como se asignar a distintas variables en base a 
los valores de la :ref:`tupla <python_tuple>` inmutable.


.. _python_fun_ejemplos:

Ejemplos de funciones
.....................

A continuación, se presentan algunos ejemplos de su uso:

**Definición de funciones**

A continuación, se presenta un ejemplo del uso de definir funciones:

.. literalinclude:: ../../recursos/leccion5/funciones.py
    :language: python
    :lines: 5-10


**Invocar funciones**

A continuación, se presenta un ejemplo del uso de llamar funciones:

::

    >>> iva()
    ¿Cual es el monto a calcular?: 300
    36


**Funciones con argumentos múltiple**

A continuación, se presenta un ejemplo del uso de funciones con argumentos múltiple:

.. literalinclude:: ../../recursos/leccion5/funciones.py
    :language: python
    :lines: 13-16

Y se llama de la siguiente forma:

::

    >>> suma(23,74)
    97


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion5/funciones.py>`.


.. tip::
    Para ejecutar el código :file:`funciones.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando:

    ::

        python funciones.py


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion5>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
