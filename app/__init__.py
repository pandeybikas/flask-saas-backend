from .extensions import db,migrate,jwt, cors, bycrpt
from flask import Flask
from .config import Config
from api.auth.routes import auth_bp
from api.tasks.routes import task_bp
from api.users.routes import user_bp
import os

def create_app():
    app=  Flask(__name__)

    #select environment
    env= os.getenv("FLASK_ENV")
    app.config.from_object(Config)

    #initialize extensions
    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)
    cors.init_app(app)
    bycrpt.init_app(app)

    #register blueprint
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(user_bp, url_prefix='/api/v1/user')
    app.register_blueprint(task_bp, url_prefix='/api/v1/tasks')
    return app

