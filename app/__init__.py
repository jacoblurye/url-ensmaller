from flask import Flask
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from werkzeug.contrib.cache import SimpleCache
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)
bootstrap = Bootstrap(app)
cache = SimpleCache()

from app import routes