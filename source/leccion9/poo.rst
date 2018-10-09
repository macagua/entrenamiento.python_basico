.. -*- coding: utf-8 -*-

Programación orientada a objetos
================================

El mecanismo de clases de Python agrega clases al lenguaje con un mínimo de
nuevas sintaxis y semánticas.  Es una mezcla de los mecanismos de clase
encontrados en C++ y Modula-3.  Como es cierto para los módulos, las clases en
Python no ponen una barrera absoluta entre la definición y el usuario, sino que
más bien se apoya en la cortesía del usuario de no "forzar la definición".  Sin
embargo, se mantiene el poder completo de las características más importantes
de las clases: el mecanismo de la herencia de clases permite múltiples clases
base, una clase derivada puede sobreescribir cualquier método de su(s) clase(s)
base, y un método puede llamar al método de la clase base con el mismo nombre.
Los objetos pueden tener una cantidad arbitraria de datos.

En terminología de C++, todos los miembros de las clases (incluyendo los
miembros de datos), son *públicos*, y todas las funciones miembro son
*virtuales*.  Como en Modula-3, no hay atajos para hacer referencia a los
miembros del objeto desde sus métodos: la función método se declara con un
primer argumento explícito que representa al objeto, el cual se provee
implícitamente por la llamada.  Como en Smalltalk, las clases mismas son
objetos.  Esto provee una semántica para importar y renombrar.  A diferencia
de C++ y Modula-3, los tipos de datos integrados pueden usarse como clases
base para que el usuario los extienda.  También, como en C++ pero a
diferencia de Modula-3, la mayoría de los operadores integrados con
sintaxis especial (operadores aritméticos, de subíndice, etc.) pueden ser
redefinidos por instancias de la clase.

(Sin haber una terminología universalmente aceptada sobre clases, haré uso
ocasional de términos de Smalltalk y C++.  Usaría términos de Modula-3, ya que
su semántica orientada a objetos es más cercana a Python que C++, pero no
espero que muchos lectores hayan escuchado hablar de él).

Ejemplo de POO
..............

Ejemplo de la clase Persona: ::

    class Persona:

            def __init__(self):
                print "soy un nuevo objeto"

Ejemplo de la clase Persona con funcion interna:

.. literalinclude:: ../../recursos/leccion9/clases.py
    :linenos:
    :language: python
    :lines: 1-8

Vídeo tutorial
--------------

- `Tutorial Python 13 - Clases y Objetos`_.


Referencia
----------

- `Clases — Tutorial de Python v2.7.0`_.
 
.. _`Tutorial Python 13 - Clases y Objetos`: https://www.youtube.com/watch?v=VYXdpjCZojA
.. _`Clases — Tutorial de Python v2.7.0`: http://docs.python.org.ar/tutorial/2/classes.html
