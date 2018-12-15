.. -*- coding: utf-8 -*-


.. _python_instalacion:

Instalación
-----------

Debido al soporte :ref:`multiplataforma <python_multiplataforma>` de Python, se ofrecen 
ciertos recursos para los sistemas operativos más populares:


.. _python_instalacion_windows:

Instalando Python en Windows
............................

- `Instalando Python en Windows <https://www.youtube.com/watch?v=VTykmP-a2KY>`_.


.. _python_instalacion_mac:

Instalando Python en una Mac
............................

- `Instalando Python en una Mac <https://es.wikibooks.org/wiki/Python/Instalaci%C3%B3n_de_Python/Python_en_Mac_OS_X>`_.


.. _python_instalacion_linux:

Instalando Python en un Linux
.............................

En una distribución estándar Linux dispone por defecto el interprete Python instalado, para 
comprobar la correcta instalación  solamente debería ejecutar el comando en la consola: 

::

    python
    Python 2.7.13 (default, Sep 26 2018, 18:42:22) 
    [GCC 6.3.0 20170516] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Si le muestra los mensajes anteriores esta correctamente instalado el interprete Python en su Linux.

Si al ejecutar el comando anterior muestra el mensaje: ::

    python
    bash: python: no se encontró la orden

Esto es debido a que no tiene instalado el interprete, así que debe ejecutar el siguiente comando: 

::

    sudo apt-get install -y python-dev 

De nuevo vuelva a ejecutar en su consola de comando el comando ``python``.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion1>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
