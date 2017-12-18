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
#auth = Auth(db, host_names=myconf.get('host.names'))
#service = Service()
#plugins = PluginManager()

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
#auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
#mail = auth.settings.mailer
#mail.settings.server = 'smtp.gmail.com:587'
#mail.settings.sender = 'staff.technology.internet@gmail.com'
#mail.settings.login = 'staff.technology.internet@gmail.com:naruto87'
#mail.settings.tls = myconf.get('smtp.tls') or False
#mail.settings.ssl = myconf.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
#auth.settings.registration_requires_verification = False
#auth.settings.registration_requires_approval = False
#auth.settings.reset_password_requires_verification = True

#############################################################################################

db.define_table('localidades',
                 db.Field('localidad', 'string'),
                 db.Field('codigo_postal','integer'))

db.localidades.codigo_postal.requires= IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')

#############################################################################################

db.define_table('auth_user',
                db.Field('first_name',length=128, label=T('First name')),
                db.Field('last_name',length=128, label=T('Last name')),
                db.Field('dni', 'integer'),
                db.Field('direccion', 'string'),
                db.Field('numero_de_calle', 'integer'),
                db.Field('localidad', db.localidades),
                db.Field('telefono', 'integer'),
                db.Field('email',length=128, label=T('E-mail')),
                db.Field('password','password',default='',label=T('Password'),readable=False),
                db.Field('registration_key',length=64,default='',readable=False,writable=False),
                db.Field('reset_password_key',length=64,default='',readable=False,writable=False),
                db.Field('registration_id', length=512, writable=False, readable=False, default=''))

db.auth_user.first_name.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.auth_user.last_name.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.auth_user.dni.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_NOT_IN_DB(db, db.auth_user.dni, error_message = 'El DNI ya se encuentra registrado'),IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.auth_user.direccion.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.auth_user.numero_de_calle.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.auth_user.localidad.requires=IS_IN_DB(db,db.localidades.id,'%(localidad)s',zero=T('Seleccione localidad'), error_message= 'Campo obligatorio')
db.auth_user.telefono.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.auth_user.email.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_EMAIL(error_message='El correo electrónico no es válido')
db.auth_user.password.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')

#############################################################################################

db.define_table('auth_group',
                db.Field('role',length=128, label=T('Role')),
                db.Field('description',length=128, label=T('Description')))

#############################################################################################

db.define_table('auth_membership',
                db.Field('user_id',db.auth_user, label=T('User ID')),
                db.Field('group_id',db.auth_group, label=T('Group ID')),
                db.Field('nombre','string'),
                db.Field('apellido','string'))

db.auth_membership.user_id.requires=IS_IN_DB(db,db.auth_user.id,'%(first_name)s' + ' ' + '%(last_name)s',zero=T('Seleccione usuario'), error_message= 'Campo obligatorio')
db.auth_membership.group_id.requires=IS_IN_DB(db,db.auth_group.id,'%(role)s',zero=T('Seleccione grupo'), error_message= 'Campo obligatorio')
auth = Auth(db)
auth.define_tables(username=False, signature=False)
auth.settings.on_failed_authorization=URL(c='default',f='sin_autorizacion')
auth.settings.logout_next=URL(c='default',f='index')

#############################################################################################

db.define_table('costos_instalaciones',
                 db.Field('descripcion','string'),
                 db.Field('precio','double'))

db.costos_instalaciones.descripcion.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.costos_instalaciones.precio.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(7, error_message='Solo hasta 7 caracteres')

#############################################################################################

db.define_table('costos_soportes',
                 db.Field('descripcion','string'),
                 db.Field('precio','double'))

db.costos_soportes.descripcion.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.costos_soportes.precio.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(7, error_message='Solo hasta 7 caracteres')

#############################################################################################

db.define_table('planes',
                 db.Field('velocidad_de_bajada','string'),
                 db.Field('unidad_de_bajada','string'),
                 db.Field('velocidad_de_subida','string'),
                 db.Field('unidad_de_subida','string'),
                 db.Field('precio','double'))

db.planes.velocidad_de_bajada.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(8, error_message='Solo hasta 6 caracteres')
db.planes.unidad_de_bajada.requires=IS_IN_SET(['Mbps','Kbps', 'Gbps'], zero=T('Seleccione unidad'), error_message= 'Campo obligatorio')
db.planes.velocidad_de_subida.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(8, error_message='Solo hasta 6 caracteres')
db.planes.unidad_de_subida.requires=IS_IN_SET(['Mbps','Kbps', 'Gbps'], zero=T('Seleccione unidad'), error_message= 'Campo obligatorio')
db.planes.precio.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(7, error_message='Solo hasta 7 caracteres')

