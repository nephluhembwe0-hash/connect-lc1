from flask import Blueprint, render_template
from flask_login import current_user
from .forms import PostForm
from .models import Post, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        post = Post(
            content=form.content.data,
            gdrive_link=form.gdrive_link.data,
            author=current_user
        )
        db.session.add(post)
        db.session.commit()
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', form=form, posts=posts)