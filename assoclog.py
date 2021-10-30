from flask import Blueprint, render_template, request,flash, redirect, session
from app import User, db
import chat
from flask_login import login_user, current_user, logout_user
assoclog = Blueprint('assoclog', __name__, template_folder="templates", static_folder="static",url_prefix='/associate')



@assoclog.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form:
            musername = request.form['username']
            mpassword = request.form['password']
            user = User.query.filter_by(username=musername, isAssociate=True).first()
            print(user)
            if user is None:
                flash('username not registered')
                return redirect('login')
            elif user.password == mpassword:
                flash('login successful')
                # session["CUser"] = user.username
                login_user(user)
                # print(current_user,"hi")
                return redirect('chat')
            else:
                flash('Wrong password or username')
                return redirect('login')
    # flash("login unsuccessful")
    return render_template('assoclogin.html')

@assoclog.route('/register',  methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if request.form:
            musername = request.form['username']
            memail = request.form['email']
            mpassword = request.form['password']
            print((User.query.filter_by(username=musername)))
            if len(User.query.filter_by(username=musername).all()) >0:
                flash('username is already taken')
                return redirect('register')
            elif len(User.query.filter_by(email=memail).all())>0:
                flash('email already registered')
                return redirect('register')
            else:
                user = User(username=musername, email=memail, password=mpassword, isAssociate=True)
                db.session.add(user)
                db.session.commit()
        flash("registration successful")
        return redirect('login')
    return render_template('assocregister.html')

@assoclog.route('/')
def home():
    return render_template('assoclanding.html')

    
@assoclog.route('/logout', methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        logout_user()
    return render_template('assoclogin.html')