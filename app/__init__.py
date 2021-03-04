# flaskproject1/app/__init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = '.'
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024
from app import routes