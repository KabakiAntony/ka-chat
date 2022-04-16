from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Message(db.Model):
    """Messages model"""

    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(255), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"))
    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_on = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, created_by, created_on):
        self.name = name
        self.created_by = created_by