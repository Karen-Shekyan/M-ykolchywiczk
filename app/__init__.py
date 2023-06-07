from flask import Flask, render_template, redirect, request, session
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def landing():
    return render_template("landing.html")

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
    return render_template("room.html", username=uName, roomnumber = rNum)
@socketio.on("userInfo")
def userProcess(uName, rCode):
    print(uName)
    print('"' + rCode + '"')
    if (len(rCode) <= 5):
        rCode = request.sid
    print(request.sid)
    join_room(rCode)
    emit("approvedUser", (uName, rCode))

@app.route("/end", methods=["POST", "GET"])
def end():
    return render_template("end.html")

if __name__ == '__main__':
    socketio.run(app)
