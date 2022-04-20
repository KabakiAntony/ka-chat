from config import DevelopmentConfig
from flask import Flask
from flask_login import LoginManager
from app.api.views.users import users as users_blueprint


login_manager = LoginManager()


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


def create_app():
    """
    initializing the app factory
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    app.register_blueprint(users_blueprint)
    login_manager.init_app(app)
    
    return app
