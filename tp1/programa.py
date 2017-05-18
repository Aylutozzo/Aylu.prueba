from clases.personas import Personas
from clases.avion import Avion
from clases.pasajero import Pasajero
from clases.piloto import Piloto
from clases.servicio import Servicio
from clases.tripulantes import Tripulantes
from clases.vuelos import Vuelos



def agregarPasajero(nombre, apellido, fecha_nac, dni,vip, necesidad_especial):
    p=Pasajero()
    p.setNombre (nombre)
    p.setApellido (apellido)
    p.Dni (dni)
    p.fechaNacimiento (fecha_nac)
    p.Vip (vip)
    p.necesidadEspecial (necesidad_especial)

def agregarServiciosTrip(nombre,apellido, fecha_nac, dni,acc_avion, idioma):
    s= Servicio()
    s.setNombre=(nombre)
    s.setApellido (apellido)
    s.Dni (dni)
    s.fechaNacimiento (fecha_nac)
    s.Idioma (idioma)
    s.accesoAvion (acc_avion)

def agregarPilotos(nombre,apellido, fecha_nac,dni):
    p= Piloto()
    p.setNombre=(nombre)
    p.setApellido (apellido)
    p.Dni (dni)
    p.fechaNacimiento (fecha_nac)

def agregarAvion(cant_pasajeros, cant_tripulantes, codigo):
    a=Avion()
    a.Codigo=codigo
    a.cantidadTripulantes=cant_tripulantes
    a.cantidadPasajeros=cant_pasajeros

