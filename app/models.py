from app import app, mongo, cache
from flask import escape

ctx = app.app_context()
ctx.push()

# TODO: Add in-memory cache support

class URLMap:
  collection = mongo.db.urls

  @staticmethod
  def insert(alias, url):
    """
      Try to insert a new alias to URL mapping in the db.
      If the alias already maps to a different URL, return False.
      Otherwise, insert the alias if necessary and return True.
    """
    record = URLMap.findURL(alias)
    if record and record != url: 
      return False
    if not record:
      cache.set(alias, url, timeout=app.config['CACHE_TIMEOUT'])
      URLMap.collection.insert_one({
        'alias': alias,
        'url' : url
      })
    return True

  @staticmethod
  def findURL(alias, setcache=False):
    """
      Return full URL associated with alias if it exists.
    """
    cached_url = cache.get(alias)
    if cached_url: 
      print('CACHE HIT!')
      return cached_url
    record = URLMap.collection.find_one({'alias': alias})
    if record:
      print('CACHE MISS!')
      url = record['url']
      if setcache and:
        cache.set(alias, url, timeout=app.config['CACHE_TIMEOUT'])
      return url

  @staticmethod
  def suggest(alias):
    pass

ctx.pop()