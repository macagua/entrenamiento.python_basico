.. -*- coding: utf-8 -*-

=========================================================
Entrenamiento "Programación en Python - Nivel básico"
=========================================================

Repositorio de manuales y recursos del entrenamiento "Programación en `Python`_ - Nivel 
básico".

.. contents :: :local:


Estructura general
==================

La estructura general de contenidos esta confirmada por los principales archivos:

**00-entrenamiento_python_basico.odt**
  Describe el contenido del entrenamiento.

**01-introduccion-lenguaje-python.odp**
  Describe los contenidos del módulo *1* del entrenamiento.

**source**
  Describe los contenidos de los módulos *1, 2, 3, 4, 5, 6, 7, 8, 9, 10* del 
  entrenamiento. Además de otros temas complementarios de Python.


Obtener y compilar la documentación
===================================

El almacenamiento de este material está disponible en un repositorio Git 
"`entrenamiento.python_basico`_". 

Si usted tiene una credenciales en este servidor y desea convertirse en un colaborador 
de los materiales de este entrenamiento, usted debe seguir los siguientes pasos:


Dependencias
------------

Para construir estos recursos, debe ejecutar las dependencias, entonces debe ejecutar 
los siguientes comando:

::

  $ sudo apt install python-pip python-setuptools git
  $ sudo pip install virtualenv


Descargar repositorio
---------------------

Para descargar repositorio para modificar los recursos del entrenamiento, ejecute los 
siguientes comando:

::

  $ cd $HOME
  $ git clone https://github.com/Covantec/entrenamiento.python_basico.git

Crear entorno virtual de Python para reconstruir este proyecto, ejecutando el siguiente 
comando:

::

  $ cd $HOME/entrenamiento.python_basico
  $ virtualenv --python=/usr/bin/python2.7 venv
  (venv)$ source ./venv/bin/activate

Luego instale dependencias del paquete ``Sphinx``, ejecutando el siguiente comando:

::

  (venv)$ pip install -r requirements.txt


Recursos del entrenamiento
==========================

La herramienta Sphinx le permite generar los recursos usado en el entrenamiento, en diversos 
formatos, actualmente se tiene bien soportado los siguientes:


Formato HTML
------------

Usted puede generar la documentación en HTML del módulo *1, 2, 3, 4, 5, 6, 7, 8, 9, 10*; ejecute 
los siguientes comando:

::

  (venv)$ make html

Una vez generado el formato HTML se puede abrir desde el directorio ``build/html/index.html``
con su navegador Web favorito (Mozilla Firefox, Google Chrome, etc).


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


Licencia
========

Esta obra está licenciada bajo la licencia Creative Commons Atribución-CompartirIgual 
3.0 Venezuela. Para ver una copia de esta licencia, visite 
https://creativecommons.org/licenses/by-sa/3.0/ve/ o envíe una carta a Creative Commons, 
444 Castro Street, Suite 900, Mountain View, California, 94041, EE.UU.

Una copia de esta licencia en formato de texto se incluye en este paquete dentro del 
directorio ``docs`` tanto en el idioma Ingles (LICENSE.rst) como el idioma Español 
(LICENSE.es.rst).

.. _`Covantec R.L`: https://github.com/Covantec
.. _`Python 2.7`: https://docs.python.org/
.. _`entrenamiento.python_basico`: https://github.com/Covantec/entrenamiento.python_basico
.. _`ticket de soporte`: https://github.com/Covantec/entrenamiento.python_basico/issues/new
