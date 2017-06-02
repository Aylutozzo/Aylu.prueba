from clases.personas import Persona
from clases.avion import Avion
from clases.pasajero import Pasajero
from clases.piloto import Piloto
from clases.servicio import Servicio
from clases.tripulantes import Tripulantes
from clases.vuelos import Vuelos
from datetime import date

lista_pasajero=[]
lista_tripulantes=[]
aux=None

def AgregarAviones():
    a = open("/home/alumno/Descargas/aviones.dat", "r")
    for line in a:
        unAvion=Avion()
        a=line.split("|")
        unAvion.Codigo(a[0])
        unAvion.cantidadPsajero(a[1])
        unAvion.cantidadTripulantes(a[2])
    aviones.closes

def AgregarPersonas():
    p=open("/home/alumno/Descargas/personas.dat","r")
    for line in p:
        unaPiloto=Piloto()
        unPasajero= Pasajero()
        unServicio=Servicio()
        p=line.split("|")
        if p[0]== "Pasajero":
            unPasajero.setNombre (p[1])
            unPasajero.setApellido (p[2])
            unPasajero.fechaNacimiento (p[3])
            unPasajero.Dni = (p[4])
            unPasajero.Vip = (p[5])
            unPasajero.necesidadEspeciall(p[6])
            p.append(unPasajero)

        elif p[0]=="servicio":
            unServicio.setNombre(p[1])
            unServicio.setApellido(p[2])
            unServicio.fechaNacimiento(p[3])
            unServicio.Dni(p [4])
            x.p[5].split(",")
            for imten in Codigo
                if item.Codigo==
            unServicio.Codigo=(p[5]).split(",")
            unServicio.Idioma=(p[6])
            p.append(unServicio)


        elif p[0]=="piloto":
            unPiloto.setNombre(p[1])
            unPiloto.setApellido(p[2])
            unPiloto.fechaNacimiento(p[3])
            unPiloto.Dni(p[4])
            x.p[5].split(",")
            for imten in lista_aviones:
                if avion.codigo== item:
                    unaPiloto.Codigo (avion)
            p.append(unPiloto)

personas.close()

def AgregarVuelos():
    v= open("/home/alumno/Descargas/vuelos.dat."r"")
    unVuelo=Vuelos
    v=line.split("|")
    unVuelo.Avion(v[0])
    unVuelo.Dia(v[1])
    unVuelo.Hora(v[2])
    unVuelo.Destino(v[3])
    unVuelo.Origen(v[4])

