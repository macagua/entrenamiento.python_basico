.. -*- coding: utf-8 -*-


.. _python_caracteristicas:

Características
---------------

Las `características`_ del lenguaje de programación Python se resumen
a continuación:

-   Es un `lenguaje interpretado`_, **no compilado**, usa :ref:`tipado dinámico <python_tipado_dinamico>`,
    :ref:`fuertemente tipado <python_fuertemente_tipado>`.

-   Es :ref:`multiplataforma <python_multiplataforma>`, lo cual es ventajoso para hacer
    ejecutable su código fuente entre varios sistema operativos.

-   Es un lenguaje de programación `multiparadigma`_, el cual soporta varios paradigma de
    programación como :ref:`orientación a objetos <python_poo>`,
    :ref:`estructurada <python_programacion_estructurada>`,
    `programación imperativa`_ y, en menor medida, `programación funcional`_.

-   En Python, el formato del código (p. ej., la indentación) es estructural.


.. _python_fuertemente_tipado:

Fuertemente tipado
..................

El `fuertemente tipado`_ significa que el tipo de valor no cambia repentinamente.
Un :ref:`string <python_str>` que contiene solo dígitos no se convierte mágicamente
en un número. Cada cambio de tipo requiere una conversión explícita. A continuación un
ejemplo de este concepto:

.. literalinclude:: ../../recursos/leccion1/fuertemente_tipados.py
    :language: python
    :linenos:
    :lines: 17-22


.. _python_tipado_dinamico:

Tipado dinámico
...............

El `tipado dinámico`_ significa que los objetos en tiempo de ejecución (valores)
tienen un tipo, a diferencia del tipado estático donde las variables tienen un tipo.
A continuación un ejemplo de este concepto:

.. literalinclude:: ../../recursos/leccion1/tipado_dinamico.py
    :language: python
    :linenos:
    :lines: 14-20


.. _python_multiplataforma:

Multiplataforma
...............

Python es `multiplataforma`_, lo cual es ventajoso para hacer ejecutable su código fuente
entre varios sistema operativos, eso quiere decir, soporta las siguientes plataformas para
su ejecución:

- Versiones Python para `Microsoft Windows (y DOS) <https://www.python.org/downloads/windows/>`_
  (arquitectura x86/x86-64 en presentación de ejecutable, archivo Zip, instalador basado en
  la Web).

  .. tip:: Para mayor información consulte la sección :ref:`Instalando Python en Windows <python_instalacion_windows>`.

- Versiones Python para `macOS (Macintosh) <https://www.python.org/downloads/macos/>`_
  (arquitectura 32bit/64bit en presentación de instalador ejecutable).

  .. tip:: Para mayor información consulte la sección :ref:`Instalando Python en una Mac <python_instalacion_mac>`.

- Versiones Python en `código fuente <https://www.python.org/downloads/source/>`_ (archivo
  tarball del código fuente comprimido con XZ y con Gz). Para las mayoría de los sistemas
  Linux/UNIX, usted debe descargar y compilar el código fuente.

  .. tip:: Para mayor información consulte la sección :ref:`Instalando Python en un Linux <python_instalacion_linux>`.

- Versiones de `Implementaciones Alternativas Python <https://www.python.org/download/alternatives/>`_,
  la versión "tradicional" de Python (tiene nombre código ``CPython``). Existen un número de
  implementaciones alternativas que están disponibles a continuación:

    - `IronPython <https://ironpython.net/>`_, Python ejecutando en .NET.

    - `Jython <https://www.jython.org/>`_, Python ejecutando en el Java Virtual Machine.

    - `PyPy <https://www.pypy.org/>`_, Una rápida implementación de python con un compilador JIT.

    - `Stackless Python <https://github.com/stackless-dev/stackless/wiki/>`_, Una rama del desarrollo
      del ``CPython`` que soporta microthreads.

    - `MicroPython <http://micropython.org/>`_, Python ejecutando en micro controladores.

