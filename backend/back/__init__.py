from flask import Flask
from back.config import Config
from back.extensions import db, migrate, cors
from back.api import api
from back.commands import init_db, populate_db

COMMANDS=[init_db, populate_db]


def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_commands(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    api.init_app(app)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)