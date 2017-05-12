from clases.alumno import Alumno
from clases.profesores import Profesor
from clases.plato import Platos
from clases.pedido import Pedido
from date import datetime

lista_alumno=[]
lista_profesor=[]
lista_pedidos=[]
lista_platos=[]
lista_personas=[]

opcion=None
opcion2= None
opcion3= None
n= None #nombre personas
a= None
div= None
dni= None
desc= None

nombreplato=None #nombre del plato a buscar
np= None #nombre del plato a cambiar
p=None #precio del plato
nombreplato=None

dia=None #dia
fechac=None # fecha de creacion
plato=None #plato
persona=None #persona
entregado=bool #entregado


def agregarAlumno(n,a,div,dni):
    unAlumno= Alumno()
    unAlumno.setNombre=n
    unAlumno.setApellido= a
    unAlumno.Dni=dni
    unAlumno.Division= div
    lista_alumno.append(unAlumno)

def agregarProfesor(n, a, desc,dni):
    unProfesor= Profesor()
    unProfesor.setNombre= n
    unProfesor.setApellido= a
    unProfesor.Dni= dni
    unProfesor.getDescuento= desc
    lista_alumno.append(unProfesor)

def modificarAlumno(n, dni, a, div):
    for item1 in lista_personas:
        if type[i tem] is Alumno:
            if item.dni==dni:
                item.setNombre = n
                item.setAapellido = a
                item.Division = div

        elif type [item] is Profesor:
            if item.dni==dni:
                item.setNombre= n
                item.setApellido= a
                item.getDescuento= desc

def eliminarAlumno(dni):
    if type[item] is Alumno
         for item in lista_personas:
             if item.dni= dni
             lista_personas.remove(item)

def eliminarProfesor(dni):
    if type[item] is Profesor:
         for item in lista_personas:
             if item.dni==dni:
             lista_personas.remove(item)

def agregarPlatos(np, p):
    plato=Platos()
    plato.agregarPlato=np
    plato.agregarPrecio=p
    lista_platos.append(plato)

def modificarPlato(nombreplato,np, p):
    for item in lista_platos:
        if item.nombre==nombreplato:
            print("ingrese que desea modiicar")
            print("1: nombre")
            print("2: precio")
            opcion3= input()
            if opcion3==1:
                item.nombre=np
            if opcion3==2:
                item.precio=p

def eliminarPlato(nombre):
    for item in lista_platos:
        if item.nombre==nombre:
            lista_platos.remove(item)

def agregarPedido(dia, fehcac,plato, persona, entrega, hora, idpedido):
    pedido= Pedido()
    pedido.dia=dia
    pedido.fecha_creacion=fechac
    pedido.agregarPlato=plato
    pedido.persona=persona
    pedido.entregado=entrega
    pedido.hora=hora
    pedido.id_pedido=idpedido

def modificarPedido(fehcac,plato, persona, hora, idpedido):
    for item in lista_pedidos:
        if item.id_pedido == idpedido:
            item.plato= plato
            item.fecha_creacion= fechac
            item.persona= persona
            item.hora=hora

def eliminarPedido(idpedido):
    for item in lista_pedidos:
        if item.id_pedido==idpedido:
            lista_pedidos.remove(item)

print("menu buffes")
print(\n)
print ("elija opcion:")

print("opcion1: agregar persona")
print("opcion2: modificar persona")
print("opcion3: eliminar persona")
print("opcion4: agregar plato")
print("opcion5: modificar plato")
print("opcion6: eliminar plato")
print("opcion7: agregar pedido")
print("opcion8: modificar pedido")
print("opcion9: eliminar pedido")

opcion= input()

if opcion==1:
    print("elija a quien quiere agregar")
    print("1: alumno")
    print("2: persona")
    opcion2= input()
    if opcion2==1:
        agregarAlumno(n, a, div, dni)
    elif opcion2==2
        agregarProfesor(n, a,dni, desc)

elif opcion==2:
    print("elija a quien quiere modificar")
    print("1: alumno")
    print("2: persona")
    opcion2 = input()

    if opcion2 == 1: #alumno
        print("nombre")
        n=input()
        print("apellido")
        a= input()
        print("dni")
        dni= input()
        print("division")
        div= input()
        modificarAlumno(n, dni,a, div):

    elif opcion2 == 2: #alumno
        print("nombre")
        n=input()
        print("apellido")
        a= input()
        print("dni")
        dni= input()
        print("descuento")
        desc= input()
        modificarProfesor(n, dni,a, div)

elif opcion==3:
    print("elija a quien quiere eliminar")
    print("1: alumno")
    print("2: persona")
    opcion2 = input()

    if opcion2==1 # alumno
        print("dni")
        dni = input()
        eliminarAlumno(dni)

    elif opcion2==2 #profesores
        print("dni")
        dni=input()
        eliminarProfesor(dni)

elif opcion==4:
    print("nombre")
    np=input()
    print("precio")
    p=input()
    agregarPlatos(np, p)

elif opcion==5:
    print("nombre")
    nombre=input()
    print("precio")
    precio=input()
    modificarPlato(nombreplato, np, p)

elif opcion==6:
    print("plato")
    plato=input()
    eliminarPlato(nombre)

elif opcion==7:
    print("id_pedido")
    idpedido=input()
    print("dia")
    dia=input()
    print("plato")
    plato=input()
    print("persona")
    persona=input()
    print("fecha de creacion")
    fechac=input()
    print("hora")
    hora=input()
    agregarPedido(dia, fechac, plato, persona, hora, idpedido):

elif opcion==8:
    print("plato")
    plato=input()
    print("persona")
    persona=input()
    print("fecha ")
    fechac=input()
    print("hora")
    hora=input()

    modificarPedido(fehcac, plato, persona, hora, idpedido):

elif opcion==9:
    print("id_pedido")
    idpedido=input()
    eliminarPedido(idpedido)