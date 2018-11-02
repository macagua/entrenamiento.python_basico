.. -*- coding: utf-8 -*-


.. _python_poo:

Programación orientada a objetos
--------------------------------

La programación orientada a objetos (POO, u OOP según sus siglas 
en inglés) es un paradigma de programación que viene a innovar la 
forma de obtener resultados. Los objetos manipulan los datos de 
entrada para la obtención de datos de salida específicos, donde 
cada objeto ofrece una funcionalidad especial.

Muchos de los objetos prediseñados de los lenguajes de programación 
actuales permiten la agrupación en bibliotecas o librerías, sin 
embargo, muchos de estos lenguajes permiten al usuario la creación 
de sus propias bibliotecas.

Está basada en varias técnicas, como las siguientes:

- :ref:`herencia <python_poo_herencia>`.

- cohesión.

- :ref:`abstracción <python_poo_abstraccion>`.

- :ref:`polimorfismo <python_poo_polimorfismo>`.

- acoplamiento.

- :ref:`encapsulación <python_poo_encapsulacion>`.

La programación orientada a objetos tiene sus raíces en la década 
del 60 con el lenguaje de programación Simula que en 1967, el cual 
fue el primer lenguaje que posee las características principales 
de un lenguaje orientado a objetos. 

Smalltalk (de 1972 a 1980) es posiblemente el ejemplo canónico, y 
con el que gran parte de la teoría de la programación orientada 
a objetos se ha desarrollado. Más su uso se popularizó a principios 
de la década de 1990. 

En la actualidad, existe una gran variedad de lenguajes de programación 
que soportan la orientación a objetos.

Los objetivos de la POO son:

- Organizar el código fuente, y

- re-usar código fuente en similares contextos.


Definiciones necesarias
.......................

**¿Qué es un Objeto?**
    Los objetos son la clave para entender la Programación Orientada 
    a Objetos. Si miramos a nuestro alrededor  encontraremos un sin 
    fin de objetos de la vida real: perro, escritorio, televisor, 
    bicicleta, etc...

**¿Qué es un Atributo?**
    Los atributos o propiedades de los objetos son las características 
    que puede tener un objeto: Si el objeto fuera ``Persona``, los 
    atributos podrían ser: ``cedula``, ``nombre``, ``apellido``, 
    ``sexo``, etc...

**¿Qué es un Método?**
    Los métodos son la acción o función que realiza un objeto. Si 
    nuestro objeto es ``Persona``, los métodos pueden ser: ``hablar``, 
    ``caminar``, ``comer``, ``dormir``, etc...

**¿Qué es una Clase?**
    Con todos los conceptos anteriores explicados, se puede decir que 
    una clase es una plantilla genérica de un objeto. La clase proporciona 
    variables iniciales de estado (donde se guardan los atributos) e 
    implementaciones de comportamiento (métodos).

**¿Qué es una Instancia?**
    Ya sabemos que una clase es una estructura general del objeto. 
    Por ejemplo, podemos decir que la clase ``Persona`` necesita tener 
    una ``cedula``, un ``nombre``, un ``apellido`` y una ``sexo``, pero 
    no nos va a decir cual es ``cedula``, ``nombre``, ``apellido`` y 
    ``sexo``, es aquí donde entran las instancias. Una instancia es una 
    copia específica de la clase con todo su contenido.

    Ejemplo: Leonardo = Persona (13567098, "Leonardo", "Caballero", 38)
    
    Aquí podemos decir que ``Leonardo`` es una instancia de la clase 
    ``Persona``.


Las clases nos dan la posibilidad de crear estructuras de datos más complejas. 
En nuestro ejemplo crearemos una clase ``Persona`` que realizará un seguimiento 
del ``cedula``, ``nombre``, ``apellido`` y ``sexo`` (que pasaremos como atributos).

.. note:: 
    Más información consulte el articulo `Programación orientada a objetos - Wikipedia`_.


Programación orientada a objetos en Python
..........................................

El mecanismo de clases de Python agrega clases al lenguaje 
con un mínimo de nuevas sintaxis y semánticas. Es una mezcla 
de los mecanismos de clase encontrados en ``C++`` y ``Modula-3``. 
Como es cierto para los módulos, las clases en Python no ponen 
una barrera absoluta entre la definición y el usuario, sino que
más bien se apoya en la cortesía del usuario de no "forzar la 
definición". Sin embargo, se mantiene el poder completo de las 
características más importantes de las clases: el mecanismo de 
la herencia de clases permite múltiples clases base, una clase 
derivada puede sobrescribir cualquier método de su(s) clase(s)
base, y un método puede llamar al método de la clase base con 
el mismo nombre.

    "Los objetos pueden tener una cantidad arbitraria de datos."

