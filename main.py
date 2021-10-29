from app import socketio, app
from flask import render_template
import events
from log import log
from assoclog import assoclog
from chat import chat

app.register_blueprint(log)
app.register_blueprint(assoclog)
app.register_blueprint(chat)

@app.route('/')
def home():
    return render_template('landing.html')

if __name__ == "__main__":
    socketio.run(app)