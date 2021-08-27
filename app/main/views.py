from flask import render_template,redirect,url_for,flash,request,abort
from . import main
from ..models import User,Comment,Post,PostLike,Subscribers
from .forms import PostForm,CommentForm,UpdatePostForm,UpdateProfile
from flask_login import login_required,current_user
from ..import db
from ..requests import get_quote
from ..email import mail_message,notification_message
from datetime import datetime

@main.route('/', methods = ['GET', 'POST'])
def index():
    posts = Post.get_all_posts()
    quote = get_quote()

    if request.method == 'POST':
        new_sub = Subscribers(email = request.form.get("subscriber"))
        db.session.add(new_sub)
        db.session.commit()
        mail_message('Thank you for subscribing to the_Phi Construction Blog', 'email/welcome', new_sub.email)
    return render_template('index.html',posts = posts, quote = quote)

@main.route('/post/<int:id>', methods = ['POST', 'GET'])
def post(id):
    post = Post.query.filter_by(id = id).first()
    comments = Comment.query.filter_by(post_id = id).all()
    comment_form = CommentForm()
    comment_count = len(comments)

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        comment_form.comment.data = ""
        comment_alias = comment_form.alias.data
        comment_form.alias.data = ""
        if current_user.is_authenticated:
            comment_alias = current_user.username
        new_comment = Comment(comment = comment, comment_at = datetime.now(), comment_by = comment_alias, post_id = id)
        new_comment.save_comment()
        return redirect(url_for('main.post', id = post.id))

    return render_template('post.html', post = post, comments = comments, comment_form = comment_form,comment_count = comment_count)

