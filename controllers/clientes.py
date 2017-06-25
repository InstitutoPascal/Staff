# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from clientes.py")

def inicio():
    d = 4
    return dict(datos=d)



def listadoPlanes():
    datosPlanes = db().select(db.planes.ALL)
    i=0
    for x in datosPlanes:
         i=i+1
    return dict (datos=datosPlanes, cantidad=i)

def descripcionPlan():
    d = 4
    return dict(datos=d)

def descripcionPlan2():
    d = 4
    return dict(datos=d)

def datosUbicacion():
    d = 4
    return dict(datos=d)


def datosPersonales():
    d = 4
    return dict(datos=d)

def datosContacto():
    d = 4
    return dict(datos=d)
def consulta():
    d=4
    return dict(datos=d)
