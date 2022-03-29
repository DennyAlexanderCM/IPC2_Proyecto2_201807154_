class RobotChapinFighter():
    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
    
    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo

    def getCapacidad(self):
        return self.capacidad
    
    def setReduceCapacidad(self, capacidad):
        self.capacidad = (self.capacidad - capacidad)

class RobotChapinRescue():
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo
        

    