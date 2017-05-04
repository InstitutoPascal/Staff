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
    datosClientes = db((db.clientes.localidad==db.localidades.id)&(db.clientes.panel==db.paneles.id)).select(db.clientes.ALL, db.localidades.localidad,       db.paneles.panel)
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
                            &(db.tecnicos.id == db.mantenimientos.tecnico_secundario)).select(db.mantenimientos.ALL,db.nodos.ALL, db.tecnicos.ALL)
    i=0
    for x in datosMantenimiento:
         i=i+1
    return dict (datos=datosMantenimiento, cantidad=i)

def prueba():
    datos=db((db.mantenimientos.nodo == db.nodos.id)&(db.mantenimientos.tecnico_principal == db.tecnicos.id)&(db.mantenimientos.tecnico_secundario == db.tecnicos.id)).select(db.mantenimientos.ALL)
    return dict(d=datos)

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
    datosinstalaciones = db((db.instalacion.localidad == db.localidades.id)&(db.instalacion.costo_de_instalacion == db.costos_instalaciones.id)).select(db.instalacion.ALL, db.localidades.localidad, db.costos_instalaciones.precio)
    i=0
    tablafinal=[]
    for x in datosinstalaciones:
         i=i+1
    return dict (tabla=tablafinal, cantidad=i)


def listadoPlanes():
    datosPlanes = db().select(db.planes.ALL)
    i=0
    for x in datosPlanes:
         i=i+1
    return dict (datos=datosPlanes, cantidad=i)
