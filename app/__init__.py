from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from config import DevelopmentConfig
from app.api.models.users import User
from app.api.views.users import users as users_blueprint


login_manager = LoginManager()
migrate = Migrate(compare_type=True)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


def create_app():
    """
    initializing the app factory
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())

    from app.api.models import db

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(users_blueprint)
    login_manager.init_app(app)
    app.app_context().push()

    return app
