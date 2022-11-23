.. -*- coding: utf-8 -*-


.. _python_skel:

Scaffolding en proyectos Python
-------------------------------

.. sidebar:: Sobre este artículo

    :Autor(es): Leonardo J. Caballero G.
    :Correo(s): :email:`leonardoc@plone.org`
    :Compatible con: Python 3.7 o versiones superiores
    :Fecha: 23 de Noviembre de 2022

.. _scaffolding_python:

La estructura del :term:`paquete Egg` Python es poco compleja. Por lo cual para empezar
con su primer proyecto y diversos módulos, puede usar el concepto **Scaffolding** para
crear un esqueleto de código usando las plantillas adecuadas para :term:`paquetes Python`.

Este concepto *scaffolding*, es muy útil para del arranque de su desarrollo, ofreciendo una
serie de colecciones de plantillas *esqueletos* que permiten iniciar rápidamente proyectos,
existente diversos *esqueletos* orientados a tipos de desarrollos específicos.

.. _que_es_pastescript:

¿Qué es PasteScript?
....................

Es una herramienta de linea de comando basada en plugins que le permiten crear
estructuras de paquetes de proyectos Python además sirve aplicaciones web, con
configuraciones basadas en `paste.deploy`_.


Instalación
~~~~~~~~~~~

Dentro de su `entorno virtual`_ activado debe instalar el paquete `PasteScript`_,
ejecutando el siguiente comando:

.. code-block:: console

    (venv)$ pip install PasteScript

.. note::

  No olvidar que estos paquetes han sido instalados con el entorno virtual que
  previamente usted activo, eso quiere decir que los paquetes previamente
  instalados con `easy_install`_ están instalados en el
  directorio :file:`~/virtualenv/venv/lib/python3.x/site-packages/` en ves del
  directorio de su versión de Python de sistema :file:`/usr/lib/python3.x/site-packages/`

Al finalizar la instalación podrá opcionalmente consultar cuales plantillas
tiene disponible para usa, ejecutando el siguiente comando:

.. code-block:: console

    (venv)$ paster create --list-templates
      Available templates:
        basic_package:       A basic setuptools-enabled package
        paste_deploy:        A web application deployed through paste.deploy

Usted puede usar el comando :command:`paster` para crear paquetes Python.

.. code-block:: console

    (venv)$ paster create -t basic_package mipaquetepython

      Selected and implied templates:

        PasteScript#basic_package  A basic setuptools-enabled package

      Variables:
        egg:      mipaquetepython
        package:  mipaquetepython
        project:  mipaquetepython
      Enter version (Version (like 0.1)) ['']: 0.1
      Enter description (One-line description of the package) ['']: Mi Paquete Básico
      Enter long_description (Multi-line description (in reST)) ['']: Mi Paquete Básico para demostrar el uso de PasteScript
      Enter keywords (Space-separated keywords/tags) ['']: PasteScript Basic Package Demo
      Enter author (Author name) ['']: Pedro Picapiedra
      Enter author_email (Author email) ['']: pedro@acme.com
      Enter url (URL of homepage) ['']: https://github.com/pyve/mipaquetepython
      Enter license_name (License name) ['']: GPL
      Enter zip_safe (True/False: if the package can be distributed as a .zip file) [False]:
      Creating template basic_package
      Creating directory ./mipaquetepython
        Recursing into +package+
          Creating ./mipaquetepython/mipaquetepython/
          Copying __init__.py to
          ./mipaquetepython/mipaquetepython/__init__.py
        Copying setup.cfg to ./mipaquetepython/setup.cfg
        Copying setup.py_tmpl to ./mipaquetepython/setup.py
      Running /home/macagua/virtualenv/venv/bin/python setup.py egg_info

Usted puede verificar el paquete previamente creado y observará como este
paquete básico ha habilitado el `Setuptools`_.

