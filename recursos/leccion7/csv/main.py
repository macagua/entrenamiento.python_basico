import csv
import os

RUTA = os.path.join(os.path.dirname(os.path.abspath(__file__)))

try:
    # Abrir el archivo en modo lectura
    with open(os.path.join(RUTA, "colesterol.csv"), encoding="utf-8") as csv_leido:
        print(f"✅ Archivo leido desde la ruta '{csv_leido.name}'.\n")
        reader = csv.reader(csv_leido, delimiter=",") 
        filas = list(reader)
        for fila in filas:
            print(fila)
        # Cerrar el archivo después de leerlo
        csv_leido.close()
    # Agregar una fila al final del archivo
    filas.append(["Leonardo Caballero", "44", "H", "61.0", "1.77", "194.0"])
    # Abrir el archivo en modo escritura para agregar nuevas líneas
    with open(os.path.join(RUTA, "colesterol_modificado.csv"), "w", newline='', encoding="utf-8") as csv_nuevo:
        print(f"\n✅ Archivo nuevo creado en la ruta '{csv_nuevo.name}'.\n")
        writer = csv.writer(csv_nuevo, delimiter=",")
        for fila in filas:
            writer.writerow(fila)
        # Cerrar el archivo después de escribir las nuevas líneas
        csv_nuevo.close()
    # Abrir el archivo en modo lectura para leer las líneas modificadas
    with open(os.path.join(RUTA, "colesterol_modificado.csv"), encoding="utf-8") as csv_leido:
        reader = csv.reader(csv_leido, delimiter=",") 
        filas = list(reader)
        for fila in filas:
            print(fila)
        print(f"\n✅ Archivo nuevo leido desde la ruta '{csv_leido.name}'.")
        # Cerrar el archivo después de leerlo
        csv_leido.close()
except FileNotFoundError as e:
    print(f"❌ Error: No se encontró el archivo: {e}")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
