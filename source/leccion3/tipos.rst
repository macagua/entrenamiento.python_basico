.. -*- coding: utf-8 -*-


.. _python_tipos:

Jerarquizar de tipos estándar
=============================

En Python tiene varios tipos de datos *compuestos* estándar disponibles por defecto en 
el interprete, como los tipos *numéricos*, *secuencias*, *mapeos* y *conjuntos* usados 
para agrupar otros valores.

Para el caso de las estructuras de datos se usan variables y constantes las cuales usan 
operadores para tratar los tipos de datos estándar. 

Los tipos de datos *compuestos* estándar se pueden clasificar como los dos siguientes:

- **Mutable:** su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.

- **Inmutable:** su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.

Se pueden resumir los tipos de datos *compuestos* estándar en la siguiente tabla:

+-----------------------+----------------+------------------------------------------------+
| **Categoría de tipo** | **Nombre**     | **Descripción**                                |
+-----------------------+----------------+------------------------------------------------+
|                       | ``int``        | :ref:`entero <python_num_entero>`              |
| *Números inmutables*  +----------------+------------------------------------------------+
|                       | ``long``       | :ref:`entero long <python_num_entero_long>`    |
|                       +----------------+------------------------------------------------+
|                       | ``float``      | :ref:`coma flotante <python_num_float>`        |
|                       +----------------+------------------------------------------------+
|                       | ``complex``    | :ref:`complejo <python_num_complex>`           |
|                       +----------------+------------------------------------------------+
|                       | ``bool``       | :ref:`booleano <python_bool>`                  |
+-----------------------+----------------+------------------------------------------------+
|                       | ``str``        | :ref:`cadena de caracteres <python_str>`       |
| *Secuencias           +----------------+------------------------------------------------+
| inmutables*           | ``unicode``    | cadena de caracteres ``Unicode``               |
|                       +----------------+------------------------------------------------+
|                       | ``tuple``      | :ref:`tupla <python_tuple>`                    |
|                       +----------------+------------------------------------------------+
|                       | ``xrange``     | :ref:`rango inmutable <python_fun_xrange>`     |
+-----------------------+----------------+------------------------------------------------+
|                       | ``list``       | :ref:`lista <python_list>`                     |
| *Secuencias mutables* +----------------+------------------------------------------------+
|                       | ``range``      | :ref:`rango mutable <python_fun_range>`        |
+-----------------------+----------------+------------------------------------------------+
| *Mapeos*              | ``dict``       | :ref:`diccionario <python_dict>`               |
+-----------------------+----------------+------------------------------------------------+
| *Conjuntos mutables*  | ``set``        | :ref:`conjunto mutable <python_set>`           |
+-----------------------+----------------+------------------------------------------------+
| *Conjuntos inmutables*| ``frozenset``  | :ref:`conjunto inmutable <python_set>`         |
+-----------------------+----------------+------------------------------------------------+

.. comments:

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
   |                       | ``bool``       | :ref:`booleano <python_bool>`                  |
   +-----------------------+----------------+------------------------------------------------+
   |                       | ``str``        | :ref:`cadena de caracteres <python_str>`       |
   |                       +----------------+------------------------------------------------+
   |                       | ``list``       | :ref:`lista <python_list>`                     |
   | Secuencias            +----------------+------------------------------------------------+
   |                       | ``tuple``      | :ref:`tupla <python_tuple>`                    |
   |                       +----------------+------------------------------------------------+
   |                       | ``range``      | :ref:`rango mutable <python_fun_range>`        |
   |                       +----------------+------------------------------------------------+
   |                       | ``xrange``     | :ref:`rango inmutable <python_fun_xrange>`     |
   +-----------------------+----------------+------------------------------------------------+
   | Mapeos                | ``dict``       | :ref:`diccionario <python_dict>`               |
   +-----------------------+----------------+------------------------------------------------+
   |                       | ``set``        | :ref:`conjunto mutable <python_set>`           |
   | Conjuntos             +----------------+------------------------------------------------+
   |                       | ``frozenset``  | :ref:`conjunto inmutable <python_set>`         |
   +-----------------------+----------------+------------------------------------------------+

Otros tipos de datos incorporados, se describen a continuación:

+-----------------------+------------------------+--------------------------------------------+
| **Categoría de tipo** | **Nombre**             | **Descripción**                            |
+-----------------------+------------------------+--------------------------------------------+
| *Objeto integrado*    | ``NoneType``           | el objeto                                  |
|                       |                        | :ref:`None <python_obj_none>`.             |
+-----------------------+------------------------+--------------------------------------------+
| *Objeto integrado*    | ``NotImplementedType`` | el objeto                                  |
|                       |                        | :ref:`NotImplemented <python_obj_notimp>`. |
+-----------------------+------------------------+--------------------------------------------+
| *Objeto integrado*    | ``ellipsis``           | el objeto                                  |
|                       |                        | :ref:`Ellipsis <python_obj_ellipsis>`.     |
+-----------------------+------------------------+--------------------------------------------+
| *Objeto integrado*    | ``file``               | el objeto                                  |
|                       |                        | :ref:`file <python_cls_file>`.             |
+-----------------------+------------------------+--------------------------------------------+

