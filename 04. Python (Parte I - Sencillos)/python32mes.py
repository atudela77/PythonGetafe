from class32mes import Mes
from os import system
import random

system("clear")
print("Programa para probar la clase Mes", "\n")

# # Declaramos el objeto enero para el mes de enero
# enero = Mes()
# print(f"La temperatura media de {enero.nombre} es de "
#       f"{enero.getTemperaturaMedia()}ºC")
# print(enero, "\n")
# # Declaramos el objeto agosto para el mes de agosto
# agosto = Mes()
# agosto.nombre = "Agosto"
# agosto.temperatura_max = 41
# agosto.temperatura_min = 15
# print(f"La temperatura media de {agosto.nombre} es de "
#       f"{agosto.getTemperaturaMedia()}ºC")
# print(agosto, "\n")


# Declaramos el objeto mes 10 para el mes de octubre
meses = ("Enero", "Febrero", "Marzo", "Abril",
         "Mayo", "Junio", "Julio", "Agosto",
         "Septiembre", "Octubre", "Noviembre", "Diciembre")

for nombreMes in meses:
    mes = Mes()
    mes.nombre = nombreMes
    mes.temperatura_max = random.randint(15, 40)
    mes.temperatura_min = random.randint(1, 15)
    print(f"La temperatura media de {mes.nombre} es de "
          f"{mes.getTemperaturaMedia()}ºC")
    print(mes, "\n")
