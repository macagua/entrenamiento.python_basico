.. _python_poo_polimorfismo:

Polimorfismo
------------

El polimorfismo es un concepto de la :ref:`programación orientada a objetos (OOP) <python_poo>`
que se refiere a la capacidad de un objeto de tomar diferentes formas según el contexto.

Una operación puede presentar diferentes comportamientos en diferentes instancias. El
comportamiento depende de los tipos de datos utilizados en la operación. El polimorfismo
es ampliamente utilizado en la aplicación de la :ref:`herencia <python_poo_herencia>`.

En Python, el polimorfismo se puede lograr de varias maneras, como:

- :ref:`Sobrecarga de operadores <python_overloading_operators>`.

- :ref:`Sobrecarga de métodos <python_overriding_methods>`.

- :ref:`Polimorfismo de subtipos <python_overriding_subtype_polymorphism>`.

Veamos a continuación mas detalle de cada uno de ellos.


.. _python_overloading_operators:

Sobrecarga de operadores
........................

Python permite definir el comportamiento de los operadores estándar para tipos de datos
personalizados. Por ejemplo, podemos crear una clase ``Fracción`` que representa una
fracción matemática y definir el operador + para sumar dos fracciones.

.. code-block:: pycon

    >>> import math
    >>>
    >>> class Fraccion:
    ...     def __init__(self, numerador, denominador):
    ...         """Método Constructor"""
    ...         self.numerador = numerador
    ...         self.denominador = denominador
    ...     def simplificar(self):
    ...         """Método para simplificar la fracción"""
    ...         # Buscar el máximo común divisor
    ...         mcd = math.gcd(self.numerador, self.denominador)
    ...         # Dividir el numerador y el denominador por el mcd
    ...         self.numerador //= mcd
    ...         self.denominador //= mcd
    ...     def mostrar(self):
    ...         """Método para mostrar la fracción"""
    ...         print(f"{self.numerador}/{self.denominador}")
    ...     def __add__(self, otra):
    ...         """Método para sobrecargar el operador +"""
    ...         # Sumar las fracciones usando la regla de cruz
    ...         nuevo_numerador = (
    ...             self.numerador * otra.denominador + self.denominador * otra.numerador
    ...         )
    ...         nuevo_denominador = self.denominador * otra.denominador
    ...         # Crear una nueva fracción con el resultado
    ...         nueva_fraccion = Fraccion(nuevo_numerador, nuevo_denominador)
    ...         # Simplificar la nueva fracción
    ...         nueva_fraccion.simplificar()
    ...         # Devolver la nueva fracción
    ...         return nueva_fraccion
    ...
    >>>


Crear instancias de objetos para dos fracciones:

.. code-block:: pycon

    >>> f1 = Fraccion(2, 3)
    >>> f2 = Fraccion(3, 4)
    >>>


Sumar las fracciones usando el operador :ref:`+ <python_opers_arit_suma>`:

.. code-block:: pycon

    >>> f3 = f1 + f2
    >>> f3.mostrar()
    17/12
    >>>

Otro ejemplo de la *sobrecarga de operadores* es también es conocida por `Overloading Operators`_,
trata básicamente de lo mismo que la :ref:`sobrecarga de métodos <python_overriding_methods>`
pero pertenece en esencia al ámbito de los siguientes operadores:

- :ref:`operadores aritméticos <python_opers_aritmeticos>`.

- `operadores binarios <https://ellibrodepython.com/operadores-bitwise>`_.

- :ref:`operadores de comparación <python_opers_relacionales>`.

- :ref:`operadores lógicos <python_opers_logicos>`.

Por ejemplo, podemos crear una clase ``Punto`` que representa una fracción
matemática y definir el operador + para sumar dos fracciones.

