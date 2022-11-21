.. -*- coding: utf-8 -*-


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
    :lines: 1-15

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    Fecha de nacimiento: 1980-12-03.


.. _python_fun_strftime:

strftime
~~~~~~~~

Los objetos ``date``, ``datetime``, y ``time`` admiten un método ``strftime(format)``,
para crear una cadena que represente el tiempo bajo el control de una cadena de caracteres
de formato explícito.


.. literalinclude:: ../../recursos/leccion10/datetime_strptime.py
    :language: python
    :linenos:
    :lines: 1-19

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    Fecha y lugar de nacimiento: 03 de December de 1980 en Maracaibo, Zulia, Venezuela.


.. _python_fun_strptime:

strptime
~~~~~~~~

El método de clase ``datetime.strptime()`` crea un objeto ``datetime`` a partir de una
cadena que representa una fecha y hora y una cadena de formato correspondiente.

.. literalinclude:: ../../recursos/leccion10/datetime_strptime.py
    :language: python
    :linenos:
    :lines: 1-16

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    Fecha y lugar de nacimiento: 03 de December de 1980 en Maracaibo, Zulia, Venezuela.


.. todo::
    TODO Terminar de escribir esta sección.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion10_datetime>`
    del entrenamiento para ampliar su conocimiento en esta temática.

.. _`datetime`: https://docs.python.org/es/3.7/library/datetime.html
