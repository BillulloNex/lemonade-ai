from llmware.agents import LLMfx

def create_report(prompt):
    agent = LLMfx()
    agent.load_work(prompt)
    agent.load_tool('sentiment')
    agent.load_tool('ner')
    agent.load_tool_list(['emotions', 'topics', 'intent','tags','ratings','answer'])

    agent.sentiment()
    agent.emotions()
    agent.intent()
    agent.topics()
    agent.tags()
    agent.ratings()
    agent.answer('write a short summary', key='summary')

    #agent.exec_function_call(['emotions', 'topics', 'intent','tags','ratings','answer'])

create_report('The old woman, Elsie, sat on the park bench, her weathered hands clasped tightly around a worn leather bag. Her gaze, though clouded with age, held a quiet strength, a lifetime of stories etched into its depths. A stray dog, drawn by the warmth of her presence, nudged her hand with its cold nose, eliciting a soft chuckle. She offered the dog a piece of bread from her bag, a small act of kindness in the bustling city.')