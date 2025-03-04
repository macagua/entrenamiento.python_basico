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

.. code-block:: console

    python3

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: console
    :class: no-copy

    Python 3.11.2 (main, Nov 30 2024, 21:22:50) [GCC 12.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Si le muestra los mensajes anteriores esta correctamente instalado el interprete Python en su Linux.

.. tip::
    Si al ejecutar el comando anterior muestra el mensaje:

    .. code-block:: console

        python3

    Si ejecuto el comando anterior, este da como resultado lo siguiente:

    .. code-block:: console
        :class: no-copy

        bash: python3: no se encontró la orden

    Esto es debido a que no tiene instalado el interprete, así que debe ejecutar el siguiente comando:

    .. code-block:: console

        sudo apt install -y python3-dev

    De nuevo vuelva a ejecutar en su consola de comando el comando ``python3``.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion1>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
