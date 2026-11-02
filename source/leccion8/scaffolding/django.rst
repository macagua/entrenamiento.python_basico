.. _python_scaffolding_django:

Ejemplo 2: Proyecto Django
..........................

Por defecto, :ref:`Django <python_django>` incluye un comando para crear un nuevo proyecto y aplicaciones.

Paso 1: Instalación
~~~~~~~~~~~~~~~~~~~

Para instalar este paquete :ref:`Django <python_django>` use la herramienta :ref:`pip <python_pip>`
ejecutando el siguiente comando, el cual a continuación se presentan el correspondiente
comando de tu sistema operativo:

.. tabs::

   .. group-tab:: macOS, Linux, y WSL

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


De esta manera, ya tiene un proyecto Django listo para ser usado y desplegar.

----

.. important::
    Usted puede descargar el código usado en esta sección, haciendo clic en los
    siguientes enlaces:

    - :download:`mi_sitio.zip <../../../recursos/leccion8/mi_sitio.zip>`.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion8>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../../_templates/partials/soporte_profesional.html

..
  .. disqus::
