.. -*- coding: utf-8 -*-


.. _python_errores:

Errores y excepciones
---------------------

Hasta ahora los mensajes de error no habían sido más que mencionados, pero si probaste
los ejemplos probablemente hayas visto algunos. Hay (al menos) dos tipos diferentes
de errores: *errores de sintaxis* y *excepciones*.


Errores de sintaxis
...................

Los errores de sintaxis, también conocidos como errores de interpretación, son quizás
el tipo de queja más común que tenés cuando todavía estás aprendiendo Python:

::

    >>> while True print('Hola Mundo')
    Traceback (most recent call last):
    ...
        while True print('Hola Mundo')
                      ^
    SyntaxError: invalid syntax

El intérprete repite la línea culpable y muestra una pequeña 'flecha' que apunta al
primer lugar donde se detectó el error. Este es causado por (o al menos detectado en)
el símbolo que *precede* a la flecha: en el ejemplo, el error se detecta en la
sentencia ``print``, ya que faltan dos puntos (``':'``) antes del mismo. Se muestran
el nombre del archivo y el número de línea para que sepas dónde mirar en caso de que
la entrada venga de un programa.


Excepciones
...........

Incluso si la sentencia o expresión es sintácticamente correcta, puede generar un
error cuando se intenta ejecutarla. Los errores detectados durante la ejecución se
llaman *excepciones*, y no son incondicionalmente fatales: pronto aprenderás cómo
manejarlos en los programas en Python. Sin embargo, la mayoría de las excepciones
no son manejadas por los programas, y resultan en mensajes de error como los
mostrados aquí:

.. code-block:: pycon

    >>> 10 * (1 / 0)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ZeroDivisionError: integer division or modulo by zero
    >>> 4 + spam * 3
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    NameError: name 'spam' is not defined
    >>> "2" + 2
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    TypeError: cannot concatenate 'str' and 'int' objects


La última línea de los mensajes de error indica qué sucedió. Las excepciones vienen
de distintos tipos, y el tipo se imprime como parte del mensaje: los tipos en el
ejemplo son:
:ref:`ZeroDivisionError <python_exception_zerodivisionerror>`,
:ref:`NameError <python_exception_nameerror>` y
:ref:`TypeError <python_exception_typeerror>`.

La cadena mostrada como tipo de la excepción es el nombre de la excepción predefinida
que ocurrió. Esto es verdad para todas las excepciones predefinidas del intérprete,
pero no necesita ser verdad para excepciones definidas por el usuario (aunque es una
convención útil). Los nombres de las excepciones estándar son identificadores
incorporados al intérprete (no son palabras clave reservadas).

El resto de la línea provee un detalle basado en el tipo de la excepción y qué la causó.

La parte anterior del mensaje de error muestra el contexto donde la excepción sucedió,
en la forma de un *trazado del error* listando líneas fuente; sin embargo, no mostrará
líneas leídas desde la entrada estándar.

:ref:`python_excepciones_builtins`, es una lista las excepciones predefinidas y sus
significados.


.. _python_sent_try_except:

Manejando excepciones
.....................

Es posible escribir programas que manejen determinadas excepciones. Mirá el siguiente
ejemplo, que le pide al usuario una entrada hasta que ingrese un entero válido, pero
permite al usuario interrumpir el programa (usando :kbd:`Control-C` o lo que sea que
el sistema operativo soporte); notá que una interrupción generada por el usuario se
señaliza generando la excepción :ref:`KeyboardInterrupt <python_exception_keyboardinterrupterror>`.

.. code-block:: pycon

    >>> while True:
    ...     try:
    ...         x = int(input("Por favor ingrese un número: "))
    ...         break
    ...     except ValueError:
    ...         print("Oops!  No era válido. Intente nuevamente...")
    ...

La sentencia ``try`` funciona de la siguiente manera:

* Primero, se ejecuta el *bloque try* (el código entre las sentencias
  ``try`` y ``except``).

* Si no ocurre ninguna excepción, el *bloque except* se saltea y
  termina la ejecución de la sentencia ``try``.

* Si ocurre una excepción durante la ejecución del *bloque try*,
  el resto del bloque se saltea. Luego, si su tipo coincide con
  la excepción nombrada luego de la palabra reservada ``except``,
  se ejecuta el *bloque except*, y la ejecución continúa luego de la
  sentencia ``try``.

* Si ocurre una excepción que no coincide con la excepción nombrada
  en el ``except``, esta se pasa a declaraciones ``try``
  de más afuera; si no se encuentra nada que la maneje, es una
  *excepción no manejada*, y la ejecución se frena con un mensaje como
  los mostrados arriba.

