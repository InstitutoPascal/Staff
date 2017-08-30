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

def cobertura():
    return dict()

def tipoInstalacion():
    if request.vars.seleccion:
        session.tipo_inst = request.vars.seleccion
        redirect(URL(c="clientes",f="datosUbicacion"))
    return {}

def descripcionPlan():
    d = 4
    return dict(datos=d)

def descripcionPlan2():
    d = 4
    return dict(datos=d)

def descripcionPlan3():
    d = 4
    return dict(datos=d)

def descripcionPlan4():
    d = 4
    return dict(datos=d)

def datosUbicacion():
    if request.vars.localidad:
        session.localidad = request.vars.localidad
        session.direccion = request.vars.direccion
        session.num_calle = request.vars.num_calle
        session.entre_calle1 = request.vars.entre_calle_1
        session.entre_calle2 = request.vars.entre_calle_2
        redirect(URL(c="clientes",f="datosPersonales"))
    return {}


def datosPersonales():
    d = 4
    return dict(datos=d)

def datosContacto():
    d = 4
    return dict(datos=d)

def consulta():
    d=4
    return dict(datos=d)

def cierreFormulario():
    d=4
    return dict(datos=d)
