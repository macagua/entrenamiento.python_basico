# Importar el modulo llamado "utilidades"
import utilidades

print(
    f"Importo el modulo '{utilidades.__file__.replace(utilidades.__file__, 'utilidades.pyc')}'\n"
)

print(
    f"Función '{utilidades.suma_total.__name__}' del módulo '{utilidades.__file__.replace(utilidades.__file__, 'utilidades.pyc')}' llamado y mostró:"
)

# Usted puede llamar una función definida dentro del módulo
print(
    f"Monto total a facturar: {utilidades.suma_total(int(input('Ingrese un monto: ')))} Bs (VES)."
)
