import os
import pandas as pd

RUTA = os.path.dirname(os.path.abspath(__file__)) + os.sep

try:
    # Abrir el archivo CSV y leerlo en un DataFrame
    df = pd.read_csv(os.path.join(RUTA, "colesterol.csv"), sep=",", decimal=",")
    print(
        f"✅ El conjunto de datos en la ruta '{os.path.join(RUTA, 'colesterol.csv')}' fue cargado correctamente.\n"
    )
    # Mostrar las primeras 5 filas del DataFrame
    print(df.head())
    print(f"\n📜 El conjunto de datos original contiene '{len(df)}' lineas.")
except FileNotFoundError as e:
    print(f"❌ Error: No se encontró el archivo en la ruta '{os.path.join(RUTA, 'colesterol.csv')}': {e}")
except pd.errors.EmptyDataError as e:
    print(f"❌ Error: El archivo está vacío, en la ruta '{os.path.join(RUTA, 'colesterol.csv')}': {e}")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
