from app import create_app
from flask_socketio import SocketIO

app = create_app()
socketio = SocketIO(app)


@app.route('/')
def root():
    """
    this is the root of our app
    """
    return "hello there"


if __name__ == "__main__":
    socketio.run(app)
