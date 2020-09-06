from flask import Flask

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config)

    from . import main
    app.register_blueprint(main.bp)
    return app