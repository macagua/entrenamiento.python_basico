from utilidades import calculos, impuestos

monto = int(input("Introduzca un monto entero: "))
impuesto = int(input("Introduzca un numero del impuesto: "))
# Llama función definida en el módulo "impuestos"
print(f"El impuesto IVA de {impuesto}%: {impuestos.impuesto_iva(monto, impuesto)}")

suma = int(input("Introduzca un monto entero a sumar: "))
# Llama función definida en el módulo "calculos"
print("La suma total es:", calculos.suma_total(suma))
