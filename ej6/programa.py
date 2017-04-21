from empresa import Empresa
from .Camioneta import Camioneta
from .auto import Auto

c=Camioneta()
c.capacidad_carga=50
c.patente="aa000aa"

a=auto()
a.descapotable= True

print(a.descapotanble)
print(c.patente)
print(c.capacidad_carga)

