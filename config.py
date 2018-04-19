import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hehe-no-luck'
    MONGO_URI = os.environ.get('MONGO_URI')
    CACHE_TIMEOUT = 60 * 60 * 24
