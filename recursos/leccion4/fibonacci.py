""" Módulo de Sucesión de números Fibonacci.
Más información en https://es.wikipedia.org/wiki/Sucesión_de_Fibonacci """

a, b = 0, 1
while b < 100:
    print(
        b,
    )
    a, b = b, a + b
