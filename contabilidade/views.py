from pyramid.view import view_config
from contabilidade.models.root import *

@view_config(context=Root, renderer='index.mako')
def index(context, request):
    return {'index': context}

@view_config(context=Periodo, renderer='periodo.mako')
def periodo(context, request):
    return {'periodo': context}

@view_config(context=Contabilidade, renderer='contabilidade.mako')
def contab(context, request):
    return {'contab': context}

