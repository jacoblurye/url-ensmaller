import random
import string
from app import app, mongo, cache
from flask import escape

ctx = app.app_context()
ctx.push()

ascii_chars = string.ascii_lowercase + string.ascii_uppercase

class URLMap:
  collection = mongo.db.urls

  @staticmethod
  def insert(url):
    """
      Try to insert a URL into the db if it isn't already present,
      returning the randomly generated alias.
    """
    # Try to get existing alias
    alias = URLMap.find_alias(url)
    if alias:
      return alias

    # Generate new alias
    alias = URLMap.__random_alias()
    cache.set(alias, url, timeout=app.config['CACHE_TIMEOUT'])
    URLMap.collection.insert_one({
      'alias': alias,
      'url' : url
    })
    return alias

  @staticmethod
  def find_url(alias, setcache=True):
    """
      Return full URL associated with alias if it exists.
    """
    cached_url = cache.get(alias)
    if cached_url: 
      return cached_url

    record = URLMap.collection.find_one({'alias': alias})
    if record:
      url = record['url']
      if setcache:
        cache.set(alias, url, timeout=app.config['CACHE_TIMEOUT'])
      return url

  @staticmethod
  def find_alias(url):
    """
      Return alias associated with URL if it exists.
    """
    # TODO: caching?
    record = URLMap.collection.find_one({'url': url})
    if record:
      alias = record['alias']
      return alias

  @staticmethod
  def __random_alias(length=6):
    alias = ''.join(random.choice(ascii_chars) for _ in range(length))
    if not URLMap.find_alias(alias):
      return alias
    return URLMap.__random_alias()
    

ctx.pop()