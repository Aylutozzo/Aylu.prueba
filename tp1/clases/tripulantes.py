from .personas import Persona

class Tripulantes (Persona):
    acceso_modelo_avion=None

    def accesoAvion(self,acceso_avion):
        self.acceso_modelo_avion=acceso_avion


