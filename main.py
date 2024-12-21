import os
import json
from llm.ollama_func import model
from tool.tavily_web import tavily_web
from knowledge.external_data import WorldKnowledge

config = {}
atlas = model(model = 'qwen2.5:0.5b')
knowledge = WorldKnowledge()
def init():
    config_dir = "config"
    for filename in os.listdir(config_dir):
        # print(filename)
        if filename.endswith(".json"):
            filepath = os.path.join(config_dir, filename)
            with open(filepath, 'r') as f:
                var_name = filename.replace(".json", "")
                config[var_name] = json.load(f)

def loop():
    search = tavily_web()
    while True:
        prompt = input("You: ")
        web_result = knowledge.search(prompt)
        print(f'Context: {web_result}')
        print("Atlas: ")
        output = atlas.stream_chat_response(f" Given this context: {web_result}, answer this question: {[prompt]}")
        print('\n')
    #print(data)

init()
# print(config)
loop()