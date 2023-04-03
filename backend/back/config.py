from os import path, environ
from datetime import timedelta

class Config(object):
    # SECRET_KEY=environ.get('SECRET_KEY')
    SECRET_KEY='ajsdhkajsdhkasd'
    BASE_DIR=path.abspath(path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    PROPAGATE_EXCEPTIONS=True
    SQLALCHEMY_DATABASE_URI='sqlite:///'+path.join(BASE_DIR, 'db.sqlite')