.. -*- coding: utf-8 -*-


.. _python_excepciones_builtins:

Excepciones integradas
----------------------

Las excepciones pueden ser objetos de una clase u objetos cadena. Aunque la mayoría
de las excepciones eran objetos cadena en las anteriores versiones de Python, en
Python 1.5 y versiones posteriores, todas las excepciones estándar han sido convertidas
en objetos de clase y se anima a los usuarios a que hagan lo propio. Las excepciones
están definidas en el módulo ``exceptions``. Nunca es necesario importar este módulo
explícitamente, pues las excepciones vienen proporcionadas por el espacio nominal
interno.

Dos objetos de cadena distintos con el mismo valor se consideran diferentes excepciones.
Esto es así para forzar a los programadores a usar nombres de excepción en lugar
de su valor textual al especificar gestores de excepciones. El valor de cadena de
todas las excepciones internas es su nombre, pero no es un requisito para las
:ref:`excepciones definidas por el usuario <python_excepciones_usuario>` u otras
excepciones definidas por módulos de biblioteca.

En el caso de las clases de excepción, en una sentencia ``try`` con una sentencia
``except`` que mencione una clase particular, esta sentencia también gestionará
cualquier excepción derivada de dicha clase (pero no las clases de excepción de
las que deriva ella). Dos clases de excepción no emparentadas mediante sub-clasificación
nunca son equivalentes, aunque tengan el mismo nombre.

Las excepciones internas enumeradas a continuación pueden ser generadas por el
intérprete o por funciones internas. Excepto en los casos mencionados, tienen un
``valor asociado`` indicando en detalle la causa del error. Este valor puede ser
una cadena o tupla de varios elementos informativos (es decir, un código de error
y una cadena que explica el código). El valor asociado es el segundo argumento a
la sentencia ``raise``. En las cadenas de excepción, el propio valor asociado se
almacenará en la variable nombrada como el segundo argumento de la sentencia ``except``
(si la hay). En las clases de excepción, dicha variable recoge la instancia de la
excepción. Si la clase de excepción deriva de la clase raíz estándar
:ref:`Exception <python_exception>`, el valor asociado está disponible en el atributo
``args`` de la instancia de excepción y es probable que aparezca en otros atributos.

El código de usuario puede lanzar excepciones internas. Se puede usar para comprobar
un gestor de excepciones o para informar de una condición de error del mismo modo
que el intérprete lanza la misma excepción. Hay que ser precavido, pues nada incluye
que el código de usuario lance una excepción inadecuada.

Las siguientes excepciones sólo se usan como clase base de otras excepciones.


.. _python_exception_baseexceptionerror:

``BaseException``
    La clase base de todas las comunes excepciones. Deriva de la clase raíz ``__builtin__.object``,
    es el tipo más básico.


.. _python_exception:

``Exception``
    La clase base de todas las excepciones no existentes. Deriva de la clase raíz
    :ref:`BaseException <python_exception_baseexceptionerror>`.

    La clase base de las excepciones. Todas las excepciones internas derivan de esta
    clase. Todas las excepciones definidas por usuario deberían derivarse de esta
    clase, aunque no es obligatorio (todavía). La función ``str()``, aplicada a una
    instancia de una clase (o la mayoría de sus clases derivadas) devuelve un valor
    cadena a partir de sus argumentos o una cadena vacía si no se proporcionaron
    argumentos al constructor. Si se usa como secuencia, accede a los argumentos
    proporcionados al constructor (útil para compatibilidad con código antiguo). Los
    argumentos también están disponibles en el atributo ``args`` de la instancia,
    como tupla.


.. _python_exception_standarderror:

``StandardError``
    La clase base para todas las excepciones internas excepto
    :ref:`SystemExit <python_exception_systemexit>`. Deriva de la clase raíz
    :ref:`Exception <python_exception>`.


.. _python_exception_arithmeticerror:

``ArithmeticError``
    La clase base de las excepciones lanzadas por diversos errores aritméticos:
    :ref:`OverflowError <python_exception_overflowerror>`,
    :ref:`ZeroDivisionError <python_exception_zerodivisionerror>` y
    :ref:`FloatingPointError <python_exception_floatingpointerror>`. Deriva de la clase raíz
    :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_lookuperror:

