# World knowledge allows you to ask anything (prompt) and get back an LLM-friendly set of information. All cached for fast access.
from googlesearch import search
from bs4 import BeautifulSoup
import requests


from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import Html2TextTransformer

class WebPageReader:
    def __init__(self, urls):
        self.urls = urls if isinstance(urls, list) else [urls]
        self.loader = AsyncHtmlLoader(self.urls)
        self.transformer = Html2TextTransformer()
        
    def load_and_transform(self):
        """Load URLs and transform HTML to readable text"""
        docs = self.loader.load()
        return self.transformer.transform_documents(docs)
    
    def get_content(self):
        """Get the transformed content of the first page"""
        docs_transformed = self.load_and_transform()
        return docs_transformed[0].page_content if docs_transformed else None


class WorldKnowledge:
    def __init__(self, source=None):
        self.source = source
        self.data = []
        
    def search(self, query):
        url_list = []
        scraped_data = []
        for result in search(query, num_results=5, region='us', lang='en'):
            url_list.append(result)
            web_reader = WebPageReader([result])
            try:
                text_content = web_reader.get_content()
                scraped_data.append(text_content)
            except:
                print('failed to scrape')
                continue
            print(f"Scraped {result}")
        self.data = scraped_data
        print(scraped_data)[0]
        return scraped_data
        
        print('donezo')
    def read(self):
        print(self.data[0])
        return self.data        
    
    def cache(url, result):
        pass
    def ask():
        pass

ok = WorldKnowledge()
ok.search("who is the president of the united states")
ok.read()