En terminología de ``C++``, todos los miembros de las clases (incluyendo 
los miembros de datos), son *públicos*, y todas las funciones 
miembro son *virtuales*. Como en ``Modula-3``, no hay atajos para 
hacer referencia a los miembros del objeto desde sus métodos: 
la función método se declara con un primer argumento explícito 
que representa al objeto, el cual se provee implícitamente por 
la llamada. Como en ``Smalltalk``, las clases mismas son objetos. 
Esto provee una semántica para importar y renombrar. A diferencia
de ``C++`` y ``Modula-3``, los tipos de datos integrados pueden usarse 
como clases base para que el usuario los extienda. También, como 
en ``C++`` pero a diferencia de ``Modula-3``, la mayoría de los operadores 
integrados con sintaxis especial (operadores aritméticos, de 
subíndice, etc.) pueden ser redefinidos por instancias de la clase.

(Sin haber una terminología universalmente aceptada sobre clases, 
haré uso ocasional de términos de ``Smalltalk`` y ``C++``. Usaría términos 
de ``Modula-3``, ya que su semántica orientada a objetos es más cercana 
a Python que ``C++``, pero no espero que muchos lectores hayan escuchado 
hablar de él).


Clase Base
..........

Clase Base o también conocida como *Clase abstracta* le permite definir una 
clase que puede heredarse en otras clases los atributos y comportamientos 
definido en esta.

Ejemplo de la clase ``Persona`` con función interna:

.. literalinclude:: ../../recursos/leccion9/clases.py
    :linenos:
    :language: python
    :lines: 3-32


En el ejemplo previo, es donde empieza a crear una clase (lo hace con la 
palabra ``class``). La segunda palabra ``Persona`` es el nombre de la clase. 
La tercera palabra que se encuentra dentro de los paréntesis ``object`` se 
conoce con el nombre de herencia (mas tarde abajo se explicará el concepto 
de herencia). Lo que debe saber es que ``object`` es una variable especial 
en Python que se utiliza de herencia cuando creamos una nueva clase en Python.

La clase ``Persona`` tiene los métodos ``__init__``, ``__str__``, ``hablar`` 
y ``getSexo``. Sus atributos son ``cedula``, ``nombre``, ``apellido`` y ``sexo``. 

La instancia de dos nuevos objetos ``Persona`` seria de la siguiente forma:

.. literalinclude:: ../../recursos/leccion9/clases.py
    :linenos:
    :language: python
    :lines: 59-60

El método constructor ``__init__`` es un método especial el cual debe escribir 
como: ``MiClase(parámetros iniciales si hay cualquiera)``.

Usted puede invocar esos métodos y atributos con la siguiente notación: 
``claseinstancia.metodo`` o ``claseinstancia.atributo``. 

.. literalinclude:: ../../recursos/leccion9/clases.py
    :linenos:
    :language: python
    :lines: 63

El método ``__str__`` es un método usando para imprimir la descripción de la 
instancia de objeto el cual debe mostrar como:

.. literalinclude:: ../../recursos/leccion9/clases.py
    :linenos:
    :language: python
    :lines: 69

En el anterior código se usan para cierto formato para imprimir la instancia de 
objeto usando la sentencia ``print``, concatenando el carácter ``\n`` para 
generar un salto de página y seguidamente convertir a formato cadena de caracteres 
usando la función ``str()`` a la instancia de objeto llamada ``persona2``. 

.. _python_poo_herencia:

Herencia
........

La herencia en Python nos permite a los programadores crear una clase general 
primero y luego más tarde crear clases más especializadas que re utilicen código 
de la clase general. La herencia también nos permite escribir un código más 
limpio y legible.



Herencia simple
~~~~~~~~~~~~~~~

El siguiente es un ejemplo de la clase ``Supervisor`` 
que derivada de la clase ``Persona`` con función interna:

.. literalinclude:: ../../recursos/leccion9/clases.py
    :linenos:
    :language: python
    :lines: 35-56

Ahora, se creará una nueva clase ``Supervisor`` con los mismos métodos y atributos 
como la clase ``Persona``, pero con dos nuevos atributos ``permisos`` y ``tareas``. 
No se copia la clase previa, pero si **se hereda** de ella.

La instancia del nuevo objeto ``Supervisor`` seria de la siguiente forma:

.. literalinclude:: ../../recursos/leccion9/clases.py
    :linenos:
    :language: python
    :lines: 79

Luego que generá la instancia del nuevo objeto ``Supervisor`` llamada ``supervisor1`` 
se puede imprimir sus detalles de la siguiente forma:

.. literalinclude:: ../../recursos/leccion9/clases.py
    :linenos:
    :language: python
    :lines: 80

Si desea usar los métodos de la clase ``Supervisor`` se puede imprimir de la siguiente forma:

.. literalinclude:: ../../recursos/leccion9/clases.py
    :linenos:
    :language: python
    :lines: 81-82

Como la instancia de objeto ``supervisor1`` hereda los métodos de la clase ``Persona`` 
usted puede reusarlo e invocarlo de la siguiente forma:

.. literalinclude:: ../../recursos/leccion9/clases.py
    :linenos:
    :language: python
    :lines: 84-85

