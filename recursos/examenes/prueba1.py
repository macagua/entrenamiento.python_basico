import os.path


def creararchivo():
    archivo = open(RUTA_ARCHIVO, "w")
    archivo.close()
    menu()


def guardar():
    archivo = open(RUTA_ARCHIVO, "w")
    archivo.write("Ejemplo de archivos en Python\n")
    archivo.write("=============================")
    archivo.write("\n")
    archivo.write("Para guardar datos")
    archivo.write("\n")
    archivo.write("\nFIN")
    archivo.write("============================")
    archivo.close()
    print("Los datos fueron guardados!")
    menu()


def leer():

    print(RUTA_ARCHIVO)
    archivo = open(RUTA_ARCHIVO)
    if archivo:
        # archivo.read()
        for lineas in archivo.readlines():
            print(lineas)
        archivo.close()
        menu()


def menu():
    opcion = 0

    print("\n==============")
    print("MENÚ PRINCIPAL")
    print("==============\n")

    print("1.- Cargar Datos\n")
    print("2.- Consultar Datos\n")
    print("3.- Eliminar Datos\n")
    print("4.- Salir\n")

    opcion = int(input("Cual es su opción: "))

    if opcion == 1:
        print("Cargando Datos")
        guardar()
    elif opcion == 2:
        print("Consultado Datos")
        leer()
    elif opcion == 3:
        print("Eliminando Datos")
    elif opcion == 4:
        print("Saliendo")
        import sys

        sys.exit()


if __name__ == "__main__":
    """Inicia el programa Python"""
    RUTA_BASE = os.path.dirname(__file__)
    RUTA_ARCHIVO = os.path.join(RUTA_BASE, "datos.txt")
    creararchivo()
    menu()
elif __name__ == "prueba1":
    initialize()
else:
    print("Este programa esta mal configurado, debes llamar a su modulo....")
