.. -*- coding: utf-8 -*-


.. _python_expresiones_condicional:

Expresiones condicional
-----------------------

Estos son los distintos tipos de expresiones condicionales:

+-------------------+--------------------------------------------------------------+
| **Expresiones**   | **Descripción**                                              |
+-------------------+--------------------------------------------------------------+
| ``if <OBJECT>``:  | Evaluá a ``False``:                                          |
|                   |  - cualquier numero igual a cero (0, 0.0, 0+0j).             |
|                   |  - un contenedor vació (:ref:`lista <python_listas>`,        |
|                   |    :ref:`tupla <python_tuplas>`,                             |
|                   |    :ref:`conjunto <python_conjuntos>`,                       |
|                   |    :ref:`diccionario <python_diccionarios>`).                |
|                   |  - ``False``, ``None``.                                      |
|                   | Evaluá a ``True``:                                           |
|                   |  - cualquier cosa de lo contrario.                           |
|                   |                                                              |
+-------------------+--------------------------------------------------------------+
| ``a == b``:       | Prueba igualdad, con lógicas:                                |
|                   |                                                              |
|                   | ::                                                           |
|                   |                                                              |
|                   |     >>> 1 == 1                                               |
|                   |     True                                                     |
|                   |                                                              |
+-------------------+--------------------------------------------------------------+
| ``a is b``:       | Prueba identidad: ambos lados debe ser el mismo objecto:     |
|                   |                                                              |
|                   | ::                                                           |
|                   |                                                              |
|                   |     >>> 1 is 1.                                              |
|                   |     False                                                    |
|                   |                                                              |
|                   |     >>> a = 1                                                |
|                   |     >>> b = 1                                                |
|                   |     >>> a is b                                               |
|                   |     True                                                     |
|                   |                                                              |
+-------------------+--------------------------------------------------------------+
| ``a in b``:       | Para cualquier colección b: ``b`` contenga ``a``:            |
|                   | ::                                                           |
|                   |                                                              |
|                   |     >>> b = [1, 2, 3]                                        |
|                   |     >>> 2 in b                                               |
|                   |     True                                                     |
|                   |     >>> 5 in b                                               |
|                   |     False                                                    |
|                   |                                                              |
|                   | Si ``b`` es un diccionario, este prueba que ``a`` sea una    |
|                   | key de ``b``.                                                |
|                   |                                                              |
+-------------------+--------------------------------------------------------------+

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion4>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
