.. -*- coding: utf-8 -*-


.. _python_decoradores:

Decoradores
-----------

Un decorador es una función Python permite que agregar funcionalidad a otra función,
pero sin modificarla. También, esto es llamado meta-programación, por que parte del
programa trata de modificar a otro al momento de compilar.

Los decoradores son una funcionalidad relativamente importante en Python son definidos
en el PEP-318. https://peps.python.org/pep-0318/

Se podría decir que son funciones que modifican la funcionalidad de otras funciones,
y ayudan a hacer el código más corto y Pytónico. A continuación vera lo que son, cómo
se crean y cómo se puede usar.

Para llamar un decorador se utiliza el signo de arroba (@).

Todo es un objeto en Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Antes de entrar en materia con los decoradores, va a entender bien las funciones.

.. code-block:: pycon

    >>> def hola(nombre="Plone"):
    ...     return f"Hola {nombre}"
    ...
    >>> print(hola())
    Hola Plone
    >>> # Puede asignar una función a una variable
    ... saluda = hola
    >>> # No usa () porque no la esta llamando, sino que la esta
    ... # asignado a una variable.
    >>> print(saluda())
    Hola Plone
    >>> # También puede eliminar la función asignada a la variable
    ... # con el hola.
    >>> print(hola())
    Hola Plone
    >>> print(saluda())
    Hola Plone
    >>>


Definir funciones dentro de funciones
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Avance un paso más allá. En Python puede definir funciones dentro de otras funciones.
Vea el siguiente ejemplo:

.. code-block:: pycon

    >>> def hola(nombre="Plone"):
    ...     print("Estás dentro de la función hola()")
    ...     def saluda():
    ...         return "Estás dentro de la función saluda()"
    ...     def bienvenida():
    ...         return "Estás dentro de la función bienvenida()"
    ...     print(saluda())
    ...     print(bienvenida())
    ...     print("De vuelta a la función hola()")
    ...
    >>> hola()
    Estás dentro de la función hola()
    Estás dentro de la función saluda()
    Estás dentro de la función bienvenida()
    De vuelta a la función hola()
    >>> # Esto muestra como cada vez que llamas a la función hola()
    ... # se llama en realidad también a saluda() y bienvenida()
    ... # Sin embargo estas dos últimas funciones no están accesibles
    ... # fuera de hola(). Si lo intenta, tendrá un error.
    >>> saluda()
    'Hola Plone'
    >>>


Entonces pudo ver como puede definir funciones dentro de otras funciones. En otras
palabras, puede crear funciones anidadas. Pero para entender bien los decoradores, es
necesario ir un paso más allá. Las funciones también pueden devolver otras funciones.

Devolviendo funciones desde funciones
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No es necesario ejecutar una función dentro de otra. Simplemente puede devolverla como salida:

.. code-block:: pycon

    >>> def hola(nombre="Plone"):
    ...     def saluda():
    ...         return "Estás dentro de la función saluda()"
    ...     def bienvenida():
    ...         return "Estás dentro de la función bienvenida()"
    ...     if nombre == "Plone":
    ...         return saluda
    ...     else:
    ...         return bienvenida
    ...
    >>> hey = hola()
    >>> print(hey)
    <function hola.<locals>.saluda at 0x7f7b83214268>
    >>> # Es decir, la variable 'hey' ahora apunta a la función
    ... # saluda() declarada dentro de hola(). Por lo tanto puede llamarla.
    ... print(hey())
    Estás dentro de la función saluda()
    >>>

Echa un vistazo otra vez al código. Si te fijas en el ``if/else``, esta devolviendo
``saluda`` y ``bienvenida`` y no ``saluda()`` y ``bienvenida()``. ¿A qué se debe esto?
Se debe a que cuando usas paréntesis ``()`` la función se ejecuta. Por lo contrario, si
no los usas la función es pasada y puede ser asignada a una variable sin ser ejecutada.

