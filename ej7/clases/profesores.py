from .persona import Persona

class Profesor(Persona):
    descuento= None

    def getDescuento(self):
       return self.descuento
