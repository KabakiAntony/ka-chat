from config import DevelopmentConfig
from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
    """
    initializing the app factory
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    login_manager.init_app(app)
    
    return app
