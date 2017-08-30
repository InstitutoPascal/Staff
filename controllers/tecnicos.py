# -*- coding: utf-8 -*-
# intente algo como


def alta_mantenimientos():
    form = SQLFORM(db.mantenimientos)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def alta_historiales():
    form = SQLFORM(db.historiales)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def agregar_cliente():
    id_instalacion = request.args[0]
    dni = db(id_instalacion == db.instalaciones.id).select(db.instalaciones.dni)[0].dni
    nombre = db(id_instalacion == db.instalaciones.id).select(db.instalaciones.nombre)[0].nombre
    apellido = db(id_instalacion == db.instalaciones.id).select(db.instalaciones.apellido)[0].apellido
    localidad = db(id_instalacion == db.instalaciones.id).select(db.instalaciones.localidad)[0].localidad
    calle = db(id_instalacion == db.instalaciones.id).select(db.instalaciones.direccion)[0].direccion
    numero_calle = db(id_instalacion == db.instalaciones.id).select(db.instalaciones.numero_de_calle)[0].numero_de_calle
    latitud = db(id_instalacion == db.instalaciones.id).select(db.instalaciones.latitud)[0].latitud
    longitud = db(id_instalacion == db.instalaciones.id).select(db.instalaciones.longitud)[0].longitud
    entre_calle_1 = db(id_instalacion == db.instalaciones.id).select(db.instalaciones.entre_calle_1)[0].entre_calle_1
    entre_calle_2 = db(id_instalacion == db.instalaciones.id).select(db.instalaciones.entre_calle_2)[0].entre_calle_2
    plan = db(id_instalacion == db.instalaciones.id).select(db.instalaciones.tipo_de_plan)[0].tipo_de_plan
    telefono = db(id_instalacion == db.instalaciones.id).select(db.instalaciones.telefono)[0].telefono
    form=SQLFORM(db.clientes)
    form.vars.dni = dni
    form.vars.nombre = nombre
    form.vars.apellido = apellido
    form.vars.localidad = localidad
    form.vars.direccion = calle
    form.vars.numero_de_calle = numero_calle
    form.vars.latitud = latitud
    form.vars.longitud = longitud
    form.vars.entre_calle_1 = entre_calle_1
    form.vars.entre_calle_2 = entre_calle_2
    form.vars.telefono = telefono
    form.vars.tipo_de_plan = plan
    if form.accepts(request.vars, session):
        redirect(URL(c="tecnicos", f="editar_instalacion", args=(id_instalacion, )))
        session.flash = 'Formulario modificado'
    elif form.errors:
		response.flash = 'El formulario tiene errores'
    else:
		response.flash = 'Modifique el formulario'
    return dict(f=form, nom=nombre, ape=apellido)

def editar_instalacion():
    id_instalacion = request.args[0]
    db(db.instalaciones.id == id_instalacion).update(estado='Finalizado')
    redirect(URL(c="tecnicos", f="inicio"))


def inicio():
    d = 4
    return dict(datos=d)



def busquedaInstalacion():
    dni_recibido=request.vars.dni
    resultado = db((db.instalaciones.dni == dni_recibido)&(db.instalaciones.localidad == db.localidades.id)&(db.instalaciones.tipo_de_plan == db.planes.id)&(db.instalaciones.costo_de_instalacion == db.costos_instalaciones.id)&(db.instalaciones.estado == 'Pendiente')).select(db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.instalaciones.ALL)
    if resultado:
        return dict(datos= resultado)
    else:
        return dict(datos=0)

def busquedaSoporte():
    d = 4
    return dict(datos=d)

def instalacionesDiaActual():
    #La siguiente busqueda debe tener filtro de dia actual
    resultado = db((db.instalaciones.localidad == db.localidades.id)&(db.instalaciones.tipo_de_plan == db.planes.id)&(db.instalaciones.costo_de_instalacion == db.costos_instalaciones.id)&(db.instalaciones.estado == 'Pendiente')).select(db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.instalaciones.ALL)
    i=0
    for x in resultado:
         i=i+1
    return dict(datos=resultado, cantidad=i)


def instalacionesTodas():
    resultado = db((db.instalaciones.localidad == db.localidades.id)&(db.instalaciones.tipo_de_plan == db.planes.id)&(db.instalaciones.costo_de_instalacion == db.costos_instalaciones.id)&(db.instalaciones.estado == 'Pendiente')).select(db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.instalaciones.ALL)
    i=0
    for x in resultado:
         i=i+1
    return dict(datos=resultado, cantidad=i)




def soportesDiaActual():
    d = 4
    return dict(datos=d)



def soportesTodas():
    d = 4
    return dict(datos=d)

def mantenimientosRealizados():
    d = 4
    return dict(datos=d)

def instalacionesDetalles():
    instalacion_id = request.args[0]
    resultado = db((db.instalaciones.id == instalacion_id)&(db.instalaciones.localidad == db.localidades.id)&(db.instalaciones.tipo_de_plan == db.planes.id)&(db.instalaciones.costo_de_instalacion == db.costos_instalaciones.id)).select(db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.instalaciones.ALL)
    return dict(datos=resultado)

def mantenimientosDetalles():
    d=4
    return dict(datos=d)

def mapaInstalaciones():
    rows=db((db.instalaciones.id>0)&(db.instalaciones.estado == 'Pendiente')&(db.instalaciones.localidad==db.localidades.id)).select(
            db.instalaciones.nombre,
            db.instalaciones.apellido,
            db.instalaciones.direccion,
            db.instalaciones.numero_de_calle,
            db.localidades.localidad,
            db.instalaciones.latitud,
            db.instalaciones.longitud)
    x0,y0= COORDS_INICIO_MAPA
    d = dict(x0=x0,y0=y0,rows=rows)
    return response.render(d)


def mapaSoportes():
    d=4
    return dict(datos=d)

def ubicacionSolicitante():
    instalacion_id = request.args[0]
    rows=db((db.instalaciones.id == instalacion_id)&(db.instalaciones.localidad==db.localidades.id)).select(
            db.instalaciones.nombre,
            db.instalaciones.apellido,
            db.instalaciones.direccion,
            db.instalaciones.numero_de_calle,
            db.localidades.localidad,
            db.instalaciones.latitud,
            db.instalaciones.longitud)
    x0,y0= COORDS_INICIO_MAPA
    d = dict(x0=x0,y0=y0,rows=rows)
    return response.render(d)
