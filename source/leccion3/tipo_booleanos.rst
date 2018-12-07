.. -*- coding: utf-8 -*-


.. _python_booleanos:

Tipo booleanos
--------------

El tipo booleano sólo puede tener dos valores: ``True`` (verdadero) y ``False`` (falso). 
Estos valores son especialmente importantes para las expresiones condicionales y los 
bucles, como verá más adelante.

+----------+-----------+----------------------------------+----------------------+
| **Tipo** | **Clase** | **Notas**                        | **Ejemplo**          |
+----------+-----------+----------------------------------+----------------------+
| ``bool`` | Booleano  | Valor booleano verdadero o falso | ``True`` o ``False`` |
+----------+-----------+----------------------------------+----------------------+

En el contexto de las operaciones booleanas, y también cuando las expresiones son 
usadas bajo sentencias de flujo de control, los siguientes valores son interpretados 
como ``False``: 

- ``False``.

- :ref:`None <python_objeto_none>`.

- :ref:`Número cero <python_numericos>` en todos los tipos.

- :ref:`Cadena de caracteres <python_cadenas>` vaciás.

- Contenedores, incluyendo *cadenas de caracteres*, :ref:`tuplas <python_tuplas>`, 
  :ref:`listas <python_listas>`, :ref:`diccionarios <python_diccionarios>` y 
  :ref:`conjuntos <python_conjuntos>` mutables e inmutables.

A continuación, varios ejemplos en códigos de los citado previamente:

::

    >>> False
    False
    >>> False == False
    True
    >>> 0 == False
    True
    >>> "" == False
    False
    >>> None == False
    False
    >>> [] == False
    False
    >>> () == False
    False
    >>> {} == False
    False
    >>> ['', ''] == False
    False

Todos los otros valores son interpretadas a ``True``.

Los tipos integrados ``True`` y ``False`` son solamente dos instancias de la clase 
``bool``. En realidad el tipo ``bool`` (el tipo de los booleanos) es una 
:ref:`subclase <python_poo_herencia>` del tipo ``int``, y no puede ser a su vez una 
subclase. 

Puede que esto para usted, no lo entienda mucho, si no conoces los términos de 
la :ref:`orientación a objetos <python_poo>`, que se tocará más adelantes, aunque 
tampoco es nada importante.


Convertir a booleanos
.....................

Para convertir a *tipos booleanos* debe usar la función :ref:`bool() <python_fun_bool>` 
la cual :ref:`esta integrada <python_funciones_integradas>` en el interprete Python.


Ejemplo de booleanos
....................

A continuación, se presentan algunos ejemplos de su uso:

**Ejemplo de tipos de datos booleanos**

.. literalinclude:: ../../recursos/leccion3/tipo_booleanos.py
    :linenos:
    :language: python
    :lines: 7-11


**Ejemplo de operadores booleanos**

.. literalinclude:: ../../recursos/leccion3/tipo_booleanos.py
    :linenos:
    :language: python
    :lines: 17-24


----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los **booleanos**
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente 
forma:

::

    >>> help(bool)

Para salir de esa ayuda presione la tecla ``q``.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic 
    :download:`aquí <../../recursos/leccion3/tipo_booleanos.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_booleanos.py`, abra una 
    consola de comando, acceda al directorio donde se encuentra el mismo, 
    y ejecute el siguiente comando:

    ::

        python tipo_booleanos.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion3>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
