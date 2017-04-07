from Clases.equipos import Equipo
from Clases.torneo import Torneo
from Clases.jugador import Jugador
from datetime import date

elTorneo= Torneo ()
jugador1=Jugador()
jugador2=Jugador()
jugador3=Jugador()
jugador4=Jugador()
jugador5=Jugador()
jugador6=Jugador()
equipo1=Equipo()
equipo2=Equipo()


jugador1.setNombre("Ponzio")
jugador1.Fecha_de_nacimiento(date(1995,5,12))
jugador1.setNum_camiseta(11)

jugador2.setNombre("Alario")
jugador2.Fecha_de_nacimiento(date(1986,8,5))
jugador2.setNum_camiseta(10)

jugador3.setNombre("Driusi")
jugador3.Fecha_de_nacimiento(date(1986,8,5))
jugador3.setNum_camiseta(10)

jugador4.setNombre("Mora")
jugador4.Fecha_de_nacimiento(date(1986,8,3))
jugador4.setNum_camiseta(10)

jugador5.setNombre("Mascherano")
jugador5.Fecha_de_nacimiento(date(1986,8,8))
jugador5.setNum_camiseta(10)

jugador6.setNombre("Messi")
jugador6.Fecha_de_nacimiento(date(1986,8,16))
jugador6.setNum_camiseta(10)

equipo1.setNombreEquipo("river")
equipo1.setCapitan(jugador1)

equipo2.setNombreEquipo("argentina")
equipo2.setCapitan(jugador6)

elTorneo.Agregar_equipo(equipo1)
elTorneo.Agregar_equipo(equipo2)

print (jugador1.nombre)
print (jugador1.num_camiseta)

