"""Ejemplo de uso del condicional 'if' usando operadores relacionales"""

dato1, dato2, dato3, dato4 = 21, 10, 5, 20

print(f"Valor de variable 'dato1': {dato1}")
print(f"Valor de variable 'dato2': {dato2}")
print(f"Valor de variable 'dato3': {dato3}")
print(f"Valor de variable 'dato4': {dato4}")

# Operador de comparación Igual
if dato1 == dato2:
    print("'dato1' y 'dato2' son iguales.")
else:
    print("'dato1' y 'dato2' no son iguales.")

# Operador de comparación Distinto/Diferente
if dato1 != dato2:
    print("'dato1' y 'dato2' son distintas/diferentes.")
else:
    print("'dato1' y 'dato2' no son distintas/diferentes.")

# Operador de comparación Menor que
if dato1 < dato2:
    print("'dato1' es menor que 'dato2'.")
else:
    print("'dato1' no es menor que 'dato2'.")

# Operador de comparación Mayor que
if dato1 > dato2:
    print("'dato1' es mayor que 'dato2'.")
else:
    print("'dato1' no es mayor que 'dato2'.")

# Operador de comparación Menor o igual que
if dato3 <= dato4:
    print("'dato3' es menor o igual que 'dato4'.")
else:
    print("'dato3' no es menor o igual que 'dato4'.")

# Operador de comparación Mayor o igual que
if dato4 >= dato3:
    print("'dato4' es mayor o igual que 'dato3'.")
else:
    print("'dato4' no es mayor o igual que 'dato3'.")


# Ejemplo completo de condicional if / elif / else
numero = int(input("\nIngresa un número entero, por favor: "))

if numero < 0:
    numero = 0
    print("El número ingresado es negativo cambiado a cero.\n")
elif numero == 0:
    print("El número ingresado es 0.\n")
elif numero == 1:
    print("El número ingresado es 1.\n")
else:
    print("El número ingresado es mayor que uno.\n")