.. code-block:: console

    (venv)$ tree mipaquetepython/
      mipaquetepython/
      |-- mipaquetepython
      |   `-- __init__.py
      |-- mipaquetepython.egg-info
      |   |-- PKG-INFO
      |   |-- SOURCES.txt
      |   |-- dependency_links.txt
      |   |-- entry_points.txt
      |   |-- not-zip-safe
      |   `-- top_level.txt
      |-- setup.cfg
      `-- setup.py

Para instalar este paquete ejecute el siguiente comando:

.. code-block:: console

    (venv)$ cd mipaquetepython/mipaquetepython/
    (venv)$ vim app.py

Escriba un simple código que solicita un valor y luego lo muestra:

.. code-block:: python
    :linenos:

    var = input("Introduzca alguna frase: ")
    print("Usted introdujo: ", var)

Guarde los cambios en el archivo :file:`app.py`, luego importe su aplicación
:file:`app.py` en el archivo :file:`__init__.py` con el siguiente código fuente:

.. code-block:: python
    :linenos:

    from mipaquetepython import app

Para comprobar su instalación ejecute el siguiente comando:

.. code-block:: console

    (venv)$ python

Y realice una importación del paquete ``mipaquetepython`` ejecutando
el siguiente comando:

.. code-block:: pycon

    >>> import mipaquetepython
    Introduzca alguna frase: Esta cadena
    Usted introdujo:  Esta cadena
    >>> exit()

De esta forma tienes creado un :term:`paquete Egg` Python.


Esqueletos en diversos proyectos Python
.......................................

A continuación se muestran algunos esqueletos útiles:

- `Esqueletos de proyectos Zope/Plone`_.

- `Esqueletos de proyectos Odoo (Antiguo OpenERP)`_.

  .. note::
      `Odoo`_, es un sistema ERP y CRM programado con Python,
      de propósito general.

- **Esqueletos de proyectos Django**:

  .. note::
      `Django`_, es un Framework Web Python, de propósito general.

  - `django-project-templates`_, plantillas Paster para crear proyectos
    Django.

  - `fez.djangoskel`_, es una colección de plantillas Paster para crear
    aplicaciones Django como :term:`paquetes Egg`.

  - `django-harness`_, es una aplicación destinada a simplificar las
    tareas típicas relacionadas con la creación de un sitio web hechos
    con Django, el mantenimiento de varias instalaciones (local, producción,
    etc) y cuidando su instalación global y su estructura de "esqueleto"
    actualizado del sitio de manera fácil.

  - `lfc-skel`_, Provee una plantilla para crear una aplicación `django-lfc`_ CMS.

- **Esqueletos de proyectos Pylons**:

  .. note::
      `Pylons`_, es un Framework Web Python, de propósito general.

  - `Pylons`_, al instalarse usando la utilidad `easy_install`_
    instala dos plantillas de proyectos Pylons.

  - `PylonsTemplates`_, le ofrece plantillas adicionales ``paster`` para aplicaciones
    Pylons, incluyendo implementación de ``repoze.what``.

  - `BlastOff`_, Una plantilla de aplicación `Pylons`_ que proporciona un
    esqueleto de entorno de trabajo configurado con ``SQLAlchemy``, ``mako``,
    ``repoze.who``, ``ToscaWidgets``, ``TurboMail``, ``WebFlash`` y (opcionalmente)
    ``SchemaBot``. La aplicación generada esta previamente configurada con
    autenticación, inicio de sesión y formularios de registro, y (opcionalmente)
    confirmación de correo electrónico. ``BlastOff`` ayudar a acelerar el desarrollo
    de aplicaciones en Pylons por que genera un proyecto con una serie de dependencias
    configuraciones previamente.

- **Esqueletos de proyectos CherryPy**:

  .. note::
      `CherryPy`_, es un MicroFramework Web Python, de propósito general.

  - `CherryPaste`_, Usar CherryPy dentro Paste.

- **Esqueletos de proyectos Trac**:

  .. note::
      `Trac`_, es un sistema de gestión de proyectos de desarrollos de software.

  - `TracLegosScript`_, TracLegos es un software diseñado para ofrecer plantillas
    para proyectos Trac y asiste con la creación de proyecto trac.

  - `trac_project`_, Plantilla de proyecto Trac de software de código abierto.


Recomendaciones
...............

Si desea trabajar con algún proyecto de desarrollo basado en esqueletos o plantillas
``paster`` y Buildout simplemente seleccione cual esqueleto va a utilizar para su
desarrollo y proceso a instalarlo con `easy_install`_ o `PIP`_ (como se explico anteriormente)
y siga sus respectivas instrucciones para lograr con éxito la tarea deseada.


Referencias
...........

- `Gestión de proyectos con Buildout, instalando Zope/Plone con este mecanismo`_
  desde la comunidad de Plone Venezuela.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion8>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::

.. _`PasteScript`: https://pypi.org/project/PasteScript
.. _`paste.deploy`: https://pypi.org/project/PasteDeploy
.. _`Odoo`: https://www.odoo.com/
.. _`Django`: https://www.djangoproject.com/
.. _`django-project-templates`: https://pypi.org/project/django-project-templates
.. _`fez.djangoskel`: https://pypi.org/project/fez.djangoskel
.. _`django-harness`: https://pypi.org/project/django-harness
.. _`lfc-skel`: https://pypi.org/project/lfc-skel/
.. _`django-lfc`: https://pypi.org/project/django-lfc
.. _`ZopeSkel`: https://pypi.org/project/ZopeSkel
.. _`zopeproject`: https://pypi.org/project/zopeproject/
.. _`grokcore.startup`: https://pypi.org/project/grokcore.startup
.. _`grokproject`: https://pypi.org/project/grokproject/
.. _`Pylons`: https://pypi.org/project/Pylons/
.. _`PylonsTemplates`: https://pypi.org/project/PylonsTemplates/
.. _`BlastOff`: https://pypi.org/project/BlastOff/
.. _`CherryPy`: https://pypi.org/project/CherryPy
.. _`CherryPaste`: https://pypi.org/project/CherryPaste
.. _`Trac`: https://pypi.org/project/Trac
.. _`TracLegosScript`: https://trac-hacks.org/wiki/TracLegosScript
.. _`trac_project`: https://trac-hacks.org/browser/traclegosscript/anyrelease/example/oss
.. _`Esqueletos de proyectos Zope/Plone`: https://plone-spanish-docs.readthedocs.io/es/latest/python/skel_proyectos_plone.html
.. _`Esqueletos de proyectos Odoo (Antiguo OpenERP)`: https://plone-spanish-docs.readthedocs.io/es/latest/python/skel_proyectos_openerp.html
.. _`PIP`: https://plone-spanish-docs.readthedocs.io/es/latest/python/distribute_pip.html
.. _`Gestión de proyectos con Buildout, instalando Zope/Plone con este mecanismo`: https://coactivate.org/projects/ploneve/gestion-de-proyectos-con-buildout
.. _`entorno virtual`: https://plone-spanish-docs.readthedocs.io/es/latest/python/creacion_entornos_virtuales.html
.. _`easy_install`: https://plone-spanish-docs.readthedocs.io/es/latest/python/setuptools.html#que-es-easyinstall
.. _`Setuptools`: https://plone-spanish-docs.readthedocs.io/es/latest/python/setuptools.html
