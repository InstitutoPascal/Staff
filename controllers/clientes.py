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


def datosContacto():
    if request.vars.tel:
        session.tel = request.vars.tel
        session.tel2 = request.vars.tel2
        session.email = request.vars.email
        redirect(URL(c="clientes",f="vistaFormulario"))
    return {}

def cierreFormulario():
    db.solicitudes_instalacion.insert(
                 costo_de_instalacion = session.costo,
                 dni = session.dni,
                 nombre =session.nombre,
                 apellido =session.apellido,
                 tipo_de_plan=session.plan_id,
                 localidad =session.localidad,
                 direccion=session.direccion,
                 numero_de_calle =session.num_calle,
                 entre_calle_1 =session.calle1,
                 entre_calle_2 =session.calle2,
                 telefono =session.tel,
                 telefono_alternativo =session.tel2,
                 correo_electronico =session.email
                 )
    session.flash= "Codigo OK!"
    return {}

def consulta():
    reg = db(db.clientes.dni == request.vars.dni_soporte).select(db.clientes.id).first()
    if reg:
        session.dni_soporte = request.vars.dni_soporte
        session.email_soporte = request.vars.email_soporte
        session.comentario_soporte = request.vars.comentario_soporte
        db.solicitudes_soporte.insert(
            cliente=reg)
        response.flash= 'Se envio'

    else:
        response.flash='El dni ingresado no pertence a un cliente nuestro'
    return {}
