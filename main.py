import os
import json
from llm.ollama_func import model
from tool.tavily_web import tavily_web

from llmware.models import ModelCatalog
atlas = ModelCatalog().load_model("slim-nli-tool")




config = {}
#atlas = model(model = 'smollm2:360m')
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
        web_result = search.qna_search(prompt)
        print(f'Context: {web_result}')
        print("Atlas: ")
        output = atlas.inference(f" Given this context: {web_result}, answer this question: {[prompt]}")
        print(output)        
        print('\n')
    #print(data)

init()
print(config)
loop()