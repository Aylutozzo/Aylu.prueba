from .personas import Personas

class Profesores(Personas):
    descuento= None

    def getDescuento(self):
       return self.descuento
