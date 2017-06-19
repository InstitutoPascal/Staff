# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from gerentes.py")

def inicio():
    d = 4
    return dict(datos=d)


def estadisticas():
    title="Gráfico Informativo"
    data=XML('[ ["item", "value"], ["Solicitud de instalaciones", 20], ["Cantidad de clientes", 30], ["Solicitud de soportes", 20],["Soportes                       realizados", 15],["Mantenimientos", 14]]') #convert list in string and string in XML
    return dict(title=title, data=data)
