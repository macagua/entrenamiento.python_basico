.. -*- coding: utf-8 -*-


.. _python_poo_abstraccion:

Abstracción
-----------

El concepto de encapsulamiento se apoya sobre el concepto de abstracción.

En :ref:`POO <python_poo>` solo necesita saber como interaccionar con los 
objetos, no necesita conocer los detalles de cómo está implementada la clase 
a partir de la cual se instancia el objeto. Sólo necesita conocer su interfaz 
pública.

La encapsulación es una forma de abstracción, ademas es un mecanismo para 
llevar a la práctica la abstracción.

El nivel de abstracción puede ser bajo (en un objeto se manipulan datos y 
métodos individualmente), o alto (en un objeto solo se usan sus métodos de 
servicio).


.. _python_poo_encapsulacion:

Encapsulación
.............

La encapsulación se considera una de las características definitorias de la 
:ref:`POO <python_poo>`.

Cuando una clase existe (se define), se crean objetos a partir de ella, y se 
usan dichos objetos invocando los métodos necesarios. Es decir, crea objetos 
para usar los servicios que nos proporciona la clase a través de sus métodos.

No necesita saber cómo trabaja el objeto, ni saber las variables que usa, ni 
el código que contiene.

El objeto es una *caja negra*. --> Modelo cliente - servidor. Es decir, el objeto 
es un servidor que proporciona servicios a los clientes que lo solicitan.

La encapsulación describe el hecho de que los objetos se usan como *cajas negras*. 
Así, un objeto encapsula datos y métodos, que están dentro del objeto.

**Interfaz pública de una clase:** Es el conjunto de métodos (métodos de servicio) 
que sirve para que los objetos de una clase proporcionen sus servicios. Estos 
servicios son los que pueden ser invocados por un cliente.

**Métodos de soporte:** Son métodos adicionales en un objeto que no definen un servicio 
utilizable por un cliente, pero que ayudan a otros métodos en sus tareas.

La encapsulación es un **mecanismo de control**. El estado (el conjunto de propiedades, 
atributos ó datos) de un objeto sólo debe ser modificado por medio de los métodos 
del propio objeto.

La técnica de encapsulación, es conocida como ocultación de datos, le permite que 
los atributos de un objeto pueden ocultarse (superficialmente) para que no sean 
accedidos desde fuera de la definición de una clase. Para ello, es necesario nombrar 
los atributos con un prefijo de doble subrayado: ``__atributo``.

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

.. todo::
    TODO terminar de escribir esta sección


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion9>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
