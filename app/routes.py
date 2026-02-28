from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from .forms import PostForm
from .models import Post, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        if current_user.mode == 'offline':
            flash("Mode offline : vous ne pouvez pas publier de message.", "warning")
        else:
            post = Post(
                content=form.content.data,
                gdrive_link=form.gdrive_link.data,
                author=current_user
            )
            db.session.add(post)
            db.session.commit()
            flash("Message publié !", "success")
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', form=form, posts=posts)

@main_bp.route('/toggle_mode', methods=['POST'])
@login_required
def toggle_mode():
    if current_user.mode == 'online':
        current_user.mode = 'offline'
        flash("Vous êtes maintenant en mode offline (lecture seule).", "info")
    else:
        current_user.mode = 'online'
        flash("Vous êtes maintenant en mode online (publication autorisée).", "success")
    db.session.commit()
    return redirect(url_for('main.index'))