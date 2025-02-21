"""El diccionario define una relación uno a uno entre claves y valores."""

# Definir un diccionario
datos_basicos = {
    "nombres": "Leonardo Jose",
    "apellidos": "Caballero Garcia",
    "cedula": "26938401",
    "fecha_nacimiento": "03/12/1980",
    "lugar_nacimiento": "Maracaibo, Zulia, Venezuela",
    "nacionalidad": "Venezolana",
    "estado_civil": "Soltero",
}
print(datos_basicos, type(datos_basicos))

print("\nDetalle del diccionario")
print("=======================")

print(f"\nClaves de diccionario: {datos_basicos.keys()}")
print(f"\nValores de diccionario: {datos_basicos.values()}")
print(f"\nElementos de diccionario: {datos_basicos.items()}")

print("\nDetalle del diccionario con iteritems()")
print("=======================================")

for key, value in iter(datos_basicos.items()):
    print(f"Clave: {key}, tiene el valor: {value}")

# Ejemplo practico de los diccionarios
print("\n\nInscripción de Curso")
print("====================")

print("\nDatos de participante")
print("---------------------")

print(f"Cédula de identidad: {datos_basicos['cedula']}")
print(f"Nombre completo: {datos_basicos['nombres']} {datos_basicos['apellidos']}")
import datetime, locale, os

fecha_nacimiento = datetime.datetime.strftime(
    datetime.datetime.strptime(datos_basicos["fecha_nacimiento"], "%d/%m/%Y"),
    "%d de %B de %Y",
)
locale.setlocale(locale.LC_ALL, os.environ["LANG"])
print(f"Fecha y lugar de nacimiento: {fecha_nacimiento} en {datos_basicos['lugar_nacimiento']}.")
print(f"Nacionalidad: {datos_basicos['nacionalidad']}")
print(f"Estado civil: {datos_basicos['estado_civil']}")
