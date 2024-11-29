import os
import json
from knowledge.ingest import read_txt
from llm.ollama_func import get_chat_response, stream_chat_response
config = {}

def init():
    config_dir = "config"
    for filename in os.listdir(config_dir):
        print(filename)
        if filename.endswith(".json"):
            filepath = os.path.join(config_dir, filename)
            with open(filepath, 'r') as f:
                var_name = filename.replace(".json", "")
                config[var_name] = json.load(f)

def loop():
    print('looping shit')
    data = read_txt('knowledge/data/joe-rogan-trump-interview.txt')
    stream_chat_response(
        model=config['app_config']['llmName'], 
        prompt= read_txt('prompt/recipes/create_5_sentence_recipe/system.md') + data
        )
    #print(data)

init()
print(config)
loop()