# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from consultas.py")

def clientes_dni():
    #Se debe recibir el dni, desde la vista y devolver el registro.
    i=0
    cliente =db().select(db.clientes.ALL)
    for x in cliente:
        i= i+1
    return dict(datos=cliente, cantidad=i)

def tecnicos_dni():
    #Se debe recibir el dni, desde la vista y devolver el registro.
    i=0
    tecnico =db().select(db.tecnicos.ALL)
    for x in tecnico:
        i= i+1
    return dict(datos=tecnico, cantidad=i)

def instalaciones_dni():
    #recibir dni, comparar con los registros y devolver
    i=0
    instalacion =db().select(db.instalaciones.ALL)
    for x in instalacion:
        i= i+1
    return dict(datos=instalacion, cantidad=i)

def soportes_dni():
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

def tecnicos_nombre_apellido():
    #Se debe recibir el dni, desde la vista y devolver el registro.
    i=0
    tecnico =db().select(db.tecnicos.ALL)
    for x in tecnico:
        i= i+1
    return dict(datos=tecnico, cantidad=i)

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

def registrarRecargo():
    i=0
    cliente =db().select(db.clientes.ALL)
    for x in cliente:
        i= i+1
    return dict(datos=cliente, cantidad=i)

################################################### < LISTADOS > ########################################################################

def listadoSoportes():
    datosSoportes = db((db.soportes_tecnicos.tecnico_asignado==db.tecnicos.id)|(db.soportes_tecnicos.tecnico_asignado == None) & (db.soportes_tecnicos.cliente==db.clientes.id)).select(db.soportes_tecnicos.ALL, db.tecnicos.ALL, db.clientes.ALL)
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

def listadoLocalidades():
    datosLocalidades = db().select(db.localidades.ALL)
    i=0
    for x in datosLocalidades:
         i=i+1
    return dict (datos=datosLocalidades, cantidad=i)

def listadoMantenimientos():
    datosMantenimiento = db((db.mantenimientos.nodo == db.nodos.id)
                            &(db.mantenimientos.tecnico_principal == db.tecnicos.id)
                            &(db.mantenimientos.tecnico_secundario == db.tecnicos.id)).select(db.mantenimientos.ALL,db.nodos.ALL, db.tecnicos.ALL)
    i=0
    for x in datosMantenimiento:
         i=i+1
    return dict (datos=datosMantenimiento, cantidad=i)

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


def listadoGerentes():
    datosusuario = db().select(db.gerentes.ALL)
    i=0
    tablafinal=[]
    for x in datosusuario:
         i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('Nombre',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                          TH('Apellido',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                          TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                          TH('Email',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                          TH('Telefono',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                          TH('Password (encriptada)',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                          TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                   TH(i,' Gerente/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.dni,_style='width:200px; color:#000; background: #eef; border: 2px solid      #cdcdcd'),
          TD(x.email,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.telefono,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.password,_style='width:200px; color:#000; background: #eef; border: 2px solid      #cdcdcd'),)
     for x in datosusuario]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)


def listadoAdministradores():
    datosusuario = db().select(db.administradores.ALL)
    i=0
    tablafinal=[]
    for x in datosusuario:
         i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('Nombre',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                          TH('Apellido',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                          TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                          TH('Email',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                          TH('Telefono',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                          TH('Password (encriptada)',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                          TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                   TH(i,' Administrador/es',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.dni,_style='width:200px; color:#000; background: #eef; border: 2px solid      #cdcdcd'),
          TD(x.email,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.telefono,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.password,_style='width:200px; color:#000; background: #eef; border: 2px solid      #cdcdcd'),)
     for x in datosusuario]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoTecnicos():
    datosTecnicos = db().select(db.tecnicos.ALL)
    i=0
    for x in datosTecnicos:
         i=i+1
    return dict (datos=datosTecnicos, cantidad=i)

def listadoSoportesPendientes():
    datosSoportesPendientes = db((db.tecnicos.id==db.soportes_tecnicos.tecnico)&(db.soportes_tecnicos.cliente == db.clientes.id)&(db.soportes_tecnicos.estado == 'Pendiente')).select(db.soportes_tecnicos.ALL, db.tecnicos.ALL, db.clientes.ALL)
    i=0
    tablafinal=[]
    for x in datosSoportesPendientes:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
       (TH('Tecnico',_style='width:40px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Cliente',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Fecha',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Problematica',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Opcion',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:40px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Soporte/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.tecnicos.nombre,' ',x.tecnicos.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.nombre, ' ', x.clientes.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.soportes_tecnicos.fecha,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.soportes_tecnicos.problematica,_style='width:200px; color:#000; background: #eef; border: 2px solid      #cdcdcd'),
          TD(A('Registrar en historial',_href=URL(c='registros_automaticos', f='agregar_soporte_historial', args=(x.soportes_tecnicos.id,))),_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosSoportesPendientes]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)


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
