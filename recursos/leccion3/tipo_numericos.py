# -*- coding: utf8 -*-
"""Ejemplo del uso del numero enteros"""

# Entero int
entero = 7
print entero, type(entero)

# Entero long
entero_long = 7L
print entero_long, type(entero_long)

# Coma flotante o reales simple
float_1, float_2, float_3 = 0.348, 10.5, 1.5e2
print float_1, type(float_1)
print float_2, type(float_2)
print float_3, type(float_3)

# Este número tiene un exponente en base 10
# es decir, multiplicado por 10 a la N
real = 0.56e-3
print real, type(real)

# Este número es de tipo Complex
complejo = 3.14j
print complejo, complejo.imag, complejo.real, type(complejo)
