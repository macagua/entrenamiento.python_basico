.. -*- coding: utf-8 -*-


.. _python_leccion3:

Tipos y estructuras de datos
============================

En Python para estructuras de datos se usan variables y constantes las cuales usan operadores 
para tratar los tipos de datos estándar disponibles por defecto en el interprete. Se pueden 
resumir en esta tabla:

+-----------------------+----------------+------------------------------------------------+
| **Categoría de tipo** | **Nombre**     | **Descripción**                                |
+-----------------------+----------------+------------------------------------------------+
|                       | ``int``        | :ref:`entero <python_numericos>`               |
|                       +----------------+------------------------------------------------+
|                       | ``long``       | :ref:`entero long <python_num_entero_long>`    |
|                       +----------------+------------------------------------------------+
|                       | ``float``      | :ref:`coma flotante <python_num_float>`        |
| Números               +----------------+------------------------------------------------+
|                       | ``complex``    | :ref:`complejo <python_num_complex>`           |
|                       +----------------+------------------------------------------------+
|                       | ``bool``       | :ref:`booleano <python_booleanos>`             |
+-----------------------+----------------+------------------------------------------------+
|                       | ``str``        | :ref:`cadena de caracteres <python_str>`       |
|                       +----------------+------------------------------------------------+
|                       | ``list``       | :ref:`lista <python_listas>`                   |
| Secuencias            +----------------+------------------------------------------------+
|                       | ``tuple``      | :ref:`tupla <python_tuplas>`                   |
|                       +----------------+------------------------------------------------+
|                       | ``range``      | :ref:`rango mutable <python_fun_range>`        |
+-----------------------+----------------+------------------------------------------------+
|                       | ``xrange``     | :ref:`rango inmutable <python_fun_xrange>`     |
+-----------------------+----------------+------------------------------------------------+
| Mapeos                | ``dict``       | :ref:`diccionario <python_diccionarios>`       |
+-----------------------+----------------+------------------------------------------------+
|                       | ``set``        | :ref:`conjunto mutable <python_conjuntos>`     |
| Conjuntos             +----------------+------------------------------------------------+
|                       | ``frozenset``  | :ref:`conjunto inmutable <python_conjuntos>`   |
+-----------------------+----------------+------------------------------------------------+

Otros tipos de datos incorporados, se describen a continuación:

+-----------------------+----------------+-------------------------------------+
| **Categoría de tipo** | **Nombre**     | **Descripción**                     |
+-----------------------+----------------+-------------------------------------+
|                       | ``NoneType``   | el objeto                           |
| None                  |                | :ref:`nulo <python_objeto_none>` o  |
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
