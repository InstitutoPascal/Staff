# -*- coding: utf-8 -*-

@auth.requires_membership(role="Tecnicos")
def inicio(): return dict(message="hello from tecnicos.py")

######################################### SOLICITUDES DE INSTALACION #########################################

def solicitudesInstalacionDiaActual():
    import datetime
    fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d")
    #Solo funciona si se loguean
    tecnico_logueado = db(db.auth_user.id == auth.user_id).select(db.auth_user.id)[0].id
    resultado = db((db.solicitudes_instalacion.fecha_estimada == fecha_hoy)&(db.solicitudes_instalacion.tecnico == tecnico_logueado)&(db.solicitudes_instalacion.localidad == db.localidades.id)&(db.solicitudes_instalacion.tipo_de_plan == db.planes.id)&(db.solicitudes_instalacion.costo_de_instalacion == db.costos_instalaciones.id)&(db.solicitudes_instalacion.estado == 'Pendiente')).select(db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.solicitudes_instalacion.ALL)
    i=0
    for x in resultado:
         i=i+1
    return dict(datos=resultado, cantidad=i)

def solicitudesInstalacionTodas():
    #Solo funciona si se loguean
    tecnico_logueado = db(db.auth_user.id == auth.user_id).select(db.auth_user.id)[0].id
    resultado = db((db.solicitudes_instalacion.tecnico == tecnico_logueado)&(db.solicitudes_instalacion.fecha_estimada != None)&(db.solicitudes_instalacion.localidad == db.localidades.id)&(db.solicitudes_instalacion.tipo_de_plan == db.planes.id)&(db.solicitudes_instalacion.costo_de_instalacion == db.costos_instalaciones.id)&(db.solicitudes_instalacion.estado == 'Pendiente')).select(db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.solicitudes_instalacion.ALL)
    i=0
    for x in resultado:
         i=i+1
    return dict(datos=resultado, cantidad=i)

def busquedaSolicitudInstalacion():
    dni_recibido=request.vars.dni
    tecnico_logueado = db(db.auth_user.id == auth.user_id).select(db.auth_user.id)[0].id
    resultado = db((db.solicitudes_instalacion.tecnico == tecnico_logueado)&(db.solicitudes_instalacion.fecha_estimada != None)&(db.solicitudes_instalacion.dni == dni_recibido)&(db.solicitudes_instalacion.localidad == db.localidades.id)&(db.solicitudes_instalacion.tipo_de_plan == db.planes.id)&(db.solicitudes_instalacion.costo_de_instalacion == db.costos_instalaciones.id)&(db.solicitudes_instalacion.estado == 'Pendiente')).select(db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.solicitudes_instalacion.ALL)
    if resultado:
        return dict(datos= resultado)
    else:
        return dict(datos=0)

def solicitudesInstalacionDetalles():
    id_solicitud = request.args[0]
    resultado = db((db.solicitudes_instalacion.id == id_solicitud)&(db.solicitudes_instalacion.localidad == db.localidades.id)&(db.solicitudes_instalacion.tipo_de_plan == db.planes.id)&(db.solicitudes_instalacion.costo_de_instalacion == db.costos_instalaciones.id)).select(db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.solicitudes_instalacion.ALL)
    return dict(datos=resultado)

def alta_instalacion():
    id_solicitud = request.args[0]
    nombre = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.nombre).first().nombre
    apellido = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.apellido).first().apellido
    form = SQLFORM(db.instalaciones)
    form.vars.numero_de_solicitud = id_solicitud
    if form.accepts(request.vars, session):
        redirect(URL(c="tecnicos", f="agregar_cliente", args=(id_solicitud,)))
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form, nom=nombre, ape=apellido)