Va a analizar el código paso por paso. Al principio usa ``hey = hola()``, por lo que el
parámetro para ``nombre`` que se toma es "Plone" ya que es el que se ha asignado por
defecto. Esto hará que en el ``if`` se entre en ``nombre == "Plone"``, lo que hará que
se devuelva la función saluda. Si por lo contrario hace la llamada a la función con
``hey = hola(nombre="Pelayo")``, la función devuelta será ``bienvenida``.

Usando funciones como argumento de otras
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Por último, puede hacer que una función tenga a otra como entrada y que además la
ejecute dentro de sí misma. En el siguiente ejemplo puede ver como
``haz_esto_antes_del_hola()`` es una función que de alguna forma encapsula a la función
que se le pase como parámetro, añadiendo una determinada funcionalidad. En este ejemplo
simplemente imprime algo por pantalla antes de llamar a la función.

.. code-block:: pycon

    >>> def hola():
    ...     return "¡Hola!"
    ...
    >>> def haz_esto_antes_del_hola(function):
    ...     print("Hacer algo antes de llamar a function")
    ...     print(function())
    ...
    >>> haz_esto_antes_del_hola(hola)
    Hacer algo antes de llamar a function
    ¡Hola!
    >>>


Ahora ya tienes todas las piezas del rompecabezas. Los decoradores son funciones que
decoran a otras funciones, pudiendo ejecutar código antes y después de la función que
está siendo decorada.

Tu primer decorador
^^^^^^^^^^^^^^^^^^^

Realmente en el ejemplo anterior ya vio como crear un decorador. Va a modificarlo y
hacerlo un poco realista.

.. code-block:: pycon

    >>> def nuevo_decorador(function):
    ...     def envuelve_la_funcion():
    ...         print("Haciendo algo antes de llamar a function()")
    ...         function()
    ...         print("Haciendo algo después de llamar a function()")
    ...     return envuelve_la_funcion
    ...
    >>> def funcion_a_decorar():
    ...     print("Soy la función que necesita ser decorada")
    ...
    >>> funcion_a_decorar()
    Soy la función que necesita ser decorada
    >>> funcion_a_decorar = nuevo_decorador(funcion_a_decorar)
    >>> # Ahora funcion_a_decorar está envuelta con el decorador que ha creado
    ... funcion_a_decorar()
    Haciendo algo antes de llamar a function()
    Soy la función que necesita ser decorada
    Haciendo algo después de llamar a function()
    >>>


Simplemente ha aplicado todo lo aprendido en los apartados anteriores. Así es
exactamente como funcionan los decoradores en Python. Envuelven una función para
modificar su comportamiento de una manera determinada.

Tal vez te preguntes ahora porqué no ha usado ``@`` en el código. Esto es debido
a que ``@`` es simplemente una forma de hacerlo más corto, pero ambas opciones son
perfectamente válidas.

.. code-block:: pycon

    >>> @nuevo_decorador
    ... def funcion_a_decorar():
    ...     print("Soy la función que necesita ser decorada")
    ...
    >>> funcion_a_decorar()
    Haciendo algo antes de llamar a function()
    Soy la función que necesita ser decorada
    Haciendo algo después de llamar a function()
    >>> # El uso de @nuevo_decorador es simplemente una forma acortada
    ... # de hacer lo siguiente.
    >>> funcion_a_decorar = nuevo_decorador(funcion_a_decorar)
    >>> funcion_a_decorar
    <function nuevo_decorador.<locals>.envuelve_la_funcion at 0x7f7b83214598>
    >>>


Una vez visto esto, hay un pequeño problema con el código. Si ejecuta lo siguiente:

.. code-block:: pycon

    >>> print(funcion_a_decorar.__name__)
    envuelve_la_funcion
    >>>


Se encontró con un comportamiento un tanto inesperado. La función es
``funcion_a_decorar`` pero al haberla envuelto con el decorador es en realidad
``envuelve_la_funcion``, por lo que sobrescribe el nombre y el *docstring* de la misma,
algo que no es muy conveniente.

