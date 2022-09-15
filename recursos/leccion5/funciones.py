""" Funciones en Python """


def iva():
    """Función básica para el calculo del IVA"""
    iva = 12
    costo = int(input("¿Cual es el monto a calcular?: "))
    calculo = costo * iva / 100
    print("El calculo de IVA es: " + str(calculo) + "\n")


def suma(numero1, numero2):
    """Función la cual suma dos números"""
    print(str(numero1 + numero2) + "\n")


# def imprime_fibonacci(n):
#    """ Escribe la sucesión Fibonacci hasta n """
#    a, b = 0, 1
#    while b < n:
#        print(b,)
#        a, b = b, a + b


def devuelve_fibonacci(n):
    """Devuelve la sucesión Fibonacci hasta n"""
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a + b
    return resultado


mensaje = "Calcular el IVA de un monto"
print(mensaje)
print("=" * len(mensaje))
iva()

mensaje1 = "Suma de dos números"
print(mensaje1)
print("=" * len(mensaje1))
suma(13, 37)

mensaje2 = "Sucesión de Fibonacci"
print(mensaje2)
print("=" * len(mensaje2))

# print("La sucesión Fibonacci hasta 10 es:", imprime_fibonacci(10))
# print("\nLa sucesión Fibonacci hasta 50 es:", devuelve_fibonacci(50))
print("La sucesión Fibonacci hasta 50 es:", devuelve_fibonacci(50))
