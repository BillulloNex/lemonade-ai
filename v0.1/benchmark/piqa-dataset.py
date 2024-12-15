from datasets import load_dataset
from talk import talk, talk_gpt
import csv


ds = load_dataset("ybisk/piqa",trust_remote_code=True)

def craft_prompt(goal, sol1, sol2):

    return f"""
Carefully choose the correct answer. 
Validation rules:
- Your entire response must be EXACTLY one character
- ONLY valid responses are: 'A' or 'B'
- ANY OTHER RESPONSE IS INVALID

Question: To achieve this goal of {goal}, what is the best solution?
A) {sol1}
B) {sol2}

Answer:
    """


def check_answer(answer, correct_label):
    if answer.strip().upper() == 'A' and correct_label == 0:
        print('true')
        return True
    if answer.strip().upper() == 'B' and correct_label == 1:
        print('true')
        return True
    print('false')
    return False

def run_test():
    for data in ds['validation']:
        prompt = craft_prompt(data['goal'], data['sol1'], data['sol2'])
        answer = talk('llama3.2:1b',prompt)
        print('Answer:', answer)
        print('Correct:', data)
        check_answer(answer, data['label'])
        with open('piqa_results.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([data['goal'], data['sol1'], data['sol2'], answer, data['label'], check_answer(answer, data['label'])])
        answer_gpt = talk_gpt(prompt)
        print('GPT Answer:', answer_gpt)
        print('Correct:', data)
        check_answer(answer_gpt, data['label'])
        with open('piqa_results_gpt.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([data['goal'], data['sol1'], data['sol2'], answer_gpt, data['label'], check_answer(answer_gpt, data['label'])])

def read_test():
    print('---')
    with open('piqa_results.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        total = 0
        correct = 0
        for row in reader:
            total += 1
            if row[5] == 'True':
                correct += 1
        print(f'Accuracy for ollama: {correct/total:.2%}')
    print('---')

    print('---')
    with open('piqa_results_gpt.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        total = 0
        correct = 0
        for row in reader:
            total += 1
            if row[5] == 'True':
                correct += 1
        print(f'Accuracy for gpt: {correct/total:.2%}')
    print('---')

read_test()