Por suerte, Python nos da una forma de arreglar este problema usando ``functools.wraps``.
Va a modificar el ejemplo anterior haciendo uso de esta herramienta.

.. code:: pycon

    >>> from functools import wraps
    >>> def nuevo_decorador(function):
    ...     @wraps(function)
    ...     def envuelve_la_funcion():
    ...         print("Haciendo algo antes de llamar a function()")
    ...         function()
    ...         print("Haciendo algo después de llamar a function()")
    ...     return envuelve_la_funcion
    ...
    >>> @nuevo_decorador
    ... def funcion_a_decorar():
    ...     print("Soy la función que necesita ser decorada")
    ...
    >>> print(funcion_a_decorar.__name__)
    funcion_a_decorar
    >>>


Mucho mejor ahora. Vea también unos fragmentos de código muy usados.

**Ejemplos:**

.. code:: pycon

    >>> from functools import wraps
    >>> def nombre_decorador(f):
    ...     @wraps(f)
    ...     def decorada(*args, **kwargs):
    ...         if not can_run:
    ...             return "La función no se ejecutará"
    ...         return f(*args, **kwargs)
    ...     return decorada
    ...
    >>> @nombre_decorador
    ... def function():
    ...     return "La función se esta ejecutando"
    ...
    >>> can_run = True
    >>> print(function())
    La función se esta ejecutando
    >>> can_run = False
    >>> print(function())
    La función no se ejecutará
    >>>


.. note::
    ``@wraps`` toma una función para ser decorada y añade la funcionalidad de copiar
    el nombre de la función, el *docstring*, los argumentos y otros parámetros
    asociados. Esto nos permite acceder a los elementos de la función a decorar una
    vez decorada. Es decir, resuelve el problema que vio con anterioridad.


Casos de uso
~~~~~~~~~~~~

A continuación vera algunos áreas en las que los decoradores son realmente útiles.


Autorización
~~~~~~~~~~~~

Los decoradores permiten verificar si alguien está o no autorizado a usar una
determinada función, por ejemplo en una aplicación web. Son muy usados en *frameworks*
como `Flask`_ o `Django`_. Aquí se muestra como usar un decorador para verificar
que se está autenticado.

**Ejemplo:**

.. code:: pycon

    >>> from functools import wraps
    >>> def requires_auth(f):
    ...     @wraps(f)
    ...     def decorated(*args, **kwargs):
    ...         auth = request.authorization
    ...         if not auth or not check_auth(auth.username, auth.password):
    ...             authenticate()
    ...         return f(*args, **kwargs)
    ...     return decorated
    ...
    >>>


Iniciar sesión
~~~~~~~~~~~~~~

El inicio de sesión es otra de las áreas donde los decoradores son muy útiles. Vea el
siguiente ejemplo:

.. code:: pycon

    >>> from functools import wraps
    >>> def log_it(function):
    ...     @wraps(function)
    ...     def with_logging(*args, **kwargs):
    ...         print(function.__name__ + " fue llamada")
    ...         return function(*args, **kwargs)
    ...     return with_logging
    ...
    >>> @log_it
    ... def funcion_suma(x):
    ...     """Función suma"""
    ...     return x + x
    ...
    >>> result = funcion_suma(4)
    funcion_suma fue llamada
    >>>


Decoradores con argumentos
^^^^^^^^^^^^^^^^^^^^^^^^^^

Ha visto ya el uso del decorador ``@wraps``, y tal vez te preguntes ¿pero no es
también un decorador? De hecho si te fijas acepta un parámetro (que en nuestro
caso es una función). A continuación se le explica como crear un decorador que
también acepta parámetros de entrada.


Anidando un Decorador dentro de una Función
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vaya de vuelta al ejemplo de inicio de sesión, y cree un *wraper* que permita
especificar el archivo de salida que quiere usar para el archivo de *log*. Si
se fijas, el decorador ahora acepta un parámetro de entrada.

