# -*- coding: utf-8 -*-
def index(): return dict(message="hello from registros_automaticos.py")

def agregar_cliente():
    id_instalacion = request.args[0]
    dni = db(id_instalacion == db.instalacion.id).select(db.instalacion.dni)[0].dni
    nombre = db(id_instalacion == db.instalacion.id).select(db.instalacion.nombre)[0].nombre
    apellido = db(id_instalacion == db.instalacion.id).select(db.instalacion.apellido)[0].apellido
    localidad = db(id_instalacion == db.instalacion.id).select(db.instalacion.localidad)[0].localidad
    calle = db(id_instalacion == db.instalacion.id).select(db.instalacion.calle)[0].calle
    numero_calle = db(id_instalacion == db.instalacion.id).select(db.instalacion.numero_calle)[0].numero_calle
    entre_calle_1 = db(id_instalacion == db.instalacion.id).select(db.instalacion.entre_calle_1)[0].entre_calle_1
    entre_calle_2 = db(id_instalacion == db.instalacion.id).select(db.instalacion.entre_calle_2)[0].entre_calle_2
    telefono = db(id_instalacion == db.instalacion.id).select(db.instalacion.telefono)[0].telefono
    form=SQLFORM(db.clientes)
    form.vars.dni = dni
    form.vars.nombre = nombre
    form.vars.apellido = apellido
    form.vars.localidad = localidad
    form.vars.calle = calle
    form.vars.numero_calle = numero_calle
    form.vars.entre_calle_1 = entre_calle_1
    form.vars.entre_calle_2 = entre_calle_2
    form.vars.telefono_1 = telefono
    if form.accepts(request.vars, session):
        redirect(URL(c="registros_automaticos", f="editar_instalacion", args=(id_instalacion, )))
        session.flash = 'Formulario modificado'
    elif form.errors:
		response.flash = 'El formulario tiene errores'
    else:
		response.flash = 'Modifique el formulario'
    return dict(f=form)


def editar_instalacion():
    id_instalacion = request.args[0]
    # busco el registro en la bbdd
    db(db.instalacion.id == id_instalacion).update(estado='Finalizado')
    redirect(URL(c="consultas", f="listadoPendientes"))
    

def agregar_soporte_tecnico():
    resultado = request.args[0]
    form=SQLFORM(db.soportes_tecnicos)
    form.vars.cliente = resultado
    if form.accepts(request.vars, session):
        redirect(URL(c="consultas", f="listadoSoportes"))
        session.flash = 'Formulario modificado'
    elif form.errors:
		response.flash = 'El formulario tiene errores'
    else:
		response.flash = 'Modifique el formulario'
    return dict(f=form)


def agregar_soporte_historial():
    id_soporte = request.args[0]
    form=SQLFORM(db.historiales)
    form.vars.soporte = id_soporte
    if form.accepts(request.vars, session):
        redirect(URL(c="registros_automaticos", f="editar_soporte_tecnico", args=(id_soporte, )))
        session.flash = 'Formulario modificado'
    elif form.errors:
		response.flash = 'El formulario tiene errores'
    else:
		response.flash = 'Modifique el formulario'
    return dict(f=form)


def editar_soporte_tecnico():
    id_soporte = request.args[0]
    db(db.soportes_tecnicos.id == id_soporte).update(estado='Finalizado')
    redirect(URL(c="consultas", f="listadoSoportes"))
    

def agregar_pago():
    resultado = request.args[0]
    form=SQLFORM(db.pagos)
    form.vars.cliente = resultado
    if form.accepts(request.vars, session):
        redirect(URL(c="registros_automaticos", f="agregar_abono", args=(resultado, )))
        session.flash = 'Formulario modificado'
    elif form.errors:
		response.flash = 'El formulario tiene errores'
    else:
		response.flash = 'Modifique el formulario'
    return dict(f=form)

def agregar_abono():
    resultado = request.args[0]
    ultimo_pago = db().select(db.pagos.id, orderby=~db.pagos.id, limitby=(0,1))[0].id
    form=SQLFORM(db.abonos)
    form.vars.cliente = resultado
    form.vars.importe = ultimo_pago
    if form.accepts(request.vars, session):
        redirect(URL(c="consultas", f="clientes_nro_tarjeta"))
        session.flash = 'Formulario modificado'
    elif form.errors:
		response.flash = 'El formulario tiene errores'
    else:
		response.flash = 'Modifique el formulario'
    return dict(f=form)
