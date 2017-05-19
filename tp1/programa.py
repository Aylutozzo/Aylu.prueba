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

personas=open("/home/alumno/Descargas/personas.dat","r")
for line in personas:
    lista_personas = line.split("|")
    unPasajero= Pasajero()
    unServicio=Servicio()

    if lista_personas[0]== "pasajero":
        unPasajero.tipo = lista_personas[0]
        unPasajero.nombre = lista_personas[1]
        unPasajero.apellido = lista_personas[2]
        unPasajero.fecha_nacimiento = lista_personas[3]
        unPasajero.dni = lista_personas[4]
        unPasajero.vip = lista_personas[5]
        # unPasajero.necesidad_especial=lista_pasajero[6]
       lista_pasajero.append(unPasajero)

    elif lista_personas[0]=="servicio":
        unServicio.nombre=lista_personas[1]
        unServicio.apellido=lista_personas[2]
        unServicio.fecha_nacimiento=lista_personas[3]
        unServicio.dni=lista_personas[4]
       # unServicio.codigo=lista_personas[5].split(",")
        unServicio.idioma=lista_personas[6]
        lista_tripulantes.append(unServicio)


    elif lista_personas[0]=="piloto":
        unPiloto.nombre=lista_personas[1]
        unPiloto.apellido=lista_personas[2]
        unPiloto.fecha_nacimiento=lista_personas[3]
        unPiloto.dni=lista_personas[4]
        #unPiloto.codigo=lista_personas[5].split(",")#


personas.close()

