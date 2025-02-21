"""Una tupla es una lista inmutable. Una tupla no puede
modificarse de ningún modo después de su creación.
"""

# Ejemplo simple de tupla
tupla = 12345, 54321, "hola!"

# Ejemplo de tuplas anidadas
otra = tupla, (1, 2, 3, 4, 5)

# Operación asignación de valores de una tupla en variables
x, y, z = tupla

print("Definiendo conexión a BD MySQL")
print("==============================\n")

conexion_bd = (
    "127.0.0.1",
    "root",
    "qwerty",
    "nomina",
)
print(f"Conexión típica: {conexion_bd}, {type(conexion_bd)}")

conexion_completa = (
    conexion_bd,
    "3307",
    "10",
)
print(
    f"\nConexión con parámetros adicionales: {conexion_completa}, {type(conexion_completa)}\n",
)

print(f"IP de la BD: {conexion_completa[0][0]}")
print(f"Usuario de la BD: {conexion_completa[0][1]}")
print(f"Contraseña de la BD: {conexion_completa[0][2]}")
print(f"Nombre de la BD: {conexion_completa[0][3]}")
print(f"Puerto de conexión: {conexion_completa[1]}")
print(f"Tiempo de espera en conexión: {conexion_completa[2]}")

print(
    """\nMás información acerca de MySQL y Python \
https://pymysql.readthedocs.io/en/latest/"""
)

print("\nIterar tupla con función enumerate")
print("==================================\n")

for index, item in enumerate(conexion_completa):
    print(index, item)
