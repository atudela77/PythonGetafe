def saludar(nombre):
    print("Bienvenido a Python Mr/Mrs " + nombre)


def despedirse(nombre, dia):
    print("Un placer hoy " + str(dia) + " Mr/Mrs " + nombre)


# Programa principal
print("Métodos con parámetros")
name = "Alumno"
dia = "miércoles"
saludar(name)
despedirse(name, dia)
# Se pueden pasar valores directamente
saludar("Antonio")
despedirse("Marta", "domingo")
print("Fin del programa")
