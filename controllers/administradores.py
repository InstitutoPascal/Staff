# intente algo como
def index(): return dict(message="hello from consultas.py")

##################################################################

def inicio():
    d = 4
    return dict(datos=d)

##################################################################

def listadoPlanes():
    datosPlanes = db().select(db.planes.ALL)
    i=0
    for x in datosPlanes:
         i=i+1
    return dict (datos=datosPlanes, cantidad=i)

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

def listadoNodos():
    datosNodos = db(db.nodos.localidad==db.localidades.id).select(db.nodos.ALL, db.localidades.ALL)
    i=0
    for x in datosNodos:
         i=i+1
    return dict (datos=datosNodos, cantidad=i)

def listadoPaneles():
    datosPaneles = db(db.paneles.nodo==db.nodos.id).select(db.paneles.ALL, db.nodos.ALL)
    i=0
    for x in datosPaneles:
         i=i+1
    return dict (datos=datosPaneles, cantidad=i)

##################################################################

def alta_solicitud_instalacion():
    form = SQLFORM(db.solicitudes_instalacion)
    if form.accepts(request.vars, session):
        redirect(URL(c="administradores", f="actualizar_coords"))
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def listadoSolicitudes_instalacion():
    datosSolicitudes = db((db.solicitudes_instalacion.localidad == db.localidades.id)&(db.solicitudes_instalacion.tipo_de_plan == db.planes.id)&(db.solicitudes_instalacion.costo_de_instalacion==db.costos_instalaciones.id)&((db.solicitudes_instalacion.tecnico_asignado == db.tecnicos.id) | db.solicitudes_instalacion.tecnico_asignado != db.tecnicos.id)).select(db.solicitudes_instalacion.ALL, db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.tecnicos.ALL)
    i=0
    for x in datosSolicitudes:
         i=i+1
    return dict (datos=datosSolicitudes, cantidad=i)

##################################################################

def solicitarSoporte():
    dni_recibido=request.vars.dni
    resultado = db((db.clientes.dni == dni_recibido)&(db.clientes.localidad==db.localidades.id)).select(db.clientes.ALL, db.localidades.ALL)
    if resultado:
        return dict(datos= resultado)
    else:
        return dict(datos=0)

def alta_soportes():
    id_cliente = request.args[0]
    nombre = db(id_cliente == db.clientes.id).select(db.clientes.nombre)[0].nombre
    apellido = db(id_cliente == db.clientes.id).select(db.clientes.apellido)[0].apellido
    form = SQLFORM(db.soportes_tecnicos)
    form.vars.cliente = id_cliente
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
        redirect(URL(c="administradores", f="inicio"))
    elif form.errors:
        response.flash = 'El formulario tiene errores'

def listadoSoportes():
    datosSoportes = db((db.soportes_tecnicos.tecnico_asignado==db.tecnicos.id) & (db.soportes_tecnicos.cliente==db.clientes.id)).select(db.soportes_tecnicos.ALL, db.tecnicos.ALL, db.clientes.ALL)
    i=0
    for x in datosSoportes:
         i=i+1
    return dict (datos=datosSoportes, cantidad=i)

def listadoHistoriales():
    datosHistorial = db().select(db.historiales.ALL)
    i=0
    for x in datosHistorial:
         i=i+1
    return dict (datos=datosHistorial, cantidad=i)

##################################################################

def clientes_dni():
    dni_recibido=request.vars.dni
    resultado = db((db.clientes.dni == dni_recibido)&(db.clientes.localidad==db.localidades.id)).select(db.clientes.ALL, db.localidades.ALL)
    if resultado:
        return dict(datos= resultado)
    else:
        return dict(datos=0)

def clientes_nombre_apellido():
    nom=request.vars.nom_ape
    if nom != None:
        resultado = db(
            ((db.clientes.nombre.lower()==nom.lower())&(db.clientes.localidad == db.localidades.id)) |
            ((db.clientes.apellido.lower()==nom.lower())&(db.clientes.localidad == db.localidades.id)) |
            ((db.clientes.nombre.lower() + ' ' + db.clientes.apellido.lower() == nom.lower())&(db.clientes.localidad == db.localidades.id)) |
            ((db.clientes.nombre.lower().contains(nom.lower()))&(db.clientes.localidad == db.localidades.id)) |
            ((db.clientes.apellido.lower().contains(nom.lower()))&(db.clientes.localidad == db.localidades.id))).select(db.clientes.ALL, db.localidades.ALL)
        if resultado:
            return dict(datos= resultado)
        else:
            return dict(datos=0)
    else:
        return dict(datos="None")

