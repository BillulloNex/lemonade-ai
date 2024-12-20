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

# Example usage:
if __name__ == "__main__":
    urls = ["https://en.wikipedia.org/wiki/President_of_the_United_States"]
    reader = WebPageReader(urls)
    print(reader.get_content())
