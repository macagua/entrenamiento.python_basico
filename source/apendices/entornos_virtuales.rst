.. _python_entornos_virtuales:

Entornos virtuales Python
=========================

`virtualenv`_ es una herramienta de Python que permite crear entornos virtuales
aislados para proyectos Python. Esto es útil para gestionar dependencias y evitar
conflictos entre diferentes proyectos.

Instalación
-----------

Para instalar este paquete ``virtualenv`` use la herramienta :ref:`pip <python_pip>`
ejecutando el siguiente comando, el cual a continuación se presentan el correspondiente
comando de tu sistema operativo:

.. tabs::

   .. group-tab:: macOS, Linux, y Windows con WSL

      .. code-block:: console

          sudo apt install -y python3-virtualenv

   .. group-tab:: Windows

      .. code-block:: console

          pip3 install virtualenv

Cree un directorio raíz para almacenar los diversos entornos virtuales,
ejecutando el siguiente comando:

.. code-block:: console

    mkdir ~/virtualenv && cd $_

Cree un entorno virtual llamado :command:`python3`, ejecutando el siguiente comando:

.. code-block:: console

    virtualenv --python /usr/bin/python3 python3

Activar el entorno virtual llamado :command:`python3`, ejecutando el siguiente comando:

.. code-block:: console

    source ~/virtualenv/python3/bin/activate

Para desactivar entorno virtual creado, con el siguiente comando:

.. code-block:: console

    deactivate

De esta forma, puedes tener un directorio común para almacenar diversos entornos virtuales.
Con herramientas como ``virtualenv`` puede gestionar diversos entornos virtuales de Python
para diversas versiones de Python, por ejemplo:

Diversas versiones de Python, es posible que requiera trabajar con un proyecto Python que
requiera la versión ``3.9`` y y al otro proyecto que requiera la versión ``3.11``, para estés
caso puede gestionar la instalación de las dos versiones de Python con la herramienta `pyenv`_
y luego crear dos entornos virtuales para cada version, con los siguientes comandos:

Crear y activar un entorno virtual para la versión Python ``3.9``, ejecutando el siguiente comando:

.. code-block:: console

    virtualenv --python ~/.pyenv/shims/python3.9 ~/virtualenv/python39 && source ~/virtualenv/python39/bin/activate


Crear y activar un entorno virtual para la versión Python ``3.11``, ejecutando el siguiente comando:

.. code-block:: console

    virtualenv --python ~/.pyenv/shims/python3.11 ~/virtualenv/python311 && source ~/virtualenv/python311/bin/activate


En estos casos anteriores, hemos creado dos entornos virtuales como ``python39`` y ``python311``,
esto le permite crear diversos entornos virtuales para proyectos, con el nombre que quiera,
podría ser un entorno virtual para llamado ``acme_inc`` para un cliente llamado **ACME Industry**
o otro entorno virtual llamado ``test-django`` para unas pruebas de un proyecto de Django.

.. tip::

   Normalmente es muy común conseguir en las instrucciones de instalación de entornos virtuales
   para diversos proyectos Python, con los siguientes nombres ``.env``, ``.venv`` y ``venv``.


Con esto, ya tiene todo listo para continuar.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::

.. _`virtualenv`: https://pypi.org/project/virtualenv/
.. _`pyenv`: https://github.com/pyenv/pyenv
