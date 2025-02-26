print("Este programa comprueba si un ISBN es correcto.")
# Variable lógica para controlar el bucle que comprueba que el
#  código ISBN tenga 10 dígitos numéricos
isbn_nok = True
print("Introduzca número ISBN: ")
# El bucle se rompe cuando el ISBN introducido tiene el formato
#  correcto.
while (isbn_nok):
    # Se solicita al usuario el número
    isbn = input()
    # Si la longitud es 10 se comprueba que sean todo números
    if (len(isbn) == 10):
        # Se comprueba que la cadena sea numérica
        if (isbn.isnumeric()):
            # Si todo ok, se cambia la variable lógica a False para romper
            #  el bucle.
            isbn_nok = False
        else:
            # Se muestra un mensaje y se vuelve a solicitar el número
            print("Solo debe contener caracteres numéricos")
    else:
        # Se muestra un mensaje y se vuelve a solicitar el número
        print("Debe introducir un ISBN de 10 dígitos")
# Se inicializa la variable donde se va a guardar la suma de los productos
suma = 0
# Se multiplica cada caracter por su posición dentro de la cadena.
for i in range(len(isbn)):
    suma += int(isbn[i]) * int(i + 1)
# Si el resto de dividir por 11 es 0, entonces el ISBN es correcto,
#  sino es incorrecto.
if (suma % 11 == 0):
    print("CORRECTO")
else:
    print("INCORRECTO")
# Fin del programa.
print("Fin del programa")
