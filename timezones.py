# Modulo pytz. Se debe instalar con PIP

from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone) #Si le doy de parametro el uso horario lo toma. Si no paso nada usa el UTC de la CPU donde estes o el universal si trabajas en un servidor
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone) #Si le doy de parametro el uso horario lo toma. Si no paso nada usa el UTC de la CPU donde estes o el universal si trabajas en un servidor
print("Ciudad de México: ", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))

caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timezone) #Si le doy de parametro el uso horario lo toma. Si no paso nada usa el UTC de la CPU donde estes o el universal si trabajas en un servidor
print("Caracas: ", caracas_date.strftime("%d/%m/%Y, %H:%M:%S"))
