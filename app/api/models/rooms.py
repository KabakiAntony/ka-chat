from app.api.models import db
from datetime import datetime


class Room(db.Model):
    """rooms model"""

    __tablename__ = "rooms"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_on = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, created_by):
        self.name = name
        self.created_by = created_by
