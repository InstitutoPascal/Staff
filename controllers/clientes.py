# -*- coding: utf-8 -*-
# intente algo como

import os, sys
import json


def index(): return dict(message="hello from clientes.py")

def inicio():
    datosPlanes = db().select(db.planes.ALL)
    return dict (datos=datosPlanes)

def listadoPlanes():
    datosPlanes = db().select(db.planes.ALL)
    return dict (datos=datosPlanes)

def cobertura():
    bandera=0
    localidad= db(db.localidades.id>0).select()
    if request.vars:
            reg= db(db.localidades.id == request.vars.cob_localidad).select(db.localidades.localidad).first()
            session.cob_altura = request.vars.cob_altura
            session.cob_calle = request.vars.cob_calle
            session.cob_localidad = reg.localidad
            response.view ="generic.html"
            try:
                direccion=request.vars.cob_calle + " " + request.vars.cob_altura + ", " + reg.localidad
                #direccion = "Puerto Argentino 4243, Gonzalez Catan, Buenos Aires, Argentina"
                lat, lon, url = coords_by_address(direccion)
                session.lat=lat
                session.lon=lon
                redirect(URL(c="clientes",f="mapaCliente",))
                #return {"lat": lat, "lon": lon, "direccion": direccion}
            except IndexError:
                bandera=bandera+2
                redirect(URL(c="clientes",f="mensaje",args=[bandera]))
                # no completo el form
    return dict (localidad = localidad)

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
    if request.args:
        bandera= request.args[0]
        return dict(bandera=bandera)

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
    form_sop = db(db.clientes.dni == request.vars.dni_cliente).select(db.clientes.id).first()
    bandera=0
    if request.vars:
        if request.vars.dni_soporte:
                if form_cons:
                        session.dni_soporte = request.vars.dni_soporte
                        session.email_soporte = request.vars.email_soporte
                        session.comentario_soporte = request.vars.comentario_soporte
                        db.solicitudes_soporte.insert(
                        cliente=form_cons.id,
                        problematica=session.comentario_soporte)
                        bandera=bandera+2
                        redirect(URL(c="clientes",f="confimacionConsulta",args=[bandera]))
                else:
                    bandera=bandera+3
                    redirect(URL(c="clientes",f="confimacionConsulta",args=[bandera]))

        if request.vars.dni_cliente:
                if form_sop:
                    session.dni_cliente=request.vars.dni_cliente
                    session.email_cliente=request.vars.email_cliente
                    session.mens_cliente=request.vars.mens_cliente
                    x=mail.send(to=['staff.technology.internet@gmail.com'],
                        subject='consulta',
                        message= "Consulta de usuario que es cliente \nDNI: "+ session.dni_cliente +"\nEmail:" + session.email_cliente +"\nMensaje : "+ session.mens_cliente +".\n ")
                    if x == True:
                        bandera=bandera+1
                        redirect(URL(c="clientes",f="confimacionConsulta",args=[bandera]))
                else:
                    bandera=bandera+3
                    redirect(URL(c="clientes",f="confimacionConsulta",args=[bandera]))

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
                    bandera=bandera+1
                    redirect(URL(c="clientes",f="confimacionConsulta",args=[bandera]))
                else:
                    redirect(URL(c="clientes",f="confimacionConsulta",args=[bandera]))

    return dict (bandera=bandera)

def confimacionConsulta():
    if request.args:
        bandera= request.args[0]
        return dict(bandera=bandera)

def mapaCliente():
    return{}


def ingresarDni():
    dni_recibido=request.vars.dni
    resultado = db((db.clientes.dni == dni_recibido)&(db.clientes.tipo_de_plan==db.planes.id)).select(db.clientes.ALL, db.planes.ALL)
    if resultado:
        return dict(datos= resultado)
    else:
        return dict(datos=0)


def realizarPago():

    import mercadopago

    id_cliente = request.args[0]

    precio_plan = db((db.clientes.id == id_cliente)&(db.clientes.tipo_de_plan==db.planes.id)).select(db.planes.precio).first().precio
    neto =  precio_plan
    importe_iva = neto * 0.27
    subtotal = neto + importe_iva
    imp_total=subtotal

    plan = db((db.clientes.id == id_cliente)&(db.clientes.tipo_de_plan==db.planes.id)).select(db.planes.velocidad_de_bajada).first().velocidad_de_bajada

    mp = mercadopago.MP(myconf.take('mercadopago.client_id'), myconf.take('mercadopago.client_secret'))
    print(myconf.take('mercadopago.client_id'), myconf.take('mercadopago.client_secret'))
    # creamos un dict con los datos del pago solicitado:
    preference = {
		"items": [
			{
				"title": "Internet" + " " + plan + " " + "Mb",
				"unit_price": imp_total,
                "quantity": 1,
                "currency_id": "ARS",
				"picture_url": "https://www.mercadopago.com/org-img/MP3/home/logomp3.gif"
			}
         ],
        "marketplace_fee": 2.29 # fee to collect
	}
    # llamamos a MP para que cree un link...
    preferenceResult = mp.create_preference(preference)
    try:
        url = preferenceResult["response"]["init_point"]
        redirect(url)
    except:
        raise
        response.view = "generic.html"
        return {"pref": preferenceResult}
