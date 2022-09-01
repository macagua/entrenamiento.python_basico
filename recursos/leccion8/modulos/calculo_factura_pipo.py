# Importar el modulo llamado "utilidades"
import utilidades

print("Importo el modulo '{0}'\n".format(
    utilidades.__file__.replace(
        utilidades.__file__, "utilidades.pyc")))

print("Función '{0}' del módulo '{1}' llamado y mostró:".format(
    utilidades.suma_total.__name__,
    utilidades.__file__.replace(
        utilidades.__file__, "utilidades.pyc")))

# Usted puede llamar una función definida dentro del módulo
print("Monto total a facturar: {0} BsS.".format(
    utilidades.suma_total(int(input("Ingrese un monto: ")))))
