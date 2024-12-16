import os
import json
from knowledge.ingest import read_txt
from llm.ollama_func import model
config = {}
atlas = model(model = 'qwen2.5:0.5b')
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
    while True:
        prompt = input("You: ")
        print("Atlas: ")
        atlas.stream_chat_response(prompt= prompt)
        print('\n')
    #print(data)

init()
print(config)
loop()