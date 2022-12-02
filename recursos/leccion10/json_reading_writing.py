""" Programa para leer y escribir un archivo JSON """

import json
import logging
import os

logging.basicConfig(level=logging.INFO)

NOMBRE_ARCHIVO = "json_reading_writing.json"
DIR_ARCHIVO = os.path.dirname(os.path.abspath(__file__)) + os.sep
ARCHIVO = DIR_ARCHIVO + NOMBRE_ARCHIVO

# Data a escribir
DATA = {
    "clientes": [
        {
            "nombre": "Leonardo",
            "apellido": "Caballero",
            "codigo_postal": "5001",
            "telefono": "+58-412-4734567",
        },
        {
            "nombre": "Ana",
            "apellido": "Poleo",
            "codigo_postal": "6302",
            "telefono": "+58-426-5831297",
        },
        {
            "nombre": "Pedro",
            "apellido": "Lopez",
            "codigo_postal": "4001",
            "telefono": "+58-414-2360943",
        },
    ]
}

print(DATA, type(DATA), "\n")

# Abriendo archivo JSON para escribir un tipo diccionario
with open(ARCHIVO, "w") as archivo_json:
    json.dump(DATA, archivo_json)
    logging.info("Se escribió un tipo diccionario en archivo JSON\n")

# Abriendo archivo JSON
with open(ARCHIVO) as archivo_json:
    # Leyendo desde archivo JSON
    data = json.load(archivo_json)
    logging.info("Se leyó desde archivo JSON\n")
    for cliente in data["clientes"]:
        print(f"Nombre:", cliente["nombre"])
        print(f"Apellido:", cliente["apellido"])
        print(f"Código postal:", cliente["codigo_postal"])
        print(f"Teléfono:", cliente["telefono"])
        print(f"Datos detallados: {cliente}\n")
