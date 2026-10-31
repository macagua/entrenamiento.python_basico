.. _python_entornos_virtuales:

Entornos virtuales Python
=========================

Las aplicaciones en Python usualmente hacen uso de paquetes y módulos que no forman
parte de la librería estándar. Las aplicaciones a veces necesitan una versión específica
de una librería, debido a que dicha aplicación requiere que un bug particular haya sido
solucionado o bien la aplicación ha sido escrita usando una versión obsoleta de la
interface de la librería.

Esto significa que tal vez no sea posible para una instalación de Python cumplir los
requerimientos de todas las aplicaciones. Si la aplicación ``A`` necesita la versión ``1.0``
de un módulo particular y la aplicación ``B`` necesita la versión ``2.0``, entonces los
requerimientos entran en conflicto e instalar la versión ``1.0`` o ``2.0`` dejará una de las
aplicaciones sin funcionar.

La solución a este problema consiste en crear un entorno virtual (a menudo abreviado como
``virtualenv``), un árbol de directorios autónomo que contiene una instalación de Python
para una versión concreta de este lenguaje, además de una serie de paquetes adicionales.

venv vs virtualenv
------------------

Son herramientas casi totalmente intercambiables; la diferencia radica en que
:ref:`virtualenv <python_modulo_virtualenv>` es compatible con versiones anteriores de Python
y cuenta con algunas características únicas menores,  mientras que :ref:`venv <python_modulo_venv>`
forma parte de la biblioteca estándar.

A continuación, se describe cada una de estas, como parte del temario de esta lección:

.. toctree::
   :maxdepth: 2

   venv
   virtualenv


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion2>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../../_templates/partials/soporte_profesional.html


..
  .. disqus::
