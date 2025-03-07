import os

RUTA = os.path.join(os.path.dirname(os.path.abspath(__file__)))

try:
    # Abrir el archivo en modo lectura
    with open(os.path.join(RUTA, "colesterol.csv"), encoding="utf-8") as csv_leido:
        print(f"✅ Archivo leido desde la ruta '{csv_leido.name}'.\n")
        leido = csv_leido.read()
        print(leido)
        # Cerrar el archivo después de leerlo
        csv_leido.close()
    # Agregar una fila al final del archivo
    nuevas_lineas = ["\nLeonardo Caballero,44,M,61.0,1.77,194.0"]
    # Abrir el archivo en modo escritura para agregar nuevas líneas
    with open(
        os.path.join(RUTA, "colesterol_modificado.csv"),
        "w",
        newline="",
        encoding="utf-8",
    ) as csv_nuevo:
        print(f"\n✅ Archivo nuevo creado en la ruta '{csv_nuevo.name}'.\n")
        csv_nuevo.write(leido + "\n".join(nuevas_lineas))
        # Cerrar el archivo después de escribir las nuevas líneas
        csv_nuevo.close()
    # Abrir el archivo en modo lectura para leer las líneas modificadas
    with open(
        os.path.join(RUTA, "colesterol_modificado.csv"), encoding="utf-8"
    ) as csv_leido:
        print(f"{csv_leido.read()}")
        print(f"\n✅ Archivo nuevo leido desde la ruta '{csv_leido.name}'.")
        # Cerrar el archivo después de leerlo
        csv_leido.close()
except FileNotFoundError as e:
    print(f"❌ Error: No se encontró el archivo: {e}")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
