.. -*- coding: utf-8 -*-


.. _python_leccion3:

Tipos y estructuras de datos
============================

Los tipos de datos estándar disponibles por defecto en el interprete 
son numéricos, secuencias, mapeo, archivos, clases, instancias y 
excepciones. Se pueden resumir en esta tabla:

+-----------------------+----------------+---------------------------------+
| **Categoría de tipo** | **Nombre**     | **Descripción**                 |
+-----------------------+----------------+---------------------------------+
|                       | ``int``        | entero (precisión arbitraria)   |
|                       +----------------+---------------------------------+
|                       | ``float``      | coma flotante                   |
| Números               +----------------+---------------------------------+
|                       | ``complex``    | complejo                        |
|                       +----------------+---------------------------------+
|                       | ``bool``       | booleano (``True`` o ``False``) |
+-----------------------+----------------+---------------------------------+
|                       | ``str``        | cadena de caracteres            |
|                       +----------------+---------------------------------+
|                       | ``list``       | lista                           |
| Secuencias            +----------------+---------------------------------+
|                       | ``tuple``      | tupla                           |
|                       +----------------+---------------------------------+
|                       | ``range``      | rango de enteros                |
+-----------------------+----------------+---------------------------------+
| Mapeos                | ``dict``       | diccionario                     |
+-----------------------+----------------+---------------------------------+
|                       | ``set``        | conjunto mutable                |
| Conjuntos             +----------------+---------------------------------+
|                       | ``frozenset``  | conjunto inmutable              |
+-----------------------+----------------+---------------------------------+

Otros tipos de datos incorporados, se decscriben a continuación:

+-----------------------+----------------+-------------------------------------------+
| **Categoría de tipo** | **Nombre**     | **Descripción**                           |
+-----------------------+----------------+-------------------------------------------+
|                       | ``type(None)`` | el objeto                                 |
| None                  |                | :ref:`nulo <python_objeto_none>`          |
|                       |                | ``None``.                                 |
+-----------------------+----------------+-------------------------------------------+
|                       | ``file``       | el objeto                                 |
| Archivos              |                | :ref:`archivo <python_manipular_archivo>` |
|                       |                | o fichero.                                |
+-----------------------+----------------+-------------------------------------------+

En esta lección se describen los tipos de datos en el lenguaje Python, los 
cuales se resumieron en esta tabla. A continuación el temario de esta lección:

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