Gracias a las clases y la programación orientada a objetos, usted puede organizar 
el código con diferentes clases correspondientes a diferentes objetos que encontramos 
(una clase ``Persona``, una clase ``Carro``, una clase ``Departamento``, etc.), con sus 
propios métodos y atributos. Luego podemos usar la herencia para considerar las 
variaciones en torno a una clase base y reutilizar el código. Ej.: a partir de una 
clase base de ``Persona``, podemos crear clases derivadas como ``Supervisor``, 
``Profesor``, ``Obrero``, etc.

.. literalinclude:: ../../recursos/leccion9/clases.py
    :linenos:
    :language: python
    :lines: 89-92


Herencia múltiple
~~~~~~~~~~~~~~~~~

A diferencia de lenguajes como *Java* y *C#*, Python permite la herencia múltiple, 
es decir, se puede heredar de múltiples clases.


.. _python_poo_polimorfismo:

Polimorfismo
.............


.. todo::
    TODO escribir esta sección


.. _python_overriding_methods:

Sobrecarga de métodos
~~~~~~~~~~~~~~~~~~~~~

La *sobrecarga de métodos* es también es conocida por *Overriding Methods*, 
le permite sustituir un método proveniente de la Clase Base, en la Clase 
Derivada debemos definir un método con la **misma forma** (es decir, mismo 
nombre de método y mismo número de parámetros que como está definido en la 
Clase Base).

::

    >>> class Persona():
    ...     def __init__(self):
    ...         self.cedula = 13765890
    ...     def mensaje(self):
    ...         print("mensaje desde la clase Persona")
    ... 
    >>> class Obrero(Persona):
    ...     def __init__(self):
    ...         self.__especialista = 1
    ...     def mensaje(self):
    ...         print("mensaje desde la clase Obrero")
    ... 
    >>> obrero_planta = Obrero()
    >>> obrero_planta.mensaje()
    mensaje desde la clase Obrero
    >>> 


Lo que se logra definiendo el método ``mensaje()`` en la Clase Derivada 
(``Obrero``) se conoce como **Método Overriding** (cuando se cree el objeto 
(en este caso ``obrero_planta`` y se llame al método ``mensaje()``, este será 
tomado de la propia clase y no de la Clase Base ``Persona``). Si **comentamos 
o borramos** el método ``mensaje()`` de la clase ``Obrero`` (Clase Derivada) 
y corremos nuevamente el código, el método llamado será el ``mensaje()`` de la 
Clase Base ``Persona``.


.. _python_overloading_operators:

Sobrecarga de Operadores
~~~~~~~~~~~~~~~~~~~~~~~~

La *sobrecarga de operadores* es también es conocida por *Overloading Operators*, 
trata básicamente de lo mismo que la **sobrecarga de métodos** pero pertenece en 
esencia al ámbito de los operadores aritméticos, binarios, de comparación y lógicos.

::

    >>> class Punto:
    ...     def __init__(self,x = 0,y = 0):
    ...         self.x = x
    ...         self.y = y
    ...     def __add__(self,other):
    ...         x = self.x + other.x
    ...         y = self.y + other.y
    ...         return x, y
    ... 
    >>> punto1 = Punto(4,6)
    >>> punto2 = Punto(1,-2)
    >>> print punto1 + punto2
    (5, 4)


.. _python_poo_abstraccion:

Abstracción
...........


.. todo::
    TODO escribir esta sección


.. _python_poo_encapsulacion:

Encapsulación (Ocultación de datos)
...................................

Los atributos de un objeto pueden ocultarse (superficialmente) para que no sean 
accedidos desde fuera de la definición de una clase. Para ello, es necesario 
nombrar los atributos con un prefijo de doble subrayado: ``__atributo``.

::

    >>> class Factura:
    ...     __tasa = 19
    ...     def __init__(self, unidad, precio):
    ...         self.unidad = unidad
    ...         self.precio = precio
    ...     def por_pagar(self):
    ...         total = self.unidad * self.precio
    ...         impuesto = total * Factura.__tasa / 100
    ...         return(total + impuesto)
    ... 
    >>> compra1 = Factura(12, 110)
    >>> print compra1.unidad
    12
    >>> print compra1.precio
    110
    >>> print compra1.por_pagar(), "bitcoins"
    (1570, 'bitcoins')
    >>> print Factura.__tasa
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: class Factura has no attribute '__tasa'
    >>> 


Python protege estos atributos cambiando su nombre internamente. A sus 
nombres agrega el nombre de la clase:

    ``objeto._NombreClase__NombreAtributo``

::

    >>> print compra1._Factura__tasa
    19
    >>> 

----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion9>` 
    del entrenamiento para ampliar su conocimiento en esta temática.

.. _`Programación orientada a objetos - Wikipedia`: https://es.wikipedia.org/wiki/Programaci%C3%B3n_orientada_a_objetos
