class Jugador(object):
    nombre=""
    fecha_nacimiento= None
    num_camiseta= None

    def setNombre (self, n)   :
        self.nombre= str(n)

    def setNum_camiseta(self, numero):
        self.num_camiseta = numero

    def Fecha_de_nacimiento(self, fecha_nac):
        self.fecha_nacimiento=fecha_nac


