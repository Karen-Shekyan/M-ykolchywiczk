from flask import Flask, render_template, redirect, request, session
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/create", methods=["POST", "GET"])
def creation():
    return render_template("create.html")

@app.route("/join", methods=["POST", "GET"])
def joining():
    return render_template("join.html")

@app.route("/room", methods=["POST", "GET"])
def roomed():
    uName = request.form["username"]
    rNum = request.form["roomnumber"]
    print(uName)
    print(rNum)
    return render_template("room.html")



@socketio.on('roomRes')
def respond(room):
    print(request.sid)
    print(room)
    join_room(room)
    emit('info', room)

if __name__ == '__main__':
    socketio.run(app)
