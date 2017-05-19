class Persona (object):
    nombre=None
    apellido=None
    fecha_nacimiento=None
    dni=None
    tipo=None

    def setNombre(self,nombre):
        self.nombre=str(nombre)

    def setApellido(self,apellido):
        self.apellido=str(apellido)

    def fechaNacimeinto(self,fecha_nac):
        self.fecha_nacimiento=fecha_nac

    def Dni(self,dni):
        self.dni=dni

    def tipo(self,tipo):
        self.tipo=tipo


