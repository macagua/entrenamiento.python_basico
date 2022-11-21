import datetime

datos_basicos = {
    "fecha_nacimiento": "03121980",
    "lugar_nacimiento": "Maracaibo, Zulia, Venezuela",
}

dia = datos_basicos["fecha_nacimiento"][0:2]
mes = datos_basicos["fecha_nacimiento"][2:4]
ano = datos_basicos["fecha_nacimiento"][4:8]

fecha_nacimiento = datetime.date(int(ano), int(mes), int(dia))

print(
    "Fecha y lugar de nacimiento: {fecha} en {lugar}.".format(
        fecha=datetime.datetime.strftime(fecha_nacimiento, "%d de %B de %Y"),
        lugar=datos_basicos["lugar_nacimiento"],
    )
)
