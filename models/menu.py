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

response.menu = [(T('Home'), False, URL('administradores', 'inicio'), [])]  #Boton Home (vuelve a index)

DEVELOPMENT_MENU = True

if "auth" in locals():
    auth.wikimenu()



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
           [(T('Planes'), False, URL('administradores', 'listadoPlanes'),[]),
           (T('Costos de instalaciones'), False, URL('administradores', 'listadoCostos_instalaciones'),[]),
           (T('Costos de soportes'), False, URL('administradores', 'listadoCostos_soportes'),[]),
           (T('Nodos'), False, URL('administradores', 'listadoNodos'),[]),
           (T('Paneles'), False, URL('administradores', 'listadoPaneles'),[]),
           (T('Mantenimientos'), False, URL('administradores', 'listadoMantenimientos'),[])])]


response.menu += [
           (T('Instalaciones'), False, '#',
           [(T('Solicitar nueva Instalacion'), False, URL('altas', 'alta_instalacion'),[]),
           (T('Agregar cliente'), False, URL('administradores', 'instalaciones_dni'),[]),
           (T('Listado completo'), False, URL('administradores', 'listadoInstalaciones'),[])])]

response.menu += [
           (T('Soportes tecnicos'), False, '#',
           [(T('Solicitar nuevo soporte'), False, URL('administradores', 'solicitarSoporte'),[]),
           (T('Archivar soporte'), False, URL('administradores', 'archivarSoporte'),[]),
           (T('Listado completo'), False, URL('administradores', 'listadoSoportes'),[]),
           (T('Historial'), False, URL('administradores', 'ListadoHistorial'),[])])]

response.menu += [(T('Gestion de pago'), False, URL('administradores', 'gestionPago'), [])]
"""
response.menu += [
           (T('Gestion de pago'), False, '#',
           [(T('Registrar nuevo pago'), False, URL('administradores', 'clientes_nro_tarjeta'),[]),
           (T('Registrar descuento'), False, URL('administradores', 'registrarDescuento'),[]),
           (T('Registrar recargo'), False, URL('administradores', 'registrarRecargo'),[]),
           (T('Cuenta corriente'), False, URL('administradores', 'cuentaCorriente'),[])])]
"""
response.menu+=[(T('consultas'),False,'#',
                     [(T('Clientes'),False,'#',
                       [(T('Por DNI'),False,URL(request.application,'administradores','clientes_dni'),[]),
                        (T('Por nombre/apellido'),False,URL(request.application,'administradores','clientes_nombre_apellido'),[]),
                        (T('Por direccion IP'),False,URL(request.application,'administradores','clientes_ip'),[]),
                        (T('Listado completo'),False,URL(request.application,'administradores','listadoClientes'),[])],),
                       (T('Tecnicos'),False,'#',
                       [(T('Por DNI'),False,URL(request.application,'administradores','tecnicos_dni'),[]),
                        (T('Por nombre/apellido'),False,URL(request.application,'administradores','tecnicos_nombre_apellido'),[]),
                       (T('Listado completo'), False, URL(request.application, 'administradores', 'listadoTecnicos'),[])],),],)]

response.menu += [
           (T('Herramientas'), False, '#',
           [(T('Geolocalizacion de nodos'), False, URL('administradores', 'geolocalizacionNodos'),[]),
           (T('Geolocalizacion de clientes'), False, URL('administradores', 'geolocalizacionClientes'),[])])]

### FIN MENU ADMINISTRADORES ###



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
