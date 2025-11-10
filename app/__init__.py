from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('FLASK_APP_SECRET_KEY', 'defaultkey')

    from .routes import main
    app.register_blueprint(main)

    return app
