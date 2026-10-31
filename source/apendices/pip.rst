.. _python_pip:


Python package installer - pip
==============================

`pip`_, es el instalador de paquetes de Python. Se integra con el módulo
:ref:`venv <python_modulo_venv>`, no hace instalaciones parciales,
puede guardar el estado del paquete para reproducirlo, puede instalar desde fuentes
que no sean :term:`Egg`, y puede instalar desde repositorios de control de versiones.

Instalación
-----------

Para instalar este paquete ``pip`` ejecute el siguiente comando, el cual a continuación
se presentan el correspondiente comando de tu sistema operativo:

.. tabs::

   .. group-tab:: macOS, Linux, y WSL

      .. code-block:: console

          sudo apt install -y python3-pip

   .. group-tab:: Windows

      En primer lugar, asegúrese de que Python está instalado en su sistema. Abra el símbolo
      del sistema y escriba el siguiente comando:

      .. code-block:: console

         python --version

      Si Python está instalado, mostrará el número de versión.

      Descargue el script :file:`get-pip.py` de la pagina web oficial, con el siguiente comando:

      .. code-block:: console

         curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

      Ejecute el script descargado utilizando Python, con el siguiente comando:

      .. code-block:: console

         python get-pip.py

      Para verificar que el comando :command:`pip` se ha instalado correctamente, escriba el
      siguiente comando:

      .. code-block:: console

         pip --version

      Si muestra la versión del comando :command:`pip`, tiene correctamente instalado el módulo.

      Si se encuentra con un error "pip no reconocido", añada el comando :command:`pip` a su variable de entorno ``PATH``:

      #. Localice el directorio de instalación del comando :command:`pip` (por ejemplo, :file:`C:\\Python311\\Scripts`).

      #. Vaya a *Panel de control* > *Sistema y seguridad* > *Sistema* > *Configuración avanzada del sistema*.

      #. Haga clic en *Variables de entorno*, busque la variable ``PATH`` y añada el directorio donde está instalado el comando :command:`pip`.

Para comprobar que la instalación de la herramienta :ref:`pip <python_pip>` este correctamente hecha,
ejecute el siguiente comando:

.. code-block:: console

    pip3 -V

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: console

    pip 26.2.2 from /usr/bin/lib/python3.11/site-packages/pip (python 3.11)

Si muestra el numero de la versión instalada de :ref:`pip <python_pip>`, tiene correctamente instalada
la paquete.

Con esto, ya tiene todo listo para continuar.

----


.. _python_pip_cache:


Cache local de paquetes
-----------------------

Crear directorio cache para paquetes Python descargados. Cuando hay latencia de
Internet y se requiere la instalación de paquetes de Python por un archivo
``requirements.txt`` de la herramienta :ref:`pip <python_pip>`
pero la instalación falló, entonces puede evitar que la herramienta :ref:`pip <python_pip>` vuelva
a descargar los paquetes previamente descargados, ejecutando este comando:

Cree un directorio cache para los paquetes descargando con la herramienta :ref:`pip <python_pip>`,
ejecutando el siguiente comando:

.. code-block:: console

    mkdir -p ~/.cache/pip && mkdir ~/.pip


Cree el archivo de configuración de la herramienta :ref:`pip <python_pip>`,
ejecutando el siguiente comando:

.. code-block:: console

    printf '[global]\ndownload_cache = ~/.cache/pip\n' >> ~/.pip/pip.conf

Así cada ves que ejecute el comando :command:`pip3 install` de la herramienta :ref:`pip <python_pip>`
usara el directorio :file:`~/.cache/pip` como directorio cache, esto permite agilizar la descarga
de paquetes, ya que :ref:`pip <python_pip>` primero buscara en ese archivo
primero, si no esta descargado, lo buscara en Internet en el repositorio :term:`PyPI`. Con esto,
ya tiene todo listo para continuar.


----


.. _python_pip_requirements:


Gestionar paquetes Python
-------------------------

Para gestionar paquetes Python dentro de un entorno virtual creado, con el siguiente comando:

.. code-block:: console

    pip3 install cookiecutter

