"""Ejemplo del Tipos de datos booleanos"""

print("\nTipos de datos booleanos")
print("========================\n")

aT, aF = True, False
print(f"El valor es {aT} de tipo: {type(aT)}\n")
print(f"El valor es {aF} de tipo: {type(aF)}")

print("\nOperadores booleanos")
print("====================\n")

# Operadores booleanos
aAnd = True and False
print(f"SI es Verdadero Y Falso, es {aAnd} de {type(aAnd)}\n")
aOr = True or False
print(f"SI es Verdadero O Falso, es {aOr} de {type(aOr)}\n")
aNot = not True
print(f"Si NO es Verdadero, es {aNot} de {type(aNot)}\n")
