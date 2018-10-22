# -*- coding: utf8 -*-

"""
    Una tupla es una lista inmutable. Una tupla no puede 
    modificarse de ningún modo después de su creación.
"""

# Ejemplo simple de tupla
tupla = 12345, 54321, 'hola!'

# Ejemplo de tuplas anidadas
otra = tupla, (1, 2, 3, 4, 5)

# operación asignación de valores de una tupla en variables
x, y, z = tupla


print "\nDefiniendo conexión a BD MySQL"
print "==============================\n"

conexion_bd = "127.0.0.1","root","qwerty","nomina",
print "Conexión típica:", conexion_bd
print type(conexion_bd)
conexion_completa = conexion_bd, "3307","10",
print "\nConexión con parámetros adicionales:", conexion_completa
print type(conexion_completa)

print "\n"

print "IP de la BD:",  conexion_completa[0][0]
print "Usuario de la BD:",  conexion_completa[0][1]
print "Contraseña de la BD:",  conexion_completa[0][2]
print "Nombre de la BD:",  conexion_completa[0][3]
print "Puerto de conexión:", conexion_completa[1]
print "Tiempo de espera en conexión:", conexion_completa[2]

print """\nMás información acerca de MySQL y Python \
http://mysql-python.sf.net/MySQLdb.html\n"""

print "\nIterar tupla con función enumerate"
print "==================================\n"

for index, item in enumerate(conexion_completa):
    print index, item
