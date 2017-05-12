class  Persona (object):
    nombre= " "
    apellido= " "
    dni= None

    def setNombre (self, nombre):
        self.nombre= str(nombre)

    def setApellido(self,apellido):
        self.apellido= str(apellido)

    def Dni(self,dni):
        self.dni= dni

    def getDescuento(self):
        return 0
