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
una cadenas de caracteres literal; esta es la cadenas de caracteres de documentación 
de la función, o ``docstrings``. (Puedes encontrar más acerca de 
``docstrings`` en la sección `Cadenas de texto de documentación`_.)

Hay herramientas que usan las ``docstrings`` para producir automáticamente 
documentación en línea o imprimible, o para permitirle al usuario que 
navegue el código en forma interactiva; es una buena práctica incluir 
``docstrings`` en el código que uno escribe, por lo que se debe hacer 
un hábito de esto.

La ejecución de la función ``prueba()`` muestra la impresión de un 
mensaje **función de prueba** que se imprime por consola. Return object 
for optionally returning values.


Sentencia return
................

Las funciones puede opcionalmente *retornar valores*, usando la palabra 
reservada ``return``. A continuación, un ejemplo de función usando ``return``:

.. literalinclude:: ../../recursos/leccion5/funciones.py
    :linenos:
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


Funciones de predicado
......................

.. todo::
    TODO escribir esta sección.


Funciones recursiva
...................

.. todo::
    TODO escribir esta sección.


Objetos de función
..................

.. todo::
    TODO escribir esta sección.


Funciones anónimas
..................

.. todo::
    TODO escribir esta sección.


Funciones de orden superior
...........................

.. todo::
    TODO escribir esta sección.


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


.. seealso::

    .. figure:: https://img.youtube.com/vi/_C7Uj7O5o_Q/0.jpg
        :align: center
        :width: 60%

        Vídeo `Tutorial Python 12 - Funciones`_, cortesía de `CodigoFacilito.com`_.

    .. todo:: Cambiar la URL de imagen de previsualización del video, de forma local.


Referencia
..........

- `Introducción a Funciones`_ - ¿Por qué?.
 
.. _`Introducción a Funciones`: http://docs.python.org.ar/tutorial/2/controlflow.html#definiendo-funciones
.. _`Tutorial Python 12 - Funciones`: https://www.youtube.com/watch?v=_C7Uj7O5o_Q
.. _`CodigoFacilito.com`: https://www.codigofacilito.com/
.. _`Cadenas de texto de documentación`: http://docs.python.org.ar/tutorial/2/controlflow.html#tut-docstrings
.. _`Defining functions - Scipy lecture notes`: https://www.pybonacci.org/scipy-lecture-notes-ES/intro/language/functions.html
