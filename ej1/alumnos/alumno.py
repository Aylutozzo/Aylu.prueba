class Alumno (object):

    nombre = " "
    apellido = " "
    fecha_nac= None
    lista_notas = [ ]

    def setNombre(self,n):
        self.nombre =str(n)

    def setApellido(self,a):
        self.apellido = str(a)

    def setFecha_nacimiento(self,fecha):
        self.fecha_nac= fecha

    def agregar_nota (self, nota):
        self.lista_notas.append(nota)

    def menor_nota (self):
        return min (self.lista_notas)

    def mayor_nota(self):
        return max(self.lista_notas)

    def promedio (self):
        return (sum(self.lista_notas))/ len(self. lista_notas)