``LookupError``
    La clase base de las excepciones lanzadas cuando una clave o índice utilizado en
    una correspondencia (diccionario) o secuencia son incorrectos:
    :ref:`IndexError <python_exception_indexerror>`, :ref:`KeyError <python_exception_keyerror>`.
    Deriva de la clase raíz :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_environmenterror:

``EnvironmentError``
    La clase base de las excepciones que pueden ocurrir fuera del sistema Python:
    :ref:`IOError <python_exception_ioerror>`, :ref:`OSError <python_exception_oserror>`.
    Cuando se crean excepciones de este tipo con una tupla de dos valores, el
    primer elemento queda disponible en el atributo ``errno`` de la instancia (se
    supone que es un número de error) y el segundo en el atributo ``strerror`` (suele
    ser el mensaje de error asociado). La propia tupla está disponible en el atributo
    ``args``.
    Cuando se instancia una excepción ``EnvironmentError`` con una tupla de tres
    elementos, los primeros dos quedan disponibles como en el caso de dos elementos y
    el tercero queda en el atributo ``filename``. Sin embargo, por compatibilidad con
    sistemas anteriores, el atributo ``args`` contiene sólo una tupla de dos elementos
    de los dos primeros argumentos del constructor.
    El atributo ``filename`` es :ref:`None <python_obj_none>` cuando se cree la excepción
    con una cantidad de argumentos diferente de 3. Los atributos ``errno`` y ``strerror``
    son también ``None`` cuando la instancia no se cree con 2 ó 3 argumentos. En este
    último caso, ``args`` contiene los argumentos del constructor tal cual, en forma de
    tupla. Deriva de la clase raíz :ref:`StandardError <python_exception_standarderror>`.


Las siguientes excepciones son las realmente lanzadas.

.. _python_exception_assertionerror:

``AssertionError``
    Se lanza cuando una sentencia ``assert`` es ``False``. Deriva de la clase raíz
    :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_attributeerror:

``AttributeError``
    Se lanza cuando una referencia o asignación a atributo fracasa (cuando un objeto no tenga
    referencias o asignaciones a atributos en absoluto, se lanza, la excepción
    :ref:`TypeError <python_exception_typeerror>`.) Deriva de la clase raíz
    :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_buffererror:

``BufferError``
    Se lanza cuando un error Buffer sucede. Deriva de la excepción
    :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_eoferror:

``EOFError``
    Se lanza cuando la función interna (:ref:`input() <python_fun_input>`)
    alcanzan un *end of file* ``EOF`` (final de archivo) sin leer datos.
    N.B.: Los métodos :ref:`read() <python_mtd_read>` y :ref:`readline() <python_mtd_readline>`
    de los objetos archivo devuelven una cadena vacía al alcanzar ``EOF``.
    Deriva de la clase raíz :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_floatingpointerror:

``FloatingPointError``
    Se lanza cuando falla una operación de coma flotante. Esta excepción siempre está definida,
    pero sólo se puede lanzar cuando Python esta configurado con la opción ``--with-fpectl`` o
    se ha definido el símbolo ``WANT_SIGFPE_HANDLER`` en el archivo :file:`config.h`. Deriva de
    la clase raíz :ref:`ArithmeticError <python_exception_arithmeticerror>`.


.. _python_exception_generatorexiterror:

``GeneratorExit``
    Se lanza cuando la solicitud de salida de un generador Python sucede. Deriva de la
    excepción :ref:`BaseException <python_exception_baseexceptionerror>`.


.. _python_exception_ioerror:

``IOError``
    Se lanza cuando una operación de E/S (tal como una sentencia :ref:`print <python_salida>`,
    la función integrada :ref:`open() <python_fun_open>` o un método de un objeto
    archivo) fracasa por motivos relativos a E/S, por ejemplo, por no encontrarse un archivo
    o llenarse el disco. Esta clase se deriva de
    :ref:`EnvironmentError <python_exception_environmenterror>`. En la explicación anterior
    se proporciona información adicional sobre los atributos de instancias de excepción.
    Deriva de la clase raíz :ref:`EnvironmentError <python_exception_environmenterror>`.


