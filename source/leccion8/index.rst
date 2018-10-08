.. -*- coding: utf-8 -*-

.. _skel_python:

Scaffolding en proyectos Python
===============================

.. sidebar:: Sobre este artículo

    :Autor(es): Leonardo J. Caballero G.
    :Correo(s): leonardocaballero@gmail.com
    :Compatible con: Python 2.4 o versiones superiores
    :Fecha: 03 de Octubre de 2014

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
-----------

Dentro de su `entorno virtual`_ activado debe 
instalar el paquete `PasteScript`_, ejecutando el siguiente comando: 

.. code-block:: sh

  (python)$ pip install PasteScript

.. note::

  No olvidar que estos paquetes han sido instalados con el entorno virtual que
  previamente usted activo, eso quiere decir que los paquetes previamente
  instalados con `easy_install`_ están instalados en el 
  directorio :file:`~/virtualenv/python/lib/python2.x/site-packages/` en ves del 
  directorio de su versión de Python de sistema :file:`/usr/lib/python2.x/site-packages/`

Al finalizar la instalación podrá opcionalmente consultar cuales plantillas
tiene disponible para usa, ejecutando el siguiente comando: 

.. code-block:: sh

  (python)$ paster create --list-templates
    Available templates:
      basic_package:       A basic setuptools-enabled package
      paste_deploy:        A web application deployed through paste.deploy

Usted puede usar el comando :command:`paster` para crear paquetes Python.

.. code-block:: sh

  (python)$ paster create -t basic_package mipaquetepython

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
    Enter url (URL of homepage) ['']: http://github.com/pyve/mipaquetepython
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
    Running /home/macagua/virtualenv/python/bin/python setup.py egg_info

Usted puede verificar el paquete previamente creado y observará como este
paquete básico ha habilitado el `Setuptools`_. 

.. code-block:: sh

  (python)$ tree mipaquetepython/
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

.. code-block:: sh

  (python)$ cd mipaquetepython/mipaquetepython/
  (python)$ vim app.py

Escriba un simple código que solicita un valor y luego lo muestra: 

.. code-block:: python

  var = raw_input("Introduzca alguna frase: ")
  print "Usted introdujo: ", var

Guarde los cambios en el archivo :file:`app.py`, luego importe su aplicación 
:file:`app.py` en el archivo :file:`__init__.py` con el siguiente código fuente: 

.. code-block:: python

  from mipaquetepython import app

Para comprobar su instalación ejecute el siguiente comando:

.. code-block:: sh

  (python)$ python

Y realice una importación del paquete ``mipaquetepython`` ejecutando 
el siguiente comando: 

.. code-block:: python

  >>> import mipaquetepython
  Introduzca alguna frase: Esta cadena
  Usted introdujo:  Esta cadena
  >>> exit()

De esta forma tienes creado un :term:`paquete Egg` Python.

Esqueletos en diversos proyectos Python
---------------------------------------

A continuación se muestran algunos esqueletos útiles:

- `Esqueletos de proyectos Zope/Plone`_.

- `Esqueletos de proyectos OpenERP`_.

  .. note::
      `OpenERP`_, es un sistema ERP y CRM programado con Python,
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
---------------

Si desea trabajar con algún proyecto de desarrollo basado en esqueletos o plantillas
``paster`` y Buildout simplemente seleccione cual esqueleto va a utilizar para su
desarrollo y proceso a instalarlo con `easy_install`_ o `PIP`_ (como se explico anteriormente) y siga sus respectivas instrucciones para lograr con éxito la tarea deseada.

Descarga código fuente
----------------------

Para descargar el código fuente de este ejemplo ejecute el siguiente 
comando:

.. code-block:: sh

  $ svn co https://svn.plone.org/svn/collective/spanishdocs/tags/0.1rc/src/mini-tutoriales/mipaquetepython/ mipaquetepython

Referencias
-----------

- `Gestión de proyectos con Buildout, instalando Zope/Plone con este mecanismo`_ 
  desde la comunidad de Plone Venezuela.

.. _PasteScript: http://pypi.python.org/pypi/PasteScript
.. _paste.deploy: http://pypi.python.org/pypi/PasteDeploy
.. _OpenERP: https://www.openerp.com/
.. _Django: https://www.djangoproject.com/
.. _django-project-templates: http://pypi.python.org/pypi/django-project-templates
.. _fez.djangoskel: http://pypi.python.org/pypi/fez.djangoskel
.. _django-harness: http://pypi.python.org/pypi/django-harness
.. _lfc-skel: http://pypi.python.org/pypi/lfc-skel/
.. _django-lfc: http://pypi.python.org/pypi/django-lfc
.. _ZopeSkel: http://pypi.python.org/pypi/ZopeSkel
.. _zopeproject: http://pypi.python.org/pypi/zopeproject/
.. _grokcore.startup: http://pypi.python.org/pypi/grokcore.startup
.. _grokproject: http://pypi.python.org/pypi/grokproject/
.. _Pylons: http://pypi.python.org/pypi/Pylons/
.. _PylonsTemplates: http://pypi.python.org/pypi/PylonsTemplates/
.. _BlastOff: http://pypi.python.org/pypi/BlastOff/
.. _CherryPy: http://pypi.python.org/pypi/CherryPy
.. _CherryPaste: http://pypi.python.org/pypi/CherryPaste
.. _Trac: http://pypi.python.org/pypi/Trac
.. _TracLegosScript: http://trac-hacks.org/wiki/TracLegosScript
.. _trac_project: http://trac-hacks.org/browser/traclegosscript/anyrelease/example/oss
.. _Esqueletos de proyectos Zope/Plone: https://plone-spanish-docs.readthedocs.org/es/latest/python/skel_proyectos_plone.html
.. _Esqueletos de proyectos OpenERP: https://plone-spanish-docs.readthedocs.org/es/latest/python/skel_proyectos_openerp.html
.. _PIP: https://plone-spanish-docs.readthedocs.org/es/latest/python/distribute_pip.html
.. _Gestión de proyectos con Buildout, instalando Zope/Plone con este mecanismo: http://coactivate.org/projects/ploneve/gestion-de-proyectos-con-buildout
.. _entorno virtual: https://plone-spanish-docs.readthedocs.-org/es/latest/python/creacion_entornos_virtuales.html
.. _easy_install: https://plone-spanish-docs.readthedocs.org/es/latest/python/setuptools.html#que-es-easyinstall
.. _Setuptools: https://plone-spanish-docs.readthedocs.org/es/latest/python/setuptools.html
