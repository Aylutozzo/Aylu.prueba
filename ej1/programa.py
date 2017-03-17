from alumnos.alumno import Alumno
from datetime import date

a = Alumno()
a.setNombre = ("aylu")
a.setAapellido = ("Tozzo")
a.setFecha_nacimiento = (date(2000, 4, 26))
a.agregar_nota(4)
a.agregar_nota(5)

print(a.promedio())
