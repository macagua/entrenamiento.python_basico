.. _python_scaffolding_python_pkg:

Ejemplo 1: Paquete Python
.........................

`cookiecutter`_, ofrece varias plantillas para cualquier tipo de proyecto Python.

Para este caso, vamos a generar un proyecto de ejemplo para un paquete Python
que se llama ``mi_paquete``.

Paso 1: Instalación
~~~~~~~~~~~~~~~~~~~

Para instalar este paquete ``cookiecutter`` use la herramienta :ref:`pip <python_pip>`
ejecutando el siguiente comando, el cual a continuación se presentan el correspondiente
comando de tu sistema operativo:

.. tabs::

   .. group-tab:: macOS, Linux, y WSL

      .. code-block:: console

          pip3 install cookiecutter

   .. group-tab:: Windows

      .. code-block:: console

          pip3 install cookiecutter


Paso 2: Crear paquete Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`cookiecutter-pypackage`_, es una plantilla ``cookiecutter`` para un paquete Python.

.. code-block:: console

    cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage


Paso 3: Responder preguntas
~~~~~~~~~~~~~~~~~~~~~~~~~~~

El generador te preguntará:

.. code-block:: console
    :class: no-copy

    [1/14] full_name (Audrey Roy Greenfeld): Leonardo J. Caballero G.
    [2/14] email (audreyr@example.com): leonardocaballero@gmail.com
    [3/14] github_username (audreyr): macagua
    [4/14] project_name (Python Boilerplate): Mi Paquete
    [5/14] project_slug (mi_paquete):
    [6/14] project_short_description (Python Boilerplate contains all the boilerplate you need to create a Python package.): Mi primer paquete Python
    [7/14] pypi_username (macagua):
    [8/14] version (0.1.0): 0.0.1
    [9/14] use_pytest (n): y
    [10/14] use_pypi_deployment_with_travis (y):
    [11/14] add_pyup_badge (n):
    [12/14] Select command_line_interface
      1 - Typer
      2 - Argparse
      3 - No command-line interface
      Choose from [1/2/3] (1):
    [13/14] create_author_file (y):
    [14/14] Select open_source_license
      1 - MIT license
      2 - BSD license
      3 - ISC license
      4 - Apache Software License 2.0
      5 - GNU General Public License v3
      6 - Not open source
      Choose from [1/2/3/4/5/6] (1):


✅ Resultado: carpeta con todo lo necesario:

.. code-block:: console
    :class: no-copy

    mi_paquete/
    ├── AUTHORS.rst
    ├── CODE_OF_CONDUCT.rst
    ├── CONTRIBUTING.rst
    ├── docs
    │   ├── authors.rst
    │   ├── conf.py
    │   ├── contributing.rst
    │   ├── history.rst
    │   ├── index.rst
    │   ├── installation.rst
    │   ├── make.bat
    │   ├── Makefile
    │   ├── readme.rst
    │   └── usage.rst
    ├── HISTORY.rst
    ├── LICENSE
    ├── Makefile
    ├── MANIFEST.in
    ├── pyproject.toml
    ├── README.rst
    ├── requirements_dev.txt
    ├── ruff.toml
    ├── src
    │   └── mi_paquete
    │       ├── cli.py
    │       ├── __init__.py
    │       └── mi_paquete.py
    ├── tests
    │   ├── __init__.py
    │   └── test_mi_paquete.py
    └── tox.ini


De esta manera, ya tiene un paquete Python listo para ser usado y distribuido.


----

.. important::
    Usted puede descargar el código usado en esta sección, haciendo clic en los
    siguientes enlaces:

    - :download:`mi_paquete.zip <../../../recursos/leccion8/mi_paquete.zip>`.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion8>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`cookiecutter`: https://pypi.org/project/cookiecutter/
.. _`cookiecutter-pypackage`: https://github.com/audreyfeldroy/cookiecutter-pypackage
