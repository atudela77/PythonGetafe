print("Este programa calcula el día de la semana de la fecha de nacimiento.")
print("Introduzca el día de su fecha de nacimiento: ")
dia = int(input())
print("Introduzca el mes de su fecha de nacimiento: ")
mes = int(input())
print("Introduzca el año de su fecha de nacimiento: ")
anno = int(input())

if (mes == 1):
    mes = 13
    anno = anno - 1
elif (mes == 2):
    mes = 14
    anno = anno - 1

# Operación 1
calculo_mes = int(((mes + 1) * 3) / 5)
# Operación 2
calculo_anno_4 = int(anno/4)
# Operación 3
calculo_anno_100 = int(anno/100)
# Operación 4
calculo_anno_400 = int(anno/400)
# Operación 5: Sumar el día, doble mes, año, operación 1 y operación 2, restar operación 3 y sumar operación 4 más 2
calculo_1 = (dia + (2 * mes) + anno + calculo_mes + calculo_anno_4 - calculo_anno_100 + calculo_anno_400 + 2)
# Operación 6: Dividir el número anterior por 7
calculo_2 = int(calculo_1 / 7)
# Resultado = Operación 5 menos Operación 6 multiplicado por 7
resultado = calculo_1 - (calculo_2 * 7)

# Mostramos el nombre del día de la semana
if (resultado == 0):
    print("El día de la semana para la fecha dada fue sábado.")
elif (resultado == 1):
    print("El día de la semana para la fecha dada fue domingo.")
elif (resultado == 2):
    print("El día de la semana para la fecha dada fue lunes.")
elif (resultado == 3):
    print("El día de la semana para la fecha dada fue martes.")
elif (resultado == 4):
    print("El día de la semana para la fecha dada fue miércoles.")
elif (resultado == 5):
    print("El día de la semana para la fecha dada fue jueves.")
elif (resultado == 6):
    print("El día de la semana para la fecha dada fue viernes.")
else:
    print("Se ha producido algún error: ", resultado)

print("Fin del programa.")
