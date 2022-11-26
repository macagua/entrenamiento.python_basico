.. _python_modulo_email:

email - Correo electrónico
..........................

.. note::
    **Propósito:** es una libraría para administrar mensajes de correo electrónico.

El correo electrónico es una de las formas más antiguas de comunicación digital,
pero sigue siendo una de las más populares. La libraría estándar de Python
incluye módulos para enviar, recibir y almacenar mensajes de correo electrónico por
medio de la librería `email`_.

`smtplib`_ se comunica con un servidor de correo para entregar un mensaje. `smtpd`_ se
puede utilizar para crear un servidor de correo personalizado y proporciona clases
útiles para depurar la transmisión de correo electrónico en otras aplicaciones.

`imaplib`_ utiliza el protocolo IMAP para manipular mensajes almacenados en un servidor.
Proporciona una API de bajo nivel para clientes IMAP y puede consultar, recuperar, mover
y eliminar mensajes.

Los archivos de mensajes locales se pueden crear y modificar `mailbox`_ utilizando varios
formatos estándar, incluidos los populares formatos ``mbox`` y ``Maildir`` utilizados por
muchos programas de clientes de correo electrónico.

Envío de correo básico
^^^^^^^^^^^^^^^^^^^^^^

A continuación, un ejemplo de envió de correo electrónico, usando el servicio Gmail, usando una plantilla
de correo básica basado en una :ref:`cadena de caracteres <python_str>`:

.. literalinclude:: ../../recursos/leccion10/email_smtplib_demo1.py
    :language: python
    :linenos:
    :lines: 1-30

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    Correo enviado correctamente

Y para captura todas las excepciones posibles, muestra el siguiente mensaje:

.. code-block:: console

    Error: no se pudo enviar el correo


Envío de correo personalizado
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A continuación, un ejemplo de envió de correo electrónico, usando el servicio Gmail, acoplando variables
en una plantilla de correo básica basado en una :ref:`cadena de caracteres <python_str>`:

.. literalinclude:: ../../recursos/leccion10/email_smtplib_demo2.py
    :language: python
    :linenos:
    :lines: 1-32

El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console

    Correo enviado correctamente

Y para captura todas las excepciones posibles, muestra el siguiente mensaje:

.. code-block:: console

    Error: no se pudo enviar el correo


Envío de correo avanzado
^^^^^^^^^^^^^^^^^^^^^^^^

A continuación, un ejemplo de envió de correo electrónico, usando el servicio Gmail, usando
una objeto de tipo `Template`_ acoplando variables, usando diversas :ref:`excepciones <python_excepciones_builtins>`
para manipular los posibles errores:

.. literalinclude:: ../../recursos/leccion10/emails_gmail_send.py
    :language: python
    :linenos:
    :lines: 1-99

Archivo que incluye la lista de contactos:

.. literalinclude:: ../../recursos/leccion10/email_contactos.txt
    :language: text
    :linenos:
    :lines: 1-2

Archivo que incluye la plantilla del mensaje:

.. literalinclude:: ../../recursos/leccion10/email_mensaje.txt
    :language: text
    :linenos:
    :lines: 1-7


El anterior código al ejecutar debe mostrar el siguiente mensaje:

.. code-block:: console


    Estimado(a) Leonardo,

    Este es un mensaje de prueba.
    Espero tengas una gran semana!

    Sinceramente


    Estimado(a) Macagua,

    Este es un mensaje de prueba.
    Espero tengas una gran semana!

    Sinceramente

    Correo(s) enviado(s) correctamente

Cuando hay error de conexión al servidor SMTP, muestra el siguiente mensaje:

.. code-block:: console

    Error: Conexión al servidor de correo fallo: [Errno -2] Name or service not known

Cuando hay error de en las credenciales de acceso al correo, muestra el siguiente mensaje:

.. code-block:: console

    Error: Credenciales de acceso al correo no coinciden: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials g24-20020ab02058000000b00418c627a089sm538715ual.7 - gsmtp')

Y para captura todas las excepciones posibles, muestra el siguiente mensaje:

.. code-block:: console

    Error: no se pudo enviar el correo: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials h199-20020a1f9ed0000000b003b7d46d80b6sm569582vke.16 - gsmtp')


Además de los procesos de permisos específicos de Gmail (que incluyen aplicaciones menos seguras,
etc.), estas secuencias de comandos y ejemplos funcionarían con casi cualquier otro servicio de
correo que proporcione conectividad SMTP, siempre que tenga la dirección del servidor y el puerto
necesarios.

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion10_email>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::


.. _`email`: https://docs.python.org/es/3.7/library/email.html
.. _`smtplib`: https://docs.python.org/es/3.7/library/smtplib.html
.. _`smtpd`: https://docs.python.org/es/3.7/library/smtpd.html
.. _`imaplib`: https://docs.python.org/es/3.7/library/imaplib.html
.. _`mailbox`: https://docs.python.org/es/3.7/library/mailbox.html
.. _`Template`: https://docs.python.org/es/3.7/library/string.html#template-strings
