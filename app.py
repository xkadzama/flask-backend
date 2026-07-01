import os

from flask import Flask, render_template
from flask_login import LoginManager, current_user

from todo.routes import task_bp
from auth.routes import auth_bp
from profiles.routes import profile_bp # <---
from database.engine import db
from database.models.todo import Task
from database.models.auth import User


app = Flask(__name__)
login_manager = LoginManager()


POSTGRES_USER = os.getenv('POSTGRES_USER', 'admin')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '123')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'database')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '773uwgfhadgfhegf'


db.init_app(app)
login_manager.init_app(app)

# with app.app_context():
#     db.create_all()


app.register_blueprint(task_bp, url_prefix='/tasks')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(profile_bp, url_prefix='/profile') # <---


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()


@app.route('/')
def main():
    return render_template('index.html', current_user=current_user)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)