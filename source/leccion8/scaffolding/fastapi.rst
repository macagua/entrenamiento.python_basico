.. _python_scaffolding_fastapi:

Ejemplo 3: Proyecto FastAPI
...........................

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

   .. group-tab:: macOS, Linux, y WSL

      .. code-block:: console

          pip3 install "fastapi-code-generator==0.5.2"

   .. group-tab:: Windows

      .. code-block:: console

          pip3 install fastapi-code-generator

Usted puede probar la instalación existe, ejecutando el siguiente comando:

.. tabs::

   .. group-tab:: macOS, Linux, y WSL

      .. code-block:: console

          python3 -c "import fastapi_code_generator ; print(fastapi_code_generator.__package__)"

   .. group-tab:: Windows

      .. code-block:: console

          python3 -c "import fastapi_code_generator ; print(fastapi_code_generator.__package__)"

Si muestra el nombre del módulo ``fastapi_code_generator``, tiene correctamente instalado el módulo.
Con esto, ya tiene todo listo para continuar.

.. code-block:: console

    fastapi-codegen --help



.. code-block:: console
    :class: no-copy

    Usage: fastapi-codegen [OPTIONS]

    ╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │    --encoding               -e      TEXT                                                                                 [default: utf-8]                                                                     │
    │ *  --input                  -i      TEXT                                                                                 [default: None] [required]                                                           │
    │ *  --output                 -o      PATH                                                                                 [default: None] [required]                                                           │
    │    --model-file             -m      TEXT                                                                                 [default: None]                                                                      │
    │    --template-dir           -t      PATH                                                                                 [default: None]                                                                      │
    │    --model-template-dir             PATH                                                                                 [default: None]                                                                      │
    │    --enum-field-as-literal          [all|one]                                                                            [default: None]                                                                      │
    │    --generate-routers       -r                                                                                                                                                                                │
    │    --specify-tags                   TEXT                                                                                 [default: None]                                                                      │
    │    --custom-visitor         -c      PATH                                                                                 [default: None]                                                                      │
    │    --disable-timestamp                                                                                                                                                                                        │
    │    --output-model-type      -d      [pydantic.BaseModel|pydantic_v2.BaseModel|dataclasses.dataclass|typing.TypedDict|ms  [default: pydantic.BaseModel]                                                        │
    │                                     gspec.Struct]                                                                                                                                                             │
    │    --python-version         -p      [3.6|3.7|3.8|3.9|3.10|3.11|3.12]                                                     [default: 3.8]                                                                       │
    │    --install-completion                                                                                                  Install completion for the current shell.                                            │
    │    --show-completion                                                                                                     Show completion for the current shell, to copy it or customize the installation.     │
    │    --help                                                                                                                Show this message and exit.                                                          │
    ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


De esta manera, puedes generar un proyecto FastAPI listo para ser usado y desplegar.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion8>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`cookiecutter`: https://pypi.org/project/cookiecutter/
.. _`fastapi-code-generator`: https://pypi.org/project/fastapi-code-generator/
.. _`SQLModel`: https://sqlmodel.tiangolo.com/
.. _`Typer`: https://typer.tiangolo.com/
