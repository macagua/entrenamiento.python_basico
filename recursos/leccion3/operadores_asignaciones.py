""" Operadores de asignaciones """

a, b, c = 21, 10, 0

print("Valor de variable 'a':", a)
print("Valor de variable 'b':", b)

c = a + b
print("Operador = | El valor de variable 'c' es ", c)

c += a
print("Operador += | El valor de variable 'c' es ", c)

c *= a
print("Operador *= | El valor de variable 'c' es ", c)

c /= a
print("Operador /= | El valor de variable 'c' es ", c)

c = 2
c %= a
print("Operador %= | El valor de variable 'c' es ", c)

c **= a
print("Operador **= | El valor de variable 'c' es ", c)

c //= a
print("Operador //= | El valor de variable 'c' es ", c)
