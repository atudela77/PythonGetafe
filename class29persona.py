class Persona:
    # Primero se declaran las propiedades.
    nombre = ""
    apellidos = ""
    email = ""
    anyonacimiento = 0
    pais = ""

    # No es necesario declarar un constructor, es opcional.
    def __init__(self):
        self.pais = "Francia"

    # El siguiente metodo personaliza lo que muestra print(objeto)
    def __str__(self):
        return self.apellidos + " " + self.nombre + ", " + self.pais

    # A continuación se define los métodos.
    # Con self podemos acceder a las propiedades definidas anteriormente.
    def getNombreCompleto(self):
        return self.nombre + " " + self.apellidos

    def getEdad(self):
        return 2025 - self.anyonacimiento

    def getDescripcion(self, descripcion):
        return self.getNombreCompleto() + " " + descripcion
