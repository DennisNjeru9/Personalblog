from flask import render_template,redirect,url_for,flash,request,abort
from . import main
from ..models import User
from .forms import PostForm,CommentForm,UpdatePostForm,UpdateProfile
from flask_login import login_required,current_user
from ..import db
from ..requests import get_quote
from ..email import mail_message,notification_message
