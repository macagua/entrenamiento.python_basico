# Importar el modulo llamado "utilidades"
import utilidades

print(
    "Importo el modulo '{}'\n".format(
        utilidades.__file__.replace(utilidades.__file__, "utilidades.pyc")
    )
)

print(
    "Función '{}' del módulo '{}' llamado y mostró:".format(
        utilidades.suma_total.__name__,
        utilidades.__file__.replace(utilidades.__file__, "utilidades.pyc"),
    )
)

# Usted puede llamar una función definida dentro del módulo
print(
    "Monto total a facturar: {} Bs (VES).".format(
        utilidades.suma_total(int(input("Ingrese un monto: ")))
    )
)
