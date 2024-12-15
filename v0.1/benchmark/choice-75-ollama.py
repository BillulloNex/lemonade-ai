import openai
import re
import httpx
import os
from dotenv import load_dotenv
import json
_ = load_dotenv()

from ollama import ChatResponse, chat
import csv

class Agent:
    def __init__(self, system=""):
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append({"role": "system", "content": system})

    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        completion = chat(model=
                        'llama3.2:1b',
                        messages=self.messages,
                        options={"temperature":0}
        )
        return completion.message.content
    

def benchmark(goal, options, context, difficulty, golden_answer, step):
    prompt = f"""
You are an expert at picking the right answer to a question. You are given a question and you must provide the correct answer.
You will be given a GOAL, a CONTEXT, and a few OPTIONS. You must choose the correct answer from the OPTIONS based on the CONTEXT to achieve the GOAL.

Example scenario:

GOAL: go out for a picnic
CONTEXT: have a tight budget

Your available answer OPTIONS are:

0. neither options are applicable for the current situation
1. park along the street
2. try to park inside the park

Answer: 1. park along the street

Here is the actual Scenario you need to solve for:

GOAL: {goal}
CONTEXT: {context}

Your available answer OPTIONS are:

0. {options[0]}
1. {options[1]}
2. {options[2]}

Answer quickly and only with the ANSWER.
""".strip()
    abot = Agent(prompt)
    result = abot("Answer the question")
    return result
    #print(result)

#benchmark('go out for a picnic', ['neither option are applicable for the current situation', 'park along the street', 'try to park inside the park'], 'see a long line of cars for park entrance', 'easy', 'park along the street', 1)

def extract_dataset():

    with open('datasets/choice-75/recompiled_dataset.json', 'r') as file:
        data = json.loads(file.read())
        for entry in data:
            goal = entry['goal']
            options = entry['options']
            for scenario in entry['scenarios']:
                context = scenario['context']
                difficulty = scenario['difficulty']
                golden_answer = scenario['answer']
                step = entry['step']
                result = benchmark(goal, options, context, difficulty, golden_answer, step)
                correct_or_not = str(golden_answer) in str(result)
                if str(golden_answer) in str(result):
                    print("Correct!")

                else:
                    print("Not correct!")
                # Create or append to results list
                result_entry = {
                    "goal": goal,
                    "context": context,
                    "options": options,
                    "difficulty": difficulty,
                    "golden_answer": golden_answer,
                    "model_answer": result.strip(),
                    "is_correct": correct_or_not
                }
                
                # Load existing results if file exists
                results = []
                if os.path.exists('benchmark_results.json'):
                    with open('benchmark_results.json', 'r') as f:
                        try:
                            results = json.load(f)
                        except json.JSONDecodeError:
                            results = []
                
                # Append new result and write back to file
                results.append(result_entry)
                with open('benchmark_results.json', 'w') as f:
                    json.dump(results, f, indent=2)
                
                # Convert JSON results to CSV


                    
def convert_to_csv():
    with open('benchmark_results.json', 'r') as json_file:
        results = json.load(json_file)
    with open('benchmark_results.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['goal', 'context', 'options', 'difficulty', 'golden_answer', 'model_answer', 'is_correct'])
        writer.writeheader()
        writer.writerows(results)
extract_dataset()
convert_to_csv()