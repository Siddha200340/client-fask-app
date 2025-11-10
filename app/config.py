import os

class Config:
    SECRET_KEY = os.environ.get('FLASK_APP_SECRET_KEY', 'defaultkey')
    PORT = int(os.environ.get('FLASK_APP_PORT', 5000))
    DEBUG = True
