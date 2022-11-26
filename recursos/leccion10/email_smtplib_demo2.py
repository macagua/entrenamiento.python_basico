import smtplib

# Tu dirección desde donde envía el correo
FROM_ADDRESS = "TU_CORREO_GOOGLE_AQUÍ"
# Tu contraseña de aplicación de Google del correo electrónico desde donde envía el correo
FROM_ADDRESS_PASSWORD = "TU_CONTRASEÑA_DE_APLICACIÓN_GOOGLE_AQUÍ"
# Tu dirección del host SMTP
SMTP_SERVER = "smtp.gmail.com"
# Tu puerto del host SMTP
SMTP_PORT = "587"

remitente = "Macagua <leonardoc@plone.org>"
destinatarios = ["Leonardo Caballero <leonardocaballero@gmail.com>"]
asunto_mensaje = "Envio de Prueba de SMTP"
cuerpo_mensaje = "Esto es un mensaje de prueba por correo electronico."

mensaje = f"""From: {remitente}
To: {", ".join(destinatarios)}
Subject: {asunto_mensaje}

{cuerpo_mensaje}
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
