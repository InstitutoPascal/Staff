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

### INICIO MENU ADMINISTRADORES ####
response.menu += [
           (T('Realizar altas'), False, '#',
           [(T('Nodos'), False, URL('altas', 'alta_nodos'),[]),
           (T('Paneles'), False, URL('altas', 'alta_paneles'),[]),
           (T('Mantenimientos'), False, URL('altas', 'alta_mantenimiento'),[]),
           (T('Costos de soporte'), False, URL('altas', 'alta_costos_soportes'),[]),
           (T('Costos de instalacion'), False, URL('altas', 'alta_costos_instalaciones'),[]),])]

response.menu+=[(T('consultas'),False,'#',
                     [(T('Clientes'),False,'#',
                       [(T('Por DNI'),False,URL(request.application,'consultas','clientes_dni'),[]),
                        (T('Por nombre/apellido'),False,URL(request.application,'consultas','clientes_nombre_apellido'),[]),
                        (T('Por direccion IP'),False,URL(request.application,'consultas','clientes_ip'),[]),
                        (T('Por nodo'),False,URL(request.application,'consultas','clientes_nodos'),[]),
                        (T('Por localidad'),False,URL(request.application,'consultas','clientes_localidad'),[]),
                        (T('Todos'),False,URL(request.application,'consultas','listadoClientes'),[])],),
                       (T('Tecnicos'),False,'#',
                       [(T('Por DNI'),False,URL(request.application,'consultas','tecnicos_dni'),[]),
                       (T('todos'), False, URL(request.application, 'consultas', 'listadoTecnicos'),[])],),],)]

response.menu += [
           (T('Registros Completos'), False, '#',
           [(T('Localidades'), False, URL('consultas', 'listadoLocalidades'),[]),
           (T('Planes'), False, URL('consultas', 'listadoPlanes'),[]),
           (T('Costos de instalaciones'), False, URL('consultas', 'listadoCostos_instalaciones'),[]),
           (T('Costos de soportes'), False, URL('consultas', 'listadoCostos_soportes'),[]),
           (T('Nodos'), False, URL('consultas', 'listadoNodos'),[]),
           (T('Paneles'), False, URL('consultas', 'listadoPaneles'),[]),
           (T('Mantenimientos'), False, URL('consultas', 'listadoMantenimientos'),[])])]

response.menu += [
           (T('Instalaciones'), False, '#',
           [(T('Pendientes'), False, URL('consultas', 'instalacionesPendientes'),[]),
           (T('Finalizadas'), False, URL('consultas', 'instalacionesFinalizadas'),[]),
           (T('Todas'), False, URL('consultas', 'listadoInstalaciones'),[])])]

response.menu += [
           (T('Soportes tecnicos'), False, '#',
           [(T('Pendientes'), False, URL('consultas', 'soportesPendientes'),[]),
           (T('Finalizados'), False, URL('consultas', 'soportesFinalizados'),[]),
           (T('Todos'), False, URL('consultas', 'listadoSoportes'),[]),
           (T('Historial'), False, URL('consultas', 'ListadoHistorial'),[])])]

response.menu += [
           (T('Gestion de pago'), False, '#',
           [(T('Registrar nuevo pago'), False, URL('consultas', 'RegistrarPago'),[]),
           (T('Registrar descuento'), False, URL('consultas', 'RegistrarDescuento'),[]),
           (T('Registrar recargo'), False, URL('consultas', 'ListadoPagos'),[])])]

### FIN MENU ADMINISTRADORES ###
