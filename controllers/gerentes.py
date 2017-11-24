# -*- coding: utf-8 -*-
@auth.requires_membership(role="Gerentes")
def inicio(): return dict(message="hello from gerentes.py")

######################################### AÑADIR DATOS #########################################

def alta_usuarios():
    tipo_usuario = request.args[0]
    if (tipo_usuario == "Administradores") | (tipo_usuario == "Tecnicos"):
        form = SQLFORM(db.auth_user)
        if form.accepts(request.vars, session):
            response.flash = 'Formulario aceptado'
            if tipo_usuario == "Administradores":
                id_usuario = db().select(db.auth_user.id).last().id
                id_grupo = db(db.auth_group.role == tipo_usuario).select(db.auth_group.id).first().id
                nom = db().select(db.auth_user.first_name).last().first_name
                ape = db().select(db.auth_user.last_name).last().last_name
                db.auth_membership.insert(user_id=id_usuario, group_id=id_grupo, nombre=nom, apellido=ape)
            elif tipo_usuario == "Tecnicos":
                id_usuario = db().select(db.auth_user.id).last().id
                id_grupo = db(db.auth_group.role == tipo_usuario).select(db.auth_group.id).first().id
                nom = db().select(db.auth_user.first_name).last().first_name
                ape = db().select(db.auth_user.last_name).last().last_name
                db.auth_membership.insert(user_id=id_usuario, group_id=id_grupo, nombre=nom, apellido=ape)
        elif form.errors:
            response.flash = 'El formulario tiene errores'
        else:
            response.flash = 'Complete el formulario'
        return dict(f=form, usuario=tipo_usuario)
    else:
        redirect(URL(c="gerentes", f="inicio"))

def alta_costos_instalaciones():
    form = SQLFORM(db.costos_instalaciones)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def alta_costos_soportes():
    form = SQLFORM(db.costos_soportes)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def alta_planes():
    form = SQLFORM(db.planes)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def alta_nodos():
    form = SQLFORM(db.nodos)
    if form.accepts(request.vars, session):
        id_nodo = db().select(db.nodos.id).last().id
        redirect(URL(c="gerentes", f="actualizar_ubicacion_nodo", args=(id_nodo)))
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def actualizar_ubicacion_nodo():
    id_nodo = request.args[0]
    ret = ""
    q = (db.nodos.localidad == db.localidades.id)
    q &= (id_nodo == db.nodos.id)
    for reg in db(q).select(db.nodos.id, db.nodos.direccion, db.nodos.numero_de_calle, db.localidades.localidad, db.localidades.codigo_postal):
        dom = "%s %s, %s, %s, %s" % (reg.nodos.direccion, reg.nodos.numero_de_calle, reg.localidades.localidad,"buenos aires","argentina")
        lat, lon , url = coords_by_address(dom)
        db(db.nodos.id==reg.nodos.id).update(latitud=lat, longitud=lon)
        ret += "solicitante: %s coords= %s,%s url: %s\n\r" % (reg.nodos.id, lat, lon, url)
    redirect(URL(c="gerentes", f="alta_nodos"))
    return {}

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


def alta_paneles():
    form = SQLFORM(db.paneles)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def alta_localidad():
    form = SQLFORM(db.localidades)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def alta_productos():
    form = SQLFORM(db.productos)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def alta_proveedores():
    form = SQLFORM(db.proveedores)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def alta_compra():
    form = SQLFORM(db.compras)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
        redirect(URL(c="gerentes", f="calcularTotalCompra"))
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def calcularTotalCompra():
    id_ultima_compra = db().select(db.compras.id).last().id
    ultimo_producto = db().select(db.compras.producto).last().producto
    ultima_fecha = db().select(db.compras.fecha_de_compra).last().fecha_de_compra
    ultimo_precio = db().select(db.compras.precio_de_compra).last().precio_de_compra
    ultima_cantidad = db().select(db.compras.cantidad).last().cantidad
    precio_utilizado = ultima_cantidad * ultimo_precio
    db(db.compras.id == id_ultima_compra).update(total=precio_utilizado)
    redirect(URL(c="gerentes", f="AgregarStock"))

