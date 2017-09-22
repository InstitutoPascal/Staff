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

def alta_solicitud_soporte():
    id_cliente = request.args[0]
    nombre = db(id_cliente == db.clientes.id).select(db.clientes.nombre)[0].nombre
    apellido = db(id_cliente == db.clientes.id).select(db.clientes.apellido)[0].apellido
    form = SQLFORM(db.solicitudes_soporte)
    form.vars.cliente = id_cliente
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
        redirect(URL(c="administradores", f="inicio"))
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form, nom=nombre, ape=apellido)

def listadoSolicitudes_soporte():
    datosSolicitudes = db((db.solicitudes_soporte.tecnico_asignado==db.tecnicos.id) & (db.solicitudes_soporte.cliente==db.clientes.id)).select(db.solicitudes_soporte.ALL, db.tecnicos.ALL, db.clientes.ALL)
    i=0
    for x in datosSolicitudes:
         i=i+1
    return dict (datos=datosSolicitudes, cantidad=i)

def editar_solicitud_soporte():
    id_solicitud = request.args[0]
    solicitud =  db(db.solicitudes_soporte.id == id_solicitud).select().first()
    form=SQLFORM(db.solicitudes_soporte, solicitud)
    if form.accepts(request.vars, session):
        session.flash = 'Formulario correctamente cargado'
        redirect(URL(c="administradores", f="listadoSolicitudes_soporte"))
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else: 
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)

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


def solicitudesDetalles():
    id_solicitud = request.args[0]
    resultado = db((db.solicitudes_instalacion.id == id_solicitud)&(db.solicitudes_instalacion.localidad == db.localidades.id)&(db.solicitudes_instalacion.tipo_de_plan == db.planes.id)&(db.solicitudes_instalacion.costo_de_instalacion==db.costos_instalaciones.id)&((db.solicitudes_instalacion.tecnico_asignado == db.tecnicos.id) | db.solicitudes_instalacion.tecnico_asignado != db.tecnicos.id)).select(db.solicitudes_instalacion.ALL, db.localidades.ALL, db.planes.ALL, db.costos_instalaciones.ALL, db.tecnicos.ALL)
    return dict(datos=resultado)

def clientesDetalles():
    id_cliente = request.args[0]
    resultado = db((db.clientes.id == id_cliente)&(db.clientes.localidad==db.localidades.id)&(db.clientes.tipo_de_plan==db.planes.id)&(db.clientes.numero_de_instalacion == db.instalaciones.id)&(db.instalaciones.panel == db.paneles.id)).select(db.clientes.ALL, db.localidades.localidad, db.paneles.ALL, db.planes.ALL, db.instalaciones.ALL)
    return dict(datos=resultado)


##################################################################

import datetime
from ConfigParser import SafeConfigParser
from pyafipws.pyfepdf import FEPDF

