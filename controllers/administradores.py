# intente algo como
def index(): return dict(message="hello from consultas.py")

def alta_instalacion():
    form = SQLFORM(db.instalaciones)
    if form.accepts(request.vars, session):
        redirect(URL(c="administradores", f="actualizar_coords"))
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def alta_soportes():
    form = SQLFORM(db.soportes_tecnicos)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)




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
    criterios = db.instalaciones.localidad == db.localidades.id
    #criterios &= db.clientes.latitud == 0
    for reg in db(criterios).select(db.instalaciones.id, db.instalaciones.direccion, db.instalaciones.numero_de_calle, db.localidades.localidad, db.localidades.codigo_postal):
        dom = "%s %s, %s, %s, %s" % (reg.instalaciones.direccion, reg.instalaciones.numero_de_calle, reg.localidades.localidad,"buenos aires","argentina")
        lat, lon , url = coords_by_address(dom)
        db(db.instalaciones.id==reg.instalaciones.id).update(latitud=lat, longitud=lon)
        ret += "solicitante: %s coords= %s,%s url: %s\n\r" % (reg.instalaciones.id, lat, lon, url)
    redirect(URL(c="administradores", f="alta_instalacion"))


def inicio():
    d = 4
    return dict(datos=d)

def geolocalizacionNodos():
    d = 4
    return dict(datos=d)

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

def clientes_dni():
    dni_recibido=request.vars.dni
    resultado = db((db.clientes.dni == dni_recibido)&(db.clientes.localidad==db.localidades.id)).select(db.clientes.ALL, db.localidades.ALL)
    if resultado:
        return dict(datos= resultado)
    else:
        return dict(datos=0)

def solicitarSoporte():
    #recibir dni, comparar con los registros y devolver
    i=0
    instalacion =db().select(db.instalaciones.ALL)
    for x in instalacion:
        i= i+1
    return dict(datos=instalacion, cantidad=i)
    
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
    datosClientes = db((db.clientes.localidad==db.localidades.id)&(db.clientes.panel==db.paneles.id)&(db.clientes.tipo_de_plan==db.planes.id)).select(db.clientes.ALL, db.localidades.localidad, db.paneles.panel, db.planes.ALL)
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

def instalacionesDetalles():
    instalacion_id = request.args[0]
    resultado = db((db.instalaciones.id == instalacion_id)&(db.instalaciones.localidad == db.localidades.id)&(db.instalaciones.tipo_de_plan == db.planes.id)&(db.instalaciones.costo_de_instalacion == db.costos_instalaciones.id)&(db.instalaciones.tecnico_asignado == db.tecnicos.id)).select(db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.instalaciones.ALL, db.tecnicos.ALL)
    return dict(datos=resultado)

def clientesDetalles():
    cliente_id = request.args[0]
    resultado = db((db.clientes.id == cliente_id)&(db.clientes.localidad == db.localidades.id)&(db.clientes.tipo_de_plan == db.planes.id)&(db.paneles.nodo == db.nodos.id)&(db.clientes.panel == db.paneles.id)).select(db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.clientes.ALL, db.nodos.ALL, db.paneles.ALL)
    return dict(datos=resultado)
