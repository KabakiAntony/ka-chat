from app.api.models import db
from datetime import datetime


class Message(db.Model):
    """Messages model"""

    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(255), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"))
    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_on = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, message, room_id, sender_id):
        self.message = message
        self.room_id = room_id
        self.sender_id = sender_id
