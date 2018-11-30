.. -*- coding: utf-8 -*-


.. _python_funciones_propias:

Funciones definidas por el usuario
----------------------------------

Son bloques que puede contener código fuente y ser invocados 
cuando se necesite, a continuación un ejemplo:

::

  >>> def prueba():
  ...     """ ejemplo simple de una función """
  ...     print "función de prueba"
  ... 
  >>> 
  >>> prueba()
  función de prueba


.. warning:: 
    Los bloques de ``function`` deben estar indentado como otros 
    bloques estructuras de control.

La palabra reservada ``def`` se usa para definir funciones. Debe 
seguirle el nombre de la función en el ejemplo anterior ``prueba()`` 
y la lista de parámetros formales entre paréntesis. Las sentencias 
que forman el cuerpo de la función empiezan en la línea siguiente, 
y deben estar indentado.

La primer sentencia del cuerpo de la función puede ser opcionalmente 
una cadenas de caracteres literal; esta es la cadenas de caracteres 
de documentación de la función, o ``docstrings``. (Puedes encontrar 
más acerca de ``docstrings`` en la sección `Cadenas de texto de documentación`_.)

Hay herramientas que usan las ``docstrings`` para producir automáticamente 
documentación en línea o imprimible, o para permitirle al usuario que 
navegue el código en forma interactiva; es una buena práctica incluir 
``docstrings`` en el código que uno escribe, por lo que se debe hacer 
un hábito de esto.

La ejecución de la función ``prueba()`` muestra la impresión de un 
mensaje **función de prueba** que se imprime por consola. Devolver 
el objeto por los valores de retorno opcionales.


.. _python_sentencia_pass:

Sentencia pass
................

Es una operación nula --- cuando es ejecutada, nada sucede. Eso es útil 
como un contenedor cuando una sentencia es requerida sintácticamente, 
pero no necesita código que ser ejecutado, por ejemplo:

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
    >>> 


.. _python_sentencia_return:

Sentencia return
................

Las funciones puede opcionalmente *retornar valores*, usando la palabra 
reservada ``return``. A continuación, un ejemplo de función usando ``return``:

.. literalinclude:: ../../recursos/leccion5/funciones.py
    :language: python
    :lines: 15-17

Esta función se invoca de la siguiente forma:

::

    >>> suma(23,74)
    97
    >>> 

.. note:: Por defecto, las funciones retorna el valor ``None``.


Parámetros


Funciones con argumentos
........................

A continuación, un ejemplo de función con argumentos:

.. literalinclude:: ../../recursos/leccion5/funciones.py
    :linenos:
    :language: python
    :lines: 20-25

La ejecución de una función introduce una nueva tabla de símbolos usada para 
las variables locales de la función. Más precisamente, todas las asignaciones 
de variables en la función almacenan el valor en la tabla de símbolos local; 
así mismo la referencia a variables primero mira la tabla de símbolos local, 
luego en la tabla de símbolos local de las funciones externas, luego la tabla 
de símbolos global, y finalmente la tabla de nombres predefinidos. Así, no se 
les puede asignar directamente un valor a las variables globales dentro de una 
función (a menos se las nombre en la sentencia ``global``), aunque si pueden ser 
referenciadas.

Los parámetros reales (argumentos) de una función se introducen en la tabla de 
símbolos local de la función llamada cuando esta es ejecutada; así, los argumentos 
son pasados por valor (dónde el valor es siempre una referencia a un objeto, no 
el valor del objeto). [1] Cuando una función llama a otra función, una nueva 
tabla de símbolos local es creada para esa llamada.

La definición de una función introduce el nombre de la función en la tabla de 
símbolos actual. El valor del nombre de la función tiene un tipo que es reconocido 
por el interprete como una función definida por el usuario. Este valor puede ser 
asignado a otro nombre que luego puede ser usado como una función. Esto sirve como 
un mecanismo general para renombrar:


**Funciones con argumentos múltiple**

A continuación, se presenta un ejemplo del uso de funciones con argumentos múltiple:

.. literalinclude:: ../../recursos/leccion5/funciones.py
    :linenos:
    :language: python
    :lines: 15-17

