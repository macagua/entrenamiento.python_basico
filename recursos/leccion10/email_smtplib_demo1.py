import smtplib

# Tu dirección desde donde envía el correo
FROM_ADDRESS = "TU_CORREO_GOOGLE_AQUÍ"
# Tu contraseña de aplicación de Google del correo electrónico desde donde envía el correo
FROM_ADDRESS_PASSWORD = "TU_CONTRASEÑA_DE_APLICACIÓN_GOOGLE_AQUÍ"
# Tu dirección del host SMTP
SMTP_SERVER = "smtp.gmail.com"
# Tu puerto del host SMTP
SMTP_PORT = "587"

remitente = "leonardoc@plone.org"
destinatarios = ["leonardocaballero@gmail.com"]

mensaje = """From: Macagua <leonardoc@plone.org>
To: Leonardo Caballero <leonardocaballero@gmail.com>
Subject: Envio de Prueba de SMTP

Esto es un mensaje de prueba por correo electronico.
"""

try:
    smtp = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)
    smtp.starttls()
    smtp.login(FROM_ADDRESS, FROM_ADDRESS_PASSWORD)
    smtp.sendmail(remitente, destinatarios, mensaje)
    smtp.quit()
    print("Correo enviado correctamente")
except Exception:
    print("Error: no se pudo enviar el correo")
