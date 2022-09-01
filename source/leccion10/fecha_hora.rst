.. -*- coding: utf-8 -*-


.. _python_modulo_datetime:

datetime
--------

Fecha y hora

.. comments:

    datos_basicos = {
        "nombres":"Leonardo Jose",
        "apellidos":"Caballero Garcia",
        "cedula":"26938401",
        "fecha_nacimiento":"03121980",
        "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
        "nacionalidad":"Venezolana",
        "estado_civil":"Soltero"
    }
    day, month, year = datos_basicos['fecha_nacimiento'][0:2], datos_basicos['fecha_nacimiento'][2:4], datos_basicos['fecha_nacimiento'][4:8]
    import datetime
    fecha_nacimiento = datetime.date(int(year), int(month), int(day))
    print("Fecha y lugar de nacimiento:", datetime.datetime.strftime(fecha_nacimiento, "%d de %B de %Y") + " en " + datos_basicos['lugar_nacimiento'] + ".")

    datos_basicos = {
        "nombres":"Leonardo Jose",
        "apellidos":"Caballero Garcia",
        "cedula":"26938401",
        "fecha_nacimiento":"03/12/1980",
        "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
        "nacionalidad":"Venezolana",
        "estado_civil":"Soltero"
    }

    import datetime, locale
    print("Fecha y lugar de nacimiento:", datetime.datetime.strftime(datetime.datetime.strptime(datos_basicos['fecha_nacimiento'], '%d/%m/%Y'), "%d de %B de %Y") + " en " + datos_basicos['lugar_nacimiento'] + ".")

    import locale
    locale.setlocale(locale.LC_TIME,'')
    locale.nl_langinfo(locale.MON_12).capitalize()

    dt = datetime.datetime(2015, 11, 15, 16, 30)
    locale.setlocale(locale.LC_ALL, "es_VE.UTF-8")
    print(dt.strftime("%A, %d. %B %Y %I:%M%p"))

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

.. todo::
    TODO escribir esta sección.

.. _`Formatting Python Dates According to Locale`: http://www.skybert.net/python/formatting-python-dates-according-to-locale/
