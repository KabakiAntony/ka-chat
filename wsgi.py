from app import create_app
from flask_socketio import SocketIO, send, join_room, leave_room
from time import localtime, strftime


app = create_app()
socketio = SocketIO(app)


@socketio.on('message')
def message(data):
    send({'msg': data['msg'], 'username': data['username'], 'time_stamp':
        strftime('%b-%d %I:%M%p', localtime())}, room=data['room'])


@socketio.on('join')
def join(data):
    join_room(data['room'])
    send({'msg': data['username'] + "  has joined the " + data['room'] + "  room"}, 
        room=data['room'])


@socketio.on('leave')
def leave(data):
    leave_room(data['room'])
    send({'msg': data['username'] + "  has left the " + data['room'] + "  room"}, 
        room=data['room'])


if __name__ == "__main__":
    socketio.run(app)
