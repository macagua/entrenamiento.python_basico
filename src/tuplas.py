# -*- coding: utf8 -*-

"""
    Una tupla es una lista inmutable. Una tupla no puede 
    modificarse de ningún modo después de su creación.
"""

# Ejemplo simple de tupla
tupla = 12345, 54321, 'hola!'

# Ejemplo de tuplas anidadas
otra = tupla, (1, 2, 3, 4, 5)

# operación asinacion de valores de una tupla en variables
x, y, z = tupla


print "\nDefiniendo conexion a BD MySql"
print "==============================\n"

conexion_bd = "127.0.0.1","root","123456","nomina",
print "Conexion tipica:", conexion_bd
print type(conexion_bd)
conexion_completa = conexion_bd, "3307","10",
print "\nConexion con parametros adicionales:", conexion_completa
print type(conexion_completa)

print "\n"

print "Acceder a la IP de la bd:",  conexion_completa[0][0]
print "Acceder al usuario de la bd:",  conexion_completa[0][1]
print "Acceder a la clave de la bd:",  conexion_completa[0][2]
print "Acceder al nombre de la bd:",  conexion_completa[0][3]
print "Acceder al puerto de conexion:", conexion_completa[1]
print "Acceder al tiempo de espera de conexion:", conexion_completa[2]

print "\nMas informacion sobre Mysql y Python http://mysql-python.sourceforge.net/MySQLdb.html"