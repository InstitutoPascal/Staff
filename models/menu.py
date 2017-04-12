# -*- coding: utf-8 -*-

response.logo = A(B('web', SPAN(2), 'py'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

response.google_analytics_id = None

response.menu = [(T('Home'), False, URL('default', 'index'), [])]  #Boton Home (vuelve a index)

DEVELOPMENT_MENU = True

if "auth" in locals():
    auth.wikimenu()


### Menu Altas ###

response.menu+=[(T('realizar altas'),False,'#',
                     [(T('Internas'),False,'#',
                       [(T('Gerentes'),False,URL(request.application,'altas','alta_gerentes'),[]),
                        (T('Administradores'),False,URL(request.application,'altas','alta_administradores'),[]),
                        (T('Tecnicos'),False,URL(request.application,'altas','alta_tecnicos'),[]),
                        (T('Localidades'),False,URL(request.application,'altas','alta_localidad'),[])],),
                       (T('Sistema'),False,'#',
                       [(T('Nodos'),False,URL(request.application,'altas','alta_nodos'),[]),
                        (T('Paneles'),False,URL(request.application,'altas','alta_paneles'),[]),
                        (T('Mantenimientos'),False,URL(request.application,'altas','alta_mantenimiento'),[]),
                        (T('Planes'),False,URL(request.application,'altas','alta_planes'),[]),
                        (T('costos de soporte'),False,URL(request.application,'altas','alta_costos_soportes'),[]),
                        (T('costos de instalacion'),False,URL(request.application,'altas','alta_costos_instalaciones'),[])],),
                     ],
                       )]

####Consultas (con parametros)#####
response.menu+=[(T('Consultas'),False,'#',
                     [(T('Clientes'),False,'#',
                       [(T('Por nombre/apellido'),False,URL(request.application,'consultas','clientes_nombre_apellido'),[]),
                        (T('Por dirección IP'),False,URL(request.application,'consultas','clientes_ip'),[]),
                        (T('Por nodo'),False,URL(request.application,'consultas','clientes_nodos'),[]),
                        (T('Por localidad'),False,URL(request.application,'consultas','clientes_localidad'),[]),],),
                     ],
                       )]


####Registros Completos####
response.menu += [
           (T('Registros Completos'), False, '#',
           [(T('Gerentes'), False, URL('consultas', 'listadoGerentes'),[]),
           (T('Administradores'), False, URL('consultas', 'listadoAdministradores'),[]),
           (T('Tecnicos'), False, URL('consultas', 'listadoTecnicos'),[]),
           (T('Localidades'), False, URL('consultas', 'listadoLocalidades'),[]),
           (T('Planes'), False, URL('consultas', 'listadoPlanes'),[]),
           (T('Costos de instalaciones'), False, URL('consultas', 'listadoCostos_instalaciones'),[]),
           (T('Costos de soportes tecnicos'), False, URL('consultas', 'listadoCostos_soportes'),[]),
           (T('Nodos'), False, URL('consultas', 'listadoNodos'),[]),
           (T('Paneles'), False, URL('consultas', 'listadoPaneles'),[]),
           (T('Mantenimientos'), False, URL('consultas', 'listadoMantenimientos'),[]),
           (T('Instalaciones'), False, URL('consultas', 'listadoInstalaciones'),[]),
           (T('Clientes'), False, URL('consultas', 'listadoClientes'),[]),
           (T('Soportes Tecnicos'), False,URL('consultas', 'listadoSoportes'),[]),
           (T('Historiales'), False, URL('consultas', 'listadoHistoriales'),[]),
           (T('Pagos'), False, URL('consultas', 'listadoPagos'),[]),
           (T('Abonos'), False, URL('consultas', 'listadoAbonos'),[])])]


response.menu += [
           (T('Instalaciones'), False, '#',
           [(T('Nueva Instalacion'), False, URL('altas', 'alta_instalacion'),[]),
           (T('Pendientes'), False, URL('consultas', 'listadoPendientes'),[])])]

response.menu += [
           (T('Soportes y clientes'), False, '#',
           [(T('Nuevo soporte | ver cliente'), False, URL('consultas', 'clientes_dni'),[]),
           (T('Soportes Pendientes'), False, URL('consultas', 'listadoSoportesPendientes'),[])])]

response.menu+=[(T('Agregar Pago'), False, URL('consultas', 'clientes_nro_tarjeta'), [])]
response.menu+=[(T('Clientes morosos'), False, URL('consultas', 'listadoMorosos'), [])]
