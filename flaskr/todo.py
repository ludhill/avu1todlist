from flask import Blueprint, request, redirect, url_for, render_template
from flaskr.db import get_db

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        db = get_db()
        db.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        db.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/create.html')

@bp.route('/')
def index():
    db = get_db()
    tasks = db.execute("SELECT * FROM tasks").fetchall()
    return render_template('todo/index.html', tasks=tasks)
