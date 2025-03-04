.. _python_modulo_datetime:

datetime - Fecha y hora
.......................

.. note::
    **Propósito:** Manipulación de valores de fecha y hora

El módulo `datetime`_ contiene funciones y clases para realizar análisis, formateo y
aritmética de fecha y hora, por separado y en conjunto.

.. literalinclude:: ../../recursos/leccion10/datetime_date.py
    :language: python
    :linenos:
    :lines: 1-11

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    Fecha de nacimiento: 1980-12-03.


.. _python_fun_strftime:

strftime
~~~~~~~~

``strftime`` es un formateador de cadenas, esto formateará un objeto de fecha y hora en
formato de :ref:`cadena de caracteres <python_str>`.

Los objetos ``date``, ``datetime``, y ``time`` admiten un método ``strftime(format)``,
para crear una cadena que represente el objeto de fecha y hora bajo el control de una
:ref:`cadena de caracteres <python_str>` de formato explícito.

.. literalinclude:: ../../recursos/leccion10/datetime_strftime.py
    :language: python
    :linenos:
    :lines: 1-16

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    Fecha y lugar de nacimiento: 03 de December de 1980 en Maracaibo, Zulia, Venezuela.


.. _python_fun_strptime:

strptime
~~~~~~~~


``strptime`` es un analizador de :ref:`cadenas <python_str>`, esto convertirá un formato de cadena a un objeto
de fecha y hora.

El método de clase ``datetime.strptime()`` crea un objeto ``datetime`` a partir de una
:ref:`cadena de caracteres <python_str>` que representa una fecha y hora y una :ref:`cadena <python_str>` de formato correspondiente.

.. literalinclude:: ../../recursos/leccion10/datetime_strptime.py
    :language: python
    :linenos:
    :lines: 1-15

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    Fecha y lugar de nacimiento: 03 de December de 1980 en Maracaibo, Zulia, Venezuela.

.. comments:

    .. todo::
        TODO Terminar de escribir esta sección.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion10_datetime>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`datetime`: https://docs.python.org/es/3.11/library/datetime.html