#############################################################################################

db.define_table('nodos',
                 db.Field('nombre','string'),
                 db.Field('subred','string'),
                 db.Field('localidad',db.localidades),
                 db.Field('direccion','string'),
                 db.Field('numero_de_calle','integer'),
                 db.Field('rango_km','integer'),
                 db.Field('latitud','double',default=0.0,readable=False,writable=False),
                 db.Field('longitud','double',default=0.0,readable=False,writable=False))

db.nodos.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.nodos.subred.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(17, error_message='Solo hasta 3 caracteres')
db.nodos.localidad.requires=IS_IN_DB(db,db.localidades.id,'%(localidad)s',zero=T('Seleccione localidad'), error_message= 'Campo obligatorio')

#############################################################################################

db.define_table('paneles',
                 db.Field('nombre','string'),
                 db.Field('modelo', 'string'),
                 db.Field('modalidad', 'string'),
                 db.Field('orientacion', 'string'),
                 db.Field('frecuencia','string'),
                 db.Field('velocidad_de_bajada','string'),
                 db.Field('unidad_de_bajada', 'string'),
                 db.Field('velocidad_de_subida','string'),
                 db.Field('unidad_de_subida', 'string'),
                 db.Field('ssid','string'),
                 db.Field('clave','string'),
                 db.Field('nodo',db.nodos))

db.paneles.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.paneles.modelo.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.paneles.modalidad.requires=IS_IN_SET(['Punto de acceso','Estacion'], zero=T('Seleccione modo'), error_message= 'Campo obligatorio')
db.paneles.frecuencia.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.paneles.unidad_de_bajada.requires=IS_IN_SET(['Mbps','Kbps', 'Gbps'], zero=T('Seleccione unidad'), error_message= 'Campo obligatorio')
db.paneles.unidad_de_subida.requires=IS_IN_SET(['Mbps','Kbps', 'Gbps'], zero=T('Seleccione unidad'), error_message= 'Campo obligatorio')
db.paneles.ssid.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.paneles.clave.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.paneles.nodo.requires=IS_IN_DB(db,db.nodos.id,'%(nombre)s',zero=T('Seleccione nodo'), error_message= 'Campo obligatorio')

#############################################################################################

db.define_table('solicitudes_instalacion',
                 db.Field('nombre','string'),
                 db.Field('apellido','string'),
                 db.Field('dni','integer'),
                 db.Field('direccion','string'),
                 db.Field('numero_de_calle','integer'),
                 db.Field('latitud','double',default=0.0,readable=False,writable=False),
                 db.Field('longitud','double',default=0.0,readable=False,writable=False),
                 db.Field('entre_calle_1','string'),
                 db.Field('entre_calle_2','string'),
                 db.Field('localidad',db.localidades),
                 db.Field('telefono', 'string'),
                 db.Field('telefono_alternativo','string'),
                 db.Field('correo_electronico','string'),
                 db.Field('tipo_de_plan',db.planes),
                 db.Field('costo_de_instalacion',db.costos_instalaciones),
                 db.Field('tecnico',db.auth_user),
                 db.Field('fecha_estimada', 'date'),
                 db.Field('estado', 'string', readable=False, writable=False))

db.solicitudes_instalacion.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.solicitudes_instalacion.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.solicitudes_instalacion.dni.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_NOT_IN_DB(db, db.solicitudes_instalacion.dni, error_message = 'El DNI ya se encuentra registrado'),IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.solicitudes_instalacion.direccion.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.solicitudes_instalacion.numero_de_calle.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.solicitudes_instalacion.entre_calle_1.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.solicitudes_instalacion.entre_calle_2.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.solicitudes_instalacion.localidad.requires=IS_IN_DB(db,db.localidades.id,'%(localidad)s',zero=T('Seleccione localidad'), error_message= 'Campo obligatorio')
db.solicitudes_instalacion.telefono.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.solicitudes_instalacion.correo_electronico.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_EMAIL(error_message='El correo electrónico no es válido'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres')
db.solicitudes_instalacion.tipo_de_plan.requires=IS_IN_DB(db,db.planes.id,'%(velocidad_de_bajada)s' + ' ' + '%(unidad_de_bajada)s',zero=T('Seleccione plan'), error_message= 'Campo obligatorio')
db.solicitudes_instalacion.costo_de_instalacion.requires=IS_IN_DB(db,db.costos_instalaciones.id,'$ ' + '%(precio)s' + ' ( ' + '%(descripcion)s' + ' )',zero=T('Seleccione costo'), error_message= 'Campo obligatorio')
db.solicitudes_instalacion.tecnico.requires = IS_EMPTY_OR(IS_IN_DB(db((db.auth_group.role == 'Tecnicos') & (db.auth_group.id == db.auth_membership.group_id)), 'auth_membership.user_id', '%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione tecnico')))
db.solicitudes_instalacion.fecha_estimada.requires=IS_EMPTY_OR(IS_DATE(str(T('%Y-%m-%d'))))
db.solicitudes_instalacion.estado.default='Pendiente'
db.solicitudes_instalacion.tecnico.default=None
db.solicitudes_instalacion.fecha_estimada.default=None

