import datetime
dt = datetime.datetime.now() # Ahora

datetime.datetime(2016, 6, 18, 21, 29, 28, 607208)

print(dt.year) # año
print(dt.month) # mes
print(dt.day) # día
print(dt.hour) # hora
print(dt.minute) # minutos
print(dt.second) # segundos
print(dt.microsecond) # microsegundos
print(dt.tzinfo) # zona horaria, nula por defecto

print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
print("{}/{}/{}".format(dt.day, dt.month, dt.year))

dt = datetime.datetime.now()
print("Fecha actual", dt)

dt = datetime.datetime(2000,1,1)
print(dt)
print("Fecha formateada",dt.strftime("%A %d de %B del %Y - %H:%M"))# %I 12h - %H 24h