Una sentencia ``try`` puede tener más de un ``except``, para especificar
manejadores para distintas excepciones. A lo sumo un manejador será
ejecutado. Sólo se manejan excepciones que ocurren en el correspondiente
``try``, no en otros manejadores del mismo ``try``. Un ``except`` puede
nombrar múltiples excepciones usando paréntesis, por ejemplo:

::

    ... except (RuntimeError, TypeError, NameError):
    ...     pass


El último ``except`` puede omitir nombrar qué excepción captura, para servir
como comodín. Usá esto con extremo cuidado, ya que de esta manera es fácil
ocultar un error real de programación. También puede usarse para mostrar un
mensaje de error y luego re-generar la excepción (permitiéndole al que llama,
manejar también la excepción):

.. code-block:: python

    import sys

    try:
        f = open("numeros.txt")
        s = f.readline()
        i = int(s.strip())
    except IOError as err:
        print("Error E/S ({0}): {1}".format(err.errno, err.strerror))
    except ValueError:
        print("No pude convertir el dato a un entero.")
    except:
        print("Error inesperado:", sys.exc_info()[0])
        raise


Las declaraciones ``try`` ... ``except`` tienen un *bloque else* opcional, el cual,
cuando está presente, debe seguir a los ``except``. Es útil para aquel código que
debe ejecutarse si el *bloque try* no genera una excepción. Por ejemplo:

.. code-block:: python

    for arg in sys.argv[1:]:
        try:
            f = open(arg, "r")
        except IOError:
            print("no pude abrir", arg)
        else:
            print(arg, "tiene", len(f.readlines()), "lineas")
            f.close()

El uso de ``else`` es mejor que agregar código adicional en el ``try`` porque evita
capturar accidentalmente una excepción que no fue generada por el código que está
protegido por la sentencia ``try`` ... ``except``.

Cuando ocurre una excepción, puede tener un valor asociado, también conocido como el
*argumento* de la excepción. La presencia y el tipo de argumento depende del tipo de
excepción.

El ``except`` puede especificar una variable luego del nombre (o tupla) de excepción(es).
La variable se vincula a una instancia de excepción con los argumentos almacenados en
``instance.args``. Por conveniencia, la instancia de excepción define :meth:`__str__`
para que se pueda mostrar los argumentos directamente, sin necesidad de hacer referencia
a ``.args``.

Uno también puede instanciar una excepción antes de generarla, y agregarle cualquier
atributo que se desee:

.. code-block:: pycon

    >>> try:
    ...     raise Exception("carne", "huevos")
    ... except Exception as inst:
    ...     print(type(inst))  # la instancia de excepción
    ...     print(inst.args)  # argumentos guardados en .args
    ...     print(inst)  # __str__ permite imprimir args directamente
    ...     x, y = inst  # __getitem__ permite usar args directamente
    ...     print("x =", x)
    ...     print("y =", y)
    ...
    <type 'exceptions.Exception'>
    ('carne', 'huevos')
    ('carne', 'huevos')
    x = carne
    y = huevos

Si una excepción tiene un argumento, este se imprime como la última parte (el 'detalle')
del mensaje para las excepciones que no están manejadas.

Los manejadores de excepciones no manejan solamente las excepciones que ocurren en el
*bloque try*, también manejan las excepciones que ocurren dentro de las funciones que
se llaman (inclusive indirectamente) dentro del *bloque try*. Por ejemplo:

.. code-block:: pycon

    >>> def esto_falla():
    ...     x = 1 / 0
    ...
    >>> try:
    ...     esto_falla()
    ... except ZeroDivisionError as detail:
    ...     print("Manejando error en tiempo de ejecución:", detail)
    ...
    Manejando error en tiempo de ejecución: integer division or modulo by zero


.. _python_sent_raise:

Levantando excepciones
......................

La sentencia ``raise`` permite al programador forzar a que ocurra una excepción
específica. Por ejemplo:

.. code-block:: pycon

    >>> raise NameError("Hola")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    NameError: Hola

El único argumento a ``raise`` indica la excepción a generarse. Tiene que ser o
una instancia de excepción, o una clase de excepción (una clase que hereda de
:ref:`Exception <python_exception>`).

Si necesitás determinar cuando una excepción fue lanzada pero no querés manejarla,
una forma simplificada de la sentencia ``raise`` te permite relanzarla:

.. code-block:: pycon

    >>> try:
    ...     raise NameError("Hola")
    ... except NameError:
    ...     print("Ha sucedido una excepción!")
    ...     raise
    ...
    Ha sucedido una excepción!
    Traceback (most recent call last):
      File "<stdin>", line 2, in ?
    NameError: Hola


.. _python_sent_assert:

Sentencia assert
................

