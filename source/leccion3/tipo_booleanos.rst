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

En realidad el tipo ``bool`` (el tipo de los booleanos) es una :ref:`subclase <python_poo_herencia>` 
del tipo ``int``. Puede que esto para usted, no lo entienda mucho, si no conoces los 
términos de la :ref:`orientación a objetos <python_poo>`, que se tocará más adelantes, 
aunque tampoco es nada importante.


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


.. important::
	Usted puede descargar el código usado en esta sección haciendo clic 
	:download:`aquí <../../recursos/leccion3/tipo_booleanos.py>`.


.. tip::
	Para ejecutar el código :file:`tipo_booleanos.py`, abra una 
	consola de comando, acceda al dirfectorio donde se encuentra el mismo, 
	y ejecute el siguiente comando: ::

		python2 tipo_booleanos.py


----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los **booleanos**
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente 
forma:

::

    >>> help(bool)

Para salir de esa ayuda presione la tecla ``q``.


.. seealso:: 

    .. figure:: https://img.youtube.com/vi/ZrxcqbFYjiw/0.jpg
        :align: center
        :width: 60%

        Vídeo `Tutorial Python 5 - Booleanos, operadores lógicos y cadenas`_, 
        cortesía de `CodigoFacilito.com`_.

    .. todo:: Cambiar la URL de imagen de previsualización del video, de forma local.

.. _`Tutorial Python 5 - Booleanos, operadores lógicos y cadenas`: https://www.youtube.com/watch?v=ZrxcqbFYjiw
.. _`CodigoFacilito.com`: https://www.codigofacilito.com/
