.. -*- coding: utf-8 -*-

========================================================
Manual del curso "Programación en Python - Nivel básico"
========================================================

Repositorio de manuales y recursos del curso "Programación en Python - Nivel básico"
realizado por Covantec R.L.

.. contents :: :local:

Estructura general
===================

La estructura general de contenidos esta confirmada por los principales archivos:

**00-capacitacion_python_basico.odt**
  Describe el contenido de la capacitación.

**01-introduccion-lenguaje-python.odp**
  Describe los contenidos del módulo *1* de la capacitación.

**manual-de-curso**
  Describe los contenidos de los módulos *2, 3, 4, 5, 6, 7, 8, 9, 10* de la capacitación.
  Además de otros temas complementarios de Python.

Obtener y compilar la documentación
===================================

El almacenamiento de este material está disponible en un repositorio Git 
en Github.com "`entrenamiento.python_basico`_". Si usted tiene una
credenciales en este servidor y desea convertirse en un colaborador ejecute 
el siguiente comando: ::

  $ cd $HOME
  $ git clone https://github.com/Covantec/entrenamiento.python_basico.git

Crear entorno virtual de Python para reconstruir este proyecto: ::

  # aptitude install python-setuptools git-core
  # easy_install virtualenv
  $ cd $HOME ; mkdir $HOME/virtualenv ; cd $HOME/virtualenv
  $ virtualenv --python=/usr/bin/python sphinx
  $ source virtualenv/sphinx/bin/activate

Instale Sphinx: ::

  (sphinx)$ ~/entrenamiento.python_basico
  (sphinx)$ pip install -r requirements.txt

Materia de cursos
-----------------
  
Ahora puede generar la documentación en PDF del módulo *2, 3, 4, 5, 6, 7, 8, 9, 10*;
ejecute los siguientes comandos: ::

  (sphinx)$ cd ~/entrenamiento.python_basico/manual-de-curso/source
  (sphinx)$ make latexpdf

Una ves generado el PDF se puede abrir desde el directorio ``build/latex/entrenamientopython_basico.pdf``
con cualquiera de sus programas de visor de PDF favorito (Evince, Acrobat Reader, ...).

Estatus de Calidad
==================

.. image:: https://readthedocs.org/projects/entrenamiento-python-basico/badge/?version=latest
   :target: http://entrenamiento-python-basico.rtfd.org/
   :align: left
   :alt: entrenamiento-python-basico ReadTheDocs build status

Colabora
========

¿Tiene alguna idea?, ¿Encontró un error? Por favor, hágalo saber registrando un `ticket de soporte`_.

.. _entrenamiento.python_basico: https://github.com/Covantec/entrenamiento.python_basico
.. _ticket de soporte: https://github.com/Covantec/entrenamiento.python_basico/issues/new