Y se invoca de la siguiente forma:

::

    >>> suma(23,74)
    97

    >>> 


.. _python_funciones_predicado:

Funciones de predicado
......................

Las funciones de predicado no es más que una función la cual dice si algo es ``True`` 
o ``False``, es decir, es una función que devuelve un tipo de datos 
:ref:`booleano <python_booleanos>`.

.. todo::
    TODO terminar de escribir la sección Funciones de predicado.


.. _python_funciones_recursivas:

Funciones recursivas
....................

Las funciones recursivas son funciones que se llaman a sí mismas 
durante su propia ejecución. Ellas funcionan de forma similar a 
las iteraciones, pero debe encargarse de planificar el momento en 
que dejan de llamarse a sí mismas o tendrá una función recursiva 
infinita.

Estas funciones se estilan utilizar para dividir una tarea en sub-tareas 
más simples de forma que sea más fácil abordar el problema y solucionarlo.

Función recursiva sin retorno
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un ejemplo de una función recursiva sin retorno, es el ejemplo de cuenta 
regresiva hasta cero a partir de un número:

::

    def cuenta_regresiva(numero):
        numero -= 1
        if numero > 0:
            print numero
            cuenta_regresiva(numero)
        else:
            print "Boooooooom!"
        print "Fin de la función", numero

    cuenta_regresiva(5)

Dando como resultado los siguientes mensajes:

::

    4
    3
    2
    1
    Boooooooom!
    Fin de la función 0
    Fin de la función 1
    Fin de la función 2
    Fin de la función 3
    Fin de la función 4


Función recursiva con retorno
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un ejemplo de una función recursiva con retorno, es el ejemplo del calculo del 
factorial de un número corresponde al producto de todos los números desde 1 hasta 
el propio número. Es el ejemplo con retorno más utilizado para mostrar la utilidad 
de este tipo de funciones:

::


    def factorial(numero):
        print "Valor inicial ->",numero
        if numero > 1:
            numero = numero * factorial(numero -1)
        print "valor final ->",numero
        return numero

    print factorial(5)

El código anterior da como resultado los siguientes mensajes:

::

    Valor inicial -> 5
    Valor inicial -> 4
    Valor inicial -> 3
    Valor inicial -> 2
    Valor inicial -> 1
    valor final -> 1
    valor final -> 2
    valor final -> 6
    valor final -> 24
    valor final -> 120

    120

.. todo::
    TODO terminar de escribir la sección Funciones recursivas.


Objetos de función
..................

.. todo::
    TODO escribir la sección Objetos de función.


Funciones anónimas
..................

Una función anónima, como su nombre indica es una función sin nombre. Es decir, es 
posible ejecutar una función sin referenciar un nombre, en Python puede ejecutar 
una función sin definirla con ``def``. 

De hecho son similares pero con una diferencia fundamental, **el contenido de una 
función anónima debe ser una única expresión en lugar de un bloque de acciones**.

Las funciones anónimas se implementan en Python con las funciones o expresiones 
:ref:`lambda <python_funcion_lambda>`, esta es unas de las funcionalidades más potentes 
de Python, pero a la vez es la más confusas para los principiantes.

Y es que más allá del sentido de función que usted tiene hasta el momento, con su 
nombre y sus acciones internas, una función en su sentido más trivial significa 
realizar algo sobre algo. Por tanto se podría decir que, mientras las funciones 
anónimas :ref:`lambda <python_funcion_lambda>` sirven para realizar funciones simples, 
las funciones definidas con ``def`` sirven para manejar tareas más extensas.

Si deconstruye una función sencilla, puede llegar a una función ``lambda``. Por ejemplo 
la siguiente función es para doblar un valor de un número:

::

    >>> def doblar(numero):
    resultado = numero*2
    return resultado

    >>> doblar(2)
    4
    >>> type(doblar)
    <type 'function'>


Si el código fuente anterior se simplifica se verá, de la siguiente forma:

::

    >>> def doblar(numero):
    return numero*2

    >>> doblar(2)
    4
    >>> type(doblar)
    <type 'function'>


