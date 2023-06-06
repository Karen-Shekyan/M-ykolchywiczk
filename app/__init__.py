from flask import Flask, render_template, redirect, request, session
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/join")
def home():
    return render_template("join.html")

@socketio.on('roomRes')
def respond(room):
    print(room)
    join_room(room)
    emit('info', data)

@app.route("/room", methods=["POST", "GET"])
def roomed():
    return render_template("room.html")

@app.route("/game", methods=["POST", "GET"])
def game():
    return render_template("game.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)
