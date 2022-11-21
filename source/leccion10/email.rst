.. _python_modulo_email:

email - Correo electrónico
..........................

.. note::
    **Propósito:** es una biblioteca para administrar mensajes de correo electrónico.

El correo electrónico es una de las formas más antiguas de comunicación digital,
pero sigue siendo una de las más populares. La biblioteca estándar de Python
incluye módulos para enviar, recibir y almacenar mensajes de correo electrónico.

``smtplib`` se comunica con un servidor de correo para entregar un mensaje. ``smtpd`` se
puede utilizar para crear un servidor de correo personalizado y proporciona clases
útiles para depurar la transmisión de correo electrónico en otras aplicaciones.

``imaplib`` utiliza el protocolo IMAP para manipular mensajes almacenados en un servidor.
Proporciona una API de bajo nivel para clientes IMAP y puede consultar, recuperar, mover
y eliminar mensajes.

Los archivos de mensajes locales se pueden crear y modificar ``mailbox`` utilizando varios
formatos estándar, incluidos los populares formatos ``mbox`` y ``Maildir`` utilizados por
muchos programas de clientes de correo electrónico.


.. todo::
    TODO Terminar de escribir esta sección.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion10_email>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. _`email`: https://docs.python.org/es/3.7/library/email.html
