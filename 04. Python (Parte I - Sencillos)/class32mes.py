class Mes:
    nombre = ""
    temperatura_max = 0
    temperatura_min = 0

    def __init__(self):
        self.nombre = "Enero"
        self.temperatura_max = 12
        self.temperatura_min = -5

    def __str__(self):
        cad = f"Mes: {self.nombre}, "
        cad += f"Temperatura mínima: {self.temperatura_min}ºC, "
        cad += f"Temperatura máxima: {self.temperatura_max}ºC, "
        cad += f"Temperatura media: {self.getTemperaturaMedia()}ºC"
        return cad

    def getTemperaturaMedia(self):
        return (self.temperatura_max + self.temperatura_min)/2
