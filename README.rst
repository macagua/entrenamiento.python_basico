.. -*- coding: utf-8 -*-

=====================================================
Entrenamiento "Programación en Python - Nivel básico"
=====================================================

Repositorio de manuales y recursos del entrenamiento 
"Programación en Python - Nivel básico" realizado por 
la empresa Covantec R.L.

.. contents :: :local:


Estructura general
===================

La estructura general de contenidos esta confirmada por 
los principales archivos:

**00-capacitacion_python_basico.odt**
  Describe el contenido del entrenamiento.

**01-introduccion-lenguaje-python.odp**
  Describe los contenidos del módulo *1* del entrenamiento.

**source**
  Describe los contenidos de los módulos *1, 2, 3, 4, 5, 6, 
  7, 8, 9, 10* del entrenamiento. Además de otros temas 
  complementarios de Python.


Obtener y compilar la documentación
===================================

El almacenamiento de este material está disponible en un 
repositorio Git en Github.com "`entrenamiento.python_basico`_". 

Si usted tiene una credenciales en este servidor y desea 
convertirse en un colaborador de los materiales de este 
entrenamiento, usted debe seguir los siguientes pasos:


Dependencias
------------

Para construir estos recursos, debe ejecutar las dependencias, 
entonces debe ejecutar los siguientes comando:

::

  $ sudo apt-get install python-pip python-setuptools git
  $ sudo pip install virtualenv


Descargar repositorio
---------------------

Para descargar repositorio para modificar los recursos del 
entrenamiento, ejecute los siguientes comando:

::

  $ cd $HOME
  $ git clone https://github.com/Covantec/entrenamiento.python_basico.git

Crear entorno virtual de Python para reconstruir 
este proyecto, ejecutando el siguiente comando:

::

  $ sudo apt-get install python-pip python-setuptools git
  $ sudo pip install virtualenv
  $ cd ~/entrenamiento.python_basico
  $ virtualenv --python=/usr/bin/python venv
  $ source ./venv/bin/activate

Luego instale dependencias Sphinx, ejecutando el siguiente 
comando:

::

  (venv)$ pip install -r requirements.txt


Materia del entrenamiento
-------------------------
  
Ahora puede generar la documentación en PDF del módulo *1, 
2, 3, 4, 5, 6, 7, 8, 9, 10*; ejecute los siguientes comando:

::

  (venv)$ cd ~/entrenamiento.python_basico/source
  (venv)$ make latexpdf

Una ves generado el PDF se puede abrir desde el directorio 
``build/latex/entrenamientopython_basico.pdf``
con cualquiera de sus programas de visor de PDF favorito 
(Evince, Acrobat Reader, ...).


Estatus de Calidad
==================

.. image:: https://readthedocs.org/projects/entrenamiento-python-basico/badge/?version=latest
   :target: http://entrenamiento-python-basico.rtfd.org/
   :align: left
   :alt: entrenamiento-python-basico ReadTheDocs build status


Colabora
========

¿Tiene alguna idea?, ¿Encontró un error? Por favor, hágalo saber 
registrando un `ticket de soporte`_.

.. _`entrenamiento.python_basico`: https://github.com/Covantec/entrenamiento.python_basico
.. _`ticket de soporte`: https://github.com/Covantec/entrenamiento.python_basico/issues/new
