"""Initiation of our app"""
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)

from app import views, models
