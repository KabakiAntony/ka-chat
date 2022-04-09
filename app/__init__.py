from config import DevelopmentConfig
from flask import Flask


def create_app():
    """
    initializing the app factory
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    
    return app
