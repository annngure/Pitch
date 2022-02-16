from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash



class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    posts= db.relationship('posts',backref='users',lazy='dynamic') 
    comments = db.relationship('comment',backref='users',lazy='dynamic')
    up_vote = db.relationship('Upvote', backref='users', lazy='dynamic')
    down_vote = db.relationship('Downvote', backref='users', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self, password):
        self.password_secure =  generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_secure, password)

    def __repr__(self):
        return f'User: {self.username}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Post(db.Model):
    __tablename__= 'posts'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    posts= db.relationship('posts',backref='posts',lazy='dynamic') 
    category= db.Column(db.String())
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255)) 
    comments = db.relationship('comment',backref='posts',lazy='dynamic')
    up_vote = db.relationship('Upvote', backref='posts', lazy='dynamic')
    down_vote = db.relationship('Downvote', backref='posts', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Post title: {self.title}'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),index = True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    comments = db.Column(db.Text())

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, post_id):
        comments = Comment.query.filter_by(posts_id=posts_id).all()
        return comments

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comments: {self.comment}'

 
class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, default=1)
    username = db.Column(db.String(255),index = True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    comments = db.Column(db.String())


    def save(self):
        db.session.add(self)
        db.session.commit()

    def upvote(cls, id):
        upvote_post = Upvote(user=current_user, posts_id=id)
        upvote_post.save()

    @classmethod
    def query_upvotes(cls, id):
        upvote = Upvote.query.filter_by(posts_id=id).all()
        return upvote

    def __repr__(self):
        return f'{self.post_id}'

class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer, primary_key=True)
    downvote = db.Column(db.Integer, default=1)
    username = db.Column(db.String(255),index = True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    comments = db.Column(db.String())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def downvote(cls, id):
        downvote_post = Downvote(user=current_user, posts_id=id)
        downvote_post.save()
  
    @classmethod
    def query_downvotes(cls, id):
        downvote = Downvote.query.filter_by(posts_id=id).all()
        return downvote

    def __repr__(self):
        return f'{self.post_id}'