def AgregarStock():
    ultimo_producto = db().select(db.compras.producto).last().producto
    ultima_fecha = db().select(db.compras.fecha_de_compra).last().fecha_de_compra
    ultimo_precio = db().select(db.compras.precio_de_compra).last().precio_de_compra
    ultima_cantidad = db().select(db.compras.cantidad).last().cantidad
    precio_utilizado = ultima_cantidad * ultimo_precio
    registros = db(db.stock.detalle==ultimo_producto).select()
    if registros:
            ultima_cantidad_stock = db(db.stock.detalle==ultimo_producto).select(db.stock.cantidad_existencia).last().cantidad_existencia
            ultimo_total_stock = db(db.stock.detalle==ultimo_producto).select(db.stock.total_existencia).last().total_existencia
            nuevo_stock = ultima_cantidad_stock + ultima_cantidad
            nuevo_total_stock = ultimo_total_stock + precio_utilizado
            nuevo_precio_unitario_stock = nuevo_total_stock / nuevo_stock
            db.stock.insert(fecha=ultima_fecha, detalle=ultimo_producto, cantidad_entrada=ultima_cantidad, costo_unitario_entrada=ultimo_precio, total_entrada=precio_utilizado, cantidad_existencia=nuevo_stock, costo_unitario_existencia=nuevo_precio_unitario_stock, total_existencia=nuevo_total_stock)
            redirect(URL(c="gerentes", f="alta_compra"))
    else:
        unitario_existencia = precio_utilizado/ultima_cantidad
        db.stock.insert(fecha=ultima_fecha, detalle=ultimo_producto, cantidad_entrada=ultima_cantidad, costo_unitario_entrada=ultimo_precio, total_entrada=precio_utilizado, cantidad_existencia=ultima_cantidad, costo_unitario_existencia=unitario_existencia, total_existencia=precio_utilizado)
        redirect(URL(c="gerentes", f="alta_compra"))

######################################### REGISTROS COMPLETOS #########################################

def listadoAdministradores():
    datosAdministradores = db((db.auth_membership.group_id == db.auth_group.id)&(db.auth_group.role == 'Administradores')&(db.auth_membership.user_id == db.auth_user.id)&(db.auth_user.localidad == db.localidades.id)).select(db.auth_user.ALL, db.localidades.ALL)
    i=0
    for x in datosAdministradores:
         i=i+1
    return dict (datos=datosAdministradores, cantidad=i)

def listadoTecnicos():
    datosTecnicos = db((db.auth_membership.group_id == db.auth_group.id)&(db.auth_group.role == 'Tecnicos')&(db.auth_membership.user_id == db.auth_user.id)&(db.auth_user.localidad == db.localidades.id)).select(db.auth_user.ALL, db.localidades.ALL)
    i=0
    for x in datosTecnicos:
         i=i+1
    return dict (datos=datosTecnicos, cantidad=i)

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

def listadoPlanes():
    datosPlanes = db().select(db.planes.ALL)
    i=0
    for x in datosPlanes:
         i=i+1
    return dict (datos=datosPlanes, cantidad=i)

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

def listadoLocalidades():
    datosLocalidades = db().select(db.localidades.ALL)
    i=0
    for x in datosLocalidades:
         i=i+1
    return dict (datos=datosLocalidades, cantidad=i)

def listadoProductos():
    datosProductos = db().select(db.productos.ALL)
    i=0
    for x in datosProductos:
         i=i+1
    return dict (datos=datosProductos, cantidad=i)

def listadoProveedores():
    datosProveedores = db(db.proveedores.localidad == db.localidades.id).select(db.proveedores.ALL, db.localidades.ALL)
    i=0
    for x in datosProveedores:
         i=i+1
    return dict (datos=datosProveedores, cantidad=i)

def listadoCompras():
    datosCompras = db((db.compras.proveedor==db.proveedores.id)&(db.compras.producto==db.productos.id)).select(db.compras.ALL, db.proveedores.ALL, db.productos.ALL)
    i=0
    for x in datosCompras:
         i=i+1
    return dict (datos=datosCompras, cantidad=i)

def listadoStock():
    datosStock = db(db.stock.detalle==db.productos.id).select(db.stock.ALL, db.productos.ALL)
    i=0
    for x in datosStock:
         i=i+1
    return dict (datos=datosStock, cantidad=i)

######################################### ESTADISTICAS #########################################

def estadisticas():

    instalacionPendiente = db(db.solicitudes_instalacion.estado == 'Pendiente').count()
    instalacionFinalizada = db(db.solicitudes_instalacion.estado == 'Finalizado').count()

    soportePendiente = db(db.solicitudes_soporte.estado == 'Pendiente').count()
    soporteFinalizado = db(db.solicitudes_soporte.estado == 'Finalizado').count()

    return dict(instalacionPendiente = instalacionPendiente, instalacionFinalizada = instalacionFinalizada, soportePendiente = soportePendiente, soporteFinalizado = soporteFinalizado )