def agregar_cliente():
    id_solicitud = request.args[0]
    id_instalacion = db().select(db.instalaciones.id).last().id
    datos_solicitud = db(db.solicitudes_instalacion.id == id_solicitud).select().first()
    db.clientes.insert(numero_de_instalacion=id_instalacion,
                       nombre= datos_solicitud.nombre,
                       apellido= datos_solicitud.apellido,
                       dni= datos_solicitud.dni,
                       direccion= datos_solicitud.direccion,
                       numero_de_calle= datos_solicitud.numero_de_calle,
                       latitud = datos_solicitud.latitud,
                       longitud = datos_solicitud.longitud,
                       entre_calle_1 = datos_solicitud.entre_calle_1,
                       entre_calle_2 = datos_solicitud.entre_calle_2,
                       localidad = datos_solicitud.localidad,
                       telefono = datos_solicitud.telefono,
                       telefono_alternativo = datos_solicitud.telefono_alternativo,
                       correo_electronico = datos_solicitud.correo_electronico,
                       tipo_de_plan = datos_solicitud.tipo_de_plan)
    redirect(URL(c="tecnicos", f="cambiar_estado_solicitudInstalacion", args=(id_solicitud)))

def cambiar_estado_solicitudInstalacion():
    id_solicitud = request.args[0]
    db(db.solicitudes_instalacion.id == id_solicitud).update(estado='Finalizado')
    redirect(URL(c="tecnicos", f="confirmacionNuevoCliente", args=(id_solicitud)))

def confirmacionNuevoCliente():
    id_solicitud = request.args[0]
    nombre = db(db.solicitudes_instalacion.id == id_solicitud).select(db.solicitudes_instalacion.nombre).first().nombre
    apellido = db(db.solicitudes_instalacion.id == id_solicitud).select(db.solicitudes_instalacion.apellido).first().apellido
    return dict(nombre=nombre, apellido=apellido)

def ubicacionSolicitanteInstalacion():
    id_solicitud = request.args[0]
    rows=db((db.solicitudes_instalacion.id == id_solicitud)&(db.solicitudes_instalacion.localidad==db.localidades.id)).select(
            db.solicitudes_instalacion.nombre,
            db.solicitudes_instalacion.apellido,
            db.solicitudes_instalacion.direccion,
            db.solicitudes_instalacion.numero_de_calle,
            db.localidades.localidad,
            db.solicitudes_instalacion.latitud,
            db.solicitudes_instalacion.longitud)
    x0,y0= COORDS_INICIO_MAPA
    d = dict(x0=x0,y0=y0,rows=rows)
    return response.render(d)

######################################### SOLICITUDES DE SOPORTE #########################################

def solicitudesSoporteDiaActual():
    import datetime
    fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d")
    tecnico_logueado = db(db.auth_user.id == auth.user_id).select(db.auth_user.id)[0].id
    resultado = db((db.solicitudes_soporte.tecnico == tecnico_logueado)&(db.solicitudes_soporte.fecha_estimada == fecha_hoy)&(db.solicitudes_soporte.cliente == db.clientes.id)&(db.clientes.localidad == db.localidades.id)&(db.solicitudes_soporte.estado == 'Pendiente')).select(db.localidades.ALL, db.solicitudes_soporte.ALL, db.clientes.ALL)
    i=0
    for x in resultado:
         i=i+1
    return dict(datos=resultado, cantidad=i)

def solicitudesSoporteTodas():
    tecnico_logueado = db(db.auth_user.id == auth.user_id).select(db.auth_user.id)[0].id
    resultado = db((db.solicitudes_soporte.tecnico == tecnico_logueado)&(db.solicitudes_soporte.cliente == db.clientes.id)&(db.clientes.localidad == db.localidades.id)&(db.solicitudes_soporte.fecha_estimada != None)&(db.solicitudes_soporte.estado == 'Pendiente')).select(db.localidades.ALL, db.solicitudes_soporte.ALL, db.clientes.ALL)
    i=0
    for x in resultado:
         i=i+1
    return dict(datos=resultado, cantidad=i)

