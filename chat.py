from flask import Blueprint, render_template, request,flash, redirect,session
from flask_login import login_required

chat = Blueprint('chat', __name__, template_folder="templates", static_folder="static")

@chat.route('/chatbot')
@login_required
def chatbot():
    return render_template('chatbot.html')

@chat.route('/chat')
@login_required
def chatNormal():
    return render_template('chat.html')