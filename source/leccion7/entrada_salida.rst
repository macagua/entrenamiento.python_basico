.. -*- coding: utf-8 -*-


.. _python_entrada_salida:

Entrada/Salida en Python
------------------------

Los programas serían de muy poca utilidad si no fueran capaces de interaccionar 
con el usuario. 


.. _python_entrada:

Entrada estándar
................

Para pedir información al usuario, debe utilizar las funciones integradas en el 
interprete del lenguaje, así como los argumentos de línea de comandos.

.. comments:

    **Ejemplo de la función raw_input**:

    La función :ref:`raw_input() <python_fun_raw_input>` siempre devuelve un valor de 
    cadenas de caracteres:

    ::

        >>> nombre = raw_input('Ana: ¿Cómo se llama usted?: ')
        Ana: ¿Cómo se llama usted?: Leonardo
        >>> print(nombre)
        Leonardo

**Ejemplo de la función input**:

La función :ref:`input() <python_fun_input>` siempre devuelve un valor numérico:

::

    >>> edad = input('Ana: ¿Que edad tiene usted?: ')
    Ana: ¿Que edad tiene usted?: 38
    >>> print(edad)
    38

.. _python_entrada_script:

Entrada por script
..................

En muchas practicas de este entrenamiento usted lo que ha hecho ha sido escribir 
código en el intérprete, y/o escribir/ejecutar pequeños programas Python, pero 
los programas informáticos no funcionan así. 

Se basan en escribir todas las instrucciones en archivos llamados *scripts*, que 
no es mas que guiones de instrucciones. Luego se envía este archivo al intérprete 
como parámetro desde la terminal de comando (si es un lenguaje interpretado como 
Python) y éste ejecutará todas las instrucciones en bloque.

A parte de ser la base del funcionamiento de los programas, la característica de 
los *scripts* es que pueden recibir datos desde la propia terminal de comando en 
el momento de la ejecución, algo muy útil para agregar dinamismo los *scripts* a 
través de parámetros personalizables.

A continuación, un ejemplo el cual simula a sala de chat del servicio *LatinChat.com*, 
validando datos de entradas numérico y tipo cadena de caracteres e interactuá con 
el usuario y en base a condicionales muestra un mensaje.

.. literalinclude:: ../../recursos/leccion7/entrada_salida.py
    :language: python
    :lines: 12-32


.. tip::

    **LatinChat.com**, fue un servicio de Internet que ofrecía diversas salas de chat, 
    muy popular en la década de los 90 en latinoamericana.


.. _python_entrada_script_argv:

Scripts con argumentos
~~~~~~~~~~~~~~~~~~~~~~

Para poder enviar información a un script y manejarla, tenemos que utilizar la 
librería de sistema ``sys``. En ella encontraremos la lista ``argv`` que almacena 
los argumentos enviados al *script*. 

Usted debe crear un *script* llamado ``entrada_argumentos.py`` con el siguiente 
contenido:

.. literalinclude:: ../../recursos/leccion7/entrada_argumentos.py
    :language: python
    :lines: 1-3

Ejecuta el *script* llamado ``entrada_argumentos.py``, de la siguiente forma:

::

    python3.7 entrada_argumentos.py
    ['entrada_argumentos.py']


Al ejecutarlo puede ver que devuelve una lista con una cadena que contiene el nombre 
del *script*. Entonces, el primer argumento de la lista ``sys.argv`` (es decir, 
``sys.argv[0]``) es el propio nombre del *script*.

Ahora si intenta ejecutar el *script* de nuevo pasando algunos valores como números 
y cadenas de caracteres entre comillas dobles, todo separado por espacios:

::

    python3.7 entrada_argumentos.py 300 43.234 "Hola Plone"
    ['entrada_argumentos.py', '300', '43.234', 'Hola Plone']

Cada valor que enviamos al *script* durante la llamada se llama argumento e implica 
una forma de entrada de datos alternativa sin usar la función :ref:`input() <python_fun_input>`.


