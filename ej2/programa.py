
from clases.alumno import Alumno
from clases.materia import Materia

unAlumno=Alumno()
otroAlumno=Alumno()

unAlumno.set_apellido("Perez")
unAlumno.set_nombre("Godofredo")

materia1=Materia()
materia1.set_nombre("Castellano")
unAlumno.agregar_materia(materia1)
materia1.agregar_nota(5)
materia1.agregar_nota(4)

materia2=Materia()
materia2.set_nombre("Laboratorio I")
materia2.agregar_nota(5)
unAlumno.agregar_materia(materia2)

print(unAlumno.menor_promedio())
print(unAlumno.promedio_general())

