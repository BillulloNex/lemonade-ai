# Tool name: Tavily Web
# Description: Using tavily api, this tool provides a way to search for general information, context and question and answer
# TLDR: Given a prompt, Tavily search the web and get LLM-friendly response quickly

from tavily import TavilyClient
import time
import os
from dotenv import load_dotenv
# Load environment variables from .env file

class tavily_web:
    def __init__(self):
        load_dotenv()
        self.start_time = time.time()
        self.tavily_client = TavilyClient()
    def general_search(self, query):
        response = self.tavily_client.search(query)
        return response
    def context_search(self, query):
        response = self.tavily_client.get_search_context(query)
        return response
    def qna_search(self, query):
        response = self.tavily_client.qna_search(query=query)
        return response
# web = tavily_web()
# result = web.qna_search('Who is the president of Vietnam?')
# print(result)