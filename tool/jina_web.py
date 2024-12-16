# Tool name: Jina Web
# Description: Using Jina api, this tool provides a way to search for general information, context and question and answer
# TLDR: Given a url, Jina scrapes the web and returns a LLM-friendly content
import requests
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
print(os.getenv("JINA_AI_API_KEY"))
class jina_web:
    def __init__(self):
        self.headers = {'Authorization': f'Bearer {os.getenv("JINA_AI_API_KEY")}'}
    def read_web(self, url):
        response = requests.get(f'https://r.jina.ai/{url}', headers=self.headers)
        return response.text

web = jina_web()
result = web.read_web('https://www.jina.ai')
print(result)