La sentencia ``assert`` es una vía conveniente para insertar afirmaciones de
depuración dentro de un programa:

La forma simple, "assert expression", es equivalente a:

.. code-block:: python

    if __debug__:
        if not expression:
            raise AssertionError

La forma extendida, "assert expression1, expression2", es equivalente a:

.. code-block:: python

    if __debug__:
        if not expression1:
            raise AssertionError(expression2)

Estas equivalencias suponen que ``__debug__`` y la excepción
":ref:`AssertionError <python_exception_assertionerror>`" se refieren a las
variables incorporadas con esos nombres. En la corriente implementación, la
variable incorporada ``__debug__`` es ``True`` en circunstancias normales,
``False`` cuando se solicita la optimización (opción del línea de comando ``-O``).
El generador de código actual no emite ningún código para una sentencia ``assert``
cuando se solicita la optimización en tiempo de compilación. Nota que no es necesario
incluir el código fuente de la expresión que falló en el mensaje de error; se mostrará
como parte del *stack trace*.

Asignaciones a ``__debug__`` son ilegales. El valor para la variable integrada es
determinada cuando el interprete inicia.

.. todo: TODO terminar de escribir esta sección


.. _python_excepciones_usuario:

Excepciones definidas por el usuario
....................................

Los programas pueden nombrar sus propias excepciones creando una nueva clase excepción
(mirá el apartado de :ref:`Clases <python_poo>` para más información sobre las clases
de Python). Las excepciones, típicamente, deberán derivar de la clase
:ref:`Exception <python_exception>`, directa o indirectamente. Por ejemplo:

.. code-block:: pycon

    >>> class MiError(Exception):
    ...     def __init__(self, valor):
    ...         self.valor = valor
    ...     def __str__(self):
    ...         return repr(self.valor)
    ...
    >>> try:
    ...     raise MiError(2 * 2)
    ... except MiError as e:
    ...     print("Ha ocurrido mi excepción, valor:", e.valor)
    ...
    Ocurrió mi excepción, valor: 4
    >>> raise MiError("oops!")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    __main__.MiError: 'oops!'

En este ejemplo, el método :meth:`__init__` de :ref:`Exception <python_exception>`
fue sobrescrito. El nuevo comportamiento simplemente crea el atributo *valor*.

Esto reemplaza el comportamiento por defecto de crear el atributo *args*.

Las clases de Excepciones pueden ser definidas de la misma forma que cualquier otra
clase, pero usualmente se mantienen simples, a menudo solo ofreciendo un número de
atributos con información sobre el error que leerán los manejadores de la excepción.
Al crear un módulo que puede lanzar varios errores distintos, una práctica común es
crear una clase base para excepciones definidas en ese módulo y extenderla para crear
clases excepciones específicas para distintas condiciones de error:

.. code-block:: python

    class Error(Exception):
        """Clase base para excepciones en el módulo."""

        pass


    class EntradaError(Error):
        """Exception lanzada por errores en las entradas.

        Atributos:
            expresion -- expresión de entrada en la que ocurre el error
            mensaje -- explicación del error
        """

        def __init__(self, expresion, mensaje):
            self.expresion = expresion
            self.mensaje = mensaje


    class TransicionError(Error):
        """Lanzada cuando una operación intenta una
          transición de estado no permitida.

        Atributos:
            previo -- estado al principio de la transición
            siguiente -- nuevo estado intentado
            mensaje -- explicación de porque la transición no esta permitida
        """

        def __init__(self, previo, siguiente, mensaje):
            self.previo = previo
            self.siguiente = siguiente
            self.mensaje = mensaje

La mayoría de las excepciones son definidas con nombres que terminan en "Error",
similares a los nombres de las excepciones estándar.

Muchos módulos estándar definen sus propias excepciones para reportar errores que
pueden ocurrir en funciones propias. Se puede encontrar más información sobre clases
en el capítulo :ref:`Clases <python_poo>`.


.. _python_sent_finally:

Definiendo acciones de limpieza
...............................

La sentencia ``try`` tiene otra sentencia opcional que intenta definir acciones de
limpieza que deben ser ejecutadas bajo ciertas circunstancias. Por ejemplo:

.. code-block:: pycon

    >>> try:
    ...     raise KeyboardInterrupt
    ... finally:
    ...     print("Adiós, Mundo!")
    ...
    Chau, Mundo!
    Traceback (most recent call last):
      File "<stdin>", line 2, in ?
    KeyboardInterrupt


