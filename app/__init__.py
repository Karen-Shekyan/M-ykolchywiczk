from flask import Flask, render_template, redirect, request, session, url_for
from flask_socketio import SocketIO, send, emit, join_room, leave_room, rooms
from images import *
from api import *
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, logger=True, max_http_buffer_size = 1e9)

userRooms = {}
justUsers = {}

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

    players = userRooms.get(rCode)
    if (players == None):
        userRooms.update({rCode:[uName]})
        justUsers[request.sid] = uName
    else:
        if (uName in userRooms[rCode]):
            emit("redirect", {"url": "join"})
        else:
            userRooms[rCode].append(uName)
            justUsers[request.sid] = uName

    print(userRooms)

    emit("approvedUser", (uName, rCode))
    emit("listy", userRooms[rCode], to = rCode)

@socketio.on("startGame")
def start(rCode):
    emit("redirect", {"url": "game"}, to = rCode)

@app.route("/game", methods=["POST", "GET"])
def game():
    return render_template("game.html")

@app.route("/game_timer", methods=["POST", "GET"])
def game_timer():
    return render_template("game_timer.html")

@socketio.on("getUser")
def getInfo(): 
    uName = session["username"]
    rCode = session["room"]
    emit("givenInfo", (uName, rCode))

@socketio.on("endGame")
def end(rCode):
    retPics = []
    retPrompts = []
    for img in os.walk(os.join("img", rCode, "pic")):
        retPics.append(img)
    for img in os.walk(os.join("img", rCode, "pic")):
        retPics.append(img)
        
#Socket method that plays when an image is submitted
#It will take the user, room, and raw image format.
#It will create a directory for the room if no directory exists
#It will insert the raw image as a png into the folder for this room, titled as the uesr.
#It will form an image path for that image.
#It will generate an AI prompt for the image.
#It will emit the user, room, path to .png, and prompt for image.
@socketio.on("submitImg")
def imgageIn(uName, rCode, arrayImage):
    print("\n\nHI")
    #print(arrayImage)

    new_dir(rCode)
    insert_img(rCode, arrayImage, uName)
    imgPath = os.path.join("img", rCode, "img", uName + ".png")
    #prompt = gen_prompt(imgPath)
    #emit("sendImage", (uName, rCode, imgPath, prompt))

    index = 0
    for i in range(len(userRooms[rCode])):
        if (userRooms[rCode][i] == uName):
            index = i + 1

    if (index == len(userRooms[rCode]):
        print ("Trigger End Room")
    else:
        prompt = "hi"
        with open(os.path.join("img", rCode, "prompt", uName + ".txt"), 'w') as p:
            p.write(prompt)
        emit("sendImage", (userRooms[rCode][index], rCode, imgPath, prompt))


@app.route("/end", methods=["POST", "GET"])
def end():
    return render_template("end.html")

@socketio.on("disconnect")
def dead():
    print(request.sid)
    print(userRooms)
    person = justUsers[request.sid]
    print(person)
    for room in userRooms:
        if (person in userRooms[room]):
            leave_room(room)
            userRooms[room].remove(person)
            emit("listy", userRooms[room], to = room)

if __name__ == '__main__':
    socketio.run(app)
