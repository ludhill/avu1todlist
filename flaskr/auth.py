from flask import flash
from flask import Blueprint, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Usuário é obrigatório.'
        elif not password:
            error = 'Senha é obrigatória.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password))
                )
                db.commit()
            except db.IntegrityError:
                error = f"Usuário {username} já existe."

            return redirect(url_for("auth.login"))

        flash(error)
    return render_template('auth/register.html')