.. code:: pycon

    >>> from functools import wraps
    >>> def log_it(logfile="out.log"):
    ...     def logging_decorator(function):
    ...         @wraps(function)
    ...         def wrapped_function(*args, **kwargs):
    ...             log_string = function.__name__ + " fue llamada"
    ...             print(log_string)
    ...             # Abre el archivo y añade su contenido
    ...             with open(logfile, "a") as opened_file:
    ...                 # Escribe en el archivo el contenido
    ...                 opened_file.write(log_string + "\n")
    ...             return function(*args, **kwargs)
    ...         return wrapped_function
    ...     return logging_decorator
    ...
    >>> @log_it()
    ... def my_function_1():
    ...     pass
    ...
    >>> my_function_1()
    my_function_1 fue llamada
    >>> # Se ha creado un archivo con el nombre por defecto (out.log)
    >>> @log_it(logfile="function2.log")
    ... def my_function_2():
    ...     pass
    ...
    >>> my_function_2()
    my_function_2 fue llamada
    >>> # Se crea un archivo function2.log
    >>>


Clases Decoradoras
~~~~~~~~~~~~~~~~~~

Al llegar a este punto ya tiene el decorador ``log_it`` creado en el apartado anterior
funcionando en producción, pero algunas partes de la aplicación son críticas, y si
se produce un fallo este necesitará atención inmediata. En el caso supuesto que en
determinadas ocasiones quieres simplemente escribir en el *log* (como se hecho),
pero en otras quieres que se envíe un correo. En una aplicación como esta podría
usar la herencia, pero hasta ahora sólo ha usado decoradores.

Por suerte, las clases también pueden ser usadas para crear decoradores. Vuelva
definir ``log_it``, pero en este caso como una clase en vez de con una función.

.. code:: pycon

    >>> class log_it(object):
    ...     _logfile = "out.log"
    ...     def __init__(self, function):
    ...         self.function = function
    ...     def __call__(self, *args):
    ...         log_string = self.function.__name__ + " fue llamada"
    ...         print(log_string)
    ...         # Abre el archivo de log y escribe
    ...         with open(self._logfile, "a") as opened_file:
    ...             # Escribe el contenido
    ...             opened_file.write(log_string + "\n")
    ...         # Envía una notificación (ver método)
    ...         self.notify()
    ...         # Devuelve la función base
    ...         return self.function(*args)
    ...     def notify(self):
    ...         # Esta clase simplemente escribe el log, nada más.
    ...         pass
    ...
    >>>


Esta implementación es mucho más limpia que con la función anidada. Por otro lado,
la función puede ser envuelta de la misma forma que viene usando hasta ahora, usando
``@``.

.. code:: pycon

    >>> log_it._logfile = "out2.log"  # Si quiere usar otro nombre
    >>> @log_it
    ... def my_function_1():
    ...     pass
    ...
    >>> my_function_1()
    my_function_1 fue llamada
    >>>


Ahora, va a crear una subclase de *log_it* para añadir la funcionalidad de enviar un
correo electrónico. Envié el correo electrónico de manera ficticia.

.. code:: pycon

    >>> class email_log_it(log_it):
    ...     """
    ...     Implementación de log_it con envío de correo electrónico
    ...     """
    ...     def __init__(self, email="admin@myproject.com", *args, **kwargs):
    ...         self.email = email
    ...         super(email_log_it, self).__init__(*args, **kwargs)
    ...     def notify(self):
    ...         # Envía un correo electrónico a self.email
    ...         # Código para enviar correo electrónico
    ...         # ...
    ...         pass
    ...
    >>>


Una vez creada la nueva clase que hereda de ``log_it``, si usa ``@email_log_it``
como decorador tendrá el mismo comportamiento, pero además enviará un correo electrónico.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::

.. _`Flask`: https://entrenamiento-frameworks-web-python.readthedocs.io/es/latest/leccion6/index.html
.. _`Django`: https://entrenamiento-frameworks-web-python.readthedocs.io/es/latest/leccion7/index.html