Usted puede todavía simplificar más, escribirlo todo en una sola línea, de la 
siguiente forma:

::

    >>> def doblar(numero): return numero*2

    >>> lambda numero: numero*2
    <function <lambda> at 0x7f1023944e60>
    >>> doblar(2)
    4
    >>> type(doblar)
    <type 'function'>


Esta notación simple es la que una función ``lambda`` intenta replicar, observe, 
a continuación se va a convertir la función en una función anónima:

::

    >>> lambda numero: numero*2
    <function <lambda> at 0x7f1023944e60>

En este ejemplo tiene una función anónima con una entrada que recibe ``numero``, 
y una salida que devuelve ``numero * 2``.

Lo único que necesita hacer para utilizarla es guardarla en una variable y utilizarla 
tal como haría con una función normal:

::

    >>> doblar = lambda numero: numero*2
    >>> doblar(2)
    4
    >>> type(doblar)
    <type 'function'>


Con la flexibilidad de Python usted puede implementar infinitas funciones simples. 
Usted puede encontrar más ejemplos de funciones anónimas usando ``lambda`` en la 
sección :ref:`ejemplos de funciones <python_funciones_ejemplos>`.

Usted puede explotar al máximo la función lambda utilizándola en conjunto con otras 
funciones como :ref:`filter() <python_funcion_filter>` y :ref:`map() <python_funcion_map>`.


.. _python_funciones_orden_superior:

Funciones de orden superior
...........................

Las funciones de Python pueden tomar funciones como parámetros y devolver funciones 
como resultado. Una función que hace ambas cosas o alguna de ellas se llama función 
de orden superior.


.. _python_funcion_filter:

Función filter
~~~~~~~~~~~~~~

La función ``filter()`` es una función que toma un :ref:`predicado <python_funciones_predicado>` 
y una lista y devuelve una lista con los elementos que satisfacen el predicado. Tal como 
su nombre indica ``filter()`` significa filtrar, ya que a partir de una lista o iterador 
y una función condicional, es capaz de devolver una nueva colección con los elementos 
filtrados que cumplan la condición.

Todo esto podría haberse logrado también con :ref:`listas por comprensión <python_listas_comprension>` 
que usaran predicados. No hay ninguna regla que diga cuando usar la función 
:ref:`map() <python_funcion_map>` o la función ``filter()`` en lugar de las 
:ref:`listas por comprensión <python_listas_comprension>`, simplemente debe decidir que es 
más legible dependiendo del contexto.

Por ejemplo, suponga que tiene una lista varios números y requiere filtrarla, quedando 
únicamente con los números múltiples de 5, eso seria así:

::

    >>> # Primero declaramos una función condicional
    def multiple(numero):
    # Comprobamos si un numero es múltiple de cinco
    if numero % 5 == 0:
        # Sólo devolvemos True si lo es
        return True

    >>> numeros = [2, 5, 10, 23, 50, 33]
    >>> filter(multiple, numeros)
    [5, 10, 50]

Si ejecuta el filtro obtiene una lista los números múltiples de 5. Por tanto cuando utiliza 
la función ``filter()`` tiene que enviar una función condicional, para esto, puede utilizar 
una función anónima ``lambda``, como se muestra a continuación:

::

    >>> filter(lambda numero: numero%5 == 0, numeros)
    [5, 10, 50]
    >>>

Así, en una sola línea ha definido y ejecutado el filtro utilizando una función condicional 
anónima y devolviendo una lista de números.


