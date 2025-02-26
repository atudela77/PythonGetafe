from os import system
# system("clear")


# Método para calcular operaciones de dos números
# Método para sumar dos números
def sumarNumeros(a, b):
    return a + b


# Método para restar dos numeros
def restarNumeros(a, b):
    return a - b


# Método para multiplicar dos números
def multiplicarNumeros(a, b):
    return a * b


# Método para mostrar el menú de opciones
def mostrarMenu():
    print("Seleccione una opción")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Volver a introducir números")
    print("0.- Salir")


# Comprobación de numérico para la opción del menú
def compruebaNumerico(variable):
    if (variable.isdigit()):
        return int(variable)


# Comprueba si el dato introducido es númerico para el menú de opciones
def checkNumerico(ordennumero):
    inbucle = True
    dato = ""
    while (inbucle):
        print("Introduzca el " + ordennumero + " número: ")
        dato = input()
        if (dato.isdigit()):
            inbucle = False
            return int(dato)
        else:
            print("Dato no numérico")


# Programa principal
system("clear")
# Esta variable lógica controla el bucle principal
pedirnumeros = True
while (pedirnumeros):
    # Se piden los números al usuario y se controla que sean numéricos
    num1 = checkNumerico("primer")
    num2 = checkNumerico("segundo")
    # Esta variable lógica controla el bucle del menú.
    # Tiene que iterar hasta que se decida salir o pedir números nuevos
    buclemenu = True
    # Se muestra el menú de opciones
    while (buclemenu):
        # Esta variable numérica controla que se introduzca una opción válida
        opcion = -1
        while (opcion != 1 and opcion != 2 and opcion != 3
               and opcion != 4 and opcion != 0):
            mostrarMenu()
            entrada = input()
            opcion = compruebaNumerico(entrada)
        # Se selecciona la operación correspondiente
        resultado = 0
        texto = ""
        if (opcion == 0):
            buclemenu = False
            pedirnumeros = False
        elif (opcion == 1):
            texto = " + "
            resultado = sumarNumeros(num1, num2)
            buclemenu = False
        elif (opcion == 2):
            texto = " - "
            resultado = restarNumeros(num1, num2)
            buclemenu = False
        elif (opcion == 3):
            texto = " * "
            resultado = multiplicarNumeros(num1, num2)
            buclemenu = False
        elif (opcion == 4):
            buclemenu = False
        if (opcion != 0 and opcion != 4):
            print(f"{str(num1)}{texto}{str(num2)} = {str(resultado)} \n")

print("Fin del programa")
