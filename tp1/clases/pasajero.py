from .personas import Persona

class Pasajero(Persona):
    cantidad_millas=None
    vip=False
    necesidad_especial =None

    def cantidadMillas(self,cant_millas):
        self.cantidad_millas=cant_millas

    def Vip(self,vip):
        self.vip=True

    def necesidadEspecial(self,nec_especial):
        self.necesidad_especial=nec_especial