El paquete `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_ se instalo
previamente puede usarlo vía script de línea de comando, con el siguiente:

.. code-block:: console

    cookiecutter --help

Ademas si requiere instalar paquetes Python con latencia de conexión a Internet. Cuando hay
latencia de Internet y se requiere la instalación de paquetes de Python, ejecute este
comando con el parámetro ``--timeout`` habilitado para el tiempo de espera:

.. code-block:: console

    pip3 install -U pip && pip3 install cookiecutter --timeout 120

También puede gestionar una lista de instalación de paquetes y sus versiones para indicar
a la herramienta :ref:`pip <python_pip>` que los instale con un solo comando, para esto cree y edite un
archivo, ejecutando lo siguiente:

.. code-block:: console

    nano requirements.txt

Agregue el siguiente contenido:

.. code-block:: console

    cookiecutter==2.7.1

Guarde el archivo y procede a ejecutar la herramienta :ref:`pip <python_pip>`, con el parámetro ``-r``
seguido de la ruta absoluta o relativa del archivo previamente creado.

.. code-block:: console

    pip3 install -r requirements.txt

Luego de la instalación puede ejecuta el comando :command:`cookiecutter -V` el cual ofrece
una salida de la versión.

.. code-block:: console

    cookiecutter -V

El comando :command:`pip list` mostrará todos los paquetes instalados en el entorno virtual:

.. code-block:: console

    pip list

Si ejecuto el comando anterior, debería mostrar algo parecido al siguiente mensaje:

.. code-block:: console
    :class: no-copy

    Package            Version
    ------------------ ----------
    arrow              1.4.0
    binaryornot        0.6.0
    certifi            2026.10.23
    charset-normalizer 3.5.2
    click              8.5.0
    cookiecutter       2.7.1
    idna               3.20
    Jinja2             3.1.6
    markdown-it-py     4.2.0
    MarkupSafe         3.0.4
    mdurl              0.1.2
    pip                23.0.1
    Pygments           2.21.0
    python-dateutil    3.0.0
    python-slugify     9.1.3
    PyYAML             6.0.3
    requests           2.34.2
    rich               15.0.0
    setuptools         66.1.1
    six                1.17.0
    text-unidecode     1.3
    tzdata             2026.6
    urllib3            2.8.0


El comando :command:`pip freeze` generará una lista similar de los paquetes instalados,
pero la salida utiliza el formato que espera el comando :command:`pip install`.
Una convención habitual es incluir esta lista en un archivo `requirements.txt <https://pip.pypa.io/en/stable/user_guide/#requirements-files>`_.

.. code-block:: console

    pip3 freeze

Si ejecuto el comando anterior, debería mostrar algo parecido al siguiente mensaje:

.. code-block:: console
    :class: no-copy

    arrow==1.4.0
    binaryornot==0.6.0
    certifi==2026.10.23
    charset-normalizer==3.5.2
    click==8.5.0
    cookiecutter==2.7.1
    idna==3.20
    Jinja2==3.1.6
    markdown-it-py==4.2.0
    MarkupSafe==3.0.4
    mdurl==0.1.2
    Pygments==2.21.0
    python-dateutil==3.0.0
    python-slugify==9.1.3
    PyYAML==6.0.3
    requests==2.34.2
    rich==15.0.0
    six==1.17.0
    text-unidecode==1.3
    tzdata==2026.6
    urllib3==2.8.0

Usted puede actualizar el archivo ``requirements.txt`` con el resultado de la ejecución el comando
``pip3 freeze`` ejecutando el siguiente comando:

.. code-block:: console

    pip3 freeze > requirements.txt

Así de esta forma ``congela`` las versiones usadas para el proceso de instalación de sus paquetes Python.

Con esto, ya tiene todo listo para continuar.


----


.. important::
    Usted puede descargar el archivo usado en esta sección haciendo clic en el
    siguiente enlace:

    - :download:`requirements.txt <../../recursos/apendices/pip/requirements.txt>`.


.. tip::
    Para ejecutar el archivo :file:`requirements.txt`, abra una consola de comando, active el
    :ref:`entorno virtual Python <python_entornos_virtuales>`, y se ubicas en el directorio
    donde descargo el archivo, entonces ejecute el siguiente comando:

    .. code-block:: console

        pip3 install -r requirements.txt


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`pip`: https://es.wikipedia.org/wiki/Pip_(administrador_de_paquetes)
