from app import create_app
from flask_socketio import SocketIO, send
from flask import render_template

app = create_app() 
socketio = SocketIO(app)


# @app.route('/')
# def home_page():
#     return render_template('index.html')


# @socketio.on('message')
# def handleMessage(msg):
#     send(msg, broadcast=True)


# @socketio.on('disconnect')
# def handleDisconnect():
#     send("Someone has left", broadcast=True)


if __name__ == "__main__":
    socketio.run(app)
