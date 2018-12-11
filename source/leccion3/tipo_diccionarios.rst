.. -*- coding: utf-8 -*-


.. _python_diccionarios:

Tipo diccionarios
-----------------

El diccionario, define una relación uno a uno entre claves y valores.

+-----------+----------+---------------------+----------------------------------+
| **Clase** | **Tipo** | **Notas**           | **Ejemplo**                      |
+-----------+----------+---------------------+----------------------------------+
| ``dict``  | Mapeos   | Mutable, sin orden. | ``{'cms':"Plone", 'version':5}`` |
+-----------+----------+---------------------+----------------------------------+

Un objeto *mapping* mapea valores *hashable* a objetos arbitrariamente. Los objetos 
Mapeos son objetos mutable. El *diccionario* es el único tipo de mapeo estándar 
actual. Para otro contenedores ver los integrados en las clases ":ref:`lista <python_listas>`", 
":ref:`conjuntos <python_conjuntos>`", y ":ref:`tupla <python_tuple>`", y el 
modulo "``collections``".

Los diccionarios pueden ser creados colocando una lista separada por coma de pares 
"key:value" entre ``{}``, por ejemplo: "``{'python': 27, 'plone': 51}``" o 
"``{27:'python', 51:'plone'}``", o por el constructor ":ref:`dict() <python_fun_dict>`".


::

    >>> diccionario = {
    ...     "clave1":234,
    ...     "clave2":True,
    ...     "clave3":"Valor 1",
    ...     "clave4":[1,2,3,4]
    ... }
    >>> print diccionario, type(diccionario)
    {'clave4': [1, 2, 3, 4], 'clave1': 234, 
    'clave3': 'Valor 1', 'clave2': True} <type 'dict'>

Usted puede acceder a los valores del diccionario usando cada su clave, se presenta 
unos ejemplos a continuación:

::

    >>> diccionario['clave1']
    234
    >>> diccionario['clave2']
    True
    >>> diccionario['clave3']
    'Valor 1'
    >>> diccionario['clave4']
    [1, 2, 3, 4]

Un diccionario puede almacenar los diveros tipos de datos integrados en Python usando 
la función :ref:`type() <python_fun_type>`, usted puede pasar el diccionario con la 
clave que usted desea determinar el tipo de dato, se presenta unos ejemplos a 
continuación:

::

    >>> type(diccionario['clave1'])
    <type 'int'>
    >>> type(diccionario['clave2'])
    <type 'bool'>
    >>> type(diccionario['clave3'])
    <type 'str'>
    >>> type(diccionario['clave4'])
    <type 'list'>


Convertir a diccionarios
........................

Para convertir a *tipos diccionarios* debe usar la función :ref:`dict() <python_fun_dict>` 
la cual :ref:`esta integrada <python_fun_builtins>` en el interprete Python.

.. tip:: 
    Para más información consulte las funciones integradas para 
    :ref:`operaciones de secuencias <python_fun_builtins_secuencias>`.


.. _python_diccionarios_ejs:

Ejemplos
........

A continuación, se presentan un ejemplo de su uso:

**Ejemplo de definición de un diccionario**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :lines: 8-16

**Ejemplo de operaciones con tipo diccionario con funciones propias**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :lines: 22-24

**Ejemplo de iteración avanzada sobre diccionarios con función iteritems**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :lines: 29-30

**Ejemplo real de usar tipo diccionario**

.. literalinclude:: ../../recursos/leccion3/tipo_diccionarios.py
    :language: python
    :lines: 33-50


----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los **diccionarios** 
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente forma:

::

    >>> help(dict)


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_diccionarios.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_diccionarios.py`, abra una consola de comando, 
    acceda al directorio donde se encuentra el mismo, y ejecute el siguiente comando:

    ::

        python tipo_diccionarios.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
