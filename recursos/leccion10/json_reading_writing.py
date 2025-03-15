"""Programa para escribir y leer un archivo JSON"""

import json
import logging
import os

logging.basicConfig(level=logging.INFO)

# Ruta del archivo
RUTA = os.path.join(os.path.dirname(os.path.abspath(__file__)))
# Nombre de archivo JSON
ARCHIVO_JSON = "clientes.json"
# Data a escribir
clientes_data = {
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
            "nombre": "Manuel",
            "apellido": "Matos",
            "codigo_postal": "4001",
            "telefono": "+58-414-2360943",
        },
    ]
}


try:
    # Abriendo archivo para escribir un tipo diccionario 'clientes_data'
    with open(
        os.path.join(RUTA, ARCHIVO_JSON), mode="w", encoding="utf-8"
    ) as json_nuevo:
        json.dump(clientes_data, json_nuevo)
        # Cerrar el archivo después de escribirlo
        json_nuevo.close()
        logging.info(f"✅ Se escribió el archivo JSON '{ARCHIVO_JSON}'.\n")
    # Abrir el archivo en modo lectura
    with open(os.path.join(RUTA, ARCHIVO_JSON), encoding="utf-8") as json_leido:
        # Leyendo desde archivo JSON
        data = json.load(json_leido)
        for cliente in data["clientes"]:
            print(f"📜 Nombre:", cliente["nombre"])
            print(f"📜 Apellido:", cliente["apellido"])
            print(f"📜 Código postal:", cliente["codigo_postal"])
            print(f"📜 Teléfono:", cliente["telefono"])
            print(f"📜 Datos detallados: {cliente}\n")
        # Cerrar el archivo después de leerlo
        json_leido.close()
        logging.info(f"✅ Se leyó el archivo JSON '{ARCHIVO_JSON}'.")
except FileNotFoundError as e:
    print(f"❌ Error: No se encontró el archivo: {e}")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
