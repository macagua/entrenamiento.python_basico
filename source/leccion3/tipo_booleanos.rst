.. -*- coding: utf-8 -*-


.. _python_booleanos:

Tipo booleanos
--------------

Como decíamos el tipo booleano sólo puede tener dos valores: ``True``
(verdadero) y ``False`` (falso). Estos valores son especialmente importantes
para las expresiones condicionales y los bucles, como veremos más
adelante.

+----------+-----------+----------------------------------+----------------------+
| **Tipo** | **Clase** | **Notas**                        | **Ejemplo**          |
+----------+-----------+----------------------------------+----------------------+
| ``bool`` | Booleano  | Valor booleano verdadero o falso | ``True`` o ``False`` |
+----------+-----------+----------------------------------+----------------------+

En realidad el tipo ``bool`` (el tipo de los booleanos) es una subclase del
tipo ``int``. Puede que esto no tenga mucho sentido para usted si no conoces
los términos de la :ref:`orientación a objetos <python_poo>`, que se tocará 
más adelantes, aunque tampoco es nada importante.


Ejemplo de booleanos
....................

A continuación, se presentan algunos ejemplos de su uso:

**Ejemplo de tipos de datos booleanos**

.. literalinclude:: ../../recursos/leccion3/tipo_booleanos.py
    :linenos:
    :language: python
    :lines: 4-11


**Ejemplo de operadores booleanos**

.. literalinclude:: ../../recursos/leccion3/tipo_booleanos.py
    :linenos:
    :language: python
    :lines: 13-24


----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los **booleanos**
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente 
forma:

::

    >>> help(bool)

Para salir de esa ayuda presione la tecla ``q``.
