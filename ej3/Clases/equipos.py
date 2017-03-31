class Equipo (object):
    nombreE=""
    disponibilidad=None
    capitan=None
    lista_jugadores=[]
    barrio=None


    def setNombreEquipo (self,Ne):
        self.nombre= str(Ne)

    def setCapitan(self, capitan):
        if capitan in self.lista_jugadores:
            self.capitan = capitan
            return True
        return False

    def AgregarJugador(self,jugador):
        self.lista_jugadores.append(jugador)




