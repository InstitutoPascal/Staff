# -*- coding: utf-8 -*-

def sin_autorizacion():
    auth.settings.logout_next =  URL('default','index')
    return dict()

def index():
    return dict(message=T('Welcome to web2py!'))

def user():
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
