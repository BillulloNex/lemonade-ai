import openai
import re
import httpx
import os
from dotenv import load_dotenv

from ollama import ChatResponse, chat
_ = load_dotenv()
from openai import OpenAI

client = OpenAI()

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
        completion = client.chat.completions.create(
                        model="gpt-4o", 
                        temperature=0,
                        messages=self.messages)
        return completion.choices[0].message.content
    
    

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

Answer:
""".strip()
    #print(prompt)
    abot = Agent(prompt)
    result = abot("Answer the question")
    print(result)

benchmark('go out for a picnic', ['neither option are applicable for the current situation', 'park along the street', 'try to park inside the park'], 'see a long line of cars for park entrance', 'easy', 'park along the street', 1)
