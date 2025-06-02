import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Registrar o banco de dados
    from . import db
    db.init_app(app)

    # Registrar os Blueprints
    from . import auth, todo
    app.register_blueprint(auth.bp, url_prefix="/auth")
    app.register_blueprint(todo.bp, url_prefix="/todo")

    @app.route('/hello')
    def hello():
        return 'Olá, Seus Galado!'

    @app.route('/')
    def index():
        return 'Bem-vindo à To-Do List!'

    return app

    #app.register_blueprint(admin_bp, url_prefix="/admin")