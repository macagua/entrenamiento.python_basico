import datetime

datos_basicos = {
    "fecha_nacimiento": "03/12/1980",
    "lugar_nacimiento": "Maracaibo, Zulia, Venezuela",
}

fecha = (
    datetime.datetime.strftime(
        datetime.datetime.strptime(datos_basicos["fecha_nacimiento"], "%d/%m/%Y"),
        "%d de %B de %Y",
    ),
)
lugar = datos_basicos["lugar_nacimiento"]
print(f"Fecha y lugar de nacimiento: {fecha[0]} en {lugar}.")
