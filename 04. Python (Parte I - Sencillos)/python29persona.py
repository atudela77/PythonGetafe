from class29persona import Persona
from os import system
system("clear")
print("Prueba clase Persona")
# Creamos una nueva persona
person = Persona()
print(person.pais)
person.pais = "España"
person.anyonacimiento = 2000
person.email = "email@email.com"
person.nombre = "Alumno"
person.apellidos = "Python"
print(person.getNombreCompleto())
print(person.getEdad())
person2 = Persona()
print(person2.pais)
print(person)
print(person.getDescripcion("Esto es una descripción"))
print("")
