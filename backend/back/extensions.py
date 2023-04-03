from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt import JWT

db=SQLAlchemy()
migrate=Migrate()
cors=CORS()
jwt=JWT()