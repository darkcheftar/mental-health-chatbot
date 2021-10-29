from flask import Flask, url_for, request,render_template, redirect
from flask_login import UserMixin, LoginManager, login_required, login_user,logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, send
import secrets
import os

app = Flask(__name__)
app.config["SECRET"] = secrets.token_urlsafe(16)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///chatbot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key="True")
    username = db.Column(db.String(30), unique=True)
    email=db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    isAssociate = db.Column(db.Boolean, default=False, nullable=False)
    
login_manager = LoginManager(app)
login_manager.login_view = "log.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if not os.path.isfile("./chatbot.db"):
    db.create_all()
    db.session.add(User(password="weareinthistogether",username="darkcheftar", email="darkcheftar.connect@gamil.com"))
    db.session.commit()


socketio = SocketIO(app)