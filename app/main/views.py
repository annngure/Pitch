from flask import render_template,request,redirect,url_for
from . import main
# from .. import db,photos
from flask_login import login_required,current_user
from ..models import User , Comment, Post,Upvote, Downvote
from .forms import PostForm,CommentForm,UpdateProfile


@main.route('/')
def index():
    post= Post.query.all()
    religion= Post.query.filter_by(category='religion').all()
    science= Post.query.filter_by(category='science').all()
    entertainment= Post.query.filter_by(category='entertainment').all()
    message = "Welcome to pitches!"
    title = 'Pitch! Pitch! Pitch!'
    return render_template('index.html',message=message,title=title,religion=religion,science=science,entertainment=entertainment,posts=posts)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username  = uname).first()
    

    if user is None:
        abort(404)
    form = UpdateProfie()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
      
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/profile.html', form=form)

@main.route('/posts')
@login_required
def posts():
    posts= Post.query.all()
    likes= Upvote.query.all()
    user= current_user
    return render_template('dispaly.html',posts=posts, likes=likes, user=user)


@main.route('/new_post', methods=['GET','POST'])
@login_required
def new_post():
    '''
    View root page fuction tat returns the index page and its data
    '''
    form= PitchForm()

    if form.validate_on_submit():
        title=form.title.data
        post= form.post.data
        category=form.category.data
        new_post=Post(post=post,title=title,category=category,user=current_user)
        new_post.save_post()
        return redirect (url_for('main.index'))

    return render_template('pitch,html',form=form)





