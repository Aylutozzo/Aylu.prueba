from .tripulantes import Tripulantes

class Servicio (Tripulantes):
    servicio=None
    idioma=None

    def Servicio(self,servicio):
        self.servicio=servicio

    def Idioma(self,idioma):
        self.idioma=idioma

