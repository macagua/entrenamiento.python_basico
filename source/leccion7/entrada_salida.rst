.. -*- coding: utf-8 -*-


.. _python_entrada_salida:

Entrada / Salida en Python
--------------------------

Los programas serían de muy poca utilidad si no fueran capaces de
interaccionar con el usuario. 

Entrada estándar
................

Para pedir información al usuario, debe utilizar las funciones ``input``
y ``raw_input``, así como los argumentos de línea de comandos.

**Ejemplo de la función raw_input**:

::

	>>> nombre = raw_input('¿Cómo te llamás?: ')
	¿Cómo te llamás?: Leonardo
	>>>

**Ejemplo de la función input**:

::

	>>> edad = input('¿Cual es tu edad?: ')
	¿Cual es tu edad?: 38
	>>>


Salida estándar
...............

Para mostrar mensajes en pantalla, se utiliza el uso de la palabra 
reservada ``print``.

**Ejemplo del uso de print**:

::

	>>> print 'Pepe: Hola', nombre, ', encantado de conocerte :3'
	Pepe: Hola Leonardo , encantado de conocerte :3
	>>> 


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

.. seealso::

    Ver los siguientes vídeos:

	- `Tutorial Python 30 - Entrada Estándar rawInput`_.

	- `Tutorial Python 31 - Salida Estándar rawInput`_.


Referencia
..........

- `Python Programming / Input and Output`_.

- `Python - Entrada / Salida. Ficheros`_.

.. _`Python Programming / Input and Output`: https://en.wikibooks.org/wiki/Python_Programming/Input_and_Output
.. _`Python - Entrada / Salida. Ficheros`: http://mundogeek.net/archivos/2008/04/02/python-entrada-salida-ficheros/
.. _`Tutorial Python 30 - Entrada Estándar rawInput`: https://www.youtube.com/watch?v=AzeUCuMvW6I
.. _`Tutorial Python 31 - Salida Estándar rawInput`: https://www.youtube.com/watch?v=B-JPXgxK3Oc
