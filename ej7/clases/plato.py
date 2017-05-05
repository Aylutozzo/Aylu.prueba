class Platos (object):
    nombre_plato= " "
    precio= None
    lista_platos=[]

    def agregarPlato(self,plato_nombre):
        self.nombre_plato= plato_nombre

    def agregarPrecio(self.plato_precio):
        self.precio= plato_precio

    def agregarPlato(self,nombre):
        self.lista_platos.append(nombre)


    def platosacocinar(self,nombre, dia, precio, descuento):
        for item in self.lista_platos:
