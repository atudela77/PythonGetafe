import random
from os import system
system("Clear")

abecedario = "ABCDEFGHIJKLMNÑOPQSTUVWXYZ"
letra = random.choice(abecedario)
# print(letra)
oculto = True
print("Dime una letra")
while (oculto):
    intento = input()
    if (intento.upper() == letra):
        system("Clear")
        print("¡¡Enhorabuena, has acertado la letra secreta!!")
        oculto = False
    elif (intento == "0"):
        system("Clear")
        print("Te rindes facilmente")
        oculto = False
    else:
        system("Clear")
        print("Letra incorrecta, intentalo otra vez ")
