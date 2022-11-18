.. -*- coding: utf-8 -*-

.. _glosario:

Glosario
========

:Autor(es): Leonardo J. Caballero G.
:Correo(s): :email:`leonardoc@plone.org`
:Compatible con: Python 3.7.x
:Fecha: 16 de Noviembre de 2022

A continuación una serie de términos usados en las tecnologías Python.

.. glossary::
    :sorted:

    buildout
        En la herramienta `buildout`_, es un conjunto de partes
        que describe como ensamblar una aplicación.

    bundle
        Ver :term:`Paquete bundle`.

    Cheese shop
        Ver :term:`PyPI`.

    Egg
        Ver :term:`paquetes Egg`.

    esqueleto
        Los archivos y carpetas recreados por un usuario el cual los genero ejecutando
        alguna plantilla ``templer`` (``PasteScript``).

    estructura
        1) Una clase Python la cual controla la generación de un árbol de carpetas
        que contiene archivos.

        2) Una unidad de carpetas y archivos proveídos por el sistema ``templer`` para ser
        usado en una plantilla o plantillas. Las estructuras proporcionan recursos
        estáticos compartidos, que pueden ser utilizados por cualquier paquete en
        el sistema de ``templer``.

        Las estructuras diferencian de las plantillas en que no proporcionan las :term:`vars`.

    filesystem
        Termino ingles File system, referido al sistema de archivo del sistema operativo.

    grok
        Ver la documentacion del proyecto `grok <https://grok-community-docs.readthedocs.io/en/latest/>`_.

    local command
        Una clase `Paste`_ la cual provee funcionalidad adicional a una estructura
        de esqueleto de proyecto que ha sido generada.

    módulo
        Del Ingles ``module``, es un archivo fuente Python; un archivo en el sistema
        de archivo que típicamente finaliza con la extensión ``.py`` o ``.pyc``. Los modules
        son parte de un :term:`paquete`.

    Nombre de puntos Python
        Es la representación Python del "camino" para un determinado objeto / módulo / función,
        por ejemplo, ``Products.GenericSetup.tool.exportToolset``. A menudo se utiliza como referencia en configuraciones ``Paste`` y ``setuptools`` a cosas en Python.

    PYTHONPATH
        Una lista de nombre de directorios, que contiene librerías Python, con la misma
        sintaxis como la declarativa ``PATH`` del shell del sistema operativo.

    Python Package Index
        Ver :term:`PyPI`.

    PyPI
        Siglas del termino en Ingles :term:`Python Package Index`, es el servidor central
        de :term:`paquetes Egg` Python ubicado en la dirección https://pypi.org/.

    part
        En la herramienta :term:`buildout`, es un conjunto opciones que le permite a usted
        construir una pieza de la aplicación.

    paquete
        Ver :term:`Paquete Python`.

    paquete Egg
        Es una forma de empaquetar y distribuir paquetes Python. Cada Egg contiene
        un archivo :file:`setup.py` con metadata (como el nombre del autor y la correo
        electrónico y información sobre el licenciamiento), como las dependencias del
        paquete.

        La herramienta del `setuptools`_, es la librería Python que permite
        usar el mecanismo de paquetes egg, esta es capaz de encontrar y descargar
        automáticamente las dependencias de los paquetes Egg que se instale.

        Incluso es posible que dos paquetes Egg diferentes necesiten utilizar simultáneamente
        diferentes versiones de la misma dependencia. El formato de paquetes Eggs
        también soportan una función llamada ``entry points``, una especie de
        mecanismo genérico de plug-in. Mucha más detalle sobre este tema se encuentra
        disponible en el `sitio web de PEAK`_.

    paquetes Egg
        Plural del termino :term:`paquete Egg`.

    Paquete bundle
        Este paquete consististe en un archivo comprimido con todos los módulos que son
        necesario compilar o instalar en el :term:`PYTHONPATH` de tu interprete ``Python``.

    Paquete Python
        Es un termino generalmente usando para describir un módulo Python. en el
        más básico nivel, un paquete es un directorio que contiene un archivo
        :file:`__init__.py` y algún código Python.

    Paquetes Python
        Plural del termino :term:`Paquete Python`.

    plantilla
        1) Una clase Python la cual controla la generación de un esqueleto. Las
        plantillas contiene una lista de variables para obtener la respuesta de un
        usuario. Las plantillas son ejecutadas con el comando ``templer`` suministrando
        el nombre de la plantilla como un argumento ``templer basic_namespace my.package``.

        2) Los archivos y carpetas proveídas un paquete ``templer`` como contenido a ser
        generado. Las respuestas proporcionadas por un usuario en respuesta a las variables
        se utilizan para rellenar los marcadores de posición en este contenido.

    setup.py
        El archivo :file:`setup.py` es un módulo de Python, que por lo general indica que
        el módulo / paquete que está a punto de instalar ha sido empacado y distribuidos
        con ``Distutils``, que es el estándar para la distribución de módulos de Python.

        Con esto le permite instalar fácilmente paquetes de Python, a menudo es suficiente
        para escribir:

        .. code-block:: console

            $ python setup.py install

        Entonces el módulo Python se instalará.

        .. seealso::
            - https://docs.python.org/es/3.7/install/index.html

    var
        Diminutivo en singular del termino :term:`variable`.

    vars
        Diminutivo en plural del termino :term:`variable`.

    variable
        1) Una pregunta que debe ser respondida por el usuario cuando esta generando una
        estructura de esqueleto de proyecto usando el sistema de plantilla ``templer``. En este
        caso una variable (var) es una descripción de la información requerida, texto de
        ayuda y reglas de validación para garantizar la entrada de usuario correcta.

        2) Una declarativa cuyo valor puede ser variable o constante dentro de un programa
        Python o en el sistema operativo.

    variables
        Plural del termino :term:`variable`.

    ZCA
    Zope Component Architecture
        La `arquitectura de componentes de Zope (alias ZCA)`_, es un
        sistema que permite la aplicación y la expedición enchufabilidad complejo
        basado en objetos que implementan una interfaz.

.. _`sitio web de PEAK`: http://peak.telecommunity.com/DevCenter/setuptools
.. _`Paste`: https://paste.readthedocs.io/en/latest/
.. _`buildout`: https://plone-spanish-docs.readthedocs.io/es/latest/buildout/replicacion_proyectos_python.html
.. _`setuptools`: https://plone-spanish-docs.readthedocs.io/es/latest/python/setuptools.html
.. _`arquitectura de componentes de Zope (alias ZCA)`: https://plone-spanish-docs.readthedocs.io/es/latest/programacion/zca/zca-es.html
