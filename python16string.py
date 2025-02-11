print("Clase string y funciones.")
texto = "primero python"
# Vamos probando métodos y viendo a ver qué devuelven
print("upper ", texto.upper())
print("replace ", texto.replace("o", "@"))
print("Letra 0", texto[0])
print("lower ", texto.lower())
print("Longitud ", len(texto))
print("find p ", texto.find("p"))
print("find z ", texto.find("z"))
print("rfind p ", texto.rfind("p"))
# Sobrecarga de find
print("find p 1 ", texto.find("p", 1))
print("startswith a ", texto.startswith("a"))
print("startswith a ", texto.startswith("p"))
print("endswith n ", texto.endswith("n"))
print("isdigit ", texto.isdigit())
# El siguiente isalpha es False por el espacio en blanco -> Solo letras
print("isalpha ", texto.isalpha())
# El siguiente isalnum es False por el espacio en blanco -> Solo letras y núms
print("isalnum ", texto.isalnum())
# String Slicing
substring = texto[2:]
print("Posición 2 en adelante: ", substring)
# En python podemos recuperar una subcadena desde una posición (2) a
#   otra posición (5)
subtexto = texto[2:5]
print("Subcadena entre dos posiciones (2 y 5) :", subtexto)
# Podemos recorrer cada caracter de un texto.
longitud = len(texto)
for i in range(longitud):
    print("Posición " + str(i) + ": " + texto[i])
# Podemos comprobar que si el usuario ha escrito un número o no
print("Introduzca un número: ")
# Primero creo una variable auxiliar
aux = input()
if (aux.isdigit()):
    print("Esto es un número.")
else:
    print("No me has dado un número, campeón...")
print("Fin de programa.")
