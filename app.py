from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import random
import sys
from database import db_session
import json
from werkzeug.utils import secure_filename
from config import Config
from datetime import datetime

app = Flask(__name__)

try:
    if os.environ['FLASK_ENV'] == "development":
        import settings
        app.config['APP_SETTINGS'] = settings.APP_SETTINGS
        app.secret_key = settings.SECRET_KEY
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
        app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL
except:
    app.config['APP_SETTINGS'] = os.environ['APP_SETTINGS']
    app.secret_key = os.environ['SECRET_KEY']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import Participant

@app.route('/', methods=["GET", "POST"])
def html_page():
    return "Hello World"

if __name__ == '__main__':
    app.run()
