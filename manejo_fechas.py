# Para trabajar con fechas debemos importar: o el modulo 
# Datetime completo o al menos la clase datetime del modulo

from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime("%d/%m/%Y")
print(f"Formato LATAM: {my_str}")

my_str = my_datetime.strftime("%m/%d/%Y")
print(f"Formato USA: {my_str}")

my_str = my_datetime.strftime("Estamos en el año %Y")
print(f"Formato Ramdom: {my_str}")