.. _python_exception_importerror:

``ImportError``
    Se lanza cuando una sentencia ``import`` no encuentra la definición del módulo o
    cuando ``from ... import`` no encuentra un nombre a importar. Deriva de la clase raíz
    :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_indexerror:

``IndexError``
    Se lanza cuando un sub-índice de una secuencia se sale del rango. Los índices de
    corte se truncan silenciosamente al rango disponible. Si un índice no es un entero
    simple, se lanza :ref:`TypeError <python_exception_typeerror>`. Deriva de la clase raíz
    :ref:`LookupError <python_exception_lookuperror>`.


.. _python_exception_indentationerror:

``IndentationError``
    Se lanza cuando una indentación incorrecta sucede. Deriva de la excepción :ref:`SyntaxError <python_exception_syntaxerror>`.


.. _python_exception_keyerror:

``KeyError``
    Se lanza cuando no se encuentra una clave de una correspondencia (diccionario) en
    el conjunto de claves existentes. Deriva de la clase raíz
    :ref:`LookupError <python_exception_lookuperror>`.


.. _python_exception_keyboardinterrupterror:

``KeyboardInterrupt``
    Se lanza cuando el usuario pulsa la tecla de interrupción (normalmente con la
    combinación de teclas :keys:`Ctrl+C` o :keys:`DEL`).
    A lo largo de la ejecución se comprueba si se ha interrumpido regularmente. Las
    interrupciones ocurridas cuando una función :ref:`input() <python_fun_input>`
    espera datos también lanzan esta excepción. Deriva de la clase raíz
    :ref:`BaseException <python_exception_baseexceptionerror>`.


.. _python_exception_memoryerror:

``MemoryError``
    Se lanza cuando una operación agota la memoria pero aún se puede salvar la
    situación (borrando objetos). El valor asociado es una cadena que indica qué
    tipo de operación (interna) agotó la memoria. Obsérvese que por la arquitectura
    de gestión de memoria subyacente (la función de C ``malloc()``), puede que el
    intérprete no siempre sea capaz de recuperarse completamente de esta situación.
    De cualquier modo, se lanza una excepción para que se pueda imprimir una traza,
    por si la causa fue un programa desbocado. Deriva de la clase raíz
    :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_nameerror:

``NameError``
    Se lanza cuando no se encuentra un nombre local o global. Sólo se aplica a nombre
    no calificados. El valor asociado es el nombre no encontrado. Deriva de la clase raíz
    :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_notimplementederror:

``NotImplementedError``
    Esta excepción se deriva de :ref:`RuntimeError <python_exception_runtimeerror>`.
    En clases base definidas por el usuario, los métodos abstractos deberían lanzar
    esta excepción cuando se desea que las clases derivadas redefinan este método.
    Deriva de la clase raíz :ref:`RuntimeError <python_exception_runtimeerror>`.


.. _python_exception_oserror:

``OSError``
    Esta clase se deriva de :ref:`EnvironmentError <python_exception_environmenterror>`
    y se usa principalmente como excepción os.error de os. En
    :ref:`EnvironmentError <python_exception_environmenterror>` hay una descripción de
    los posibles valores asociados.


.. _python_exception_overflowerror:

``OverflowError``
    Se lanza cuando el resultado de una operación aritmética es demasiado grande para
    representarse (desbordamiento). Esto no es posible en los enteros largos (que antes
    que rendirse lanzarían :ref:`MemoryError <python_exception_memoryerror>`). Por la
    falta de normalización de la gestión de excepciones de coma flotante en C, la mayoría
    de las operaciones de coma flotante, tampoco se comprueban. En el caso de enteros
    normales, se comprueban todas las operaciones que pueden desbordar excepto el
    desplazamiento a la izquierda, en el que las aplicaciones típicas prefieren perder
    bits que lanzar una excepción. Deriva de la clase raíz
    :ref:`ArithmeticError <python_exception_arithmeticerror>`.


.. _python_exception_runtimeerror:

