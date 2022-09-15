from tostadas_pipo.utilidades import calculos
from tostadas_pipo.utilidades.impuestos import impuesto_iva14

monto = int(input("Introduzca un monto entero: "))
monto_suma = int(input("Introduzca un monto entero a sumar: "))

suma = impuesto_iva14(monto) + calculos.suma_total(monto_suma)

print(f"Total a Facturar: {suma} Bs (VES), con IVA 14%.")
