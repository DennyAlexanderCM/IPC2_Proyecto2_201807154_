class Ciudad:
    def __init__(self):
        self.name = ""
        self.filas = 0
        self.columnas = 0
        self.unidadMilitar = None
        self.mapa = None

    def setName(self, name):
        self.name = name
    
    def setFilas(self, filas):
        self.filas = filas
    
    def setColumnas(self, columnas):
        self.columnas = columnas
    
    def setUnidadMilitar(self, unidad):
        self.unidadMilitar = unidad
    
    def setMapa(self, mapa):
        self.mapa = mapa
    
    def getName(self):
        return self.name
    
    def getFilas(self):
        return self.filas
    
    def getColumnas(self):
        return self.columnas
    
    def getUnidadMilitar(self):
        return self.unidadMilitar