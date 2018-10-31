.. -*- coding: utf-8 -*-


.. _python_programacion_estructurada:

Programación estructurada
-------------------------

La programación estructurada es un paradigma de programación basado en utilizar 
:ref:`funciones <python_funciones>` o subrutinas, y únicamente tres estructuras 
de control:

- secuencia: ejecución de una instrucción tras otra.

- selección o condicional: ejecución de una instrucción o conjunto de instrucciones, 
  según el valor de una variable booleana.

- iteración (ciclo o bucle): ejecución de una instrucción o conjunto de instrucciones, 
  mientras una variable booleana sea verdadera.

Este paradigma se fundamente en el teorema correspondiente, que establece que toda 
función computable puede ser implementada en un lenguaje de programación que combine 
sólo estas tres estructuras lógicas o de control.

La estructura de secuencia es la que se da naturalmente en el lenguaje, ya que por 
defecto las sentencias son ejecutadas en el orden en que aparecen escritas en el programa.

Para las estructuras condicionales o de selección, Python dispone de la instrucción 
:ref:`if <python_condicional_if>`, que puede combinarse con instrucciones ``elif`` y/o ``else``.

Para los bucles o iteraciones existen las estructuras :ref:`while <python_bucle_while>` 
y :ref:`for <python_bucle_for>`.


Ventajas de la programación estructurada
........................................

Entre las ventajas de la programación estructurada sobre el modelo anterior (hoy 
llamado despectivamente *código espagueti*), cabe citar las siguientes:

- Los programas son más fáciles de entender, pueden ser leídos de forma secuencial y 
  no hay necesidad de tener que rastrear saltos de líneas (GOTO) dentro de los bloques 
  de código para intentar entender la lógica interna.

- La estructura de los programas es clara, puesto que las instrucciones están más ligadas 
  o relacionadas entre sí.

- Se optimiza el esfuerzo en las fases de pruebas y depuración. El seguimiento de los 
  fallos o errores del programa (debugging), y con él su detección y corrección, se 
  facilita enormemente.

- Se reducen los costos de mantenimiento. Análogamente a la depuración, durante la fase 
  de mantenimiento, modificar o extender los programas resulta más fácil.

- Los programas son más sencillos y más rápidos de confeccionar.

- Se incrementa el rendimiento de los programadores.


.. todo::
    TODO terminar de escribir esta sección

.. _`Reusing code: scripts and modules - Scipy lecture notes`: https://www.pybonacci.org/scipy-lecture-notes-ES/intro/language/reusing_code.html
.. _`Programación estructurada`: https://es.wikipedia.org/wiki/Programación_estructurada
.. _`Paseo por la programación estructurada y modular con Python - Rosalía Peña Ros`: http://www.aenui.net/ojs/index.php?journal=revision&page=article&op=viewArticle&path%5B%5D=184
