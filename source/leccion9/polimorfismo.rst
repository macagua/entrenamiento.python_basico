.. -*- coding: utf-8 -*-


.. _python_poo_polimorfismo:

Polimorfismo
------------

La técnica de polimorfismo de la :ref:`POO <python_poo>` significa la 
capacidad de tomar más de una forma. Una operación puede presentar diferentes 
comportamientos en diferentes instancias. El comportamiento depende de los 
tipos de datos utilizados en la operación. El polimorfismo es ampliamente 
utilizado en la aplicación de la herencia.

.. todo::
    TODO escribir esta sección


.. _python_overriding_methods:

Sobrecarga de métodos
.....................

La *sobrecarga de métodos* es también es conocida por *Overriding Methods*, 
le permite sustituir un método proveniente de la Clase Base, en la Clase 
Derivada debe definir un método con la **misma forma** (es decir, mismo 
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
tomado de la propia clase y no de la Clase Base ``Persona``). Si **comenta 
o borra** el método ``mensaje()`` de la clase ``Obrero`` (Clase Derivada) 
y corre nuevamente el código, el método llamado será el ``mensaje()`` de la 
Clase Base ``Persona``.


.. _python_overloading_operators:

Sobrecarga de Operadores
........................

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


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lectura_extras_sesion9>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
