.. _python_modulo_datetime:

Módulo datetime
...............

.. note::
    **Propósito:** Manipulación de valores de fecha y hora

El módulo :mod:`datetime` contiene funciones y clases para realizar análisis, formateo y
aritmética de fecha y hora, por separado y en conjunto.

.. literalinclude:: ../../recursos/leccion10/datetime_date.py
    :language: python
    :linenos:
    :lines: 1-11


.. _python_fun_strftime:

strftime
~~~~~~~~

``strftime`` es un formateador de cadenas, esto formateará un objeto de fecha y hora en
formato de :ref:`cadena de caracteres <python_str>`.

Los objetos ``date``, :mod:`datetime`, y :mod:`time` admiten un método ``strftime(format)``,
para crear una cadena que represente el objeto de fecha y hora bajo el control de una
:ref:`cadena de caracteres <python_str>` de formato explícito.

.. literalinclude:: ../../recursos/leccion10/datetime_strftime.py
    :language: python
    :linenos:
    :lines: 1-16


.. _python_fun_strptime:

strptime
~~~~~~~~


``strptime`` es un analizador de :ref:`cadenas <python_str>`, esto convertirá un formato de cadena a un objeto
de fecha y hora.

El método de clase ``datetime.strptime()`` crea un objeto :mod:`datetime` a partir de una
:ref:`cadena de caracteres <python_str>` que representa una fecha y hora y una :ref:`cadena <python_str>` de formato correspondiente.

.. literalinclude:: ../../recursos/leccion10/datetime_strptime.py
    :language: python
    :linenos:
    :lines: 1-15

.. comments:

    .. todo::
        TODO Terminar de escribir esta sección.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`datetime_date.py <../../recursos/leccion10/datetime_date.py>`.

    - :download:`datetime_strftime.py <../../recursos/leccion10/datetime_strftime.py>`.

    - :download:`datetime_strptime.py <../../recursos/leccion10/datetime_strptime.py>`.


.. tip::
    Para ejecutar el código, abra una consola de comando, acceda al directorio
    donde se encuentra el programa:

    .. code-block:: console
        :class: no-copy

        proyectos/
        └── datetime/
            ├── datetime_date.py
            ├── datetime_strftime.py
            └── datetime_strptime.py

    Si tiene la estructura de archivo previa, entonces ejecute los siguientes comandos:

    Para ejecutar el código usando el módulo ``date``, abra una consola de comando, acceda
    al directorio y ejecute el siguiente comando:

    .. code-block:: console

        python3 datetime_date.py

    El anterior código al ejecutar debe mostrar el siguiente mensaje:

    .. code-block:: console

        Fecha de nacimiento: 1980-12-03.

    Para ejecutar el código usando el método ``strftime``, abra una consola de comando, acceda
    al directorio y ejecute el siguiente comando:

    .. code-block:: console

        python3 datetime_strftime.py

    El anterior código al ejecutar debe mostrar el siguiente mensaje:

    .. code-block:: console

        Fecha y lugar de nacimiento: 03 de December de 1980 en Maracaibo, Zulia, Venezuela.

    Para ejecutar el código usando el método ``strptime``, abra una consola de comando, acceda
    al directorio y ejecute el siguiente comando:

    .. code-block:: console

        python3 datetime_strptime.py

    El anterior código al ejecutar debe mostrar el siguiente mensaje:

    .. code-block:: console

        Fecha y lugar de nacimiento: 03 de December de 1980 en Maracaibo, Zulia, Venezuela.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion10_datetime>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
