# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from clientes.py")

def inicio():
    datosPlanes = db().select(db.planes.ALL)
    return dict (datos=datosPlanes)

def listadoPlanes():
    datosPlanes = db().select(db.planes.ALL)
    return dict (datos=datosPlanes)

def cobertura():
    if request.vars:
        response.view ="generic.html"
        direccion=request.vars.calle + " " + request.vars.altura + ", " + request.vars.localidad
        #direccion = "Puerto Argentino 4243, Gonzalez Catan, Buenos Aires, Argentina"
        lat, lon, url = coords_by_address(direccion)
        session.lat=lat
        session.lon=lon
        redirect(URL(c="clientes",f="mapaCliente"))
        #return {"lat": lat, "lon": lon, "direccion": direccion}
   
    else:
        # no completo el form
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


def mensaje():
    return {}

def mensaje_dni_modformulario():
    return {}

def tipoInstalacion():
    if request.args:
        session.plan_id = request.args[0]
    if request.vars:
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

def modificarFormulario():
    costo= db(db.costos_instalaciones.id == session.costo).select(db.costos_instalaciones.precio).first()
    plan= db(db.planes.id == session.plan_id).select(db.planes.velocidad_de_bajada).first()
    localidad= db(db.localidades.id == session.localidad).select(db.localidades.localidad).first()
    reg = db(db.solicitudes_instalacion.dni == request.vars.dni).select(db.solicitudes_instalacion.id).first()
    precio = db(db.costos_instalaciones.id>0).select()
    planes = db(db.planes.id>0).select()
    localidades = db(db.localidades.id>0).select()
    if reg:
        redirect(URL(c="clientes",f="mensaje_dni_modformulario"))
    if request.vars:
        session.plan_id = request.vars.plan
        session.costo = request.vars.costo
        session.localidad = request.vars.localidad
        session.dni = request.vars.dni
        session.nombre = request.vars.nombre
        session.apellido = request.vars.apellido
        session.localidad = request.vars.localidad
        session.direccion = request.vars.direccion
        session.num_calle = request.vars.num_calle
        session.calle1 = request.vars.calle1
        session.calle2 = request.vars.calle2
        session.tel = request.vars.tel
        session.tel2 = request.vars.tel2
        session.email = request.vars.email
        redirect(URL(c="clientes",f="cierreFormulario"))
    return dict (costo=costo,plan=plan,localidad=localidad, precio=precio , planes=planes , localidades=localidades)


def datosUbicacion():
    if request.vars:
        session.localidad = request.vars.localidad
        session.direccion = request.vars.direccion
        session.num_calle = request.vars.num_calle
        session.calle1 = request.vars.calle1
        session.calle2 = request.vars.calle2
        redirect(URL(c="clientes",f="datosPersonales"))
    return {"localidades": db(db.localidades.id>0).select()}

def datosPersonales():
    if request.vars:
        reg = db(db.solicitudes_instalacion.dni == request.vars.dni).select(db.solicitudes_instalacion.id).first()
        if reg:
            redirect(URL(c="clientes",f="mensaje"))

        else:
            session.dni = request.vars.dni
            session.nombre = request.vars.nombre
            session.apellido = request.vars.apellido
            redirect(URL(c="clientes",f="datosContacto"))
    return {}


def datosContacto():
    if request.vars:
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
    from gluon.tools import Mail
    mail = Mail()
    mail.settings.server = 'smtp.gmail.com:587'
    mail.settings.sender = 'staff.technology.internet@gmail.com'
    mail.settings.login = 'staff.technology.internet@gmail.com:naruto87'
    form_cons = db(db.clientes.dni == request.vars.dni_soporte).select(db.clientes.id).first()
    form_sop=db(db.clientes.dni == request.vars.dni_cliente).select(db.clientes.id).first()
    if form_cons:
            session.dni_soporte = request.vars.dni_soporte
            session.email_soporte = request.vars.email_soporte
            session.comentario_soporte = request.vars.comentario_soporte
            db.solicitudes_soporte.insert(
            cliente=reg,
            problematica=session.comentario_soporte)
    elif form_sop:
            session.dni_cliente=request.vars.dni_cliente
            session.email_cliente=request.vars.email_cliente
            session.mens_cliente=request.vars.mens_cliente
            x=mail.send(to=['staff.technology.internet@gmail.com'],
                subject='consulta',
                message= "Consulta de usuario que es cliente \nDNI: "+ session.dni_cliente +"\nEmail:" + session.email_cliente +"\nMensaje : "+ session.mens_cliente +".\n ")
            if x == True:
                 response.flash = 'El email fue enviado correctamente'
            else:
                 response.flash = 'Fallo el envio del email'

    else:
            response.flash='El dni ingresado no pertence a un cliente nuestro'
    if request.vars.dni_consulta:
        session.nom_cons = request.vars.nom_consulta
        session.ape_cons = request.vars.ape_consulta
        session.email_cons = request.vars.email_consulta
        session.tel_cons = request.vars.tel_consulta
        session.mens_cons = request.vars.mens_consulta
        x=mail.send(to=['staff.technology.internet@gmail.com'],
                subject='Consulta',
                message= "Consulta de usuario no cliente \nNombre: "+ session.nom_cons +"\nApellido: "+ session.ape_cons +"\nEmail: " + session.email_cons +"\nTelefono: "+session.tel_cons +"\nMensaje: "+session.mens_cons+ ".\n ")
        if x == True:
             response.flash = 'El email fue enviado correctamente'
        else:
             response.flash = 'Fallo el envio del email'

    return {}

def mapaCliente():
    return{}
