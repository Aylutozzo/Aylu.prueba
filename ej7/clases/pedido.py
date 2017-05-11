from plato import Platos
from persona import Persona

class Pedido(object):
    fecha_creacion= None
    entregado=False
    persona= None
    plato= None
    dia= None
    hora=None


    def fecha_creacion(self,fecha_creacion):
        self.fecha_creacion= fecha_creacion

    def entregado(self):
        self.entregrado=True

    def agregarPersona(self,person):
        self.persona=person

    def agregarPlato(self, plato):
        self.plato=plato

    def dia(self,dia):
        self.dia=dia

    def hora(self,hora):
        self.hora=hora
