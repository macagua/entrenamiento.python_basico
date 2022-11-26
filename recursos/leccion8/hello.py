from threading import Timer
from time import sleep


def hello():
    print("Hola mundo\n\n\tEste es un ejemplo de una distribución nativa\n")
    sleep(2)


tiempo = Timer(0.05, hello)
# Después de 0.05 segundos, el mensaje de la función hello sera mostrada
tiempo.start()
