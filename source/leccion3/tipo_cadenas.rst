.. -*- coding: utf-8 -*-


.. _python_cadenas:

Tipo cadenas de texto
---------------------

Las cadenas no son más que texto encerrado entre comillas simples
('cadena') o dobles ("cadena"). Dentro de las comillas se pueden añadir
caracteres especiales escapándolos con '\\', como '\\n', el carácter de
nueva línea, o '\\t', el de tabulación.

Una cadena puede estar precedida por el carácter 'u' o el carácter 'r',
los cuales indican, respectivamente, que se trata de una cadena que
utiliza codificación **Unicode** y una cadena ``raw`` (del inglés, cruda). Las
cadenas ``raw`` se distinguen de las normales en que los caracteres
escapados mediante la barra invertida (\\) no se sustituyen por sus
contrapartidas. Esto es especialmente útil, por ejemplo, para las
expresiones regulares.

::

    unicode = u"äóè"
    raw = r"\n"

También es posible encerrar una cadena entre triples comillas (simples o
dobles). De esta forma podremos escribir el texto en varias líneas, y al
imprimir la cadena, se respetarán los saltos de línea que introdujimos
sin tener que recurrir al carácter \\n, así como las comillas sin tener
que escaparlas.

Las cadenas también admiten operadores como la suma (concatenación de
cadenas) y la multiplicación.

::

    a = "uno"
    b = "dos"

    c = a + b # c es "unodos"
    c = a * 3 # c es "unounouno"


Ejemplo de cadenas de texto
...........................

A continuación, se presentan algunos ejemplos de su uso:

**Ejemplo de cadenas de texto con Comillas simples**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 4-7


**Ejemplo de cadenas de texto con Comillas dobles**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 9-11


**Ejemplo de cadenas de texto con codigo escapes**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 14-16


**Ejemplo de cadenas de texto con multilineas**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 19-31


**Ejemplo operadores de Repeticion de cadena de texto**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 34-36


**Ejemplo operadores de Concatenacion de cadena de texto**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :linenos:
    :language: python
    :lines: 39-45


**Ejemplo de acceder a rango de la cadena**

.. literalinclude:: ../../recursos/leccion3/tipo_cadenas.py
    :language: python
    :lines: 48-48
