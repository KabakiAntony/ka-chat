from flask import Blueprint

users = Blueprint("users", __name__, url_prefix="")
rooms = Blueprint("rooms", __name__, url_prefix="")
messages = Blueprint("messages", __name__, url_prefix="")