``RuntimeError``
    Se lanza cuando se detecta un error que no cuadra en ninguna de las otras categorías.
    El valor asociado es una cadena que indica qué fue mal concretamente. Esta excepción
    es mayormente una reliquia de versiones anteriores del intérprete; ya casi no se usa.
    Deriva de la clase raíz :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_stopiteration:

``StopIteration``
    Se lanza cuando se indica el final desde ``next(iterator)``. Deriva de la excepción
    :ref:`Exception <python_exception>`.


.. _python_exception_syntaxerror:

``SyntaxError``
    Se lanza cuando el analizador encuentra un error en la sintaxis. Esto puede
    ocurrir en una sentencia ``import``, en una sentencia ``exec``, en una llamada
    a la función interna ``eval()`` o :ref:`input() <python_fun_input>`, o al
    leer el guion inicial o la entrada estándar (por ejemplo, la entrada interactiva).
    Si se usan excepciones de clase, las instancias de esta clase tienen disponibles
    los atributos ``filename`` (nombre del archivo), ``lineno`` (nº de línea),
    ``offset`` (nº de columna) y ``text`` (texto), que ofrecen un acceso más fácil a
    los detalles. En las excepciones de cadena, el valor asociado suele ser una tupla
    de la forma (mensaje, (nombreArchivo, numLinea, columna, texto)). En las excepciones
    de clase, ``str()`` sólo devuelve el mensaje. Deriva de la clase raíz
    :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_systemerror:

``SystemError``
    Se lanza cuando el intérprete encuentra un error interno, pero la situación no
    parece tan grave como para perder la esperanza. El valor asociado es una cadena
    que indica qué ha ido mal (en términos de bajo nivel). Se debería dar parte de
    este error al autor o mantenedor del intérprete Python en cuestión. Se debe incluir
    en el informe la cadena de versión del intérprete Python (``sys.version``, que
    también se muestra al inicio de una sesión interactiva), la causa exacta del error
    y, si es posible, el código fuente del programa que provocó el error. Deriva de la
    clase raíz :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_systemexit:

``SystemExit``
    Lanzada por la función ``sys.exit()``. Si no se captura, el intérprete de Python
    finaliza la ejecución sin presentar una pila de llamadas. Si el valor asociado es
    un entero normal, especifica el estado de salida al sistema (se pasa a la función
    de C ``exit()``), Si es None, el estado de salida es cero (que indica una salida
    normal sin errores). En el caso de ser de otro tipo, se presenta el valor del objeto
    y el estado de salida será ``1``.
    Las instancias tienen un atributo ``code`` cuyo valor se establece al estado de salida
    o mensaje de error propuesto (inicialmente ``None``). Además, esta excepción deriva
    directamente de :ref:`Exception <python_exception>` y no de la excepción
    :ref:`StandardError <python_exception_standarderror>`, ya que técnicamente no es un
    error. Una llamada a ``sys.exit()`` se traduce a un error para que los gestores de
    limpieza final (las sentencias ``finally`` de las sentencias ``try``) se puedan ejecutar
    y para que un depurador pueda ejecutar un guion sin riesgo de perder el control. Se
    puede usar la función os._exit() si es total y absolutamente necesario salir inmediatamente
    (por ejemplo, tras un ``fork()`` en el proceso hijo). Deriva de la clase raíz
    :ref:`BaseException <python_exception_baseexceptionerror>`.


.. _python_exception_referenceerror:

``ReferenceError``
    Se lanza cuando se usó un proxy de referencia débil después de que el referente desapareció.
    Deriva de la excepción :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_taberror:

``TabError``
    Se lanza cuando sucede una mezcla inadecuada de espacios y tabulaciones. Deriva de la
    excepción :ref:`IndentationError <python_exception_indentationerror>`.


.. _python_exception_typeerror:

``TypeError``
    Se lanza cuando una operación o función interna se aplica a un objeto de tipo
    inadecuado. El valor asociado es una cadena con detalles de la incoherencia de tipos.
    Deriva de la clase raíz :ref:`StandardError <python_exception_standarderror>`.


.. _python_exception_unboundlocalerror:

