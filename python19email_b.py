print("Este programa comprueba que un email sea correcto.")
# Se solicita el email
print("Introduzca un email: ")
email = input()
# Variables lógicas para las condiciones
# No hay arroba
noexistearroba = email.find("@") == -1
# Hay una arroba al inicio o al final
noinifinarroba = email.startswith("@") or email.endswith("@")
# Hay más de una arroba
masdeunaarroba = email.count("@") > 1
# No hay ningún punto
nohaypunto = email.find(".") == -1
# No hay un punto después de la arroba
nopuntodespuesarroba = email.find("@") > email.rfind(".")
# Índice del punto final más uno (para empezar a contar la longitud
# del dominio)
posicionpuntofinal = email.rfind(".") + 1
# Longitud del dominio
longituddominio = len(email[posicionpuntofinal:])
# El dominio tiene menos de dos caracteres o más de tres
dominiocortoolargo = longituddominio < 2 or longituddominio > 3
# Despúes de la arroba hay un punto justo después
arrobaypuntojuntos = email.rfind(".") - email.find("@") == 1

# Se comprueba que el email contenga @
if (noexistearroba):
    print("El email debe contener una @")
# Se comprueba que el email no tenga @ ni al principio ni al final
elif (noinifinarroba):
    print("El email no puede tener una @ ni al principio ni al final")
# Se comprueba que el email solamente tenga una @
elif (masdeunaarroba):
    print("El email solo puede contener una @")
# Se comprueba que el email contenga un punto
elif (nohaypunto):
    print("El email debe contener al menos un punto")
# Se comprueba que exista un punto después de la @
elif (nopuntodespuesarroba):
    print("El email debe contener un punto después de la @")
# Se comprueba que no haya un punto justo después de la @
elif (arrobaypuntojuntos):
    print("Debe haber al menos un caracter entre la @ y el punto de dominio")
# Se comprueba que el dominio sea de entre 2 y 3 caracteres
elif (dominiocortoolargo):
    print("El dominio del email debe tener entre 2 y 3 caracteres")
# Si ha llegado hasta aquí es que está bien
else:
    print("Email correcto")
# Fin del programa
print("Fin de programa.")