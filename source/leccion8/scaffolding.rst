.. _python_scaffolding:

Scaffolding en proyectos Python
-------------------------------

.. _scaffolding_python:

¿Qué es el Scaffolding en Python?
.................................

**Scaffolding** (o “andamiaje” 🏗️) es una técnica de desarrollo que genera automáticamente la
estructura básica de un proyecto, incluyendo archivos, carpetas, y a veces código predefinido
(como controladores, modelos, vistas o rutas). Esto acelera el desarrollo inicial y mantiene
una arquitectura organizada.

.. tip::
  👉 En otras palabras, es como montar un esqueleto de tu aplicación para que tú solo te enfoques
  en la lógica de negocio.

La estructura del :term:`paquete Egg` Python es poco compleja. Por lo cual para empezar
con su primer proyecto y diversos módulos, puede usar el concepto **Scaffolding** para
crear un esqueleto de código usando las plantillas adecuadas para :term:`paquetes Python`.

Este concepto *scaffolding*, es muy útil para del arranque de su desarrollo, ofreciendo una
serie de colecciones de plantillas *esqueletos* que permiten iniciar rápidamente proyectos,
existente diversos *esqueletos* orientados a tipos de desarrollos específicos.


----


¿Por qué usar Scaffolding?
..........................

- Ahorra tiempo al generar estructuras comunes.

- Facilita buenas prácticas de arquitectura.

- Mejora la organización del proyecto.

- Acelera el inicio del desarrollo en frameworks web o CLI.


----


Herramientas comunes de Scaffolding en Python
.............................................

+-----------------------------+--------------------------------------------+----------------------+
| Herramientas                | Uso                                        | Ejemplo              |
+-----------------------------+--------------------------------------------+----------------------+
| `cookiecutter`              | Plantillas para cualquier tipo de proyecto | Web, CLI, librerías  |
+-----------------------------+--------------------------------------------+----------------------+
| `flask CLI` + extensiones   | Estructura básica de proyectos             | Aplicación Web       |
|                             | para :ref:`Flask <python_flask>`.          |                      |
+-----------------------------+--------------------------------------------+----------------------+
| `django-admin startproject` | Estructura básica de proyectos             | Aplicación Web       |
|                             | para :ref:`Django <python_django>`.        |                      |
+-----------------------------+--------------------------------------------+----------------------+
| `fastapi-code-generator`    | Generar base de API desde OpenAPI          | Aplicación APIs REST |
|                             | para :ref:`FastAPI <python_fastapi>`.      |                      |
+-----------------------------+--------------------------------------------+----------------------+


----


Ejemplo 1: Scaffolding con paquete Python
.........................................

`cookiecutter`_, ofrece varias plantillas para cualquier tipo de proyecto Python.

Para este caso, vamos a generar un proyecto de ejemplo para un paquete Python
que se llama ``mi_paquete``.

Paso 1: Instalación
~~~~~~~~~~~~~~~~~~~

Para instalar este paquete ``cookiecutter`` use la herramienta :ref:`pip <python_pip>`
ejecutando el siguiente comando, el cual a continuación se presentan el correspondiente
comando de tu sistema operativo:

.. tabs::

   .. group-tab:: macOS, Linux, y Windows con WSL

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


----


Ejemplo 2: Scaffolding con Django
.................................

Por defecto, :ref:`Django <python_django>` incluye un comando para crear un nuevo proyecto y aplicaciones.

Paso 1: Instalación
~~~~~~~~~~~~~~~~~~~

Para instalar este paquete :ref:`Django <python_django>` use la herramienta :ref:`pip <python_pip>`
ejecutando el siguiente comando, el cual a continuación se presentan el correspondiente
comando de tu sistema operativo:

.. tabs::

   .. group-tab:: macOS, Linux, y Windows con WSL

      .. code-block:: console

          pip3 install Django

   .. group-tab:: Windows

      .. code-block:: console

          pip3 install Django


Paso 2: Crear proyecto
~~~~~~~~~~~~~~~~~~~~~~

Para crear un nuevo proyecto :ref:`Django <python_django>`, ejecuta el siguiente comando:

.. code-block:: console

    django-admin startproject mi_sitio && cd mi_sitio


Paso 3: Crear aplicación
~~~~~~~~~~~~~~~~~~~~~~~~

Para crear una aplicación dentro del proyecto :ref:`Django <python_django>`, usa el siguiente comando:

.. code-block:: console

    python3 manage.py startapp blog


✅ Resultado: Carpetas listas para modelos, vistas, formularios y rutas.

.. code-block:: console
    :class: no-copy

    mi_sitio/
    ├── blog
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    └── mi_sitio
        ├── asgi.py
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py


----


Ejemplo 3: Scaffolding con FastAPI
..................................

Puedes usar generadores como `fastapi-code-generator`_ para :ref:`FastAPI <python_fastapi>`, `SQLModel`_,  y `Typer`_
o montar tu estructura así:

.. code-block:: console
    :class: no-copy

    app/
    ├── main.py
    ├── models/
    ├── routers/
    ├── services/
    └── config.py

O usar generadores personalizados.

Paso 1: Instalación
~~~~~~~~~~~~~~~~~~~

Para instalar este paquete ``fastapi-code-generator`` use la herramienta :ref:`pip <python_pip>`
ejecutando el siguiente comando, el cual a continuación se presentan el correspondiente
comando de tu sistema operativo:

.. tabs::

   .. group-tab:: macOS, Linux, y Windows con WSL

      .. code-block:: console

          pip3 install fastapi-code-generator

   .. group-tab:: Windows

      .. code-block:: console

          pip3 install fastapi-code-generator

----

Conclusión
..........

- **Scaffolding** en Python no es algo nativo del lenguaje, pero se apoya en herramientas que te ayudan a estructurar
  sus proyectos rápidamente.

- Puedes usarlo para crear APIs, CLI, librerías, dashboards y más.

- Ideal para mantener orden desde el principio y escalar de forma profesional.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion8>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`cookiecutter`: https://pypi.org/project/cookiecutter/
.. _`cookiecutter-pypackage`: https://github.com/audreyfeldroy/cookiecutter-pypackage
.. _`Django`: https://www.djangoproject.com/
.. _`fastapi-code-generator`: https://pypi.org/project/fastapi-code-generator/
.. _`SQLModel`: https://sqlmodel.tiangolo.com/
.. _`Typer`: https://typer.tiangolo.com/
