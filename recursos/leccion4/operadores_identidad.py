""" Operadores de identidad """

# Operador is
print("\nOperador is")
print("===========")

monto_inicial = 200
monto_final = 200
print(monto_inicial is monto_final)
print(
    "{monto_inicial} su id es {monto_inicial_id}".format(
        monto_inicial=monto_inicial, monto_inicial_id=id(monto_inicial)
    )
)
print(
    "{monto_final} su id es {monto_final_id}".format(
        monto_final=monto_final, monto_final_id=id(monto_final)
    )
)
monto_final = 200.0
print(monto_inicial is monto_final)
print(
    "{monto_inicial} su id es {monto_inicial_id}".format(
        monto_inicial=monto_inicial, monto_inicial_id=id(monto_inicial)
    )
)
print(
    "{monto_final} su id es {monto_final_id}".format(
        monto_final=monto_final, monto_final_id=id(monto_final)
    )
)


# Operador is not
print("\nOperador is not")
print("===============")

print(
    "Python crea dos objetos diferentes, uno para cada lista. Las listas son mutables."
)
lista = [1, 2, 3]
lista_alterna = [1, 2, 3]
print(lista is not lista_alterna)
print(f"{lista} su id es {id(lista)}")
print(
    "{lista_alterna} su id es {lista_alterna_id}".format(
        lista_alterna=lista_alterna, lista_alterna_id=id(lista_alterna)
    )
)

print(
    "Python reutiliza el objeto que almacena 5 por lo que ambas variables apuntan a el mismo."
)
monto_inicial = 200
monto_final = 200
print(monto_inicial is not monto_final)
print(
    "{monto_inicial} su id es {monto_inicial_id}".format(
        monto_inicial=monto_inicial, monto_inicial_id=id(monto_inicial)
    )
)
print(
    "{monto_final} su id es {monto_final_id}".format(
        monto_final=monto_final, monto_final_id=id(monto_final)
    )
)