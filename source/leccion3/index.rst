.. -*- coding: utf-8 -*-


.. _python_leccion3:

Tipos y estructuras de datos
============================

En Python para estructuras de datos se usan variables y constantes las cuales usan operadores 
para tratar los tipos de datos estándar disponibles por defecto en el interprete. Se pueden 
resumir en esta tabla:

+-----------------------+----------------+------------------------------------------------------+
| **Categoría de tipo** | **Nombre**     | **Descripción**                                      |
+-----------------------+----------------+------------------------------------------------------+
|                       | ``int``        | :ref:`entero <python_numericos>`                     |
|                       |                | (precisión arbitraria)                               |
|                       +----------------+------------------------------------------------------+
|                       | ``float``      | :ref:`coma flotante <python_numerico_coma_flotante>` |
| Números               +----------------+------------------------------------------------------+
|                       | ``complex``    | :ref:`complejo <python_numerico_complejo>`           |
|                       +----------------+------------------------------------------------------+
|                       | ``bool``       | :ref:`booleano <python_numerico_complejo>`           |
|                       | ``bool``       | (``True`` o ``False``)                               |
+-----------------------+----------------+------------------------------------------------------+
|                       | ``str``        | :ref:`cadena de caracteres <python_cadenas>`         |
|                       +----------------+------------------------------------------------------+
|                       | ``list``       | :ref:`lista <python_listas>`                         |
| Secuencias            +----------------+------------------------------------------------------+
|                       | ``tuple``      | :ref:`tupla <python_tuplas>`                         |
|                       +----------------+------------------------------------------------------+
|                       | ``range``      | :ref:`rango de enteros <python_funcion_range>`       |
+-----------------------+----------------+------------------------------------------------------+
| Mapeos                | ``dict``       | :ref:`diccionario <python_diccionarios>`             |
+-----------------------+----------------+------------------------------------------------------+
|                       | ``set``        | :ref:`conjunto mutable <python_conjuntos>`           |
| Conjuntos             +----------------+------------------------------------------------------+
|                       | ``frozenset``  | :ref:`conjunto inmutable <python_conjuntos>`         |
+-----------------------+----------------+------------------------------------------------------+

Otros tipos de datos incorporados, se describen a continuación:

+-----------------------+----------------+-------------------------------------+
| **Categoría de tipo** | **Nombre**     | **Descripción**                     |
+-----------------------+----------------+-------------------------------------+
|                       | ``type(None)`` | el objeto                           |
| None                  |                | :ref:`nulo <python_objeto_none>`    |
|                       |                | ``None``.                           |
+-----------------------+----------------+-------------------------------------+
|                       | ``file``       | el objeto                           |
| Archivos              |                | :ref:`archivo <python_objeto_file>` |
|                       |                | o fichero.                          |
+-----------------------+----------------+-------------------------------------+

En esta lección se describen las variables, operadores y sus tipos de datos en el lenguaje Python, 
los cuales se resumieron en esta tabla. A continuación el temario de esta lección:

.. toctree::
   :maxdepth: 2

   variables_constantes
   operadores_asignaciones
   operadores_aritmeticos
   operadores_relacionales
   tipo_numericos
   tipo_booleanos
   tipo_cadenas
   tipo_listas
   tipo_tuplas
   tipo_diccionarios
   tipo_conjuntos