Filtrando objetos
````````````````` 

Sin embargo, más allá de filtrar listas con valores simples, el verdadero potencial de la 
función ``filter()`` sale a relucir cuando usted necesita filtrar varios objetos de una lista.

Por ejemplo, dada una lista con varias personas, le gustaría filtrar únicamente las que son 
menores de edad:

::

    >>> class Persona:
    ...     
    ...     def __init__(self, nombre, edad):
    ...         self.nombre = nombre
    ...         self.edad = edad
    ...     
    ...     def __str__(self):
    ...         return "{} de {} años".format(self.nombre, self.edad)
    ... 
    >>> personas = [
    ...     Persona("Leonardo", 38),
    ...     Persona("Ana", 33),
    ...     Persona("Sabrina", 12),
    ...     Persona("Enrique", 3)
    ... ]
    >>> menores = filter(lambda persona: persona.edad < 18, personas)
    >>> for menor in menores:
    print menor
    Sabrina de 12 años
    Enrique de 3 años

Este es un ejemplo sencillo, con el cual usted puede realizar filtrados con objetos, de forma 
amigable.


.. _python_funcion_map:

Función map
~~~~~~~~~~~

La función ``map()`` toma una función y una lista y aplica esa función a cada elemento 
de esa lista, produciendo una nueva lista. Va a ver su definición de tipo y como se define.

Esta función trabaja de una forma muy similar a :ref:`filter() <python_funcion_filter>`, 
con la diferencia que en lugar de aplicar una condición a un elemento de una lista o secuencia, 
aplica una función sobre todos los elementos y como resultado se devuelve un lista de números 
doblado su valor:

::

    >>> def doblar(numero):
    return numero*2

    >>> numeros = [2, 5, 10, 23, 50, 33]
    >>> map(doblar, numeros)
    [4, 10, 20, 46, 100, 66]

Usted puede simplificar el código anterior usando una función ``lambda`` para substituir 
la llamada de una función definida, como se muestra a continuación:

::

    >>> map(lambda x: x*2, numeros)
    [4, 10, 20, 46, 100, 66]

La función ``map()`` se utiliza mucho junto a expresiones ``lambda`` ya que permite evitar 
escribir :ref:`bucles for <python_bucle_for>`.

Además se puede utilizar sobre más de un objeto iterable con la condición que tengan la 
misma longitud. Por ejemplo, si requiere multiplicar los números de dos listas:

::

    >>> a = [1, 2, 3, 4, 5]
    >>> b = [6, 7, 8, 9, 10]
    >>> map(lambda x,y : x*y, a,b)
    [6, 14, 24, 36, 50]

E incluso usted puede extender la funcionalidad a tres listas o más:

::

    >>> a = [1, 2, 3, 4, 5]
    >>> b = [6, 7, 8, 9, 10]
    >>> c = [11, 12, 13, 14, 15]
    >>> map(lambda x,y,z : x*y*z, a,b,c)
    [66, 168, 312, 504, 750]


Mapeando objetos
````````````````

Evidentemente, siempre que la función ``map()`` la utilice correctamente podrá mapear 
una serie de objetos sin ningún problema:

::

    >>> class Persona:
    ...     
    ...     def __init__(self, nombre, edad):
    ...         self.nombre = nombre
    ...         self.edad = edad
    ...     
    ...     def __str__(self):
    ...         return "{} de {} años".format(self.nombre, self.edad)
    ... 
    >>> personas = [
    ...     Persona("Leonardo", 38),
    ...     Persona("Ana", 33),
    ...     Persona("Sabrina", 12),
    ...     Persona("Enrique", 3)
    ... ]
    >>> def incrementar(p):
    ...     p.edad += 1
    ...     return p
    ... 
    >>> personas = map(incrementar, personas)
    >>> for persona in personas:
    ...     print persona
    ... 
    Leonardo de 39 años
    Ana de 34 años
    Sabrina de 13 años
    Enrique de 4 años

Claro que en este caso tiene que utilizar una función definida porque no necesitamos actuar sobre 
la instancia, a no ser que usted se tome la molestia de rehacer todo el objeto:

::

    >>> class Persona:
    ...     
    ...     def __init__(self, nombre, edad):
    ...         self.nombre = nombre
    ...         self.edad = edad
    ...     
    ...     def __str__(self):
    ...         return "{} de {} años".format(self.nombre, self.edad)
    ... 
    >>> personas = [
    ...     Persona("Leonardo", 38),
    ...     Persona("Ana", 33),
    ...     Persona("Sabrina", 12),
    ...     Persona("Enrique", 3)
    ... ]
    >>> def incrementar(p):
    ...     p.edad += 1
    ...     return p
    ... 
    >>> personas = map(lambda p: Persona(p.nombre, p.edad+1), personas)
    >>> for persona in personas:
    ...     print persona
    ... 
    Leonardo de 39 años
    Ana de 34 años
    Sabrina de 13 años
    Enrique de 4 años


.. _python_funcion_lambda:

Función lambda
~~~~~~~~~~~~~~

La función ``lambda`` es una función anónima que suelen ser usadas cuando necesita una 
función una sola vez. Normalmente usted crea funciones ``lambda`` con el único propósito 
de pasarlas a funciones de orden superior.

En muchos lenguajes, el uso de ``lambdas`` sobre funciones definidas causa problemas de 
rendimiento. No es el caso en Python.

::

    >>> import os
    >>> archivos = os.listdir(os.__file__.replace("/os.pyc", "/"))
    >>> print filter(lambda x: x.startswith('os.'), archivos)
    ['os.pyc', 'os.py']

En el ejemplo anterior se el método ``os.__file__`` para obtener la ruta donde esta instalada 
el módulo ``os`` en su sistema, ejecutando la siguiente sentencia:

::

    >>> os.__file__
    '/usr/lib/python2.7/os.pyc'

Luego se inicializa la variable ``archivos`` generando una lista de archivos usando la función 
``os.listdir()``, ejecutando la siguiente sentencia:

::

    >>> archivos = os.listdir("/usr/lib/python2.7/")
    >>> type(archivos)
    <type 'list'>
    >>> len(archivos)
    443

Opcionalmente puede comprobar si la cadena de caracteres **os.pyc** se encuentras una de las 
posiciones de la lista ``archivos``, ejecutando la siguiente sentencia:

::

    >>> "os.pyc" in archivos
    True

Ya al comprobar que existe la cadena de caracteres "**os.pyc**" se usa una 
función :ref:`lambda <python_funcion_lambda>` con la función 
:ref:`filter() <python_funcion_filter>` para filtrar todos los archivos 
del directorio "*/usr/lib/python2.7/*" por medio del función ``os.listdir()`` 
que inicien con la cadena de caracteres "**os.**" usando la función 
:ref:`startswith() <python_funcion_startswith>`.

::

    >>> print filter(lambda x: x.startswith('os.'), os.listdir('/usr/lib/python2.7/'))
    ['os.pyc', 'os.py']

Así de esta forma se comprueba que existe el archivo compilado de Python junto con el mismo 
módulo Python.

::

    >>> os.__file__
    '/usr/lib/python2.7/os.pyc'
    >>> archivos = os.listdir("/usr/lib/python2.7/")
    >>> type(archivos)
    <type 'list'>
    >>> len(archivos)
    443
    >>> "os.pyc" in archivos
    True
    >>> print filter(lambda x: x.startswith('os.'), os.listdir('/usr/lib/python2.7/'))
    >>> ['os.pyc', 'os.py']

----


.. _python_funciones_ejemplos:

Ejemplos de funciones
.....................

A continuación, se presentan algunos ejemplos de su uso:

**Definición de funciones**

A continuación, se presenta un ejemplo del uso de definir funciones:

.. literalinclude:: ../../recursos/leccion5/funciones.py
    :linenos:
    :language: python
    :lines: 7-12


**Invocar funciones**

A continuación, se presenta un ejemplo del uso de invocar funciones:

::

    >>> iva()
    ¿Cual es el monto a calcular?: 300
    36


**Función lambda - operaciones aritméticas**

A continuación, se presenta un ejemplo para comprobar si un número es impar:

::

    >>> impar = lambda numero: numero%2 != 0
    >>> impar(5)
    True


**Función lambda - operaciones de cadena**

A continuación, se presenta un ejemplo para darle la vuelta a una cadena 
utilizando slicing:

::

    >>> revertir = lambda cadena: cadena[::-1]
    >>> revertir("Hola")
    'aloH'

**Función lambda - varios parámetros**

A continuación, se presenta un ejemplo para varios parámetros, por ejemplo para 
sumar dos números:

::

    >>> sumar = lambda x,y: x+y
    >>> sumar(5,2)
    7

----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion5/funciones.py>`.


.. tip::
    Para ejecutar el código :file:`funciones.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando:

    ::

        python funciones.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion5>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
