from empresa import Empresa
from .Camioneta import Camioneta
from .auto import Auto

c=Camioneta()
c.capacidad_carga=50
c.patente="aa000aa"

a=auto()
a.descapotanle= True

print(a.descapotanle)
print(c.patente)
print(c.capacidad_carga)
print(a.patente)