def clientes_ip():
    #Se debe recibir el dni, desde la vista y devolver el registro.
    i=0
    cliente =db().select(db.clientes.ALL)
    for x in cliente:
        i= i+1
    return dict(datos=cliente, cantidad=i)

def listadoClientes():
    datosClientes = db((db.clientes.localidad==db.localidades.id)&(db.clientes.tipo_de_plan==db.planes.id)&(db.clientes.numero_de_instalacion == db.instalaciones.id)&(db.instalaciones.panel == db.paneles.id)).select(db.clientes.ALL, db.localidades.localidad, db.paneles.ALL, db.planes.ALL)
    i=0
    for x in datosClientes:
         i=i+1
    return dict (datos=datosClientes, cantidad=i)

def coords_by_address(direccion):
    import re, urllib
    try:
        address=urllib.quote(direccion)
        #url='http://maps.google.com/maps/geo?q=%s&output=xml'%address
        key = KEY_API_GOOGLE_MAP
        url='https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (address, key)

        response = urllib.urlopen(url).read()
        import json
        ret = json.loads(response)
        #item=re.compile('\<coordinates\>(?P<la>[^,]),(?P<lo>[^,]).*?\</coordinates\>').search(t)
        #la,lo=float(item.group('la')),float(item.group('lo'))
        la = ret["results"][0]["geometry"]["location"]["lat"]
        lo = ret["results"][0]["geometry"]["location"]["lng"]
        return la,lo,url
    except Exception, e: 
        #raise RuntimeError(str(e))
        pass
        raise
    #raise RuntimeError(str("%s = %s" % (address, t)))
    return 0.0,0.0,url

def actualizar_coords():
    ret = ""
    criterios = db.solicitudes_instalacion.localidad == db.localidades.id
    #criterios &= db.clientes.latitud == 0
    for reg in db(criterios).select(db.solicitudes_instalacion.id, db.solicitudes_instalacion.direccion, db.solicitudes_instalacion.numero_de_calle, db.localidades.localidad, db.localidades.codigo_postal):
        dom = "%s %s, %s, %s, %s" % (reg.solicitudes_instalacion.direccion, reg.solicitudes_instalacion.numero_de_calle, reg.localidades.localidad,"buenos aires","argentina")
        lat, lon , url = coords_by_address(dom)
        db(db.solicitudes_instalacion.id==reg.solicitudes_instalacion.id).update(latitud=lat, longitud=lon)
        ret += "solicitante: %s coords= %s,%s url: %s\n\r" % (reg.solicitudes_instalacion.id, lat, lon, url)
    redirect(URL(c="administradores", f="alta_solicitud_instalacion"))

def geolocalizacionClientes():
    rows=db((db.clientes.id>0)&(db.clientes.localidad==db.localidades.id)).select(
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

def geolocalizacionNodos():
    d = 4
    return dict(datos=d)

def editar_solicitud_instalacion():
    id_solicitud = request.args[0]                                           # obtengo el primer argumento (ver URL)
    solicitud =  db(db.solicitudes_instalacion.id == id_solicitud).select().first()    # busco el registro en la bbdd
    form=SQLFORM(db.solicitudes_instalacion, solicitud)                                  # armo el formulario para modificar este registro:
    if form.accepts(request.vars, session):
        session.flash = 'Formulario correctamente cargado'
        redirect(URL(c="administradores", f="listadoSolicitudes_instalacion"))
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

def solicitudesDetalles():
    id_solicitud = request.args[0]
    resultado = db((db.solicitudes_instalacion.id == id_solicitud)&(db.solicitudes_instalacion.localidad == db.localidades.id)&(db.solicitudes_instalacion.tipo_de_plan == db.planes.id)&(db.solicitudes_instalacion.costo_de_instalacion==db.costos_instalaciones.id)&((db.solicitudes_instalacion.tecnico_asignado == db.tecnicos.id) | db.solicitudes_instalacion.tecnico_asignado != db.tecnicos.id)).select(db.solicitudes_instalacion.ALL, db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.tecnicos.ALL)
    return dict(datos=resultado)

def clientesDetalles():
    id_cliente = request.args[0]
    resultado = db((db.clientes.id == id_cliente)&(db.clientes.localidad==db.localidades.id)&(db.clientes.tipo_de_plan==db.planes.id)&(db.clientes.numero_de_instalacion == db.instalaciones.id)&(db.instalaciones.panel == db.paneles.id)).select(db.clientes.ALL, db.localidades.localidad, db.paneles.ALL, db.planes.ALL, db.instalaciones.ALL)
    return dict(datos=resultado)
