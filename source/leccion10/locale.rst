.. _python_modulo_locale:

Módulo locale
.............

.. note::
    **Propósito:** Formateo según la configuración regional, como servicios de internacionalización

El módulo :mod:`locale` abre el acceso a la base de datos y la funcionalidad de `POSIX locale`_.
El mecanismo `POSIX locale`_ permite a los programadores tratar ciertos problemas culturales
en una aplicación, sin requerir que el programador conozca todos los detalles de cada país
donde se ejecuta el software.

El módulo :mod:`locale` se implementa en la parte superior del módulo ``_locale``, que a su vez
utiliza una implementación de configuración regional ANSI C si está disponible.

Uso del módulo :mod:`locale`:


.. literalinclude:: ../../recursos/leccion10/locales.py
    :language: python
    :linenos:
    :lines: 1-27

Jugando con el módulo :mod:`locale` en el interprete :ref:`IPython <python_modulo_ipython>`:

Obtener el nombre del mes de Diciembre en base a la configuración regional actual:

.. code-block:: pycon
    :class: no-copy

    In [1]: import locale

    In [2]: locale.setlocale(locale.LC_TIME,'')
    Out[2]: 'es_VE.UTF-8'

    In [3]: locale.nl_langinfo(locale.MON_12).capitalize()
    Out[3]: 'Diciembre'

Obtener el formato de fecha y hora en base a la configuración regional actual:

.. code-block:: pycon
    :class: no-copy

    In [1]: import locale

    In [2]: import datetime

    In [3]: dt = datetime.datetime(2015, 11, 15, 16, 30)

    In [4]: dt
    Out[4]: datetime.datetime(2015, 11, 15, 16, 30)

    In [5]: locale.setlocale(locale.LC_ALL, "es_VE.UTF-8")
    Out[5]: 'es_VE.UTF-8'

    In [6]: print(dt.strftime("%A, %d. %B %Y %I:%M%p"))
    Out[6]: domingo, 15. noviembre 2015 04:30pm

Obtener el valor de la variable de entorno ``LANG`` en base a la configuración regional actual:

.. code-block:: pycon
    :class: no-copy

    In [1]: import locale

    In [2]: import os

    In [3]: os.environ['LANG']
    Out[3]: 'es_VE.UTF-8'

    In [4]: locale.setlocale(locale.LC_ALL, "")
    Out[4]: 'es_VE.UTF-8'

    In [5]: locale.setlocale(locale.LC_ALL, "es_VE.UTF-8")
    Out[5]: 'es_VE.UTF-8'

    In [6]: locale.setlocale(locale.LC_ALL, str(locale.getlocale()[0]) + "." + str(locale.getlocale()[1]))
    Out[6]: 'es_VE.UTF-8'


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`locales.py <../../recursos/leccion10/locales.py>`.


.. tip::
    Para ejecutar el código :file:`locales.py`, abra una consola de comando,
    acceda al directorio donde se encuentra el programa:

    .. code-block:: console
        :class: no-copy

        proyectos/
        └── locale/
            └── locales.py

    Si tiene la estructura de archivo previa, entonces ejecute los siguientes comandos:

    .. code-block:: console

        python3 locales.py

    El anterior código al ejecutar debe mostrar el siguiente mensaje:

    .. code-block:: console

        miércoles, 03. diciembre 1980 12:00am


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion10_locale>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`POSIX locale`: https://es.wikipedia.org/wiki/Configuraci%C3%B3n_regional
