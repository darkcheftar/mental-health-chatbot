from app import socketio
from flask import request
from flask_login import current_user
import json

user = {}
userids = {}
associateids = {}

with open('chatreply.json') as res:
    data = json.load(res)


@socketio.on("connect")
def connect():
    print(request.sid)
    socketio.send(f"Hi {current_user.username}")
    socketio.send("Please Answer the following questions with the given options")
    socketio.emit("json", {"q": data[0]["1"], "qid":"1"}, room=request.sid)
    if current_user.isAssociate:
        global associateids
        associateids[current_user.username] = request.sid
    else:
        global userids
        userids[current_user.username] = request.sid
    global user
    user[current_user.username] = 0
    print(associateids,userids)
@socketio.on('json')
def jsa(json):
    print(json)
    socketio.emit("json", {"question": "wait what?"}, room=request.sid)

@socketio.on('next_event')
def botreply(d):
    print(d)
    id = d['id']
    score = {
            'Not At All': 0,
            'Several days': 1,
            'More than half of the days': 2,
            'Everyday': 3
        }
    if d['score'] in [ "Thanks and Logout", "No Thanks and logout"]:
        socketio.emit("redirect", "logout")
    elif d['score'] == "Yes, Please":
        socketio.emit("associate", "associateid")
    else:
        user[current_user.username]+=score[d['score']]

    if id in data[0]:
        socketio.emit("json", {"q": data[0][id], "qid":id}, room=request.sid)
    else:
        cScore = user[current_user.username] 
        if cScore <= 9:
            msg = "According to your replies I recommend you some Articlas which will help you feel better. which will be sent to your registered email!"
            opts = ["Thanks and Logout"]
        elif 9 < cScore <= 18:
            msg = "According to your replies I recommend you some Articlas which will help you feel better. I feel you need some human assesstance please give you consent to let you connect with our Associate"
            opts = ["Yes, Please", "No Thanks and logout"]
        else:
            msg = "According to your replies I strongly recommend you to meet out Human associate which may help you feel better. please give you consent to let you connect with our Associate"
            opts = ["Yes, Please", "No Thanks and logout"]
        socketio.emit("assessment_complete", {"msg":msg, "opts":opts} )

@socketio.on('info')
def info(e):
    pass