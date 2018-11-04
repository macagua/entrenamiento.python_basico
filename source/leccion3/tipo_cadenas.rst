.. -*- coding: utf-8 -*-


.. _python_cadenas:

Tipo cadenas de caracteres
--------------------------

Las cadenas no son más que caracteres encerrado entre comillas simples
('cadena') o dobles ("cadena"). 

+---------------+-----------+----------------------------+---------------+
| **Tipo**      | **Clase** | **Notas**                  | **Ejemplo**   |
+---------------+-----------+----------------------------+---------------+
| ``str``       | Cadena    | Inmutable                  | 'Hola mundo'  |
+---------------+-----------+----------------------------+---------------+
| ``unicode``   | Cadena    | Versión ``Unicode`` de str | u'Hola mundo' |
+---------------+-----------+----------------------------+---------------+

.. note::

    - **Mutable:** si su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.

    - **Inmutable:** si su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.


.. _python_cadenas_escape:

Cadenas de escape
.................

Dentro de las comillas se pueden añadir caracteres especiales para 
escaparlos con:

- \\n : el carácter de salto de nueva línea.

- \\t : el carácter de tabulación.

- \\ : el carácter de barra invertida (\\).

- \\' : el carácter de comillas simple.

- \\" : el carácter de comillas doble.


Una cadena puede estar precedida por el carácter 'u' o el carácter 'r',
los cuales indican, respectivamente, que se trata de una cadena que
utiliza codificación ``unicode`` y una cadena ``raw`` (del inglés, cruda). 
Las cadenas ``raw`` se distinguen de las normales en que los caracteres
escapados mediante la barra invertida (``\``) no se sustituyen por sus
contrapartidas. Esto es especialmente útil, por ejemplo, para las
expresiones regulares.

::

    unicode = u"äóè"
    raw = r"\n"


También es posible encerrar una cadena entre triples comillas (simples o
dobles). De esta forma podremos escribir el texto en varias líneas, y al
imprimir la cadena, se respetarán los saltos de línea que introdujimos
sin tener que recurrir al carácter ``\n``, así como las comillas sin tener
que escaparlas.

Las cadenas también admiten operadores como la suma (concatenación de
cadenas) y la multiplicación.

::

    >>> a = "uno"
    >>> b = "dos"
    >>> c = a + b
    >>> c
    'unodos'
    >>> c = a * 3
    >>> c
    'unounouno'
    >>> 


.. _python_cadenas_comentarios:

Cadenas de comentarios
......................

Son cadenas de caracteres que comienzan con el carácter ``#`` y cadena entre 
triples comillas (simples o dobles) que Python ignora totalmente.

::

    >>> # comentarios en linea
    ... 
    >>> """ comentarios en varias lineas """
    ' comentarios en varias lineas '
    >>> ''' comentarios en varias lineas '''
    ' comentarios en varias lineas '
    >>> 


Ejemplo de cadenas de caracteres
................................

A continuación, se presentan algunos ejemplos de su uso:

**Ejemplo de cadenas de caracteres con comillas simples**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 9-11


**Ejemplo de cadenas de caracteres con comillas dobles**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 14-16


**Ejemplo de cadenas de caracteres con código escapes**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 19-21


**Ejemplo de cadenas de caracteres con varias lineas**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 24-36


**Ejemplo operadores de repetición de cadenas de caracteres**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 39-41


**Ejemplo operadores de concatenación de cadenas de caracteres**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 44-47


**Ejemplo de medir tamaño de la cadena con función "len()"**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :linenos:
    :language: python
    :lines: 50


**Ejemplo de acceder a rango de la cadena**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 53


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_cadenas.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_cadenas.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando: ::

        python2 tipo_cadenas.py


----


Convertir a tipos cadenas de caracteres
.......................................

Para convertir a tipos cadenas de caracteres debes usar las 
:ref:`funciones integradas <python_funciones_integradas>` 
al interprete disponible, a continuación se describen algunas 
de ellas para tipos de datos cadenas de caracteres:

str()
~~~~~

La función ``str()`` devuelve una cadenas de caracteres. 

::

    >>> str(2)
    '2'
    >>> str(2.5)
    '2.5'
    >>> str(-2.5)
    '-2.5'
    >>> str(2.3+0j)
    '(2.3+0j)'
    >>> 

.. tip:: 
    Para más información consulte las funciones integradas para 
    :ref:`operaciones en cadenas de caracteres <python_funciones_integradas_cadenas>`.


----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre las **cadenas 
de caracteres** desde la :ref:`consola interactiva <python_interactivo>` de la 
siguiente forma:

::

    >>> help(str)

Para salir de esa ayuda presione la tecla ``q``.

Usted puede consultar toda la documentación disponible sobre las **cadenas 
de caracteres unicode** desde la :ref:`consola interactiva <python_interactivo>` de la 
siguiente forma:

::

    >>> help(unicode)

Para salir de esa ayuda presione la tecla ``q``.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
