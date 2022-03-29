class Ciudad:
    def __init__(self):
        self.name = ""
        self.filas = 0
        self.columnas = 0
        self.unidadCivil = False
        self.recurso = False
        #CONTIENE LA MATRIZ ORTOGONAL CON LOS DAOTS DEL MAPA
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
    
    def setRecurso(self, recurso):
        self.recurso = recurso

    def setUnidadCivil(self, unidadCivil):
        self.unidadCivil = unidadCivil 
    
    def getName(self):
        return self.name
    
    def getFilas(self):
        return self.filas
    
    def getColumnas(self):
        return self.columnas
    
    def getUnidadMilitar(self):
        return self.unidadMilitar