import datetime

fecha_nacimiento = "03121980"

dia = fecha_nacimiento[0:2]
mes = fecha_nacimiento[2:4]
ano = fecha_nacimiento[4:8]

fecha_nacimiento = datetime.date(int(ano), int(mes), int(dia))

print(f"Fecha de nacimiento: {fecha_nacimiento}.")
