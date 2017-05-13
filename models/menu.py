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


"""
### INICIO MENU ADMINISTRADORES ####
response.menu += [
           (T('Realizar altas'), False, '#',
           [(T('Planes'), False, URL('altas', 'alta_planes'),[]),
           (T('Costos de instalaciones'), False, URL('altas', 'alta_costos_instalaciones'),[]),
           (T('Costos de soportes'), False, URL('altas', 'alta_costos_soportes'),[]),
           (T('Nodos'), False, URL('altas', 'alta_nodos'),[]),
           (T('Paneles'), False, URL('altas', 'alta_paneles'),[]),
           (T('Mantenimientos'), False, URL('altas', 'alta_mantenimiento'),[]),])]


response.menu += [
           (T('Registros Completos'), False, '#',
           [(T('Planes'), False, URL('consultas', 'listadoPlanes'),[]),
           (T('Costos de instalaciones'), False, URL('consultas', 'listadoCostos_instalaciones'),[]),
           (T('Costos de soportes'), False, URL('consultas', 'listadoCostos_soportes'),[]),
           (T('Nodos'), False, URL('consultas', 'listadoNodos'),[]),
           (T('Paneles'), False, URL('consultas', 'listadoPaneles'),[]),
           (T('Mantenimientos'), False, URL('consultas', 'listadoMantenimientos'),[])])]


response.menu += [
           (T('Instalaciones'), False, '#',
           [(T('Registrar nueva Instalacion'), False, URL('altas', 'alta_instalacion'),[]),
           (T('Agregar cliente'), False, URL('consultas', 'agregar_cliente'),[]),
           (T('Listado completo'), False, URL('consultas', 'listadoInstalaciones'),[])])]

response.menu += [
           (T('Soportes tecnicos'), False, '#',
           [(T('Registrar nuevo soporte'), False, URL('consultas', 'soportes_dni'),[]),
           (T('Listado completo'), False, URL('consultas', 'listadoSoportes'),[]),
           (T('Historial'), False, URL('consultas', 'ListadoHistorial'),[])])]

response.menu += [
           (T('Gestion de pago'), False, '#',
           [(T('Registrar nuevo pago'), False, URL('consultas', 'registrarPago'),[]),
           (T('Registrar descuento'), False, URL('consultas', 'registrarDescuento'),[]),
           (T('Registrar recargo'), False, URL('consultas', 'registrarRecargo'),[]),
           (T('Cuenta corriente'), False, URL('consultas', 'cuentaCorriente'),[])])]

response.menu+=[(T('consultas'),False,'#',
                     [(T('Clientes'),False,'#',
                       [(T('Por DNI'),False,URL(request.application,'consultas','clientes_dni'),[]),
                        (T('Por nombre/apellido'),False,URL(request.application,'consultas','clientes_nombre_apellido'),[]),
                        (T('Por direccion IP'),False,URL(request.application,'consultas','clientes_ip'),[]),
                        (T('Listado completo'),False,URL(request.application,'consultas','listadoClientes'),[])],),
                       (T('Tecnicos'),False,'#',
                       [(T('Por DNI'),False,URL(request.application,'consultas','tecnicos_dni'),[]),
                        (T('Por nombre/apellido'),False,URL(request.application,'consultas','tecnicos_nombre_apellido'),[]),
                       (T('Listado completo'), False, URL(request.application, 'consultas', 'listadoTecnicos'),[])],),],)]

response.menu += [
           (T('Herramientas'), False, '#',
           [(T('Geolocalizacion de nodos'), False, URL('consultas', 'geolocalizacionNodos'),[]),
           (T('Geolocalizacion de clientes'), False, URL('consultas', 'registrarRecargo'),[])])]

### FIN MENU ADMINISTRADORES ###
"""



### MENU TECNICOS ###

response.menu = [(T('Inicio'), False, URL('clientes', 'inicio'), [])]
response.menu += [(T('Instalaciones'), False, '#',
           [(T('Dia actual'), False, URL('consultas', 'registrarPago'),[]),
           (T('Todas'), False, URL('consultas', 'registrarRecargo'),[])])]
response.menu += [(T('soportes tecnicos'), False, '#',
           [(T('Dia actual'), False, URL('consultas', 'registrarPago'),[]),
           (T('Todas'), False, URL('consultas', 'registrarRecargo'),[])])]
response.menu += [(T('Mantenimientos'), False, '#',
           [(T('Realizar informe'), False, URL('consultas', 'registrarPago'),[]),
           (T('Realizados'), False, URL('consultas', 'registrarRecargo'),[])])]


### FIN MENU TECNICOS ###





"""
### MENU CLIENTES ###
response.menu = [(T('Inicio'), False, URL('clientes', 'inicio'), [])]
response.menu += [(T('Planes'), False, URL('clientes', 'listadoPlanes'), [])]
response.menu += [(T('Atencion al cliente'), False, '#',
           [(T('Soporte tecnico'), False, URL('consultas', 'registrarPago'),[]),
           (T('Consultas'), False, URL('consultas', 'registrarDescuento'),[]),
           (T('Ayuda'), False, URL('consultas', 'registrarDescuento'),[]),
           (T('Contacto'), False, URL('consultas', 'registrarRecargo'),[])])]
### FIN MENU CLIENTES ###
"""
