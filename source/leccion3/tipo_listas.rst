.. -*- coding: utf-8 -*-


.. _python_listas:

Tipo listas
-----------

La lista en Python son variables que almacenan ``arrays``, 
internamente cada posición puede ser un tipo de datos distinto.

En Python tiene varios tipos de datos *compuestos*, como los tipos *numéricos*, 
*secuencias*, *conjuntos* y *mapeos* usados para agrupar otros valores. 

Dentro de las secuencias, estan los tipos de cadenas de caracteres (strings).
Otro tipo muy importante de secuencia son las listas.

El más versátil de las *secuencias* es la *lista*, para definir una debe escribir 
es entre corchetes, separando sus elementos con comas cada ítems. 

::

   >>> factura = ['pan', 'huevos', 100, 1234]
   >>> factura
   ['pan', 'huevos', 100, 1234]

Las listas en Python son:

- **heterogéneas**: pueden estar conformadas por elementos de distintos tipo, 
  incluidos otras listas.

- **mutables**: sus elementos pueden modificarse.

Una lista en Python es una estructura de datos formada por una secuencia ordenada 
de objetos.

Los elementos de una lista pueden accederse mediante su índice, siendo 0 el índice 
del primer elemento.

::

    >>> factura[0]
    'pan'
    >>> factura[3]
    1234

La función :ref:`len <python_funcion_len>` devuelve la longitud de la lista (su 
cantidad de elementos).

::

    >>> len(factura)
    4

Los índices de una lista inicia entonces de **0** hasta el tamaño de la lista menos uno 
(``len(factura) - 1``):

::

    >>> len(factura) - 1
    3

Pueden usarse también índices negativos, siendo **-1** el índice del último elemento.

::

    >>> factura[-1]
    1234
    >>> 

Los índices negativos van entonces de **-1** (último elemento) a ``-len(factura)`` (primer elemento).

::

    >>> factura[-len(factura)]
    'pan'
    >>> 

A través de los índices, pueden cambiarse los elementos de una lista en el lugar.

::

    >>> factura[1] = "carne"
    >>> factura
    ['pan', 'carne', 100, 1234

De esta forma se cambia el valor inicial de un elemento de la lista lo cual hacen una la 
lista *mutable*

.. _python_listas_ejemplos:

Ejemplo de listas
.................

A continuación, se presentan algunos ejemplos de su uso:

**Ejemplo de establecer una colección ordenada/arreglos o vectores**

.. literalinclude:: ../../recursos/leccion3/tipo_listas.py
    :linenos:
    :language: python
    :lines: 9-10


**Ejemplo de acceder a un elemento especifico de una lista**

.. literalinclude:: ../../recursos/leccion3/tipo_listas.py
    :linenos:
    :language: python
    :lines: 13-14


**Ejemplo de acceder a un elemento a una lista anidada**

.. literalinclude:: ../../recursos/leccion3/tipo_listas.py
    :linenos:
    :language: python
    :lines: 17-18


**Ejemplo de establecer nuevo valor de un elemento de lista**

.. literalinclude:: ../../recursos/leccion3/tipo_listas.py
    :linenos:
    :language: python
    :lines: 21-23


**Ejemplo de obtener un rango de elemento especifico**

.. literalinclude:: ../../recursos/leccion3/tipo_listas.py
    :linenos:
    :language: python
    :lines: 26-27


**Ejemplos de obtener un rango con saltos de elementos específicos**

.. literalinclude:: ../../recursos/leccion3/tipo_listas.py
    :linenos:
    :language: python
    :lines: 30-34

**Ejemplo de iterar sobre cualquier secuencia**

Usted puede iterar sobre cualquier secuencia (cadenas de caracteres, lista, 
claves en un diccionario, lineas en un archivo, ...):

*Ejemplo de iterar sobre una cadenas de caracteres*

::

    >>> vocales = 'aeiou'

    >>> for letra in 'hermosa':
    ...     if letra in vocales:
    ...         print letra,
    e o a

*Ejemplo de iterar sobre una lista*

::

    >>> mensaje = "Hola, como estas tu?"
    >>> mensaje.split() # retorna una lista
    ['Hola,', 'como', 'estas', 'tu?']
    >>> for palabra in mensaje.split():
    ...     print palabra
    ...
    Hola,
    como
    estas
    tu?

*Ejemplo de iterar sobre dos o más secuencias*

Para iterar sobre dos o más secuencias al mismo tiempo, los valores pueden 
emparejarse con la función ``zip()``.

>>> preguntas = ['nombre', 'objetivo', 'sistema operativo']
>>> respuestas = ['Leonardo', 'aprender Python', 'Linux']
>>> for pregunta, respuesta in zip(preguntas, respuestas):
...     print '¿Cual es tu {0}?, la respuesta es: {1}.'.format(pregunta, respuesta)
... 
¿Cual es tu nombre?, la respuesta es: Leonardo.
¿Cual es tu objetivo?, la respuesta es: aprender Python.
¿Cual es tu sistema operativo?, la respuesta es: Linux.
>>> 


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_listas.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_listas.py`, abra una 
    consola de comando, acceda al dirfectorio donde se encuentra el mismo, 
    y ejecute el siguiente comando: ::

        python2 tipo_listas.py

----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre las **listas** 
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

::

    >>> help(list)


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
