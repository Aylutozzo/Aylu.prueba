class Alumno (object):

    nombre = " "
    apellido = " "
    fecha_nac= None
    listaNotas = [ ]
    listaMaterias=[ ]

    def __init__ (self):
        self.lista_materias=[]

    def setNombre(self,n):
        self.nombre =str(n)

    def setApellido(self,a):
        self.apellido = str(a)

    def agregar_materia(self, materia):
        self.listaMaterias.append(material)

    def agregar_nota (self, nota):
        self.listaNotas.append(nota)

    def lista_promedios (self):
        lista=[]
        for item in self.listaMaterias
            lista.append(item.promedio())
        return lista
    def lista_promedios_versionloca (self):
            return (item.promedio() for item in self.listaMateria)

    def menor_nota (self):
        return min (self.listaNotas)

    def mayor_nota(self):
        return max(self.listaNotas)

    def promedio (self):
        return (sum(self.lista_notas))/ len(self. lista_notas)

    def promedio_materias_alumno(self.lista_materias):
        for item in Materiaa
            promedio_nota_materia(self

