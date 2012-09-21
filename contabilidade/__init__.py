from pyramid.config import Configurator
from pyramid.events import subscriber, NewRequest

from gridfs import GridFS
from urlparse import urlparse
import pymongo
from contabilidade.models.root import Root

@subscriber(NewRequest)
def event_mongo_db(event):
    settings = event.request.registry.settings
    db_url = urlparse(settings['mongo_uri'])
    db = settings['db_conn'][db_url.path[1:]]
    if db_url.username and db_url.password:
        db.authenticate(db_url.username, db_url.password)
    event.request.db = db
    event.request.fs = GridFS(db)

def add_mongo_db(config):
    #for use mongodb:
    db_url = urlparse(config.registry.settings['mongo_uri'])
    conn = pymongo.Connection(host=db_url.hostname)
    config.registry.settings['db_conn'] = conn

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.include(add_mongo_db)
    config.scan()
    return config.make_wsgi_app()


