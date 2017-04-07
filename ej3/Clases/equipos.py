class Equipo (object):
    nombreE=""
    lista_disponibilidad=None
    capitan=None
    lista_jugadores=[]
    barrio=None

    def __init__(self):
        self.lista_jugadores = []
        self.lista_disponibilidad=[[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False]]

    def setNombreEquipo (self,Ne):
        self.nombre= str(Ne)

    def setCapitan(self, capitan):
        if capitan in self.lista_jugadores:
            self.capitan = capitan
            return True
        return False

    def AgregarJugador(self,jugador):
        self.lista_jugadores.append(jugador)
        for item in self.lista_jugadores:
            if item.num_camiseta == numero_camiseta
                return False
            self.lista_jugadores.append(jugador)
                return True

    def AgregarDisponibilidad(self,dia,turno):
        self.disponibilidad[dia][turno]=True


