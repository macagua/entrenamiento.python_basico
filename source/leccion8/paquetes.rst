.. -*- coding: utf-8 -*-


.. _python_pkgs:

Paquetes Python
---------------

Los paquetes pueden contener módulos y otros paquetes. Son directorios.
El único requisito es que contengan un archivo llamado ``__init__.py``.
Este archivo puede estar vacío.


.. _python_sent_from:

Sentencia from
..............

La sentencia ``from`` se utiliza en conjunto a la previa sentencia
:ref:`import <python_sent_import>` para importar un módulo.

.. code-block:: pycon

    >>> from utilidades import suma_total

Por ejemplo, cree un directorio llamado ``tostadas_pipo``, que contiene
los archivos llamados ``__init__.py``, ``principal.py`` (dentro del mismo
directorio).

- Archivo ``__init__.py``, este archivo no tiene ningún contenido.

- Archivo ``principal.py`` incluye el siguiente código:

.. literalinclude:: ../../recursos/leccion8/paquetes/tostadas_pipo/principal.py
    :language: python
    :lines: 1-10

Seguidamente dentro del directorio ``tostadas_pipo``, cree otro directorio
llamado ``utilidades``, dentro de este, cree los siguientes archivos:

- Archivo ``__init__.py``, este archivo no tiene ningún contenido.

- Archivo ``calculos.py`` incluye el siguiente código:

.. literalinclude:: ../../recursos/leccion8/paquetes/tostadas_pipo/utilidades/calculos.py
    :language: python
    :lines: 1-8

- Archivo ``impuestos.py`` incluye el siguiente código:

.. literalinclude:: ../../recursos/leccion8/paquetes/tostadas_pipo/utilidades/impuestos.py
    :language: python
    :lines: 1-7


Al final tendrá la siguiente estructura del directorios del paquete Python llamado
``tostadas_pipo``, como se describe a continuación:

.. code-block:: console

    tostadas_pipo/
    ├── __init__.py
    ├── principal.py
    └── utilidades/
        ├── calculos.py
        ├── impuestos.py
        └── __init__.py

Entonces realizar importaciones desde una estructura de directorios mas completa
se realiza de las siguientes formas:

- Importar todos los módulo el sub-paquete ``utilidades``, ejecutando:

.. code-block:: python

    import tostadas_pipo.utilidades
    from tostadas_pipo import utilidades
    from tostadas_pipo.utilidades import *


- Importar el módulo ``calculos.py`` desde el sub-paquete ``utilidades``,
  ejecutando:

.. code-block:: python

    from tostadas_pipo.utilidades import calculos


- Importar la función ``impuesto_iva()`` desde el módulo ``impuestos.py`` en el
  sub-paquete ``utilidades``, ejecutando:

.. code-block:: python

    from tostadas_pipo.utilidades.impuestos import impuesto_iva

Por ejemplo, cree un módulo llamado ``calculo_factura_pipo.py``, que
contiene las importaciones del paquete  ``tostadas_pipo``:

- Archivo ``calculo_factura_pipo.py`` incluye el siguiente código:

.. literalinclude:: ../../recursos/leccion8/paquetes/calculo_factura_pipo.py
    :language: python
    :lines: 1-9

----

.. important::
    Usted puede descargar el código usado en esta sección, haciendo clic en el
    siguiente enlace: :download:`paquetes.zip <../../recursos/leccion8/paquetes.zip>`.


.. tip::
    Para ejecutar el código incluido en el archivo :file:`paquetes.zip` debe
    descomprimirlo, abra una consola de comando, acceda al directorio donde
    se encuentra el archivo descomprimido, de la siguiente forma:

    ::

        calculo_factura_pipo.py
        tostadas_pipo/
        ├── __init__.py
        ├── principal.py
        └── utilidades/
            ├── calculos.py
            ├── impuestos.py
            └── __init__.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python calculo_factura_pipo.py
        $ python tostadas_pipo/principal.py


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion8>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
