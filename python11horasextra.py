print("Este programa muestra el salario de un trabajador.")
# Pedimos al usuario los datos necesarios
print("Introduzca las horas trabajadas: ")
horas = int(input())
print("Introduzca el precio hora: ")
precio = int(input())
print("Introduzca los kilómetros: ")
kilometros = int(input())

print("\n")
    
# Calculamos el salario a partir de las horas y el precio.
if (horas <= 36):
    salario_base = horas * precio
    salario_extra = 0
else:
    salario_base = 36 * precio
    salario_extra = (horas - 36) * (precio + 2)
salario = salario_base + salario_extra

dietas = ""
# Mostramos el tipo de dietas dependiendo de los kilómetros
if (kilometros <= 100):
    dietas = "Las dietas son locales."
elif (kilometros > 100 and kilometros <= 500):
    dietas = "Las dietas son provinciales."
else:
    dietas = "Las dietas son nacionales."

retencion = ""
# Calculamos las retenciones dependiendo del precio indicado
if (salario < 250):
    retencion = "Sin retención"
elif (salario >= 250 and salario <= 600):
    retencion = "Retención del 20%"
else:
    retencion = "Retención del 40%"

# Mostramos el resultado
print("\n")
print("Informe de salario")
print(" * Horas trabajadas: ", horas)
print(" * Precio hora: ", precio)
print(" * Salario base: ", salario_base)
print(" * Salario extra: ", salario_extra)
print(" * Salario total: ", salario)
print(" * Retenciones: ", retencion)
print(" * Dietas: ", dietas)
print("\n")
print("Fin del programa.")