.. code-block:: pycon

    >>> class Punto:
    ...     def __init__(self, x=0, y=0):
    ...         """Método Constructor"""
    ...         self.x = x
    ...         self.y = y
    ...     def __add__(self, other):
    ...         """Método para sobrecargar el operador +"""
    ...         x = self.x + other.x
    ...         y = self.y + other.y
    ...         return x, y
    ...
    >>>


Crear instancias de objetos para dos puntos:

.. code-block:: pycon

    >>> punto1 = Punto(4, 6)
    >>> punto2 = Punto(1, -2)
    >>>


Sumar los puntos usando el operador :ref:`+ <python_opers_arit_suma>`:

.. code-block:: pycon

    >>> print(punto1 + punto2)
    (5, 4)
    >>>


.. _python_overriding_methods:

Sobrecarga de métodos
.....................

La *sobrecarga de métodos* es también es conocida por *Overriding Methods*,
le permite sustituir un método proveniente de la Clase Base, en la Clase
Derivada debe definir un método con la **misma forma** (es decir, mismo
nombre de método y mismo número de parámetros que como está definido en la
Clase Base).

.. code-block:: pycon

    >>> class Persona:
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
    >>>


Crear instancia de objeto para un obrero de planta:

.. code-block:: pycon

    >>> obrero_planta = Obrero()
    >>>


Llamar al método ``mensaje`` del objeto creado:

.. code-block:: pycon

    >>> obrero_planta.mensaje()
    mensaje desde la clase Obrero
    >>>


Lo que se logra definiendo el método ``mensaje()`` en la Clase Derivada
(``Obrero``) se conoce como **Método Overriding** (cuando se cree el objeto
(en este caso ``obrero_planta`` y se llame al método ``mensaje()``, este será
tomado de la propia clase y no de la Clase Base ``Persona``). Si **comenta
o borra** el método ``mensaje()`` de la clase ``Obrero`` (Clase Derivada)
y corre nuevamente el código, el método llamado será el ``mensaje()`` de la
Clase Base ``Persona``.


.. _python_overriding_subtype_polymorphism:

Polimorfismo de subtipos
........................

Python permite que una clase herede de otra clase y redefina sus métodos.
Esto se llama polimorfismo de subtipos o dinámico, ya que el método a
invocar se determina en tiempo de ejecución según el tipo del objeto.
Por ejemplo, podemos crear una clase ``Animal`` que tiene un método ``hablar`` y
dos subclases ``Perro`` y ``Gato`` que heredan de ``Animal`` y redefinen el método
``hablar``.

.. code-block:: pycon

    >>> class Animal:
    ...     # Constructor
    ...     def __init__(self, nombre):
    ...         self.nombre = nombre
    ...     # Método para hablar
    ...     def hablar(self):
    ...         print(f"Soy un animal. Me llamo {self.nombre}.")
    ...
    >>> class Perro(Animal):
    ...     # Método para hablar
    ...     def hablar(self):
    ...         print(f"Soy un perro. Me llamo {self.nombre}. Guau.")
    ...
    >>> class Gato(Animal):
    ...     # Método para hablar
    ...     def hablar(self):
    ...         print(f"Soy un gato. Me llamo {self.nombre}. Miau.")
    ...
    >>>


Crear instancia de objetos para un animal, un perro y un gato:

.. code-block:: pycon

    >>> a = Animal("Lola")
    >>> p = Perro("Firulais")
    >>> g = Gato("Pelusa")
    >>>


Llamar al método ``hablar`` de cada objeto, este muestra los siguientes mensajes:

.. code-block:: pycon

    >>> a.hablar()
    Soy un animal. Me llamo Lola.
    >>> p.hablar()
    Soy un perro. Me llamo Firulais. Guau.
    >>> g.hablar()
    Soy un gato. Me llamo Pelusa. Miau.
    >>>

----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion9>`
    del entrenamiento para ampliar su conocimiento en esta temática.


----


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html

..
  .. disqus::

.. _`Overloading Operators`: https://en.wikipedia.org/wiki/Operator_overloading
