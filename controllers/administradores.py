# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from consultas.py")

def inicio():
    d = 4
    return dict(datos=d)

def gestionPago():
    d = 4
    return dict(datos=d)

def dni_descuento():
    d = 4
    return dict(datos=d)

def geolocalizacionNodos():
    d = 4
    return dict(datos=d)

def geolocalizacionClientes():
    d = 4
    return dict(datos=d)

def clientesCuenta():
    d = 4
    return dict(datos=d)

def cuentaCorriente():
     #Se debe recibir el dni, desde la vista y devolver el registro.
    i=0
    cliente =db().select(db.clientes.ALL)
    for x in cliente:
        i= i+1
    return dict(datos=cliente, cantidad=i)


def clientes_dni():
    #Se debe recibir el dni, desde la vista y devolver el registro.
    i=0
    cliente =db().select(db.clientes.ALL)
    for x in cliente:
        i= i+1
    return dict(datos=cliente, cantidad=i)

def clientes_nro_tarjeta():
    #Se debe recibir el dni, desde la vista y devolver el registro.
    i=0
    cliente =db().select(db.clientes.ALL)
    for x in cliente:
        i= i+1
    return dict(datos=cliente, cantidad=i)

def solicitarSoporte():
    #recibir dni, comparar con los registros y devolver
    i=0
    instalacion =db().select(db.instalaciones.ALL)
    for x in instalacion:
        i= i+1
    return dict(datos=instalacion, cantidad=i)
    
def clientes_nombre_apellido():
    #Se debe recibir el dni, desde la vista y devolver el registro.
    i=0
    cliente =db().select(db.clientes.ALL)
    for x in cliente:
        i= i+1
    return dict(datos=cliente, cantidad=i)

def clientes_ip():
    #Se debe recibir el dni, desde la vista y devolver el registro.
    i=0
    cliente =db().select(db.clientes.ALL)
    for x in cliente:
        i= i+1
    return dict(datos=cliente, cantidad=i)

def registrarPago():
    i=0
    cliente =db().select(db.clientes.ALL)
    for x in cliente:
        i= i+1
    return dict(datos=cliente, cantidad=i)

def registrarDescuento():
    i=0
    cliente =db().select(db.clientes.ALL)
    for x in cliente:
        i= i+1
    return dict(datos=cliente, cantidad=i)


def editar_instalacion():
    id_instalacion = request.args[0]                                           # obtengo el primer argumento (ver URL)
    solicitud =  db(db.instalaciones.id == id_instalacion).select().first()    # busco el registro en la bbdd
    form=SQLFORM(db.instalaciones, solicitud)                                  # armo el formulario para modificar este registro:
    if form.accepts(request.vars, session):
        session.flash = 'Formulario correctamente cargado'
        redirect(URL(c="consultas", f="listado_clientes"))
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else: 
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)


def editar_soporte():
    id_soporte = request.args[0]                                                # obtengo el primer argumento (ver URL)
    solicitud =  db(db.soportes_tecnicos.id == id_soporte).select().first()     # busco el registro en la bbdd
    form=SQLFORM(db.soportes_tecnicos, solicitud)                               # armo el formulario para modificar este registro:
    if form.accepts(request.vars, session):
        session.flash = 'Formulario correctamente cargado'
        redirect(URL(c="consultas", f="listado_clientes"))
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)




################################################### < LISTADOS > ########################################################################

def listadoSoportes():
    datosSoportes = db((db.soportes_tecnicos.tecnico_asignado==db.tecnicos.id) & (db.soportes_tecnicos.cliente==db.clientes.id)).select(db.soportes_tecnicos.ALL, db.tecnicos.ALL, db.clientes.ALL)
    i=0
    for x in datosSoportes:
         i=i+1
    return dict (datos=datosSoportes, cantidad=i)

def listadoClientes():
    datosClientes = db((db.clientes.localidad==db.localidades.id)&(db.clientes.panel==db.paneles.id)&(db.clientes.tipo_de_plan==db.planes.id)).select(db.clientes.ALL, db.localidades.localidad, db.paneles.panel, db.planes.velocidad)
    i=0
    for x in datosClientes:
         i=i+1
    return dict (datos=datosClientes, cantidad=i)

def listadoNodos():
    datosNodos = db(db.nodos.localidad==db.localidades.id).select(db.nodos.ALL, db.localidades.localidad, db.localidades.id)
    i=0
    for x in datosNodos:
         i=i+1
    return dict (datos=datosNodos, cantidad=i)

def listadoPaneles():
    datosPaneles = db(db.paneles.nodo==db.nodos.id).select(db.paneles.ALL, db.nodos.ALL, db.nodos.id)
    i=0
    for x in datosPaneles:
         i=i+1
    return dict (datos=datosPaneles, cantidad=i)

def listadoCostos_instalaciones():
    datosCostos_instalaciones = db().select(db.costos_instalaciones.ALL)
    i=0
    for x in datosCostos_instalaciones:
         i=i+1
    return dict (datos=datosCostos_instalaciones, cantidad=i)

def listadoCostos_soportes():
    datosCostos_soportes = db().select(db.costos_soportes.ALL)
    i=0
    for x in datosCostos_soportes:
         i=i+1
    return dict (datos=datosCostos_soportes, cantidad=i)

def listadoInstalaciones():
    datosInstalaciones = db((db.instalaciones.localidad == db.localidades.id)&(db.instalaciones.tipo_de_plan == db.planes.id)&(db.instalaciones.costo_de_instalacion==db.costos_instalaciones.id)&(db.instalaciones.tecnico_asignado==db.tecnicos.id)).select(db.instalaciones.ALL, db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.tecnicos.ALL)
    i=0
    for x in datosInstalaciones:
         i=i+1
    return dict (datos=datosInstalaciones, cantidad=i)


def listadoPlanes():
    datosPlanes = db().select(db.planes.ALL)
    i=0
    for x in datosPlanes:
         i=i+1
    return dict (datos=datosPlanes, cantidad=i)

def listadoHistoriales():
    datosHistorial = db().select(db.historiales.ALL)
    i=0
    for x in datosHistorial:
         i=i+1
    return dict (datos=datosHistorial, cantidad=i)