def busquedaSolicitudSoporte():
    dni_recibido=request.vars.dni
    tecnico_logueado = db(db.auth_user.id == auth.user_id).select(db.auth_user.id)[0].id
    resultado = db((db.solicitudes_soporte.tecnico == tecnico_logueado)&(db.solicitudes_soporte.fecha_estimada != None)&(db.solicitudes_soporte.cliente == db.clientes.id)&(db.clientes.dni == dni_recibido)&(db.clientes.localidad == db.localidades.id)&(db.solicitudes_soporte.estado == 'Pendiente')).select(db.localidades.ALL, db.solicitudes_soporte.ALL, db.clientes.ALL)
    if resultado:
        return dict(datos= resultado)
    else:
        return dict(datos=0)

def solicitudesSoporteDetalles():
    id_solicitud = request.args[0]
    resultado = db((db.solicitudes_soporte.id == id_solicitud)&(db.solicitudes_soporte.cliente == db.clientes.id)&(db.clientes.tipo_de_plan == db.planes.id)&(db.clientes.localidad == db.localidades.id)).select(db.clientes.ALL, db.localidades.ALL, db.planes.ALL, db.solicitudes_soporte.ALL)
    return dict(datos=resultado)

def ubicacionSolicitanteSoporte():
    id_solicitud = request.args[0]
    rows=db((db.clientes.id == id_solicitud)&(db.clientes.localidad==db.localidades.id)).select(
            db.clientes.nombre,
            db.clientes.apellido,
            db.clientes.direccion,
            db.clientes.numero_de_calle,
            db.localidades.localidad,
            db.clientes.latitud,
            db.clientes.longitud)
    x0,y0= COORDS_INICIO_MAPA
    d = dict(x0=x0,y0=y0,rows=rows)
    return response.render(d)

def alta_soporte():
    id_solicitud = request.args[0]
    nombre = db((id_solicitud == db.solicitudes_soporte.id)&(db.solicitudes_soporte.cliente==db.clientes.id)).select(db.clientes.nombre)[0].nombre
    apellido = db((id_solicitud == db.solicitudes_soporte.id)&(db.solicitudes_soporte.cliente==db.clientes.id)).select(db.clientes.apellido)[0].apellido
    form = SQLFORM(db.soportes)
    form.vars.numero_de_solicitud = id_solicitud
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
        redirect(URL(c="tecnicos", f="cambiar_estado_solicitudSoporte", args=(id_solicitud, nombre, apellido)))
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form, nom=nombre, ape=apellido)

def cambiar_estado_solicitudSoporte():
    id_solicitud = request.args[0]
    nombre = request.args[1]
    apellido = request.args[2]
    db(db.solicitudes_soporte.id == id_solicitud).update(estado='Finalizado')
    redirect(URL(c="tecnicos", f="confirmacionNuevoSoporte", args=(nombre, apellido)))

def confirmacionNuevoSoporte():
    nombre= request.args[0]
    apellido= request.args[1]
    return dict(nombre=nombre, apellido=apellido)

######################################### MANTENIMIENTOS #########################################

def alta_mantenimientos():
    form = SQLFORM(db.mantenimientos)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def mantenimientosRealizados():
    d = 4
    return dict(datos=d)

def mantenimientosDetalles():
    d=4
    return dict(datos=d)

######################################### OTRAS #########################################

def mapaSolicitudesInstalacion():
    rows=db((db.solicitudes_instalacion.id>0)&(db.solicitudes_instalacion.estado == 'Pendiente')&(db.solicitudes_instalacion.localidad==db.localidades.id)).select(
            db.solicitudes_instalacion.nombre,
            db.solicitudes_instalacion.apellido,
            db.solicitudes_instalacion.direccion,
            db.solicitudes_instalacion.numero_de_calle,
            db.solicitudes_instalacion.localidad,
            db.solicitudes_instalacion.latitud,
            db.solicitudes_instalacion.longitud)
    x0,y0= COORDS_INICIO_MAPA
    d = dict(x0=x0,y0=y0,rows=rows)
    return response.render(d)

def mapaSoportes():
    d=4
    return dict(datos=d)
