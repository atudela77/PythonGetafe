from class30coche import Coche


class Deportivo(Coche):
    aleron = True

    def turbo(self):
        self.velocidad += 120
        print("Activando turbo")
        print("Velocidad actual: ", self.velocidad)

    def acelerar(self):
        if (not self.estado):
            print("El coche no está arrancado. Debe arrancar antes.")
        else:
            self.velocidad += 60
            print("Velocidad actual " + str(self.velocidad))

    def getVelocidadMaxima(self):
        print('Velocidad máxima del coche: 240 km/h')
        return super().getVelocidadMaxima() + 100
