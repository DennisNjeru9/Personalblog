from . import db
from werkzeug.security import (generate_password_hash,check_password_hash)
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    # email = db.Column(db.String(120))
    # image_file = db.Column(db.String(20), default='default.jpg')
    # password = db.Column(db.String(60))
    # posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref ='role', lazy="dynamic")
#     date_posted = db.Column(db.DateTime, default=datetime.utcnow)
#     content = db.Column(db.Text)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'User {self.name}'
