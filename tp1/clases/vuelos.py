class Vuelos (object):
    avion=None
    lista_pasajeros=[]
    lista_tripulantes=[]
    dia=None
    hora=None
    origen=None
    destino=None

    def Avion(self,avion):
        self.avion=avion

    def __init__(self):
        self.lista_pasajeros = []
        self.lista_tripulantes = []

    def agregarPasajeros(self):
        self.lista_pasajeros.append()

    def agregarTripulantes(self):
        self.lista_tripulantes.append()

    def Dia(self, dia):
        self.dia = dia

    def Hora(self, hora):
        self.hora = hora

    def Origen (self,origen):
        self.origen=origen

    def Destino(self,destino):
        self.destino=destino


    def Nomina (self):
        lista_personas=[]
        for item in self.lista_pasajeros:
            self.lista_personas.append(item)
        for item in self.lista_tripulantes:
            self.lista_personas.append(item)

        return lista_personas

    def Personas_vip_especiales(self):
        lista_Pvip=[]
        lista_Pespecial=[]
        for item in self.lista_pasajeros:
            if item.Vip==True:
                self.lista_Pvip.append(item)
            if item.necesidadEspecial!= None
                self.lista_Pespecial.append(item)

        return lista_Pespecial , lista_Pvip

    def sinTriupulacionMinima(self):
        Tripulacion_minima=True
        if len(self.lista_tripulantes)<self.avion.cantidad_tripulantes
            Tripulacion_minima= False

        return Tripulacion_minima

    def Persona_mas_joven(self):
        aux = self.lista_pasajeros[1].fecha_nac
        persona_aux = None
        for item in self.lista_pasajeros:
            if item.fecha_nac > aux:
                aux = item.fecha_nac
                persona_aux = item
        return persona_aux



    def EstaAutorizado(self):
        autorizado = None
        for item in self.lista_tripulantes:
            for item2 in item.modelos_avion:
                if item2 == self.avion.codunico:
                    aux = True
                aux = False
            return autorizado