A continuación, un ejemplo el cual usa un *script* con la librería ``sys``. El *script*
recibe dos (02) argumentos: una cadena de caracteres y un número entero. Lo que hace 
es imprimir la cadena de caracteres tantas veces como le indique con el argumento de 
tipo número:

.. literalinclude:: ../../recursos/leccion7/entrada_dos_argumentos.py
    :language: python
    :lines: 1-13

Si quiere comprobar la validación de cuantos argumentos deben enviarme al script, 
ejecute el siguiente comando:

::

    python3.7 entrada_dos_argumentos.py "Hola Plone"
    ERROR: Introdujo uno (1) o más de dos (2) argumentos
    SOLUCIÓN: Introduce los argumentos correctamente
    Ejemplo: entrada_dos_argumentos.py "Texto" 5

Ahora si intenta ejecutar el *script* ``entrada_dos_argumentos.py`` con solo dos (2) 
argumentos, ejecutando el siguiente comando:

::

    python3.7 entrada_dos_argumentos.py "Hola Plone" 3
    Hola Plone
    Hola Plone
    Hola Plone


.. _python_salida:

Salida estándar
...............

La forma general de mostrar información por pantalla es mediante una consola de 
comando, generalmente podemos mostrar texto y variables separándolos con comas, 
para este se usa la sentencia :ref:`print <python_sent_print>`.


.. _python_sent_print:

Sentencia print
~~~~~~~~~~~~~~~

Sentencia ``print`` evalúa cada expresión, devuelve y escribe el objeto resultado 
a la salida estándar de la consola de comando. Si un objeto no es un 
:ref:`tipo cadena de caracteres <python_str>`, ese es primeramente convertido a un 
*tipo cadena de caracteres* usando las reglas para las 
:ref:`conversiones del tipo <python_fun_str>`. La *cadena de caracteres* (resultado 
o original) es entonces escrito.

Entonces para mostrar mensajes en pantalla, se utiliza el uso de la sentencia ``print``.

**Ejemplo del uso de la sentencia print**:

::

    >>> print('Ana: Hola', nombre, ', encantada de conocerte :3')
    Ana: Hola Leonardo , encantado de conocerte :3


.. _python_salida_formato_impresion_cadenas:

Formato de impresión de cadenas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


En la sentencia ``print`` se pueden usar el formato de impresión alternando las cadenas 
de caracteres y variables:

::

    >>> tipo_calculo = "raíz cuadrada de dos"
    >>> valor = 2**0.5
    >>> print("el resultado de", tipo_calculo, "es:", valor)
    el resultado de raíz cuadrada de dos es: 1.41421356237


.. seealso::

    Hay disponibles otras formas de aplicar formato de cadenas de caracteres:

    - :ref:`Formateo % <python_str_formateo_modulo>`.

    - :ref:`Clase formatter <python_str_formatter>`.


.. note::

    Una documentación completa del control de la salida de Python se encuentra en 
    https://docs.python.org/es/3.7/tutorial/inputoutput.html


.. important::
    Usted puede descargar los códigos usados en esta sección haciendo clic en los
    siguientes enlaces: :download:`entrada_salida.py <../../recursos/leccion7/entrada_salida.py>`, 
    :download:`entrada_argumentos.py <../../recursos/leccion7/entrada_argumentos.py>` y 
    :download:`entrada_dos_argumentos.py <../../recursos/leccion7/entrada_dos_argumentos.py>`.


.. tip::
    Para ejecutar el código :file:`entrada_salida.py`, :file:`entrada_argumentos.py` y 
    :file:`entrada_dos_argumentos.py`, abra una consola de comando, acceda al directorio 
    donde se encuentra ambos programas: 

    ::

        leccion8/
        ├── entrada_argumentos.py
        ├── entrada_dos_argumentos.py
        └── entrada_salida.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    ::

        python3.7 entrada_salida.py
        python3.7 entrada_argumentos.py
        python3.7 entrada_dos_argumentos.py


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion7>` del 
    entrenamiento para ampliar su conocimiento en esta temática.
