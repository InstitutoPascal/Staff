# -*- coding: utf-8 -*-
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
    nombre = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.nombre)[0].nombre
    apellido = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.apellido)[0].apellido
    form = SQLFORM(db.instalaciones)
    form.vars.numero_de_solicitud = id_solicitud
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
        redirect(URL(c="tecnicos", f="agregar_cliente", args=(id_solicitud,)))
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form, nom=nombre, ape=apellido)

def agregar_cliente():
    id_solicitud = request.args[0]
    id_instalacion = db().select(db.instalaciones.id).last().id
    dni = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.dni)[0].dni
    nom = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.nombre)[0].nombre
    ape = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.apellido)[0].apellido
    localidad = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.localidad)[0].localidad
    direccion = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.direccion)[0].direccion
    numero_de_calle = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.numero_de_calle)[0].numero_de_calle
    latitud = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.latitud)[0].latitud
    longitud = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.longitud)[0].longitud
    entre_calle_1 = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.entre_calle_1)[0].entre_calle_1
    entre_calle_2 = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.entre_calle_2)[0].entre_calle_2
    plan = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.tipo_de_plan)[0].tipo_de_plan
    telefono = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.telefono)[0].telefono
    telefono_alternativo = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.telefono_alternativo)[0].telefono_alternativo
    correo = db(id_solicitud == db.solicitudes_instalacion.id).select(db.solicitudes_instalacion.correo_electronico)[0].correo_electronico
    db.clientes.insert(numero_de_instalacion=id_instalacion,
                       nombre=nom,
                       apellido=ape,
                       dni=dni,
                       direccion=direccion,
                       numero_de_calle = numero_de_calle,
                       latitud = latitud,
                       longitud = longitud,
                       entre_calle_1 = entre_calle_1,
                       entre_calle_2 = entre_calle_2,
                       localidad = localidad,
                       telefono = telefono,
                       telefono_alternativo = telefono_alternativo,
                       correo_electronico = correo,
                       tipo_de_plan = plan)
    redirect(URL(c="tecnicos", f="cambiar_estado_solicitudInstalacion", args=(id_solicitud, nom, ape)))

def cambiar_estado_solicitudInstalacion():
    id_solicitud = request.args[0]
    nombre = request.args[1]
    apellido = request.args[2]
    db(db.solicitudes_instalacion.id == id_solicitud).update(estado='Finalizado')
    redirect(URL(c="tecnicos", f="confirmacionNuevoCliente", args=(nombre, apellido)))

def confirmacionNuevoCliente():
    nombre = request.args[0]
    apellido = request.args[1]
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