def generar_pdf():

    CONFIG_FILE = "ubicacion del archivo rece.ini"

    config = SafeConfigParser()
    config.read(CONFIG_FILE)
    conf_fact = dict(config.items('FACTURA'))
    conf_pdf = dict(config.items('PDF'))


    fepdf = FEPDF()
    # cargo el formato CSV por defecto (factura.csv)
    fepdf.CargarFormato(conf_fact.get("formato", "factura.csv"))
    # establezco formatos (cantidad de decimales) según configuración:
    fepdf.FmtCantidad = conf_fact.get("fmt_cantidad", "0.2")
    fepdf.FmtPrecio = conf_fact.get("fmt_precio", "0.2")

    # creo una factura de ejemplo
    HOMO = True

    # datos generales del encabezado:
    tipo_cbte = 1
    punto_vta = 4000
    fecha = datetime.datetime.now().strftime("%Y%m%d")
    concepto = 3
    tipo_doc = 80; nro_doc = "30000000007"
    cbte_nro = 12345678
    imp_total = "127.00"
    imp_tot_conc = "3.00"
    imp_neto = "100.00"
    imp_iva = "21.00"
    imp_trib = "1.00"
    imp_op_ex = "2.00"
    imp_subtotal = "105.00"
    fecha_cbte = fecha
    fecha_venc_pago = fecha
    # Fechas del período del servicio facturado (solo si concepto> 1)
    fecha_serv_desde = fecha
    fecha_serv_hasta = fecha
    # campos p/exportación (ej): DOL para USD, indicando cotización:
    moneda_id = 'PES'
    moneda_ctz = 1
    incoterms = 'FOB'                   # solo exportación
    idioma_cbte = 1                     # 1: es, 2: en, 3: pt

    # datos adicionales del encabezado:
    nombre_cliente = 'Nestor Ortigoza'
    domicilio_cliente = 'Rua 76 km 34.5 Alagoas'
    pais_dst_cmp = 212                  # 200: Argentina, ver tabla
    id_impositivo = 'PJ54482221-l'      # cat. iva (mercado interno)
    forma_pago = '30 dias'

    obs_generales = "Observaciones Generales<br/>linea2<br/>linea3"
    obs_comerciales = "Observaciones Comerciales<br/>texto libre"

    # datos devueltos por el webservice (WSFEv1, WSMTXCA, etc.):
    motivo_obs = "Factura individual, DocTipo: 80, DocNro 30000000007 no se encuentra registrado en los padrones de AFIP."
    cae = "61123022925855"
    fch_venc_cae = "20110320"

    fepdf.CrearFactura(concepto, tipo_doc, nro_doc, tipo_cbte, punto_vta,
                cbte_nro, imp_total, imp_tot_conc, imp_neto,
                imp_iva, imp_trib, imp_op_ex, fecha_cbte, fecha_venc_pago, 
                fecha_serv_desde, fecha_serv_hasta, 
                moneda_id, moneda_ctz, cae, fch_venc_cae, id_impositivo,
                nombre_cliente, domicilio_cliente, pais_dst_cmp, 
                obs_comerciales, obs_generales, forma_pago, incoterms, 
                idioma_cbte, motivo_obs)

    # completo campos extra del encabezado:
    ok = fepdf.EstablecerParametro("localidad_cliente", "Hurlingham")
    ok = fepdf.EstablecerParametro("provincia_cliente", "Buenos Aires")

    # imprimir leyenda "Comprobante Autorizado" (constatar con WSCDC!)
    ok = fepdf.EstablecerParametro("resultado", "A")

    # tributos adicionales:
    tributo_id = 99
    desc = 'Impuesto Municipal Matanza'
    base_imp = "100.00"
    alic = "1.00"
    importe = "1.00"
    fepdf.AgregarTributo(tributo_id, desc, base_imp, alic, importe)

    tributo_id = 4
    desc = 'Impuestos Internos'
    base_imp = None
    alic = None
    importe = "0.00"
    fepdf.AgregarTributo(tributo_id, desc, base_imp, alic, importe)

    # subtotales por alícuota de IVA:
    iva_id = 5 # 21%
    base_imp = 100
    importe = 21
    fepdf.AgregarIva(iva_id, base_imp, importe)


    # detalle de artículos:
    u_mtx = 123456
    cod_mtx = 1234567890123
    codigo = "P0001"
    ds = "Descripcion del producto P0001\n"
    qty = 1.00
    umed = 7
    if tipo_cbte in (1, 2, 3, 4, 5, 34, 39, 51, 52, 53, 54, 60, 64):
                # discriminar IVA si es clase A / M
        precio = 110.00
        imp_iva = 23.10
    else:
        # no discriminar IVA si es clase B (importe final iva incluido)
        precio = 133.10
        imp_iva = None
    bonif = 0.00
    iva_id = 5
    importe = 133.10
    despacho = u'Nº 123456'
    dato_a = "Dato A"
    fepdf.AgregarDetalleItem(u_mtx, cod_mtx, codigo, ds, qty, umed, 
                precio, bonif, iva_id, imp_iva, importe, despacho, dato_a)

    # descuento general (a tasa 21%):
    u_mtx = cod_mtx = codigo = None
    ds = u"Bonificación/Descuento 10%"
    qty = precio = bonif = None
    umed = 99
    iva_id = 5
    if tipo_cbte in (1, 2, 3, 4, 5, 34, 39, 51, 52, 53, 54, 60, 64):
        # discriminar IVA si es clase A / M
        imp_iva = -2.21
    else:
        imp_iva = None
    importe = -12.10
    fepdf.AgregarDetalleItem(u_mtx, cod_mtx, codigo, ds, qty, umed, 
                precio, bonif, iva_id, imp_iva, importe, "")

    # descripción (sin importes ni cantidad):
    u_mtx = cod_mtx = codigo = None
    qty = precio = bonif = iva_id = imp_iva = importe = None
    umed = 0
    ds = u"Descripción Ejemplo"
    fepdf.AgregarDetalleItem(u_mtx, cod_mtx, codigo, ds, qty, umed, 
            precio, bonif, iva_id, imp_iva, importe, "")


    # completo campos personalizados de la plantilla:
    fepdf.AgregarDato("custom-nro-cli", "Cod.123")
    fepdf.AgregarDato("custom-pedido", "1234")
    fepdf.AgregarDato("custom-remito", "12345")
    fepdf.AgregarDato("custom-transporte", "Camiones Ej.")
    print "Prueba!"


    # datos fijos:
    for k, v in conf_pdf.items():
        fepdf.AgregarDato(k, v)
        if k.upper() == 'CUIT':
            fepdf.CUIT = v  # CUIT del emisor para código de barras

    fepdf.CrearPlantilla(papel=conf_fact.get("papel", "legal"), 
                         orientacion=conf_fact.get("orientacion", "portrait"))
    fepdf.ProcesarPlantilla(num_copias=int(conf_fact.get("copias", 1)),
                            lineas_max=int(conf_fact.get("lineas_max", 24)),
                            qty_pos=conf_fact.get("cant_pos") or 'izq')

    salida = "/tmp/factura.pdf"
    fepdf.GenerarPDF(archivo=salida)

    response.headers['Content-Type'] = "application/pdf"

    return open(salida, "rb")
