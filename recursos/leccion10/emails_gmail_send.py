import os
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DIR_ARCHIVO = os.path.dirname(os.path.abspath(__file__)) + os.sep
ARCHIVO = ["email_contactos.txt", "email_mensaje.txt"]

# Dirección desde donde se envía el correo
FROM_ADDRESS = "TU_CORREO_GOOGLE_AQUÍ"
# Contraseña de aplicación de la cuenta Google desde donde se envía el correo
FROM_ADDRESS_PASSWORD = "TU_CONTRASEÑA_DE_APLICACIÓN_GOOGLE_AQUÍ"
# Dirección del servidor SMTP
SMTP_SERVER = "smtp.gmail.com"
# Puerto del servidor SMTP
SMTP_PORT = 587


def leer_contacto(nombre_archivo):
    """Devuelve dos tipo lista nombres y correos electrónicos que contienen nombres
    y direcciones de correo electrónico leídas de un archivo especificado por nombre
    de archivo.
    """

    nombres = []
    correos = []
    with open(nombre_archivo, encoding="utf-8") as archivo_contactos:
        for contacto in archivo_contactos:
            nombres.append(contacto.split()[0])
            correos.append(contacto.split()[1])
    return nombres, correos


def leer_plantilla(nombre_archivo):
    """Devuelve un objeto Template que incluye el contenido del
    archivo especificado por nombre de archivo.
    """

    with open(nombre_archivo, encoding="utf-8") as archivo_plantilla:
        contenido_archivo_plantilla = archivo_plantilla.read()
    return Template(contenido_archivo_plantilla)


def main():
    """Función principal del programa."""

    try:
        # leer contactos
        nombres, correos = leer_contacto(DIR_ARCHIVO + ARCHIVO[0])
        # leer mensaje de plantilla
        mensaje_plantilla = leer_plantilla(DIR_ARCHIVO + ARCHIVO[1])

        # configurar el servidor SMTP
        smtp = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)
        smtp.starttls()
        smtp.login(FROM_ADDRESS, FROM_ADDRESS_PASSWORD)

        # Para cada contacto, envíe el correo electrónico:
        for nombre, correo in zip(nombres, correos):
            # crear un mensaje
            msg = MIMEMultipart()
            # agregue el nombre de la persona real a la plantilla de mensaje
            mensaje = mensaje_plantilla.substitute(NOMBRE_PERSONA=nombre.title())
            # Imprime el cuerpo del mensaje por nuestro bien
            print(mensaje)
            # configurar los parámetros del mensaje
            msg["From"] = FROM_ADDRESS
            msg["To"] = correo
            msg["Subject"] = "Esto es un mensaje PRUEBA"
            # añadir en el cuerpo del mensaje
            msg.attach(MIMEText(mensaje, "plain"))
            # enviar el mensaje a través del servidor configurado anteriormente.
            smtp.send_message(msg)
            del msg
        # Terminar la sesión SMTP y cerrar la conexión
        smtp.quit()
        print("Correo(s) enviado(s) correctamente")
    except smtplib.SMTPConnectError as e:
        print(f"Error: Conexión al servidor de correo fallo: {e}")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Error: Credenciales de acceso al correo no coinciden: {e}")
    except Exception as e:
        print(f"Error: no se pudo enviar el correo: {e}")


if __name__ == "__main__":
    main()
