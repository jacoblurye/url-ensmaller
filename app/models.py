from app import app, mongo
from flask import escape

ctx = app.app_context()
ctx.push()

class URLMap:
  collection = mongo.db.urls

  @staticmethod
  def insert(key, url):
    record = URLMap.find(key)
    if record and record['long'] != url: 
      return 0
    if not record:
      URLMap.collection.insert_one({
        'short': key,
        'long' : url
      })
    return 1

  @staticmethod
  def find(key):
    record = URLMap.collection.find_one({'short': key})
    if record:
      return record['long']

ctx.pop()