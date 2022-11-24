""" Operadores lógicos """

datos_basicos = {
    "nombres": "Leonardo Jose",
    "apellidos": "Caballero Garcia",
    "cedula": "26938401",
    "fecha_nacimiento": "03/12/1980",
    "lugar_nacimiento": "Maracaibo, Zulia, Venezuela",
    "nacionalidad": "Venezolana",
    "estado_civil": "Soltero",
}
print("Valor de variable 'datos_basicos':", datos_basicos)

# Operador in
print("\nOperador in")
print("===========")

print("\nOperador in en tipo cadena de caracteres")
print("========================================")
print("Maracaibo" in datos_basicos["lugar_nacimiento"])

print("\nOperador in en tipo lista")
print("=========================")
print("Venezolana" in list(datos_basicos.values()))

print("\nOperador in en tipo tupla")
print("=========================")
print("26938401" in tuple(datos_basicos.values()))

print("\nOperador in en tipo diccionario")
print("===============================")
print("Soltero" in datos_basicos.values())

# Operador not in
print("\nOperador not in")
print("===============")

print("\nOperador not in en tipo cadena de caracteres")
print("============================================")
print("Merida" not in datos_basicos["lugar_nacimiento"])

print("\nOperador not in en tipo lista")
print("=============================")
print("Venezuela" not in list(datos_basicos.values()))

print("\nOperador not in en tipo tupla")
print("=============================")
print("26938402" not in tuple(datos_basicos.values()))

print("\nOperador not in en tipo diccionario")
print("===================================")
print("Soltera" not in datos_basicos.values())