#############################################################################################

db.define_table('instalaciones',
                 db.Field('numero_de_solicitud', db.solicitudes_instalacion,readable=False,writable=False),
                 db.Field('panel', db.paneles),
                 db.Field('direccion_ip','string'),
                 db.Field('fecha_alta','date'))

db.instalaciones.fecha_alta.requires=IS_DATE(str(T('%Y-%m-%d')))
db.instalaciones.panel.requires=IS_IN_DB(db,db.paneles.id, '%(nombre)s',zero=T('Seleccione panel'), error_message= 'Campo obligatorio')

#############################################################################################

db.define_table('clientes',
                 db.Field('numero_de_instalacion', db.instalaciones,readable=False,writable=False),
                 db.Field('nombre','string'),
                 db.Field('apellido','string'),
                 db.Field('dni','integer'),
                 db.Field('direccion','string'),
                 db.Field('numero_de_calle','integer'),
                 db.Field('latitud','double',default=0.0,readable=False,writable=False),
                 db.Field('longitud','double',default=0.0,readable=False,writable=False),
                 db.Field('entre_calle_1','string'),
                 db.Field('entre_calle_2','string'),
                 db.Field('localidad',db.localidades),
                 db.Field('telefono', 'string'),
                 db.Field('telefono_alternativo','string'),
                 db.Field('correo_electronico','string'),
                 db.Field('tipo_de_plan', db.planes))

#############################################################################################

db.define_table('solicitudes_soporte',
                 db.Field('cliente', db.clientes, readable=False, writable=False),
                 db.Field('problematica','string'),
                 db.Field('tecnico', db.auth_user),
                 db.Field('fecha_estimada','date'),
                 db.Field('estado', 'string', readable=False, writable=False))

db.solicitudes_soporte.tecnico.requires = IS_EMPTY_OR(IS_IN_DB(db((db.auth_group.role == 'Tecnicos') & (db.auth_group.id == db.auth_membership.group_id)), 'auth_membership.user_id', '%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione tecnico')))
db.solicitudes_soporte.fecha_estimada.requires=IS_EMPTY_OR(IS_DATE(str(T('%Y-%m-%d'))))
db.solicitudes_soporte.estado.default='Pendiente'
db.solicitudes_soporte.tecnico.default=None
db.solicitudes_soporte.fecha_estimada.default=None

#############################################################################################

db.define_table('soportes',
                 db.Field('numero_de_solicitud', db.solicitudes_soporte, readable=False,writable=False),
                 db.Field('descripcion', 'string'),
                 db.Field('costo_de_soporte', db.costos_soportes))

db.soportes.costo_de_soporte.requires=IS_IN_DB(db,db.costos_soportes.id,'%(precio)s',zero=T('Seleccione costo'), error_message= 'Campo obligatorio')

#############################################################################################

db.define_table('mantenimientos',
                 db.Field('tecnico_principal',db.auth_user),
                 db.Field('tecnico_secundario',db.auth_user),
                 db.Field('nodo',db.nodos),
                 db.Field('fecha','date'),
                 db.Field('descripcion','string'))

db.mantenimientos.tecnico_principal.requires = IS_IN_DB(db((db.auth_group.role == 'Tecnicos') & (db.auth_group.id == db.auth_membership.group_id)), 'auth_membership.user_id', '%(nombre)s')
db.mantenimientos.tecnico_secundario.requires = IS_IN_DB(db((db.auth_group.role == 'Tecnicos') & (db.auth_group.id == db.auth_membership.group_id)), 'auth_membership.user_id', '%(nombre)s')
db.mantenimientos.nodo.requires=IS_IN_DB(db,db.nodos.id,'%(nombre)s',zero=T('Seleccione nodo'), error_message= 'Campo obligatorio')
db.mantenimientos.fecha.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_DATE('%d/%M/%Y')
db.mantenimientos.descripcion.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio')

