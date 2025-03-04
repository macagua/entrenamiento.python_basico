.. _python_bool:

Tipo booleanos
--------------

El tipo booleano sólo puede tener dos valores: ``True`` (verdadero) y ``False`` (falso).
Estos valores son especialmente importantes para las expresiones condicionales y los
bucles, como verá más adelante.

+-----------+-----------+---------------------------+-------------+
| **Clase** | **Tipo**  | **Notas**                 | **Ejemplo** |
+-----------+-----------+---------------------------+-------------+
| ``bool``  | Números   | Valor booleano falso.     | ``False``   |
+-----------+-----------+---------------------------+-------------+
| ``bool``  | Números   | Valor booleano verdadero. | ``True``    |
+-----------+-----------+---------------------------+-------------+

En el contexto de las operaciones booleanas, y también cuando las expresiones son
usadas bajo sentencias de flujo de control, los siguientes valores son interpretados
como ``False``:

- ``False``.

- :ref:`None <python_obj_none>`.

- :ref:`Número cero <python_int>` en todos los tipos.

- :ref:`Cadena de caracteres <python_str>` vacías.

- Contenedores, incluyendo :ref:`cadenas de caracteres <python_str>`, :ref:`tuplas <python_tuple>`,
  :ref:`listas <python_list>`, :ref:`diccionarios <python_dict>` y
  :ref:`conjuntos <python_set>` mutables e inmutables.

A continuación, varios ejemplos en códigos de los citado previamente:

.. code-block:: pycon

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
    >>> ["", ""] == False
    False

Todos los otros valores son interpretados por defecto a ``True``. El operador lógico
:ref:`not <python_opers_logicos>` produce ``True`` si su argumento es falso,
``False`` de lo contrario.

Los tipos integrados ``False`` y ``True`` son solamente dos instancias de la clase
``bool``. En realidad el tipo ``bool`` es una :ref:`subclase <python_poo_herencia>`
del tipo ``int`` o entero plano, es decir, sus valores son ``0`` y ``1`` respectivamente,
en casi todos los contextos:

.. code-block:: pycon

    >>> int(False)
    0
    >>> int(True)
    1

En el ejemplo anterior se convierte tipos booleanos a tipo enteros, siempre devuelve sus
valores numéricos ``0`` y ``1``. La excepción a la regla anterior sucede cuando un tipo
booleano es convertido a un tipo de :ref:`cadenas de caracteres <python_str>`, las cadenas
*'False'* y/o *'True'* son retornadas, respectivamente:

.. code-block:: pycon

    >>> type(True)
    <type 'bool'>
    >>> str(True)
    'True'
    >>> type(str(True))
    <type 'str'>
    >>>
    >>> type(False)
    <type 'bool'>
    >>> str(False)
    'False'
    >>> type(str(False))
    <type 'str'>


Puede que esto para usted, no lo entienda mucho, si no conoces los términos de
la :ref:`orientación a objetos <python_poo>`, que se tocará más adelante, aunque
tampoco es nada importante.

.. important::
    Los tipos *booleanos* no puede ser a su vez una subclase.


Convertir a booleanos
.....................

Para convertir a *tipos booleanos* debe usar la función :ref:`bool() <python_fun_bool>`
la cual :ref:`esta integrada <python_fun_builtins>` en el interprete Python.


.. _python_bool_ejs:

Ejemplos
........

A continuación, se presentan algunos ejemplos de su uso:

**Tipos de datos booleanos**

.. literalinclude:: ../../recursos/leccion3/tipo_booleanos.py
    :language: python
    :linenos:
    :lines: 6-8


**Operadores booleanos**

.. literalinclude:: ../../recursos/leccion3/tipo_booleanos.py
    :language: python
    :linenos:
    :lines: 14-19


----

Ayuda integrada
...............

Usted puede consultar toda la documentación disponible sobre los **booleanos**
desde la :ref:`consola interactiva <python_interactivo>` de la siguiente
forma:

.. code-block:: pycon

    >>> help(bool)

Para salir de esa ayuda presione la tecla :keys:`q`.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en el
    siguiente enlace:


    - :download:`tipo_booleanos.py <../../recursos/leccion3/tipo_booleanos.py>`.


.. tip::
    Para ejecutar el código :file:`tipo_booleanos.py`, abra una
    consola de comando, acceda al directorio donde se encuentra el mismo,
    y ejecute el siguiente comando:

    .. code-block:: console

        python3 tipo_booleanos.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion3>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
