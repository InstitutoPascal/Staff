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


#############################################################################################

db.define_table('gerentes',
                 db.Field('nombre','string'),
                 db.Field('apellido','string'),
                 db.Field('dni','integer'),
                 db.Field('correo_electronico' ,'string'),
                 db.Field('telefono', 'integer'),
                 db.Field('clave', 'password'))

db.gerentes.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.gerentes.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.gerentes.dni.requires=IS_NOT_IN_DB(db, db.gerentes.dni, error_message = 'El DNI ingresado  ya se encuentra registrado') ,IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.gerentes.correo_electronico.requires=IS_EMAIL(error_message='El correo electronico no es válido'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres'),IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.gerentes.clave.requires = CRYPT(key=auth.settings.hmac_key, error_message= 'Campo obligatorio')
db.gerentes.telefono.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')

#############################################################################################

db.define_table('administradores',
                 db.Field('nombre','string'),
                 db.Field('apellido','string'),
                 db.Field('dni','integer'),
                 db.Field('correo_electronico' ,'string'),
                 db.Field('telefono', 'integer'),
                 db.Field('clave', 'password'))

db.administradores.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.administradores.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.administradores.dni.requires=IS_NOT_IN_DB(db, db.administradores.dni, error_message = 'El DNI ingresado  ya se encuentra registrado') ,IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.administradores.correo_electronico.requires=IS_EMAIL(error_message='El correo electronico no es válido'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres'),IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.administradores.clave.requires = CRYPT(key=auth.settings.hmac_key,  error_message= 'Campo obligatorio')
db.administradores.telefono.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')

#############################################################################################

db.define_table('tecnicos',
                 db.Field('nombre','string'),
                 db.Field('apellido','string'),
                 db.Field('dni','integer'),
                 db.Field('correo_electronico' ,'string'),
                 db.Field('telefono', 'integer'),
                 db.Field('clave', 'password'))

db.tecnicos.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.tecnicos.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
db.tecnicos.dni.requires=IS_NOT_IN_DB(db, db.tecnicos.dni, error_message = 'El DNI ingresado  ya se encuentra registrado') ,IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.tecnicos.correo_electronico.requires=IS_EMAIL(error_message='El correo electronico no es válido'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres'),IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.tecnicos.clave.requires = CRYPT(key=auth.settings.hmac_key, error_message= 'Campo obligatorio')
db.tecnicos.telefono.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')

#############################################################################################

db.define_table('localidades',
                 db.Field('localidad', 'string'),
                 db.Field('codigo_postal','integer'))

db.localidades.codigo_postal.requires= IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')

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
                 db.Field('localidad',db.localidades))

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
                 db.Field('tecnico_asignado', db.tecnicos),
                 db.Field('fecha_estimada', 'date'),
                 db.Field('estado', 'string', readable=False, writable=False))

db.solicitudes_instalacion.nombre.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.solicitudes_instalacion.apellido.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.solicitudes_instalacion.dni.requires=IS_NOT_IN_DB(db, db.solicitudes_instalacion.dni, error_message = 'El DNI ingresado  ya se encuentra registrado') ,IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.solicitudes_instalacion.direccion.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.solicitudes_instalacion.numero_de_calle.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.solicitudes_instalacion.entre_calle_1.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.solicitudes_instalacion.entre_calle_2.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.solicitudes_instalacion.localidad.requires=IS_IN_DB(db,db.localidades.id,'%(localidad)s',zero=T('Seleccione localidad'), error_message= 'Campo obligatorio')
db.solicitudes_instalacion.telefono.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.solicitudes_instalacion.correo_electronico.requires=IS_EMAIL(error_message='El correo electronico no es válido'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres'),IS_NOT_EMPTY(error_message= 'Campo obligatorio')
db.solicitudes_instalacion.tipo_de_plan.requires=IS_IN_DB(db,db.planes.id,'%(velocidad_de_bajada)s' + ' ' + '%(unidad_de_bajada)s',zero=T('Seleccione plan'), error_message= 'Campo obligatorio')
db.solicitudes_instalacion.costo_de_instalacion.requires=IS_IN_DB(db,db.costos_instalaciones.id,'$ ' + '%(precio)s' + ' ( ' + '%(descripcion)s' + ' )',zero=T('Seleccione costo'), error_message= 'Campo obligatorio')
db.solicitudes_instalacion.tecnico_asignado.requires=IS_IN_DB(db,db.tecnicos.id,'%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione tecnico'),error_message= 'Campo obligatorio')
db.solicitudes_instalacion.fecha_estimada.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_DATE('%d/%M/%Y')
db.solicitudes_instalacion.estado.default='Pendiente'
db.solicitudes_instalacion.tecnico_asignado.default=None
db.solicitudes_instalacion.fecha_estimada.default=None

#############################################################################################

db.define_table('instalaciones',
                 db.Field('numero_de_solicitud', db.solicitudes_instalacion,readable=False,writable=False),
                 db.Field('panel', db.paneles),
                 db.Field('direccion_ip','string'),
                 db.Field('fecha_alta','date'))

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

db.define_table('soportes_tecnicos',
                 db.Field('cliente', db.clientes, readable=False, writable=False),
                 db.Field('problematica', 'string'),
                 db.Field('tecnico_asignado', db.tecnicos),
                 db.Field('fecha_estimada','date'),
                 db.Field('estado', 'string', readable=False, writable=False))


db.soportes_tecnicos.problematica.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.soportes_tecnicos.tecnico_asignado.requires=IS_EMPTY_OR(IS_IN_DB(db,db.tecnicos.id,'%(nombre)s' + ' ' + '%(apellido)s',zero=T('Seleccione tecnico')))
db.soportes_tecnicos.fecha_estimada.requires=IS_EMPTY_OR(IS_DATE('%d/%M/%Y'))
db.soportes_tecnicos.estado.default='Pendiente'

#############################################################################################

db.define_table('historiales',
                 db.Field('soporte', db.soportes_tecnicos),
                 db.Field('solucion', 'string'),
                 db.Field('costo_de_soporte', db.costos_soportes))

db.historiales.soporte.requires=IS_IN_DB(db,db.soportes_tecnicos.id, '%(problematica)s',zero=T('Seleccione problematica'), error_message= 'Campo obligatorio')
db.historiales.costo_de_soporte.requires=IS_IN_DB(db,db.costos_soportes.id,'%(precio)s',zero=T('Seleccione costo'), error_message= 'Campo obligatorio')

#############################################################################################

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

#############################################################################################

db.define_table('productos',
                 db.Field('nombre', 'string'),
                 db.Field('marca', 'string'),
                 db.Field('descripcion', 'string'))

#############################################################################################

db.define_table('proveedores',
                 db.Field('empresa','string'),
                 db.Field('localidad',db.localidades),
                 db.Field('direccion','string'),
                 db.Field('numero_de_calle' ,'integer'),
                 db.Field('correo_electronico', 'string'),
                 db.Field('telefono', 'integer'),
                 db.Field('tipo_de_provision', 'string'),
                 db.Field('condicion_iva', 'string'),
                 db.Field('numero_de_cuit', 'integer'),
                 db.Field('ingresos_brutos', 'integer'))

db.proveedores.localidad.requires=IS_IN_DB(db,db.localidades.id,'%(localidad)s',zero=T('Seleccione localidad'), error_message= 'Campo obligatorio')
db.proveedores.tipo_de_provision.requires=IS_IN_SET(['Producto', 'Servicio'], zero=T('Seleccione tipo de provisión'),error_message= 'Campo obligatorio')
db.proveedores.condicion_iva.requires=IS_IN_SET(['Monotributista', 'Responsable inscripto'], zero=T('Seleccione condicion'),error_message= 'Campo obligatorio')

#############################################################################################

db.define_table('compras',
                 db.Field('proveedor', db.proveedores),
                 db.Field('producto', db.productos),
                 db.Field('fecha_de_compra','date'),
                 db.Field('condicion_de_pago','string'),
                 db.Field('precio_de_compra', 'double'),
                 db.Field('cantidad', 'integer'),
                 db.Field('total', 'double', readable=False, writable=False))

db.compras.proveedor.requires=IS_IN_DB(db,db.proveedores.id,'%(empresa)s',zero=T('Seleccione proveedor'), error_message= 'Campo obligatorio')
db.compras.producto.requires=IS_IN_DB(db,db.productos.id,'%(nombre)s',zero=T('Seleccione producto'), error_message= 'Campo obligatorio')
db.compras.fecha_de_compra.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_DATE('%d/%M/%Y')
db.compras.condicion_de_pago.requires=IS_IN_SET(['Contado', 'Cuenta corriente'], zero=T('Seleccione '),error_message= 'Campo obligatorio')

#############################################################################################

db.define_table('stock',
                 db.Field('fecha', 'date'),
                 db.Field('detalle', db.productos),
                 db.Field('cantidad_entrada','integer'),
                 db.Field('costo_unitario_entrada','double'),
                 db.Field('total_entrada', 'double'),
                 db.Field('cantidad_salida', 'integer', 'string'),
                 db.Field('costo_unitario_salida','double'),
                 db.Field('total_salida', 'double'),
                 db.Field('cantidad_existencia','integer'),
                 db.Field('costo_unitario_existencia','double'),
                 db.Field('total_existencia', 'double'))

#############################################################################################
