import datetime

datos_basicos = {
    "fecha_nacimiento": "03/12/1980",
    "lugar_nacimiento": "Maracaibo, Zulia, Venezuela",
}

print(
    "Fecha y lugar de nacimiento: {fecha} en {lugar}.".format(
        fecha=datetime.datetime.strftime(
            datetime.datetime.strptime(datos_basicos["fecha_nacimiento"], "%d/%m/%Y"),
            "%d de %B de %Y",
        ),
        lugar=datos_basicos["lugar_nacimiento"],
    )
)
