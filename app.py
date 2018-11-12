from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os

import random
import settings
import sys
from database import db_session
import json
from werkzeug.utils import secure_filename
from config import Config
from datetime import datetime

app = Flask(__name__)

app.config['APP_SETTINGS'] = settings.APP_SETTINGS
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.TRACK_MODIFICATIONS
app.secret_key = settings.SECRET_KEY

os.environ["APP_SETTINGS"] = settings.APP_SETTINGS
os.environ["DATABASE_URL"] = settings.DB_URL

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import User

@app.route('/')
def home_page():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
