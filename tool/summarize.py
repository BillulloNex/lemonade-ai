from transformers import pipeline
from lemonade_ai.knowledge.external_data import WorldKnowledge
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

me = WorldKnowledge()
ARTICLE = WorldKnowledge.search("who is casey neistat")[0]
print(summarizer(ARTICLE, max_length=1000, min_length=30, do_sample=False))
