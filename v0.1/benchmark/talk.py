import openai
import re
import httpx
import os
from dotenv import load_dotenv
import json
from pydantic import BaseModel

_ = load_dotenv()

class Answer(BaseModel):
  answer: str
 

from ollama import ChatResponse, chat
import csv

from openai import OpenAI

client = OpenAI()

class Agent:
    def __init__(self, model, system=""):
        self.model = model
        self.system = system

    def __call__(self, message):
        result = self.execute()
        return result

    def talk(self, prompt):
        completion = chat(model=self.model,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature":0},
            #format=Answer.model_json_schema(),
        )
        

        return completion.message.content
    
class Agent_GPT:
    def __init__(self, system=""):
        self.system = system

    def talk(self, prompt):
        completion = client.chat.completions.create(
                        model="gpt-4o", 
                        temperature=0,
                        messages=[{"role": "user", "content": prompt}])
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

Answer quickly and only with the ANSWER.
""".strip()
    abot = Agent(prompt)
    result = abot("Answer the question")
    return result
    #print(result)

#benchmark('go out for a picnic', ['neither option are applicable for the current situation', 'park along the street', 'try to park inside the park'], 'see a long line of cars for park entrance', 'easy', 'park along the street', 1)

def talk(model, prompt):
    abot = Agent(model)
    return abot.talk(prompt)

def talk_gpt(prompt):
    abot = Agent_GPT()
    return abot.talk(prompt)

#talk('smollm2:360m','what is the best letter? A or B?')