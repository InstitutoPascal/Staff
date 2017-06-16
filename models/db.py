# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ['*'] if request.is_local else []
# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True


#Gerentes
db.define_table('gerentes',
                 db.Field('nombre','string'),
                 db.Field('apellido','string'),
                 db.Field('dni','integer'),
                 db.Field('email' ,'string'),
                 db.Field('telefono', 'integer'),
                 db.Field('password', 'password'))
db.gerentes.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.gerentes.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.gerentes.dni.requires=IS_NOT_IN_DB(db, db.gerentes.dni, error_message = 'El DNI ingresado  ya se encuentra registrado') ,IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.gerentes.email.requires=IS_EMAIL(error_message='El correo electronico no es válido'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres'),IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.gerentes.password.requires = CRYPT(key=auth.settings.hmac_key, error_message= 'Campo obligatorio')
db.gerentes.telefono.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')

#Administadores
db.define_table('administradores',
                 db.Field('nombre','string'),
                 db.Field('apellido','string'),
                 db.Field('dni','integer'),
                 db.Field('email' ,'string'),
                 db.Field('telefono', 'integer'),
                 db.Field('password', 'password'))
db.administradores.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.administradores.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.administradores.dni.requires=IS_NOT_IN_DB(db, db.administradores.dni, error_message = 'El DNI ingresado  ya se encuentra registrado') ,IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.administradores.email.requires=IS_EMAIL(error_message='El correo electronico no es válido'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres'),IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.administradores.password.requires = CRYPT(key=auth.settings.hmac_key,  error_message= 'Campo obligatorio')
db.administradores.telefono.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')

#Tecnicos
db.define_table('tecnicos',
                 db.Field('nombre','string'),
                 db.Field('apellido','string'),
                 db.Field('dni','integer'),
                 db.Field('email' ,'string'),
                 db.Field('telefono', 'integer'),
                 db.Field('password', 'password'))
db.tecnicos.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.tecnicos.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.tecnicos.dni.requires=IS_NOT_IN_DB(db, db.tecnicos.dni, error_message = 'El DNI ingresado  ya se encuentra registrado') ,IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.tecnicos.email.requires=IS_EMAIL(error_message='El correo electronico no es válido'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres'),IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.tecnicos.password.requires = CRYPT(key=auth.settings.hmac_key, error_message= 'Campo obligatorio')
db.tecnicos.telefono.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')

#Costos de intalaciones
db.define_table('costos_instalaciones',
                 db.Field('descripcion','string'),
                 db.Field('precio','double'))
db.costos_instalaciones.descripcion.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.costos_instalaciones.precio.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(7, error_message='Solo hasta 7 caracteres')


#Localidades
db.define_table('localidades',
                 db.Field('localidad', 'string'),
                 db.Field('codigo_postal','integer'))
db.localidades.codigo_postal.requires= IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')


#Nodos
db.define_table('nodos',
                 db.Field('localidad',db.localidades),
                 db.Field('nombre','string'),
                 db.Field('subred','string'))
db.nodos.localidad.requires=IS_IN_DB(db,db.localidades.id,'%(localidad)s',zero=T('Seleccione localidad'), error_message= 'Campo obligatorio')
db.nodos.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.nodos.subred.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(3, error_message='Solo hasta 3 caracteres') #PreguntarBenny342325coma2

#Paneles
db.define_table('paneles',
                 db.Field('nodo',db.nodos),
                 db.Field('panel','string'),
                 db.Field('nombre','string'),
                 db.Field('equipo', 'string'),
                 db.Field('descripcion_ubicacion','string'),
                 db.Field('ap_st', 'string'),
                 db.Field('orientacion', 'string'),
                 db.Field('frecuencia','string'),
                 db.Field('rx_tx','string'),
                 db.Field('ssid','string'),
                 db.Field('password','string'))
db.paneles.nodo.requires=IS_IN_DB(db,db.nodos.id,'%(nombre)s',zero=T('Seleccione nodo'), error_message= 'Campo obligatorio')
db.paneles.panel.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.paneles.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.paneles.equipo.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.paneles.ap_st.requires=IS_IN_SET(['Punto de acceso','Estacion'], zero=T('Seleccione modo'), error_message= 'Campo obligatorio')
db.paneles.frecuencia.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.paneles.ssid.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.paneles.password.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres') #Benny


#Planes
db.define_table('planes',
                 db.Field('velocidad','string'),
                 db.Field('precio','double'))
db.planes.velocidad.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(6, error_message='Solo hasta 6 caracteres')
db.planes.precio.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(7, error_message='Solo hasta 7 caracteres')


#Instalacion
db.define_table('instalaciones',
                 db.Field('dni','integer'),
                 db.Field('nombre','string'),
                 db.Field('apellido','string'),
                 db.Field('localidad',db.localidades),
                 db.Field('calle','string'),
                 db.Field('numero_calle','integer'),
                 db.Field('entre_calle_1','string'),
                 db.Field('entre_calle_2','string'),
                 db.Field('telefono_1', 'string'),
                 db.Field('telefono_2','string'),
                 db.Field('telefono_3','string'),
                 db.Field('email','string'),
                 db.Field('tipo_de_plan',db.planes),
                 db.Field('costo_de_instalacion',db.costos_instalaciones),
                 db.Field('tecnico_asignado', db.tecnicos),
                 db.Field('fecha_estimada', 'date'),
                 db.Field('estado', 'string'))
db.instalaciones.dni.requires=IS_NOT_IN_DB(db, db.instalaciones.dni, error_message = 'El DNI ingresado  ya se encuentra registrado') ,IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.instalaciones.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.instalaciones.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.instalaciones.localidad.requires=IS_IN_DB(db,db.localidades.id,'%(localidad)s',zero=T('Seleccione localidad'), error_message= 'Campo obligatorio')
db.instalaciones.calle.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.instalaciones.numero_calle.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.instalaciones.entre_calle_1.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.instalaciones.entre_calle_2.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.instalaciones.telefono_1.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.instalaciones.email.requires=IS_EMAIL(error_message='El correo electronico no es válido'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres'),IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.instalaciones.tipo_de_plan.requires=IS_IN_DB(db,db.planes.id,'%(velocidad)s',zero=T('Seleccione localidad'), error_message= 'Campo obligatorio')
db.instalaciones.costo_de_instalacion.requires=IS_IN_DB(db,db.costos_instalaciones.id,'$ ' + '%(precio)s' + ' (' + '%(descripcion)s' + ')',zero=T('Seleccione costo'), error_message= 'Campo obligatorio')
db.instalaciones.tecnico_asignado.requires=IS_IN_DB(db,db.tecnicos.id,'%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione tecnico'),error_message= 'Campo obligatorio')
db.instalaciones.fecha_estimada.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_DATE('%d/%M/%Y')



#Costo de soporte
db.define_table('costos_soportes',
                 db.Field('descripcion','string'),
                 db.Field('precio','double'))
db.costos_soportes.descripcion.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.costos_soportes.precio.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(7, error_message='Solo hasta 7 caracteres')

#Clientes#  #Revisar
db.define_table('clientes',
                 db.Field('dni', 'integer'),
                 db.Field('nombre', 'string'),
                 db.Field('apellido','string'),
                 db.Field('localidad', db.localidades),
                 db.Field('calle','string'),
                 db.Field('numero_calle','integer'),
                 db.Field('entre_calle_1', 'string'),
                 db.Field('entre_calle_2', 'string'),
                 db.Field('telefono_1','string'),
                 db.Field('telefono_2','string'),
                 db.Field('telefono_3','string'),
                 db.Field('tipo_de_plan', db.planes),
                 db.Field('panel', db.paneles),
                 db.Field('direccion_ip', 'string'),
                 db.Field('numero_tarjeta','integer'),
                 db.Field('fecha_alta', 'date'),
                 db.Field('fecha_baja', 'date'))
db.clientes.dni.requires=IS_NOT_IN_DB(db, db.clientes.dni, error_message = 'El DNI ingresado  ya se encuentra registrado') ,IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.clientes.tipo_de_plan.requires=IS_IN_DB(db,db.planes.id,'%(velocidad)s',zero=T('Seleccione plan'),error_message= 'Campo obligatorio')
db.clientes.panel.requires=IS_IN_DB(db,db.paneles.id,'%(nombre)s',zero=T('Seleccione panel'),error_message= 'Campo obligatorio')
db.clientes.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.clientes.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.clientes.numero_tarjeta.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.clientes.localidad.requires=IS_IN_DB(db,db.localidades.id,'%(localidad)s',zero=T('Seleccione localidad'),error_message= 'Campo obligatorio')
db.clientes.calle.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.clientes.numero_calle.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.clientes.entre_calle_1.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.clientes.entre_calle_2.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.clientes.telefono_1.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.clientes.fecha_alta.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_DATE('%d/%M/%Y')
#db.clientes.fecha_baja.requires=IS_DATE('%d/%M/%Y')


#Pagos ( resolver )
db.define_table('pagos',
                 db.Field('cliente', db.clientes),
                 db.Field('fecha_pago','date'),
                 db.Field('abono', 'string'))

db.pagos.cliente.requires=IS_IN_DB(db,db.clientes.id,'%(id)s' + ' - ' + '%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione cliente'),error_message= 'Campo obligatorio')
db.pagos.fecha_pago.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_DATE('%d/%M/%Y')
db.pagos.abono.requires=IS_IN_SET(['200', '300', '400', '600'], zero=T('Seleccione abono'),error_message= 'Campo obligatorio')



##abonos
db.define_table('abonos',
                 db.Field('cliente', db.clientes),
                 db.Field('tipo_de_plan', db.planes),
                 db.Field('mes','string'),
                 db.Field('ano', 'integer'),
                 db.Field('importe',db.pagos ))

db.abonos.cliente.requires=IS_IN_DB(db,db.clientes.id,'%(id)s' + ' - ' + '%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione cliente'),error_message= 'Campo obligatorio')
db.abonos.tipo_de_plan.requires=IS_IN_DB(db,db.planes.id,'%(velocidad)s' + ' - ' + '%(precio)s',zero=T('Seleccione velocidad'),error_message= 'Campo obligatorio')
db.abonos.mes.requires=IS_IN_SET(['Enero', 'Febrero', 'Marzo', 'Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'], zero=T('Seleccione mes'),error_message= 'Campo obligatorio')
db.abonos.ano.requires=IS_IN_SET(['2017'], zero=T('Seleccione año'),error_message= 'Campo obligatorio')
db.abonos.importe.requires=IS_IN_DB(db,db.pagos.id,'%(abono)s',zero=T('Seleccione abono'),error_message= 'Campo obligatorio')


db.define_table('soportes_tecnicos',
                 db.Field('cliente', db.clientes),
                 db.Field('problematica', 'string'),
                 db.Field('tecnico_asignado', db.tecnicos),
                 db.Field('fecha_estimada','date'),
                 db.Field('estado', 'string', readable=False, writable=False))


db.soportes_tecnicos.cliente.requires=IS_IN_DB(db,db.clientes.id,'%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione cliente'), error_message= 'Campo obligatorio')
db.soportes_tecnicos.problematica.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.soportes_tecnicos.tecnico_asignado.requires=IS_EMPTY_OR(IS_IN_DB(db,db.tecnicos.id,'%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione tecnico')))
db.soportes_tecnicos.fecha_estimada.requires=IS_EMPTY_OR(IS_DATE('%d/%M/%Y'))


