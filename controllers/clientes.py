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
    if request.args:
        session.plan_id = request.args[0]
    if request.vars.costo:
        session.costo = request.vars.costo
        redirect(URL(c="clientes",f="datosUbicacion"))
    return {"precio": db(db.costos_instalaciones.id>0).select()}

def vistaFormulario():
    costo= db(db.costos_instalaciones.id == session.costo).select(db.costos_instalaciones.precio).first()
    plan= db(db.planes.id == session.plan_id).select(db.planes.velocidad_de_bajada).first()
    localidad= db(db.localidades.id == session.localidad).select(db.localidades.localidad).first()
    if request.vars:
        redirect(URL(c="clientes",f="cierreFormulario"))
    return dict (costo=costo,plan=plan,localidad=localidad)

def datosUbicacion():
    if request.vars.localidad:
        session.localidad = request.vars.localidad
        session.direccion = request.vars.direccion
        session.num_calle = request.vars.num_calle
        session.calle1 = request.vars.calle1
        session.calle2 = request.vars.calle2
        redirect(URL(c="clientes",f="datosPersonales"))
    return {"localidades": db(db.localidades.id>0).select()}

def datosPersonales():
    if request.vars.dni:
        session.dni = request.vars.dni
        session.nombre = request.vars.nombre
        session.apellido = request.vars.apellido
        redirect(URL(c="clientes",f="datosContacto"))
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



def datosContacto():
    d = 4
    return dict(datos=d)

def consulta():
    d=4
    return dict(datos=d)

def cierreFormulario():
    d=4
    return dict(datos=d)
