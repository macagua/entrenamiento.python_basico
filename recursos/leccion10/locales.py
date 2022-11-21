from datetime import datetime
import locale

datos_basicos = {
    "nombres": "Leonardo Jose",
    "apellidos": "Caballero Garcia",
    "cedula": "26938401",
    "fecha_nacimiento": "03121980",
    "lugar_nacimiento": "Maracaibo, Zulia, Venezuela",
    "nacionalidad": "Venezolana",
    "estado_civil": "Soltero",
}

dia = datos_basicos["fecha_nacimiento"][0:2]
mes = datos_basicos["fecha_nacimiento"][2:4]
ano = datos_basicos["fecha_nacimiento"][4:8]

locale.setlocale(locale.LC_TIME, "")
locale.nl_langinfo(locale.MON_12).capitalize()

try:
    locale.setlocale(locale.LC_ALL, "es_VE.UTF-8")
except locale.Error as err:
    print(f"No reconoce esa configuración de locales ({err})")

fn_traducida = datetime(int(ano), int(mes), int(dia))
print(fn_traducida.strftime("%A, %d. %B %Y %I:%M%p"))
