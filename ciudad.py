class Ciudad:
    def __init__(self):
        self.nombre = ""
        self.filas = 0
        self.columnas = 0
        self.unidadMilitar = None
        self.filasLista = None

    def setName(self, name):
        self.name = name
    
    def setFilas(self, filas):
        self.filas = filas
    
    def setColumnas(self, columnas):
        self.columnas = columnas
    
    def setUnidadMilitar(self, unidad):
        self.unidadMilitar = unidad