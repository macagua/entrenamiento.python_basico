"""El diccionario define una relación uno a uno entre claves y valores."""

datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}
print (datos_basicos, type(datos_basicos))

print ("\nDetalle del diccionario")
print ("=======================")

print ("\nClaves de diccionario:", datos_basicos.keys())
print ("\nValores de diccionario:", datos_basicos.values())
print ("\nElementos de diccionario:", datos_basicos.items())

print ("\nDetalle del diccionario con iteritems()")
print ("=======================================")

for key, value in iter(datos_basicos.items()):
    print('Clave: %s, tiene el valor: %s' % (key, value))

# Ejemplo practico de los diccionarios
print ("\n\nInscripción de Curso")
print ("====================")

print ("\nDatos de participante")
print ("---------------------")

print ("Cédula de identidad: ", datos_basicos['cedula'])
print ("Nombre completo: " + datos_basicos['nombres'] + " " + \
datos_basicos['apellidos'])
import datetime, locale, os
locale.setlocale(locale.LC_ALL, os.environ['LANG'])
print ("Fecha y lugar de nacimiento:", datetime.datetime.strftime(
    datetime.datetime.strptime(
        datos_basicos['fecha_nacimiento'], '%d/%m/%Y'
    ), "%d de %B de %Y"
) + " en " + datos_basicos['lugar_nacimiento'] + ".")
print ("Nacionalidad:", datos_basicos['nacionalidad'])
print ("Estado civil:", datos_basicos['estado_civil'])

