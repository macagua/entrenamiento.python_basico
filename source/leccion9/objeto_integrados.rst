.. -*- coding: utf-8 -*-


.. _python_obj_tipos_builtins:

Objetos de tipos integrados
---------------------------

Existe otros :ref:`tipos de datos integrados <python_tipos>` en el interprete Python, 
que para muchos no son de uso frecuente, los cuales se describen a continuación:


.. _python_obj_ellipsis:

Ellipsis
........

Este tipo tiene un solo valor. Hay un solo objeto con este valor. Se accede a este 
objeto ``elipsis`` a través del nombre incorporado "``Ellipsis``". Se utiliza para 
indicar la presencia de la sintaxis "``...``" en una porción o  la notación de corte 
extendida. Su valor de verdad es ``True``.

::

    >>> type(Ellipsis)
    <type 'ellipsis'>



.. _python_obj_none:

None
....

Este tipo tiene un solo valor. Hay un solo objeto con este valor. Se accede a este 
objeto a través del nombre incorporado "``None``". Se utiliza para indicar la ausencia 
de un valor en muchas situaciones, por ejemplo, se devuelve desde las funciones que no 
devuelven nada explícitamente. Su valor de verdad es ``False``.

::

    >>> type(None)
    <type 'NoneType'>

.. _python_obj_notimp:

NotImplemented
..............

Este tipo tiene un solo valor. Hay un solo objeto con este valor. Se accede a este 
objeto a través del nombre incorporado "``NotImplemented``". Los métodos numéricos 
y los métodos de comparación enriquecidos (como ``__eq__()``, ``__lt__()`` y amigos), 
para indicar que la comparación no se implementa con respecto al otro tipo, es decir,
pueden devolver este valor si no implementan la operación para los operandos 
proporcionados. (El intérprete luego intentará la operación reflejada, o algún otro 
respaldo "``fallback``", dependiendo del operador). Su valor de verdad es ``True``.

::

    >>> type(NotImplemented)
    <type 'NotImplementedType'>


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion9>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
