.. -*- coding: utf-8 -*-


.. _python_entrada_salida:

Entrada / Salida en Python
--------------------------

Los programas serían de muy poca utilidad si no fueran capaces de
interaccionar con el usuario. 


.. _python_entrada:

Entrada estándar
................

Para pedir información al usuario, debe utilizar las funciones integradas 
en el interprete del lenguaje, así como los argumentos de línea de comandos.

**Ejemplo de la función raw_input**:

La función :ref:`raw_input() <python_funcion_raw_input>` siempre devuelve un 
valor de cadenas de caracteres:

::

	>>> nombre = raw_input('¿Cómo te llamás?: ')
	¿Cómo te llamás?: Leonardo
	>>>

**Ejemplo de la función input**:

La función :ref:`input() <python_funcion_input>` siempre devuelve un valor 
numérico:

::

	>>> edad = input('¿Cual es tu edad?: ')
	¿Cual es tu edad?: 38
	>>>


.. _python_salida:

Salida estándar
...............

Para mostrar mensajes en pantalla, se utiliza el uso de la palabra 
reservada ``print``.

**Ejemplo del uso de print**:

::

	>>> print 'Pepe: Hola', nombre, ', encantado de conocerte :3'
	Pepe: Hola Leonardo , encantado de conocerte :3
	>>> 


.. _python_entrada_salida_ejemplo:

Ejemplo de E/S en Python
........................

Este ejemplo simula a sala de chat del servicio *LatinChat.com*, 
validando datos de entradas numérico y tipo cadena e interactuá
con el usuario y en base a condicionales muestra un mensaje.

.. literalinclude:: ../../recursos/leccion7/entrada_salida.py
    :linenos:
    :language: python
    :lines: 14-34


.. tip::

    **LatinChat.com**, fue un servicio de Internet que ofrecía diversas 
    salas de chat, muy popular en la década de los 90 en latinoamericana.


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion7/entrada_salida.py>`.


.. tip::
    Para ejecutar el código :file:`entrada_salida.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando: ::

        python2 entrada_salida.py


.. _python_salida_formato_impresion_cadenas:

Formato de impresión de cadenas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


En la sentencia ``print`` se pueden usar el formato de impresión alternando 
las cadenas de caracteres y variables:

::

	>>> tipo_calculo = "raíz cuadrada de dos"
	>>> valor = 2**0.5
	>>> print "el resultado de", tipo_calculo, "es:", valor
	el resultado de raíz cuadrada de dos es: 1.41421356237
	>>> 


.. seealso::

    Hay disponibles otras formas de aplicar formato de cadenas de caracteres:

    - :ref:`Formateo % <python_cadenas_formateo_modulo>`.

    - :ref:`Clase formatter <python_cadenas_formatter>`.


----

.. note::

	Una documentación completa del control de la salida de Python se encuentra en 
	https://docs.python.org/2/tutorial/inputoutput.html


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion7>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
