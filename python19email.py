print("Este programa comprueba que un email sea correcto.")
# Se solicita el email
print("Introduzca un email: ")
email = input()
# Comienzan las comprobaciones
# Se comprueba que el email contenga @
if (email.find("@") == -1):
    print("El email debe contener una @")
# Se comprueba que el email no tenga @ ni al principio ni al final
elif (email.startswith("@") or email.endswith("@")):
    print("El email no puede tener una @ ni al principio ni al final")
# Se comprueba que el email solamente tenga una @
elif (email.count("@") > 1):
    print("El email solo puede contener una @")
# Se comprueba que el email contenga un punto
elif (email.find(".") == -1):
    print("El email debe contener al menos un punto")
# Se comprueba que exista un punto después de la @
elif (email.find("@") > email.rfind(".")):
    print("El email debe contener un punto después de la @")
# Se comprueba que el dominio sea de entre 2 y 3 caracteres
elif (len(email[email.rfind(".") + 1:]) < 2
      or
      len(email[email.rfind(".") + 1:]) > 3):
    print("El dominio del email debe tener entre 2 y 3 caracteres")
# Se comprueba que no haya un punto justo después de la @
elif (email.rfind(".") - email.find("@") == 1):
    print("Debe haber al menos un caracter entre la @ y el punto de dominio")
# Si ha llegado hasta aquí es que está bien
else:
    print("Email correcto")
# Fin del programa
print("Fin de programa.")
