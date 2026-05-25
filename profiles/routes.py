from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from database.engine import db

profile_bp = Blueprint('profile', __name__, template_folder='templates')


@profile_bp.route('/') # /profile
@login_required
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html', current_user=current_user)
    return None


@profile_bp.route('/change-username', methods=['GET', 'POST'])
def change_username():
    if request.method == 'POST':
        new_username = request.form.get('new-username')
        if new_username and len(new_username) >= 3:
            current_user.username = new_username
            db.session.commit()
            return redirect(url_for('profile.profile'))

    return render_template('change_username.html')










