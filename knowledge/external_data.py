# World knowledge allows you to ask anything (prompt) and get back an LLM-friendly set of information. All cached for fast access.
from googlesearch import search
from bs4 import BeautifulSoup
import requests
from func.readable_web import WebPageReader


class WorldKnowledge:
    def __init__(self, source=None):
        self.source = source
        self.data = []
        
    
    def search(self, query):
        url_list = []
        scraped_data = []
        for result in search(query, num_results=5):
            url_list.append(result)
            web_reader = WebPageReader([result])
            try:
                print(f'scraping {result}')
                text_content = web_reader.get_content()
                print(text_content)
                scraped_data.append(text_content)
                print(f'processed: {text_content}')
            except:
                print('failed to scrape')
                continue
            print(f"Scraped {result}")
        self.data = scraped_data
        print('donezo')
    def read(self):
        print(self.data)
        return self.data        
    
    def cache():
        pass
    
    def ask():
        pass

ok = WorldKnowledge()
ok.search("who is the president of the united states")
ok.read()
