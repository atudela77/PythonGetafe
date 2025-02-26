from class30coche import Coche
from class31deportivo import Deportivo

print("Programa para probar la clase Deportivo heredada de coche")
print("------Coche------")
coche = Coche()
coche.arrancar()
coche.acelerar()
coche.frenar()
coche.detener()
print("Velocidad coche ", coche.getVelocidadMaxima())
print(".------------------.")
print("-----Deportivo-----")
depor = Deportivo()
depor.marca = "Porsche"
depor.arrancar()
depor.acelerar()
depor.turbo()
depor.frenar()
depor.detener()
print("Velocidad deportivo ", depor.getVelocidadMaxima())
