# ValidaciónISBN: ISBN --> True/False
def validarISBN(numero):
    # Variable lógica para controlar el bucle que comprueba que el
    #  código ISBN tenga 10 dígitos numéricos
    isbn_nok = True
    # El bucle se rompe cuando el ISBN introducido tiene el formato
    #  correcto.
    while (isbn_nok):
        # Se solicita al usuario el número
        isbn = numero
        # Si la longitud es 10 se comprueba que sean todo números
        if (len(isbn) == 10):
            # Se comprueba que la cadena sea numérica
            if (isbn.isnumeric()):
                # Si todo ok, se cambia la variable lógica a False para romper
                #  el bucle.
                isbn_nok = False
            else:
                # Se muestra un mensaje y se vuelve a solicitar el número
                return False
        else:
            # Se muestra un mensaje y se vuelve a solicitar el número
            return False
    # Se inicializa la variable donde se va a guardar la suma de los productos
    suma = 0
    # Se multiplica cada caracter por su posición dentro de la cadena.
    for i in range(len(isbn)):
        suma += int(isbn[i]) * int(i + 1)
    # Si el resto de dividir por 11 es 0, entonces el ISBN es correcto,
    #  sino es incorrecto.
    if (suma % 11 == 0):
        return True
    else:
        return False


# Letra DNI: DNI --> Letra
def letraDNI(numero):
    dni = int(numero)
    resto = dni % 23
    if (resto == 0):
        letra = 'T'
    elif (resto == 1):
        letra = 'R'
    elif (resto == 2):
        letra = 'W'
    elif (resto == 3):
        letra = 'A'
    elif (resto == 4):
        letra = 'G'
    elif (resto == 5):
        letra = 'M'
    elif (resto == 6):
        letra = 'Y'
    elif (resto == 7):
        letra = 'F'
    elif (resto == 8):
        letra = 'P'
    elif (resto == 9):
        letra = 'D'
    elif (resto == 10):
        letra = 'X'
    elif (resto == 11):
        letra = 'B'
    elif (resto == 12):
        letra = 'N'
    elif (resto == 13):
        letra = 'J'
    elif (resto == 14):
        letra = 'Z'
    elif (resto == 15):
        letra = 'S'
    elif (resto == 16):
        letra = 'Q'
    elif (resto == 17):
        letra = 'V'
    elif (resto == 18):
        letra = 'H'
    elif (resto == 19):
        letra = 'L'
    elif (resto == 20):
        letra = 'C'
    elif (resto == 21):
        letra = 'K'
    elif (resto == 22):
        letra = 'E'
    elif (resto == 23):
        letra = 'T'
    else:
        letra = 'ERROR'
    return letra


def obtenerLetraDni(numero):
    letra_dni = 'TRWAGMYFPDXBNJZSQVHLCKET'
    return letra_dni[int(numero) % 23]
