from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required # <---

from database.engine import db
from database.models.todo import Task

task_bp = Blueprint('tasks', __name__, template_folder='templates')


@task_bp.route('/')
@login_required
def get_all_tasks():
    tasks = Task.query.all() # <---
    return render_template('all_tasks.html', tasks_db=tasks)


@task_bp.route('/read/<int:id>')
@login_required
def task_detail(id):
    task_one = Task.query.filter_by(id=id).first() # <---
    return render_template('detail.html', task_one=task_one)


@task_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks.get_all_tasks'))
    return render_template('add_task.html')


@task_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_task(id):
    task_one = Task.query.filter_by(id=id).first() # <---
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        if title: # <---
            task_one.title = title  # <---
        if description: # <---
            task_one.description = description # <---
        db.session.commit() # <---

    return render_template('update.html', task_one=task_one)


@task_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_task(id): # <---
    task = Task.query.filter_by(id=id).first()  # <---
    db.session.delete(task)  # <---
    db.session.commit()  # <---
    return redirect(url_for('tasks.get_all_tasks'))



