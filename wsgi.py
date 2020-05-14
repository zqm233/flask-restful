from app.api import app_init
import os
from flask import Flask
from config import config


app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_CONFIG') or 'default'])
app_init(app)

if __name__ == '__main__':
    app.run()