Una *sentencia finally* siempre es ejecutada antes de salir de la sentencia ``try``,
ya sea que una excepción haya ocurrido o no. Cuando ocurre una excepción en la
sentencia ``try`` y no fue manejada por una sentencia ``except`` (o ocurrió en una
sentencia ``except`` o ``else``), es relanzada luego de que se ejecuta la sentencia
``finally``. La sentencia ``finally`` es también ejecutada "a la salida" cuando
cualquier otra sentencia de la sentencia ``try`` es dejada vía ``break``, ``continue``
or ``return``. Un ejemplo más complicado (sentencias ``except`` y ``finally`` en la
misma sentencia ``try``):

.. code-block:: pycon

    >>> def dividir(x, y):
    ...     try:
    ...         resultado = x / y
    ...     except ZeroDivisionError:
    ...         print("¡división por cero!")
    ...     else:
    ...         print("el resultado es", resultado)
    ...     finally:
    ...         print("ejecutando la clausula finally")
    ...
    >>> dividir(2, 1)
    el resultado es 2
    ejecutando la clausula finally
    >>> dividir(2, 0)
    ¡división por cero!
    ejecutando la clausula finally
    >>> divide("2", "1")
    ejecutando la clausula finally
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
      File "<stdin>", line 3, in divide
    TypeError: unsupported operand type(s) for /: 'str' and 'str'


Como puedes ver, la sentencia ``finally`` es ejecutada siempre. La excepción
:ref:`TypeError <python_exception_typeerror>` lanzada al dividir dos cadenas de
caracteres no es manejado por la sentencia ``except`` y por lo tanto es relanzada
luego de que se ejecuta la sentencia ``finally``.

En aplicaciones reales, la sentencia ``finally`` es útil para liberar recursos
externos (como archivos o conexiones de red), sin importar si el uso del recurso
fue exitoso.


Acciones predefinidas de limpieza
.................................

Algunos objetos definen acciones de limpieza estándar que llevar a cabo cuando el
objeto no es más necesitado, independientemente de que las operaciones sobre el
objeto hayan sido exitosas o no. Mirá el siguiente ejemplo, que intenta
:ref:`abrir un archivo <python_manipular_archivo>` e imprimir su contenido en la
pantalla.

.. code-block:: python

    for linea in open("numeros.txt"):
        print(linea)


El problema con este código es que deja el archivo abierto por un periodo de tiempo
indeterminado luego de que termine de ejecutarse. Esto no es un problema en scripts
simples, pero puede ser un problema en aplicaciones más grandes.


.. _python_sent_with:

Sentencia with
~~~~~~~~~~~~~~

La sentencia ``with`` permite que objetos como archivos sean usados de una forma que
asegure que siempre se los libera rápido y en forma correcta.

.. code-block:: python

    with open("numeros.txt") as f:
        for linea in f:
            print(linea)

Luego de que la sentencia sea ejecutada, el archivo *f* siempre es cerrado, incluso si
se encuentra un problema al procesar las líneas. Otros objetos que provean acciones de
limpieza predefinidas lo indicarán en su documentación.


Traceback
.........

El ``Traceback`` o *trazado inverso*, es un listado de las funciones en curso de ejecución,
presentadas cuando sucede un error en tiempo de ejecución. Es común que al trazado inverso
también se le conozca como *trazado de pila*, porque lista las funciones en el orden en el
cual son almacenadas en la
`pila de llamadas <https://es.wikipedia.org/wiki/Pila_(estructura_de_datos)#Pila_de_llamadas>`_.

El módulo integrado `traceback <https://docs.python.org/3/library/traceback.html>`_ incorpora el
comportamiento de ``Traceback`` o *trazado inverso* ya que extrae, formatea e imprime información
acerca de *trazado del stack* de los errores y excepciones en Python.

.. code-block:: pycon

    >>> import traceback
    >>> traceback.__doc__
    'Extract, format and print information about Python stack traces.'
    >>> help(traceback)


----


.. important::
    Usted puede descargar el código usado en esta sección haciendo clic en los
    siguientes enlaces:
    :download:`excepciones_integradas.py <../../recursos/leccion9/excepciones_integradas.py>`,
    :download:`excepciones_propias.py <../../recursos/leccion9/excepciones_propias.py>`
    y :download:`errores_propios.py <../../recursos/leccion9/errores_propios.py>`.


.. tip::
    Para ejecutar el código :file:`excepciones_integradas.py` y :file:`errores_propios.py`,
    abra una consola de comando, acceda al directorio donde se encuentra ambos programas:

    ::

        leccion9/
        ├── excepciones_integradas.py
        ├── excepciones_propias.py
        └── errores_propios.py

    Si tiene la estructura de archivo previa, entonces ejecute el siguiente comando:

    .. code-block:: console

        $ python excepciones_integradas.py
        $ python errores_propios.py


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion9>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
