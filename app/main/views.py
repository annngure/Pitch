from flask import render_template,request,redirect,url_for
from . import main
from .. import db,photos
from flask_login import login_required
from ..models import Pitch, User , Comments
from .forms import PitchForm,CommentForm,UpdateProfile


@main.route('/')
def index():

    message = "Welcome to pitches!"
    title = 'Pitch! Pitch! Pitch!'
    return render_template('index.html',message=message,title=title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username  = uname).first()

    if user is None:
        abort(404)
    
    return render_template('profile/profile.html', user = user)