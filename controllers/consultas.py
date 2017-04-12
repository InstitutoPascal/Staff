# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from consultas.py")

def clientes_nombre_apellido():
    subtitulo=T('Listado de Clientes por nombre + apellido')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Nombre/Apellido:",INPUT(_type="string",_name="nom_ape",requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'))),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db((db.clientes.nombre.lower()==form.vars.nom_ape.lower()) | (db.clientes.apellido.lower()==form.vars.nom_ape.lower()) | (db.clientes.nombre.lower() + ' ' + db.clientes.apellido.lower() == form.vars.nom_ape.lower())).count()==0:
            form.errors.codigo="El nombre o apellido ingresado no se encuentra registrado"
            response.flash = 'El nombre o apellido ingresado no se encuentra registrado'

        else:
            listado =db((db.clientes.nombre.lower()==form.vars.nom_ape.lower()) | (db.clientes.apellido.lower()==form.vars.nom_ape.lower()) | (db.clientes.nombre.lower() + ' ' + db.clientes.apellido.lower() == form.vars.nom_ape.lower())).select(db.clientes.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Ip',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Panel',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nombre',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Apellido',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nº tarjeta',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Localidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Calle',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nº calle',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Entre calle 1',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Entre calle 2',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Telefono1',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('telefono2',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('telefono3',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Fecha alta',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Fecha baja',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Estado',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                           TH(i,' Cliente/es',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.ip,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.panel,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.numero_tarjeta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.numero_calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.entre_calle_1,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.entre_calle_2,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.telefono_1,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.telefono_2,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.telefono_3,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.fecha_alta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.fecha_baja,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.estado,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
        response.flash = 'Hay un error en el formulario'
    else:
        response.flash = 'Complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

def clientes_dni():
    subtitulo=T('Listado de Clientes por dni')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Dni:",INPUT(_type="integer",_name="dni",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.clientes.dni==form.vars.dni).count()==0:
            form.errors.codigo="El dni ingresado no se encuentra registrado"
            response.flash = 'El dni ingresado no se encuentra registrado'
        else:
            listado =db(db.clientes.dni==form.vars.dni).select(db.clientes.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Ip',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Panel',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nombre',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Apellido',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nº tarjeta',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Localidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Calle',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nº calle',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Entre calle 1',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Entre calle 2',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Telefono1',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Telefono2',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Telefono3',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Fecha alta',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Fecha baja',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Estado',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('opcion',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                           TH(i,' Cliente/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.dni,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.ip,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.panel,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.numero_tarjeta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.numero_calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.entre_calle_1,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.entre_calle_2,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.telefono_1,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.telefono_2,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.telefono_3,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.fecha_alta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.fecha_baja,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.estado,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(A('Solicitar Soporte',_href=URL(c='registros_automaticos', f='agregar_soporte_tecnico', args=(x.id, ))),_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
        response.flash = 'Hay un error en el formulario'
    else:
        response.flash = 'Complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def clientes_ip():
    subtitulo=T('Listado de Clientes por ip')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Ip:",INPUT(_type="integer",_name="ip",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.clientes.ip==form.vars.ip).count()==0:
            form.errors.codigo="La direccion Ip no se encuentra registrado"
            response.flash = 'La direccion Ip no se encuentra registrado'
        else:
            listado =db(db.clientes.ip==form.vars.ip).select(db.clientes.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Ip',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Panel',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nombre',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Apellido',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nº tarjeta',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Localidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Calle',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nº calle',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Entre calle 1',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Entre calle 2',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Telefono1',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Telefono2',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Telefono3',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Fecha alta',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Fecha baja',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Estado',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                           TH(i,' Cliente/es',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.ip,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.panel,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.numero_tarjeta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.numero_calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.entre_calle_1,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.entre_calle_2,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.telefono_1,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.telefono_2,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.telefono_3,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.fecha_alta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.fecha_baja,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.estado,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
        response.flash = 'Hay un error en el formulario'
    else:
        response.flash = 'Complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def clientes_nro_tarjeta():
    subtitulo=T('Listado de Clientes por numero de tarjeta')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Numero de Tarjeta:",INPUT(_type="integer",_name="nro",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.clientes.numero_tarjeta==form.vars.nro).count()==0:
            form.errors.codigo="El numero de tarjeta no se encuentra registrado"
            response.flash = 'El numero de tarjeta no se encuentra registrado'
        else:
            listado =db(db.clientes.numero_tarjeta==form.vars.nro).select(db.clientes.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('Id',_style='width:100px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nombre',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Apellido',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nº tarjeta',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Opcion',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd')
                                           ,TH(i,' Cliente/es',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.id,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.numero_tarjeta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(A('Agregar pago',_href=URL(c='registros_automaticos', f='agregar_pago', args=(x.id, ))),_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
        response.flash = 'Hay un error en el formulario'
    else:
        response.flash = 'Complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def clientes_nodos():
    subtitulo=T('Listado de Clientes por nodo')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Ingrese nodo:  ",INPUT(_type="string",_name="nodo",requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'))),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db((db.nodos.id==db.paneles.nodo) & (db.paneles.id==db.clientes.panel) & (db.nodos.nombre.lower()==form.vars.nodo.lower())).count()==0:
            form.errors.codigo="El nodo ingresado no existe"
            response.flash = 'El nodo ingresado no existe'

        else:
            listado = db((db.nodos.id==db.paneles.nodo) & (db.paneles.id==db.clientes.panel) & (db.nodos.nombre.lower()==form.vars.nodo.lower())).select(db.clientes.ALL, db.nodos.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('Nodo',_style='width:100px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Subred',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Ip',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nombre',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Apellido',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                           TH(i,' Cliente/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.nodos.nombre,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.nodos.subred,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.clientes.ip,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'), TD(x.clientes.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.clientes.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.clientes.dni,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
        response.flash = 'Hay un error en el formulario'
    else:
        response.flash = 'Complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def clientes_localidad():
    subtitulo=T('Listado de Clientes por localidad')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Ingrese localidad:  ",INPUT(_type="string",_name="localidad",requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'))),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db((db.localidades.id==db.clientes.localidad) & (db.nodos.id==db.paneles.nodo) & (db.localidades.localidad.lower()==form.vars.localidad.lower())).count()==0:
            form.errors.codigo="La localidad ingresa no se encuentra en la base de datos"
            response.flash = "La localidad ingresa no se encuentra en la base de datos"

        else:
            listado = db((db.localidades.id==db.clientes.localidad) & (db.nodos.id==db.paneles.nodo) & (db.localidades.localidad.lower()==form.vars.localidad.lower())).select(db.clientes.ALL, db.localidades.ALL, db.nodos.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('Nodo',_style='width:100px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Subred',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Ip',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Nombre',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Apellido',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TH('Localidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                  TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                                           TH(i,' Cliente/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.nodos.nombre,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.nodos.subred,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.clientes.ip,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'), TD(x.clientes.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.clientes.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.clientes.dni,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.localidades.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))
            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
        response.flash = 'Hay un error en el formulario'
    else:
        response.flash = 'Complete el Formulario'
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)



######################################################################################################################################################################################################################################################################################################################
#REGISTROS COMPLETOS#

def listadoSoportes():
    datosSoportes = db((db.soportes_tecnicos.tecnico == db.tecnicos.id)&(db.soportes_tecnicos.cliente == db.clientes.id)).select(db.soportes_tecnicos.ALL, db.tecnicos.nombre, db.tecnicos.apellido, db.clientes.nombre, db.clientes.apellido)
    i=0
    tablafinal=[]
    for x in datosSoportes:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
      (TH('Tecnico',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Cliente',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Fecha',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Problematica',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Estado',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:130px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Soporte/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.tecnicos.nombre,' ',x.tecnicos.apellido,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.clientes.nombre,' ',x.clientes.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.soportes_tecnicos.fecha,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.soportes_tecnicos.problematica,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.soportes_tecnicos.estado,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosSoportes]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoHistoriales():
    datosHistoriales = db((db.historiales.administrador == db.administradores.id)&(db.historiales.soporte == db.soportes_tecnicos.id)&(db.historiales.costo_de_soporte == db.costos_soportes.id)).select(db.historiales.ALL, db.administradores.ALL, db.soportes_tecnicos.ALL, db.costos_soportes.ALL)
    i=0
    tablafinal=[]
    for x in datosHistoriales:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
      (TH('Administrador',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Problematica',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Solucion',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Costo de soporte',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:130px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Registro/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.administradores.nombre, ' ', x.administradores.apellido,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.soportes_tecnicos.problematica,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.historiales.solucion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.costos_soportes.precio,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosHistoriales]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)





def listadoClientes():
    datosclientes = db((db.clientes.localidad==db.localidades.id)&(db.clientes.panel==db.paneles.id)).select(db.clientes.ALL, db.localidades.localidad,       db.paneles.panel)
    i=0
    tablafinal=[]
    for x in datosclientes:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
      (TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Ip',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Panel',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Nombre',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Apellido',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Nº tarjeta',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Localidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Calle',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Nº calle',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Entre calle 1',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Entre calle 2',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Teléfono1',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Teléfono2',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Teléfono3',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Fecha de alta',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Fecha de baja',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Estado',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Clientes/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.clientes.dni,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.ip,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.paneles.panel,_style='width:200px; color:#000; background: #eef; border: 2px solid      #cdcdcd'),
          TD(x.clientes.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.clientes.numero_tarjeta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.localidades.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.numero_calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.entre_calle_1,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.entre_calle_2,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.telefono_1,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'), 
          TD(x.clientes.telefono_2,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.telefono_3,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.fecha_alta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.fecha_baja,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.estado,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosclientes]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoMorosos():
    datos_morosos = db(db.clientes.id != db.abonos.cliente).select(db.clientes.ALL)
    i=0
    tablafinal=[]
    for x in datos_morosos:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
      (TH('Nombre',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Apellido',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('telefono',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Numero tarjeta',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:130px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Cliente/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.nombre,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.dni,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.telefono_1,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.numero_tarjeta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datos_morosos]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoLocalidades():
    datoslocalidad = db().select(db.localidades.ALL)
    i=0
    tablafinal=[]
    for x in datoslocalidad:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
      (TH('Localidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Codigo postal',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:130px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Localidad/es',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.codigo_postal,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datoslocalidad]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoMantenimientos():
    datosmantenimiento = db((db.mantenimientos.nodo==db.nodos.id)&(db.mantenimientos.tecnico==db.tecnicos.id)).select(db.mantenimientos.ALL, db.nodos.nombre, db.nodos.id, db.tecnicos.nombre, db.tecnicos.apellido, db.tecnicos.id)
    i=0
    tablafinal=[]
    for x in datosmantenimiento:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
      (TH('Tecnico',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Nodo',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Fecha',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Descripcion',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:130px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Mantenimiento/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.tecnicos.nombre,' ',x.tecnicos.apellido,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.nodos.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.mantenimientos.fecha,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.mantenimientos.descripcion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosmantenimiento]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoNodos():
    datosnodos = db(db.nodos.localidad==db.localidades.id).select(db.nodos.ALL, db.localidades.localidad, db.localidades.id)
    i=0
    tablafinal=[]
    for x in datosnodos:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
      (TH('Localidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Nombre',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Subred',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:130px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Nodo/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.localidades.localidad,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.nodos.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.nodos.subred,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosnodos]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoPaneles():
    datospaneles = db(db.paneles.nodo==db.nodos.id).select(db.paneles.ALL, db.nodos.ALL, db.nodos.id)
    i=0
    tablafinal=[]
    for x in datospaneles:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
      (TH('Nodo',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Panel',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Nombre',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Equipo',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Descripción de Ubicación',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('AP ST',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Orientación',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Frecuencia',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('RX TX',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('SSID',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Password',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:130px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' panel/es',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.nodos.nombre, _style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.paneles.panel,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.paneles.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.paneles.equipo,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.paneles.descripcion_ubicacion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.paneles.ap_st,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.paneles.orientacion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.paneles.frecuencia,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.paneles.rx_tx,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.paneles.ssid,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.paneles.password,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datospaneles]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)


def listadoPagos():
    datospago = db(db.pagos.cliente==db.clientes.id).select(db.pagos.ALL, db.clientes.nombre, db.clientes.apellido)
    i=0
    tablafinal=[]
    for x in datospago:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
      (TH('Cliente',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Fecha de pago',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Abono',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:130px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Pago/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.clientes.nombre,' ',x.clientes.apellido,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.pagos.fecha_pago,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.pagos.abono,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datospago]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

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
    datosusuario = db().select(db.tecnicos.ALL)
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
                                   TH(i,' Tecnico/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.dni,_style='width:200px; color:#000; background: #eef; border: 2px solid      #cdcdcd'),
          TD(x.email,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.telefono,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.password,_style='width:200px; color:#000; background: #eef; border: 2px solid      #cdcdcd'),)
     for x in datosusuario]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)


def listadoPendientes():
    datosclientes = db((db.localidades.id==db.instalacion.localidad)&(db.instalacion.estado == 'Pendiente' )&(db.instalacion.costo_de_instalacion==db.costos_instalaciones.id)).select(db.instalacion.ALL, db.localidades.ALL, db.costos_instalaciones.ALL)
    i=0
    tablafinal=[]
    for x in datosclientes:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
       (TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Nombre',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Apellido',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Localidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Calle',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Numero de calle',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Entre calle 1',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Entre calle 2',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Telefono',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Costo',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Opcion',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Instalacion/es',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.instalacion.dni,_style='width:100px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.localidades.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid      #cdcdcd'),
          TD(x.instalacion.calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.numero_calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.entre_calle_1,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.entre_calle_2,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.telefono,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD('$ ',x.costos_instalaciones.precio,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(A('Agregar cliente',_href=URL(c='registros_automaticos', f='agregar_cliente', args=(x.instalacion.id,))),_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosclientes]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)



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
    datoscostos_instalaciones = db().select(db.costos_instalaciones.ALL)
    i=0
    tablafinal=[]
    for x in datoscostos_instalaciones:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
       (TH('Descripcion',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Precio',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Costo/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.descripcion,_style='width:100px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD('$ ',x.precio,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datoscostos_instalaciones]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoCostos_soportes():
    datoscostos_soportes = db().select(db.costos_soportes.ALL)
    i=0
    tablafinal=[]
    for x in datoscostos_soportes:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
       (TH('Descripcion',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Precio',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Costo/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.descripcion,_style='width:100px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD('$ ',x.precio,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datoscostos_soportes]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoInstalaciones():
    datosinstalaciones = db((db.instalacion.localidad == db.localidades.id)&(db.instalacion.costo_de_instalacion == db.costos_instalaciones.id)).select(db.instalacion.ALL, db.localidades.localidad, db.costos_instalaciones.precio)
    i=0
    tablafinal=[]
    for x in datosinstalaciones:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
       (TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Nombre',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Apellido',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Localidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Calle',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Numero de calle',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Entre calle 1',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Entre calle 2',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Telefono',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Costo',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Estado',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Instalacion/es',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.instalacion.dni,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.localidades.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.numero_calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.entre_calle_1,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.entre_calle_2,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.telefono,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD('$ ',x.costos_instalaciones.precio,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.instalacion.estado,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosinstalaciones]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)


def listadoPlanes():
    datosplanes = db().select(db.planes.ALL)
    i=0
    tablafinal=[]
    for x in datosplanes:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
       (TH('velocidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('precio',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Plan/es',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.velocidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD('$ ',x.precio,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosplanes]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)


def listadoAbonos():
    datosAbonos = db((db.abonos.cliente == db.clientes.id)&(db.abonos.tipo_de_plan == db.planes.id)&(db.abonos.importe == db.pagos.id)).select(db.abonos.ALL, db.clientes.ALL, db.planes.ALL, db.pagos.ALL)
    i=0
    tablafinal=[]
    for x in datosAbonos:
         i=i+1
    lista=[]
    lista.append(TABLE(TR
       (TH('Cliente',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Plan',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Mes',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Año',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TH('Importe',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
       TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
                TH(i,' Abono/s',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.velocidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.clientes.nombre, ' ', x.clientes.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.planes.velocidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.abonos.mes,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.abonos.ano,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
          TD(x.pagos.abono,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosAbonos]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)