``UnboundLocalError``
    Se lanza cuando se hace referencia a una variable local en una función o método,
    pero no se ha asignado un valor a dicha variable. Deriva de la excepción
    :ref:`NameError <python_exception_nameerror>`.


.. _python_exception_unicodeerror:

``UnicodeError``
    Se lanza cuando se da un error relativo a codificación/descodificación ``Unicode``.
    Deriva de la excepción :ref:`ValueError <python_exception_valueerror>`.


.. _python_exception_unicodedecodeerror:

``UnicodeDecodeError``
    Se lanza cuando un error al decodificar ``Unicode`` sucede. Deriva de la excepción
    :ref:`UnicodeError <python_exception_unicodeerror>`.


.. _python_exception_unicodeencodeerror:

``UnicodeEncodeError``
    Se lanza cuando un error al codificar ``Unicode`` sucede. Deriva de la excepción
    :ref:`UnicodeError <python_exception_unicodeerror>`.


.. _python_exception_unicodetranslateerror:

``UnicodeTranslateError``
    Se lanza cuando un error al traducir ``Unicode`` sucede. Deriva de la excepción
    :ref:`UnicodeError <python_exception_unicodeerror>`.


.. _python_exception_valueerror:

``ValueError``
    Se lanza cuando una operación o función interna recibe un argumento del tipo
    correcto, pero con un valor inapropiado y no es posible describir la situación
    con una excepción más precisa, como :ref:`IndexError <python_exception_indexerror>`.


.. _python_exception_zerodivisionerror:

``ZeroDivisionError``
    Se lanza cuando el segundo argumento de una operación de división o módulo
    es cero. El valor asociado es una cadena que indica el tipo de operandos y
    la operación. Deriva de la clase raíz
    :ref:`ArithmeticError <python_exception_arithmeticerror>`.



.. _python_exception_warning:

``Warning``
    La clase base para las categorías de advertencias. Deriva de la excepción
    :ref:`Exception <python_exception>`.


.. _python_exception_byteswarning:

``BytesWarning``
    La clase base para las advertencias acerca de problemas relacionados con bytes y
    buffer, mas relacionado a la conversión desde ``str`` o comparando a ``str``.
    Deriva de la excepción :ref:`Warning <python_exception_warning>`.


.. _python_exception_deprecationwarning:

``DeprecationWarning``
    La clase base para las advertencias acerca de características obsoletas. Deriva de
    la excepción :ref:`Warning <python_exception_warning>`.


.. _python_exception_futurewarning:

``FutureWarning``
    La clase base para las advertencias acerca de constructores que pueden ser cambiado
    sistemáticamente en el futuro. Deriva de la excepción :ref:`Warning <python_exception_warning>`.


.. _python_exception_importwarning:

``ImportWarning``
    La clase base para las advertencias acerca de probables errores en importar módulos.
    Deriva de la excepción :ref:`Warning <python_exception_warning>`.


.. _python_exception_pendingdeprecationwarning:

``PendingDeprecationWarning``
    La clase base para las advertencias acerca de características las cuales serán obsoletas
    en el futuro. Deriva de la excepción :ref:`Warning <python_exception_warning>`.


.. _python_exception_runtimewarning:

``RuntimeWarning``
    La clase base para las advertencias acerca de comportamiento del tiempo de ejecución dudosa.
    Deriva de la excepción :ref:`Warning <python_exception_warning>`.


.. _python_exception_syntaxwarning:

``SyntaxWarning``
    La clase base para las advertencias acerca de sintaxis dudosa. Deriva de la excepción
    :ref:`Warning <python_exception_warning>`.


.. _python_exception_unicodewarning:

``UnicodeWarning``
    La clase base para las advertencias acerca de problemas relacionado con ``Unicode``, más
    relacionado a problemas de conversión. Deriva de la excepción
    :ref:`Warning <python_exception_warning>`.


.. _python_exception_userwarning:

``UserWarning``
    La clase base para las advertencias generadas por código de usuario. Deriva de la excepción
    :ref:`Warning <python_exception_warning>`.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_leccion9>`
    del entrenamiento para ampliar su conocimiento en esta temática.


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

.. disqus::
