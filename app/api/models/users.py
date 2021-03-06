from app.api.models import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """user model"""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(255), index=True, unique=True, nullable=False)
    account_confirmed = db.Column(
        db.String(25), default="False", nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash
