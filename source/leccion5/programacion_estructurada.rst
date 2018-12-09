.. -*- coding: utf-8 -*-


.. _python_programacion_estructurada:

Programación estructurada
-------------------------

La programación estructurada es un paradigma de programación basado en utilizar 
:ref:`funciones <python_funciones>` o subrutinas, y únicamente tres estructuras 
de control:

- secuencia: ejecución de una sentencia tras otra.

- selección o condicional: ejecución de una sentencia o conjunto de sentencias, 
  según el valor de una variable booleana.

- iteración (ciclo o bucle): ejecución de una sentencia o conjunto de sentencias, 
  mientras una variable booleana sea verdadera.

Este paradigma se fundamente en el teorema correspondiente, que establece que toda 
función computable puede ser implementada en un lenguaje de programación que combine 
sólo estas tres estructuras lógicas o de control.

La estructura de secuencia es la que se da naturalmente en el lenguaje, ya que por 
defecto las sentencias son ejecutadas en el orden en que aparecen escritas en el 
programa.

Para las estructuras condicionales o de selección, Python dispone de la sentencia 
:ref:`if <python_sent_if>`, que puede combinarse con sentencias :ref:`elif <python_sent_elif>` 
y/o :ref:`else <python_sent_else>`.

Para los bucles o iteraciones existen las estructuras :ref:`while <python_bucle_while>` 
y :ref:`for <python_bucle_for>`.


Ventajas del paradigma
......................

Entre las ventajas de la programación estructurada sobre el modelo anterior (hoy 
llamado despectivamente *código espagueti*), cabe citar las siguientes:

- Los programas son más fáciles de entender, pueden ser leídos de forma secuencial 
  y no hay necesidad de tener que rastrear saltos de líneas (GOTO) dentro de los 
  bloques de código para intentar entender la lógica interna.

- La estructura de los programas es clara, puesto que las sentencias están más 
  ligadas o relacionadas entre sí.

- Se optimiza el esfuerzo en las fases de pruebas y depuración. El seguimiento de 
  los fallos o errores del programa (debugging), y con él su detección y corrección, 
  se facilita enormemente.

- Se reducen los costos de mantenimiento. Análogamente a la depuración, durante la 
  fase de mantenimiento, modificar o extender los programas resulta más fácil.

- Los programas son más sencillos y más rápidos de confeccionar.

- Se incrementa el rendimiento de los programadores.

.. important::

	Seguidamente se presenta el concepto de funciones poniendo en practica forma de 
	secuencia, implementado las estructuras condicionales :ref:`if <python_condi_if>` 
	y los bucles o iteraciones existen :ref:`while <python_bucle_while>` y 
	:ref:`for <python_bucle_for>`.


----


.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_suplementarias_sesion5>` 
    del entrenamiento para ampliar su conocimiento en esta temática.
