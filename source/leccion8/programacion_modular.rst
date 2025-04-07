.. _python_programacion_modular:

Programación modular
--------------------

La **programación modular** es un paradigma de desarrollo de software que consiste
en *dividir* un programa en partes más pequeñas y reutilizables, llamadas **módulos**.
En Python, un :ref:`módulo <python_modulos>` es simplemente un archivo ``.py`` que contiene
:ref:`funciones <python_funciones>`, :ref:`clases <python_clases>`, :ref:`variables <python_variable>`
o :ref:`constantes <python_constante>` que pueden ser reutilizadas en otros programas. Esta
técnica ayuda a mejorar la **organización** del código, la **reutilización**, la **legibilidad**
y el **mantenimiento** de los proyectos.


Características
...............

- **Reutilización de código**: Se pueden importar módulos en diferentes programas sin
  necesidad de reescribir :ref:`funciones <python_funciones>` o :ref:`clases <python_clases>`.

- **Mantenimiento más sencillo**: Facilita la actualización y corrección de errores sin
  afectar el resto del programa.

- **Legibilidad y estructura**: Permite organizar el código en archivos más pequeños y
  especializados.

- **Facilita el trabajo en equipo**: Cada programador puede desarrollar módulos independientes
  que luego se integran en un proyecto mayor.


Práctica - Caso real
....................

A continuación se presenta una práctica más real de implementar la *programación modular* en Python:

* **Uso de módulos de la librería estándar**

  Python incluye varios :ref:`módulos <python_modulos>` en la :ref:`librería estándar <python_libreria_estandar>`
  que podemos usar sin necesidad de instalación adicional, como :mod:`math` o :ref:`datetime <python_modulo_datetime>`:

  .. code-block:: pycon

      >>> import math
      >>> print(math.sqrt(25))  # Calcula la raíz cuadrada de 25
      5.0
      >>>

#. **Creación de un módulo en Python**

   Suponga que tiene un unico módulo Python llamado :file:`calculos_matematicos.py` con el siguiente
   codigo fuente:

   .. literalinclude:: ../../recursos/leccion8/modulos/calculadora/calculos_matematicos.py
       :language: python
       :linenos:
       :lines: 1-19

   Para ejecutar el módulo :file:`calculos_matematicos.py`, abra una consola de comando, acceda al
   directorio donde se encuentra el mismo, y ejecute el siguiente comando:

   .. code-block:: console

       python3 calculos_matematicos.py

   El anterior código al ejecutar debe mostrar el siguiente mensaje:

   ::

       La suma es: 15
       La resta es: 5


   Y usted necesita reusar las :ref:`funciones <python_funciones>` en otros módulos. Para esto se
   propone separar las funciones genericas en un módulo separado, por ejemplo, un módulo llamado
   :file:`operaciones.py` el cual realiza cálculos matemáticos con el siguiente codigo fuente:

   .. literalinclude:: ../../recursos/leccion8/modulos/calculadora/operaciones.py
       :language: python
       :linenos:
       :lines: 1-17


   .. tip::
       Un módulo en Python es simplemente un archivo con extensión `.py`.

   De esta manera, usted puede reutilizar el código de :file:`operaciones.py` en otros módulos
   sin necesidad de reescribir las :ref:`funciones <python_funciones>`.


#. **Importar una función en otro módulo**

   Puede importar y usar la :ref:`función <python_funciones>` de cálculos ``suma()`` en el archivo
   :file:`calculo_suma.py` de la siguiente manera:

   .. literalinclude:: ../../recursos/leccion8/modulos/calculadora/calculo_suma.py
       :language: python
       :linenos:
       :lines: 1-6


   Puede importar y usar la :ref:`función <python_funciones>` de cálculos ``resta()`` en el archivo
   :file:`calculo_resta.py` de la siguiente manera:

   .. literalinclude:: ../../recursos/leccion8/modulos/calculadora/calculo_resta.py
       :language: python
       :linenos:
       :lines: 1-6


   De esta manera, usted puede reutilizar el código de :file:`operaciones.py` en otros módulos Python.


.. important::
    La **programación modular** en Python es una práctica fundamental que mejora la **organización,
    escalabilidad y eficiencia** del código. Al dividir un programa en módulos reutilizables, los
    desarrolladores pueden trabajar de manera más estructurada y eficiente.


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:

    - :download:`calculos_matematicos.py <../../recursos/leccion8/modulos/calculadora/calculos_matematicos.py>`.

    - :download:`operaciones.py <../../recursos/leccion8/modulos/calculadora/operaciones.py>`.

    - :download:`calculo_suma.py <../../recursos/leccion8/modulos/calculadora/calculo_suma.py>`.

    - :download:`calculo_resta.py <../../recursos/leccion8/modulos/calculadora/calculo_resta.py>`.


.. tip::
    Para ejecutar el código :file:`operaciones.py`, :file:`calculo_suma.py` y :file:`calculo_resta.py`,
    abra una consola de comando, acceda al directorio donde se encuentra ambos programas:

    .. code-block:: console
      :class: no-copy

      calculadora/
      ├── operaciones.py
      ├── calculo_suma.py
      └── calculo_resta.py

    Si tiene la estructura de archivo previa, para ejecutar el módulo :file:`calculo_suma.py`,
    abra una consola de comando, acceda al directorio donde se encuentra el mismo, y ejecute el
    siguiente comando:

    .. code-block:: console

        python3 calculo_suma.py

    El anterior código al ejecutar debe mostrar el siguiente mensaje:

    ::

        La suma es: 15

    Si tiene la estructura de archivo previa, para ejecutar el módulo :file:`calculo_resta.py`,
    abra una consola de comando, acceda al directorio donde se encuentra el mismo, y ejecute el
    siguiente comando:


    .. code-block:: console

        python3 calculo_resta.py

    El anterior código al ejecutar debe mostrar el siguiente mensaje:

    ::

        La resta es: 5

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion8>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::
