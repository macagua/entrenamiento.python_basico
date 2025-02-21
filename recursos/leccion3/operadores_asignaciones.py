"""Operadores de asignaciones"""

a, b, c = 21, 10, 0

print(f"Valor de variable 'a':", a)
print(f"Valor de variable 'b':", b)

c = a + b
print(f"Operador = | El valor de variable 'c' es {c}")

c += a
print(f"Operador += | El valor de variable 'c' es {c}")

c *= a
print(f"Operador *= | El valor de variable 'c' es {c}")

c /= a
print(f"Operador /= | El valor de variable 'c' es {c}")

c = 2
c %= a
print(f"Operador %= | El valor de variable 'c' es {c}")

c **= a
print(f"Operador **= | El valor de variable 'c' es {c}")

c //= a
print(f"Operador //= | El valor de variable 'c' es {c}")
