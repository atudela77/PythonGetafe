print("Ejemplo bucles.")
print("While")
# Necesitamos una variable para la condición del bucle
contador = 0
while (contador <= 5):
    # Debemos indicar que saldremos del bucle
    print("Contador: ", contador)
    contador = contador + 1

# Bucle for
print("Bucle for.")
# Normalmente las variables de los bucles contadores se representan 
#  con una sola letra.
# Bucle for sólo con final (empieza en 0)
for i in range(5):
    print("Valor de i: ", i)
# Bucle for con inicio y final 6 (llega hasta 5)
for i in range(1, 6):
    print("Valor de i: ", i)

print("Fin del programa.")
