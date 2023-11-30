.. -*- coding: utf-8 -*-


.. _python_modulo_locale:

locale — Servicios de internacionalización
..........................................

.. note::
    **Propósito:** Formateo según la configuración regional

El módulo `locale`_ abre el acceso a la base de datos y la funcionalidad de `POSIX locale`_.
El mecanismo `POSIX locale`_ permite a los programadores tratar ciertos problemas culturales
en una aplicación, sin requerir que el programador conozca todos los detalles de cada país
donde se ejecuta el software.

El módulo ``locale`` se implementa en la parte superior del módulo ``_locale``, que a su vez
utiliza una implementación de configuración regional ANSI C si está disponible.

Uso del módulo ``locale``:


.. literalinclude:: ../../recursos/leccion10/locales.py
    :language: python
    :linenos:
    :lines: 1-27

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    miércoles, 03. diciembre 1980 12:00am

Jugando con el módulo ``locale`` en el ``ipython``:

.. code-block:: pycon

    In [1]: import locale

    In [2]: locale.setlocale(locale.LC_TIME,'')
    Out[3]: 'es_VE.UTF-8'

    In [3]: locale.nl_langinfo(locale.MON_12).capitalize()
    Out[3]: 'Diciembre'

    In [4]: dir(locale)
    Out[4]:
    ['ABDAY_1',
     'ABDAY_2',
     'ABDAY_3',
     'ABDAY_4',
     'ABDAY_5',
     'ABDAY_6',
     'ABDAY_7',
     'ABMON_1',
     'ABMON_10',
     'ABMON_11',
     'ABMON_12',
     'ABMON_2',
     'ABMON_3',
     'ABMON_4',
     'ABMON_5',
     'ABMON_6',
     'ABMON_7',
     'ABMON_8',
     'ABMON_9',
     'ALT_DIGITS',
     'AM_STR',
     'CHAR_MAX',
     'CODESET',
     'CRNCYSTR',
     'DAY_1',
     'DAY_2',
     'DAY_3',
     'DAY_4',
     'DAY_5',
     'DAY_6',
     'DAY_7',
     'D_FMT',
     'D_T_FMT',
     'ERA',
     'ERA_D_FMT',
     'ERA_D_T_FMT',
     'ERA_T_FMT',
     'Error',
     'LC_ALL',
     'LC_COLLATE',
     'LC_CTYPE',
     'LC_MESSAGES',
     'LC_MONETARY',
     'LC_NUMERIC',
     'LC_TIME',
     'MON_1',
     'MON_10',
     'MON_11',
     'MON_12',
     'MON_2',
     'MON_3',
     'MON_4',
     'MON_5',
     'MON_6',
     'MON_7',
     'MON_8',
     'MON_9',
     'NOEXPR',
     'PM_STR',
     'RADIXCHAR',
     'THOUSEP',
     'T_FMT',
     'T_FMT_AMPM',
     'YESEXPR',
     '__all__',
     '__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     '_append_modifier',
     '_build_localename',
     '_builtin_str',
     '_format',
     '_group',
     '_grouping_intervals',
     '_localeconv',
     '_override_localeconv',
     '_parse_localename',
     '_percent_re',
     '_print_locale',
     '_replace_encoding',
     '_setlocale',
     '_strcoll',
     '_strip_padding',
     '_strxfrm',
     '_test',
     'atof',
     'atoi',
     'bind_textdomain_codeset',
     'bindtextdomain',
     'collections',
     'currency',
     'dcgettext',
     'delocalize',
     'dgettext',
     'encodings',
     'format',
     'format_string',
     'functools',
     'getdefaultlocale',
     'getlocale',
     'getpreferredencoding',
     'gettext',
     'k',
     'locale_alias',
     'locale_encoding_alias',
     'localeconv',
     'nl_langinfo',
     'normalize',
     're',
     'resetlocale',
     'setlocale',
     'str',
     'strcoll',
     'strxfrm',
     'sys',
     'textdomain',
     'v',
     'windows_locale']

    In [4]: import datetime

    In [5]: dt = datetime.datetime(2015, 11, 15, 16, 30)

    In [6]: dt
    Out[6]: datetime.datetime(2015, 11, 15, 16, 30)

    In [7]: locale.setlocale(locale.LC_ALL, "es_VE.UTF-8")
    Out[7]: 'es_VE.UTF-8'

    In [8]: print(dt.strftime("%A, %d. %B %Y %I:%M%p"))
    domingo, 15. noviembre 2015 04:30pm

    In [9]: import os

    In [10]: os.environ['LANG']
    Out[10]: 'es_VE.UTF-8'

    In [11]: locale.setlocale(locale.LC_ALL, "")
    Out[11]: 'es_VE.UTF-8'

    In [12]: locale.setlocale(locale.LC_ALL, "es_VE.UTF-8")
    Out[12]: 'es_VE.UTF-8'

    In [13]: locale.setlocale(locale.LC_ALL, str(locale.getlocale()[0]) + "." + str(locale.getlocale()[1]))
    Out[13]: 'es_VE.UTF-8'

.. comments:

    .. todo::
        TODO Terminar de escribir esta sección.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion10_locale>`
    del entrenamiento para ampliar su conocimiento en esta temática.

.. _`locale`: https://docs.python.org/es/3.11/library/locale.html
.. _`POSIX locale`: https://es.wikipedia.org/wiki/Configuraci%C3%B3n_regional
