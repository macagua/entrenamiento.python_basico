.. -*- coding: utf-8 -*-


.. _python_types:

Jerarquía de tipos estándar
===========================

A continuación se muestra una lista de los tipos que están integrados en Python. Los
módulos de extensión (escritos en C, Java u otros lenguajes, dependiendo de la
implementación) pueden definir tipos adicionales. Las versiones futuras de Python
pueden agregar tipos a la jerarquía de tipos (por ejemplo, números racionales, arrays
de enteros almacenados eficientemente, etc.).

Algunas de las descripciones de tipo a continuación contienen un párrafo que
enumera los "atributos especiales". Estos son atributos que proporcionan acceso a
la implementación y no están destinados para uso general. Su definición puede cambiar
en el futuro.

En Python tiene varios tipos de datos *compuestos* estándar disponibles por defecto en
el interprete, como los tipos *numéricos*, *secuencias*, *mapeos* y *conjuntos* usados
para agrupar otros valores.

Para el caso de las estructuras de datos se usan variables y constantes las cuales usan
operadores para tratar los tipos de datos estándar.


.. _python_types_clasif:

Clasificación
-------------

Los tipos de datos *compuestos* estándar se pueden clasificar como los dos siguientes:

- **Mutable:** su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.

- **Inmutable:** su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.

Se pueden resumir los tipos de datos *compuestos* estándar en la siguiente tabla:

+-----------------------+---------------+----------------------------------------------------------+
| **Categoría de tipo** | **Nombre**    | **Descripción**                                          |
+-----------------------+---------------+----------------------------------------------------------+
|                       | ``int``       | :ref:`entero <python_num_entero>`                        |
| *Números inmutables*  +---------------+----------------------------------------------------------+
|                       | ``long``      | :ref:`entero long <python_num_entero_long>`              |
|                       +---------------+----------------------------------------------------------+
|                       | ``float``     | :ref:`coma flotante <python_num_float>`                  |
|                       +---------------+----------------------------------------------------------+
|                       | ``complex``   | :ref:`complejo <python_num_complex>`                     |
|                       +---------------+----------------------------------------------------------+
|                       | ``bool``      | :ref:`booleano <python_bool>`                            |
+-----------------------+---------------+----------------------------------------------------------+
|                       | ``str``       | :ref:`cadena de caracteres <python_str>`                 |
| *Secuencias           +---------------+----------------------------------------------------------+
| inmutables*           | ``tuple``     | :ref:`tupla <python_tuple>`                              |
+-----------------------+---------------+----------------------------------------------------------+
|                       | ``list``      | :ref:`lista <python_list>`                               |
| *Secuencias mutables* +---------------+----------------------------------------------------------+
|                       | ``range``     | :ref:`rango mutable <python_fun_range>`                  |
+-----------------------+---------------+----------------------------------------------------------+
| *Mapeos*              | ``dict``      | :ref:`diccionario <python_dict>`                         |
+-----------------------+---------------+----------------------------------------------------------+
| *Conjuntos mutables*  | ``set``       | :ref:`conjunto mutable <python_set>`                     |
+-----------------------+---------------+----------------------------------------------------------+
| *Conjuntos inmutables*| ``frozenset`` | :ref:`conjunto inmutable <python_set>`                   |
+-----------------------+---------------+----------------------------------------------------------+

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

.. _python_types_objs:

Objectos Type
-------------

Los objectos Type representan los diversos tipos de objetos. Un objecto type es accedido por
la función integrada :ref:`type() <python_fun_type>`. No hay operaciones especiales
en los tipos. El módulo estándar ``types`` defines los nombres para todos los tipos
integrados estándar.

Los tipos son escritos como esto: "<type 'int'>".


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
