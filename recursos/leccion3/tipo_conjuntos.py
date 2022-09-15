"""
    Un conjunto, es una colección no ordenada y sin elementos repetidos.
    Los usos básicos de éstos incluyen verificación de pertenencia y
    eliminación de entradas duplicadas.
"""

# crea un conjunto sin valores repetidos y lo asigna la variable
para_comer = {"pastel", "tequeno", "papa", "empanada", "mandoca"}
print(para_comer, type(para_comer))
para_tomar = {"refresco", "malta", "jugo", "cafe"}
print(para_tomar, type(para_tomar))

# usa operaciones condicionales con operador in
hay_tequeno = "tequeno" in para_comer
hay_fresco = "refresco" in para_tomar

print("\nTostadas A que Pipo!")
print("====================")

# valida si un elemento esta en el conjunto
print("Tenéis tequeno?:", "tequeno" in para_comer)

# valida si un elemento esta en el conjunto
print("Tenéis pa' tomar fresco?:", "refresco" in para_tomar)

if hay_tequeno and hay_fresco:
    print("Desayuno vergatario!!!")
else:
    print("Desayuno ligero")
