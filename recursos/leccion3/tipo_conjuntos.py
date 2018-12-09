# -*- coding: utf8 -*-

"""
    Un conjunto, es una colección no ordenada y sin elementos repetidos. 
    Los usos básicos de éstos incluyen verificación de pertenencia y 
    eliminación de entradas duplicadas.
"""

# crea un conjunto sin repetidos
plato = ['pastel', 'tequeno', 'papa', 'empanada', 'mandoca']
print plato, type(plato)
bebida = ['refresco', 'malta', 'jugo', 'cafe']
print bebida, type(bebida)

# establece un conjunto a una variable
para_comer = set(plato)
print para_comer, type(para_comer)

para_tomar = set(bebida)
print para_tomar, type(para_tomar)

# Ejemplo practico de los condicionales
hay_tequeno = 'tequeno' in para_comer
hay_fresco = 'refresco' in para_tomar

print "\nTostadas A que Pipo!"
print "===================="

# valida si un elemento esta en el conjunto
print "Tenéis tequeno?: ", 'tequeno' in para_comer

# valida si un elemento esta en el conjunto
print "Tenéis pa' tomar fresco?: ", 'refresco' in para_tomar

if (hay_tequeno and hay_fresco):
	print "Desayuno vergatario"
else:
    print "Desayuno ligero"