- Versiones de Python en `otras plataformas <https://www.python.org/download/other/>`_,
  la versión "tradicional" de Python (tiene nombre código ``CPython``), mas esta versión ha
  sido migrada a un número plataformas especializadas y/o antiguas, a continuación se destacan
  algunas de ellas.

    - `Pythonista <http://omz-software.com/pythonista/index.html>`_, Python para iOS, ofrece un
      completo entorno de desarrollo para escribir scripts Python en su iPad o iPhone.

    - `ActivePython <https://www.activestate.com/products/python/>`_, Python para Solaris, Usted puede
      comprarlo (versiones comerciales y comunitarias, incluidos los módulos de computación científica,
      no de código abierto), o compilar desde una fuente si tiene un compilador de C.
      Los paquetes UNIX tienen una variedad de versiones de Python para una variedad de versiones de
      Solaris. Estos utilizan el estándar Sun ``pkgadd``.

  .. note::

      Tenga en cuenta que estos migraciones a menudo están muy por detrás de la última versión de Python.



Filosofía "Incluye baterías"
............................

- Python ha mantenido durante mucho tiempo esta filosofía de "baterías incluidas":

  *"Tener una biblioteca estándar rica y versátil que está disponible de inmediato.
  Sin que el usuario descargue paquetes separados."*

- Esto le da al lenguaje una ventaja en muchos proyectos.

- Las "baterías incluidas" están en la :ref:`librería estándar Python <python_libreria_estandar>`.


Zen de Python
.............

Es una colección de 20 principios de software que influyen en el diseño del Lenguaje
de Programación Python, de los cuales 19 fueron escritos por *Tim Peters* en junio de
1999. El texto es distribuido como dominio público.

El *Zen de Python* está escrito como la entrada informativa número 20 de las propuestas
de mejoras de Python (*Python Enhancement Proposals - PEP*), y se puede encontrar en el
sitio oficial de Python.

Los principios están listados a continuación:

- Bello es mejor que feo.

- Explícito es mejor que implícito.

- Simple es mejor que complejo.

- Complejo es mejor que complicado.

- Plano es mejor que anidado.

- Disperso es mejor que denso.

- La legibilidad cuenta.

- Los casos especiales no son tan especiales como para quebrantar las reglas.

- Lo práctico gana a lo puro.

- Los errores nunca deberían dejarse pasar silenciosamente.

- A menos que hayan sido silenciados explícitamente.

- Frente a la ambigüedad, rechaza la tentación de adivinar.

- Debería haber una -y preferiblemente sólo una- manera obvia de hacerlo.

- Aunque esa manera puede no ser obvia al principio a menos que usted sea holandés.

- Ahora es mejor que nunca.

- Aunque nunca es a menudo mejor que ya mismo.

- Si la implementación es difícil de explicar, es una mala idea.

- Si la implementación es fácil de explicar, puede que sea una buena idea.

- Los espacios de nombres (``namespaces``) son una gran idea ¡Hagamos más de esas cosas!

También se incluye como un *huevo de pascua*, el cual se puede encontrar, desde el
:ref:`intérprete de Python <python_interactivo>`, ingresar la siguiente sentencia:

.. code-block:: pycon

    >>> import this


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion1>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::


.. _`características`: https://es.wikipedia.org/wiki/Python#Características_y_paradigmas
.. _`multiparadigma`: https://es.wikipedia.org/wiki/Categor%C3%ADa:Lenguajes_de_programaci%C3%B3n_multiparadigma
.. _`programación estructurada`: https://es.wikipedia.org/wiki/Programación_estructurada
.. _`programación imperativa`: https://es.wikipedia.org/wiki/Programación_imperativa
.. _`programación funcional`: https://es.wikipedia.org/wiki/Programación_funcional
.. _`lenguaje interpretado`: https://es.wikipedia.org/wiki/Lenguaje_interpretado
.. _`tipado dinámico`: https://es.wikipedia.org/wiki/Tipado_dinámico
.. _`fuertemente tipado`: https://es.wikipedia.org/wiki/Lenguaje_de_programación_fuertemente_tipado
.. _`multiplataforma`: https://es.wikipedia.org/wiki/Multiplataforma
