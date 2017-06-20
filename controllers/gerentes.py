# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from gerentes.py")

def inicio():
    d = 4
    return dict(datos=d)


def estadisticas():
    title="Gráfico Informativo"
    data=XML('[ ["item", "value"], ["Solicitud de instalaciones", 20], ["Cantidad de clientes", 30], ["Solicitud de soportes", 20],["Soportes                       realizados", 15],["Mantenimientos", 14]]') #convert list in string and string in XML
    return dict(title=title, data=data)

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

def listadoPlanes():
    datosPlanes = db().select(db.planes.ALL)
    i=0
    for x in datosPlanes:
         i=i+1
    return dict (datos=datosPlanes, cantidad=i)

def listadoTecnicos():
    datosTecnicos = db().select(db.tecnicos.ALL)
    i=0
    for x in datosTecnicos:
         i=i+1
    return dict (datos=datosTecnicos, cantidad=i)

def listadoAdministradores():
    datosAdministradores = db().select(db.administradores.ALL)
    i=0
    for x in datosAdministradores:
         i=i+1
    return dict (datos=datosAdministradores, cantidad=i)

def listadoLocalidades():
    datosLocalidades = db().select(db.localidades.ALL)
    i=0
    for x in datosLocalidades:
         i=i+1
    return dict (datos=datosLocalidades, cantidad=i)
