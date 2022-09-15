"""
    El fuertemente tipado significa que el tipo de valor no
    cambia repentinamente. Una cadena que contiene solo dígitos
    no se convierte mágicamente en un número. Cada cambio de tipo
    requiere una conversión explícita.

    >>> valor1, valor2 = 2, "5"
    >>> total = valor1 + valor2
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>> total = valor1 + int(valor2)
    >>> print("El total es: " + str(total))
    7
"""

# varible "valor1" guarda un valor entero, varible "valor2" guarda un valor cadena
valor1, valor2 = 2, "5"
# se usa el metodo int() para convertir a entero
total = valor1 + int(valor2)
# se usa el metodo str() para convertir a cadena
print("El total es: " + str(total))
