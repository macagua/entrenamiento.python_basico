.. _python_modulo_venv:

Módulo venv
===========

El módulo `venv`_ permite crear :ref:`entornos virtuales <python_entornos_virtuales>` ligeros,
cada uno con su propio conjunto independiente de paquetes de Python instalados en sus directorios
`site`_. Esto es útil para gestionar dependencias y evitar conflictos entre diferentes proyectos.

Instalación
-----------

Para instalar este módulo ``venv`` use la herramienta :ref:`pip <python_pip>`
ejecutando el siguiente comando, el cual a continuación se presentan el correspondiente
comando de tu sistema operativo:

.. tabs::

   .. group-tab:: Linux, y WSL

      .. code-block:: console

          sudo apt install -y python3-venv

   .. group-tab:: Windows

      Ya esta incluido en el instalador de Python

Para verificar que el módulo ``venv`` se ha instalado correctamente, escriba:

.. tabs::

   .. group-tab:: macOS, Linux, y WSL

      .. code-block:: console

          python3 -m venv --help

   .. group-tab:: Windows

      .. code-block:: console

          python3 -m venv --help


Si muestra la versión del módulo ``venv``, tiene correctamente instalado el módulo.


Crear entorno virtual
---------------------

Cree un entorno virtual llamado ``venv``, ejecutando el siguiente comando:

.. tabs::

   .. group-tab:: macOS, Linux, y WSL

      .. code-block:: console

          python3 -m venv ~/venv

   .. group-tab:: Windows

      .. code-block:: console

          python3 -m venv C:\venv


Activar entorno virtual
-----------------------

Los comandos de activación varían según el sistema operativo y el intérprete de comandos.

+-------------+----------------+--------------------------------------+
|     SO      |   Shell        | Comando de activación                |
+-------------+----------------+--------------------------------------+
| Windows     | Command Prompt | ruta\\al\\venv\\Scripts\\activate    |
+-------------+----------------+--------------------------------------+
| Windows     | PowerShell     | .\\ruta\\al\\venv\\Scripts\\Activate |
+-------------+----------------+--------------------------------------+
| macOS/Linux | Bash source    | ruta/al/venv/bin/activate            |
+-------------+----------------+--------------------------------------+
| macOS/Linux | Fish source    | ruta/al/venv/bin/activate.fish       |
+-------------+----------------+--------------------------------------+
| macOS/Linux | PowerShell     | ruta\\al\\venv\\Scripts\\Activate    |
+-------------+----------------+--------------------------------------+

Activar el entorno virtual llamado ``venv``, ejecutando el siguiente comando:

.. tabs::

   .. group-tab:: macOS, Linux, y WSL

      .. code-block:: console

          source ~/venv/bin/activate

   .. group-tab:: Windows

      .. code-block:: console

          source C:\venv\Scripts\activate


Desactivar entorno virtual
--------------------------

Para desactivar entorno virtual creado, con el siguiente comando:

.. tabs::

   .. group-tab:: macOS, Linux, y WSL

      .. code-block:: console

          deactivate

   .. group-tab:: Windows

      .. code-block:: console

          deactivate


De esta forma, puedes tener un directorio común para almacenar diversos :ref:`entornos virtuales <python_entornos_virtuales>`.

.. tip::

   Normalmente es muy común conseguir en las instrucciones de instalación de :ref:`entornos virtuales <python_entornos_virtuales>`
   para diversos proyectos Python, con los siguientes nombres ``.env``, ``.venv`` y ``venv``.


Con esto, ya tiene todo listo para continuar.

El uso del módulo ``venv`` de Python para crear un entorno virtual es una buena
práctica que te ayuda a gestionar las dependencias y a evitar conflictos entre
proyectos. Mantiene tu entorno de desarrollo limpio, organizado y más fácil de
mantener. Ahora que ya sabes cómo crear, activar y utilizar entornos virtuales,
estás listo para desarrollar aplicaciones en Python con confianza y claridad.


.. raw:: html
   :file: ../../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`venv`: https://docs.python.org/es/3/library/venv.html
.. _`site`: https://docs.python.org/es/3/library/site.html
.. _`pyenv`: https://github.com/pyenv/pyenv