#Historiales ( resolver )
db.define_table('historiales',
                 db.Field('soporte', db.soportes_tecnicos),
                 db.Field('solucion', 'string'),
                 db.Field('costo_de_soporte', db.costos_soportes))


db.historiales.soporte.requires=IS_IN_DB(db,db.soportes_tecnicos.id, '%(problematica)s',zero=T('Seleccione problematica'), error_message= 'Campo obligatorio')
db.historiales.costo_de_soporte.requires=IS_IN_DB(db,db.costos_soportes.id,'%(precio)s',zero=T('Seleccione costo'), error_message= 'Campo obligatorio')


#Mantenimientos
db.define_table('mantenimientos',
                 db.Field('tecnico_principal',db.tecnicos),
                 db.Field('tecnico_secundario',db.tecnicos),
                 db.Field('nodo',db.nodos),
                 db.Field('fecha','date'),
                 db.Field('descripcion','string'))

db.mantenimientos.tecnico_principal.requires=IS_IN_DB(db,db.tecnicos.id,'%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione tecnico'), error_message= 'Campo obligatorio')
db.mantenimientos.tecnico_secundario.requires=IS_EMPTY_OR(IS_IN_DB(db,db.tecnicos.id,'%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione tecnico')))
db.mantenimientos.nodo.requires=IS_IN_DB(db,db.nodos.id,'%(nombre)s',zero=T('Seleccione nodo'), error_message= 'Campo obligatorio')
db.mantenimientos.fecha.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_DATE('%d/%M/%Y')
db.mantenimientos.descripcion.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')
