# sintaxis con from
from math import floor, ceil, trunc

# sintaxias con import
import math

print("Ejemplo de librerías")

numero1 = 20
numero2 = 3
division = numero1 / numero2
print("La división es: ", division)

# Declaramos variables para almacenar los valores de las operaciones con from
# varFloor = floor(division)
# varCeil = ceil(division)
# varTrunc = trunc(division)

# Declaramos variables para almacenar los valores de las operaciones con import
varFloor = math.floor(division)
varCeil = math.ceil(division)
varTrunc = math.trunc(division)

# Mostramos resultados para from
print("Floor: ", varFloor)
print("Ceil: ", varCeil)
print("Trunc: ", varTrunc)

print("Fin de programa")
