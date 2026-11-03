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


A continuación se presenta algunos ejemplos de esta lección:

.. toctree::
   :maxdepth: 2

   python
   django
   fastapi

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


.. raw:: html
   :file: ../../_templates/partials/soporte_profesional.html

..
  .. disqus::