#############################################################################################

#Creamos las tablas y campos usados para AFIP
import datetime
migrate = True



# Constantes (para la aplicación)

WEBSERVICES = ['wsfe','wsbfe','wsfex','wsfev1', 'wsmtx']
INCOTERMS = ['EXW','FCA','FAS','FOB','CFR','CIF','CPT','CIP','DAF','DES','DEQ','DDU','DDP']
CONCEPTOS = {'1': 'Productos', '2': 'Servicios', '3': 'Otros/ambos'}
IDIOMAS = {'1':'Español', '2': 'Inglés', '3': 'Portugués'}
SINO = {'S': 'Si', 'N': 'No'}

# Tablas dinámicas (pueden cambiar por AFIP/Usuario):

# Tipo de documento (FCA, FCB, FCC, FCE, NCA, RCA, etc.)
db.define_table('tipo_cbte',
    Field('codigo', type='id'),
    Field('descripcion'),
    Field('discriminar', 'boolean'),
    format="%(descripcion)s",
    migrate=migrate,
    )

# Tipos de documentos (CUIT, CUIL, CDI, DNI, CI, etc.)
db.define_table('tipo_doc',
    Field('codigo', type='id'),
    Field('descripcion'),
    format="%(descripcion)s",
    migrate=migrate,
    )

# Monedas (PES: Peso, DOL: DOLAR, etc.)
db.define_table('moneda',
    Field('codigo', type='string'),
    Field('descripcion'),
    format="%(descripcion)s",
    migrate=migrate,
    )

# Unidades de medida (u, kg, m, etc.) 
db.define_table('umed',
    Field('codigo', type='id'),
    Field('descripcion'),
    format="%(descripcion)s",
    migrate=migrate,
    )

# Alícuotas de IVA (EX, NG, 0%, 10.5%, 21%, 27%)
db.define_table('iva',
    Field('codigo', type='id'),
    Field('descripcion'),
    Field('aliquota', 'double'),
    format="%(descripcion)s",
    migrate=migrate,
    )

# Paises (destino de exportación)
db.define_table('pais_dst',
    Field('codigo', type='id'),
    Field('descripcion'),
    format="%(descripcion)s",
    migrate=migrate,
    )

# CONSTANTES:

#Nomero de punto de venta, cambiar segun corresponda 
PUNTO_VTA = 4033


# Tablas principales

