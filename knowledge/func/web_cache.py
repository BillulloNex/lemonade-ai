import sqlite3
from peewee import *

class SearchResult(Model):
    url = TextField()
    content = TextField()

    class Meta:
        database = SqliteDatabase('../../data/web_cache.db')

class WebCache:
    def __init__(self):
        self.db = SqliteDatabase('../../data/web_cache.db')
        self.db.connect()
        self.db.create_tables([SearchResult])

    def save_to_cache(self, url: str, content: str) -> None:
        result = SearchResult(url=url, content=content)
        result.save()
    
    def read_all_cache(self):
        for web in SearchResult.select():
            print(web.url, web.content)
    
    def search(self, url: str):
        try:
            result = SearchResult.get(SearchResult.url == url)
            return result.content
        except DoesNotExist:
            return None
    
    def close(self):
        self.db.close()
    
# cache = WebCache()
# cache.save_to_cache("https://en.wikipedia.org/wiki/President_of_the_United_States", "The president of the United States is Joe Biden.")
# print(cache.read_all_cache())