# Datos generales del comprobante:
db.define_table('comprobante_afip',
    Field('id', type='id'),
    Field('webservice', type='string', length=6, default='wsfev1',
            requires = IS_IN_SET(WEBSERVICES)),
    Field('fecha_cbte', type='string', # default=request.now.date(), #.strftime("%Y%m%d"),
            requires=IS_NOT_EMPTY(),
            comment="Fecha de emisión"),
    Field('tipo_cbte', type=db.tipo_cbte, ),
    Field('punto_vta', type='integer', 
            comment="Prefijo Habilitado", default=PUNTO_VTA,
            requires=IS_NOT_EMPTY()),
    Field('cbte_nro', type='integer',
            comment="Número", default=1,
            requires=IS_NOT_EMPTY()),
    Field('concepto', type='integer', default=1,
            requires=IS_IN_SET(CONCEPTOS),),
    Field('permiso_existente', type='string', length=1, default="N",
            requires=IS_IN_SET(SINO),
            comment="Permiso de Embarque (exportación)"),
    Field('dst_cmp', type=db.pais_dst, default=200,
            comment="País de destino (exportación)"),
    Field('nombre_cliente', type='string', length=200),
    Field('tipo_doc', type=db.tipo_doc, default='80'),
    Field('nro_doc', type='string',
            requires=IS_CUIT()),
    Field('domicilio_cliente', type='string', length=300),
    Field('telefono_cliente', type='string', length=50),
    Field('localidad_cliente', type='string', length=50),
    Field('provincia_cliente', type='string', length=50),
    Field('email', type='string', length=100),
    Field('id_impositivo', type='string', length=50,
            comment="CNJP, RUT, RUC (exportacion)"),
    Field('imp_total', type='double', writable=False),
    Field('imp_tot_conc', type='double', writable=False),
    Field('imp_neto', type='double', writable=False),
    Field('impto_liq', type='double', writable=False),
    Field('impto_liq_rni', type='double', writable=False),
    Field('imp_op_ex', type='double', writable=False),
    Field('impto_perc', type='double', writable=False),
    Field('imp_iibb', type='double', writable=False),
    Field('impto_perc_mun', type='double', writable=False),
    Field('imp_internos', type='double', writable=False),
    Field('moneda_id', type=db.moneda, length=3, default=14),
    Field('moneda_ctz', type='double', default="1.000"),
    Field('obs_comerciales', type='string', length=1000),
    Field('obs', type='text', length=1000),
    Field('forma_pago', type='string', length=50),
    Field('incoterms', type='string', length=3,
        requires=IS_EMPTY_OR(IS_IN_SET(INCOTERMS)),
        comment="Términos de comercio exterior"),
    Field('incoterms_ds', type='string', length=20),
    Field('idioma_cbte', type='string', length=1, default="1",
           requires=IS_IN_SET(IDIOMAS)),
    Field('zona', type='string', length=5, default="0",
            comment="(no usado)", writable=False),
    Field('fecha_venc_pago', type='string', length=8,
           comment="(servicios)"),
    Field('fecha_serv_desde', type='string', length=8,
            comment="(servicios)"),
    Field('fecha_serv_hasta', type='string', 
            comment="(servicios)"),
    Field('cae', type='string', writable=False),
    Field('fecha_vto', type='string', length=8, writable=False),
    Field('resultado', type='string', length=1, writable=False),
    Field('reproceso', type='string', length=1, writable=False),
    Field('motivo', type='text', length=40, writable=False),
    Field('err_code', type='string', length=6, writable=False),
    Field('err_msg', type='string', length=1000, writable=False),
    Field('formato_id', type='integer', writable=False),
    migrate=migrate)

# detalle de los artículos por cada comprobante
db.define_table('detalle_afip',
    Field('id', type='id'),
    Field('comprobante_id', type='reference comprobante_afip', 
            readable=False, writable=False),
    Field('codigo', type='string', length=30,
            requires=IS_NOT_EMPTY()),
    Field('ds', type='text', length=4000, label="Descripción",
            requires=IS_NOT_EMPTY()),
    Field('qty', type='double', label="Cant.", default=1,
            requires=IS_FLOAT_IN_RANGE(0.0001, 1000000000)),
    Field('precio', type='double', notnull=True,
            requires=IS_FLOAT_IN_RANGE(0.01, 1000000000)),
    Field('umed', type=db.umed, default=7,
            ),
    Field('imp_total', type='double', label="Subtotal",
            requires=IS_NOT_EMPTY()),
    Field('iva_id', type=db.iva, default=5, label="IVA",
            represent=lambda id: db.iva[id].descripcion,
            comment="Alícuota de IVA"),
    Field('ncm', type='string', length=15, 
            comment="Código Nomenclador Común Mercosur (Bono fiscal)"),
    Field('sec', type='string', length=15,
            comment="Código Secretaría de Comercio (Bono fiscal)"),
    Field('bonif', type='double', default=0.00),
    Field('imp_iva', type="double", default=0.00, 
            comment="Importe de IVA liquidado",
            readable=False, writable=False),
    migrate=migrate)

db.detalle_afip.umed.represent=lambda id: db.umed[id].descripcion

# Comprobantes asociados (para NC yND):
db.define_table('cmp_asoc',
    Field('id', type='id'),
    Field('comprobante_id', type='reference comprobante_afip'),
    Field('tipo_reg', type='integer'),
    Field('cbte_tipo', type='integer'),
    Field('cbte_punto_vta', type='integer'),
    Field('cbte_nro', type='integer'),
    migrate=migrate)

# Permisos de exportación (si es requerido):
db.define_table('permiso',
    Field('id', type='id'),
    Field('comprobante_id', type='reference comprobante_afip'),
    Field('tipo_reg', type='integer'),
    Field('id_permiso', type='string', length=16),
    Field('dst_merc', type=db.pais_dst),
    migrate=migrate)

# Tablas de depuración

# Bitácora de mensajes XML enviados y recibidos
db.define_table('mensajes_xml',
    Field('id', type='id'),
    Field('comprobante_id', type='reference comprobante_afip'),
    Field('response', type='text'),
    Field('request', type='text'),
    Field('ts', type='string', default=request.now),
    migrate=migrate)
