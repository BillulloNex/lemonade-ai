from llmware.agents import LLMfx

def create_report():
    while True:
        prompt = input('Ask AI: ')
        agent = LLMfx()
        agent.load_work('''
{prompt}
                        '''
                        )

        agent.load_tool_list([
            'topics',
            ])

        result = agent.topics()
        summary = result['llm_response']
        print(f'result: {summary}')

create_report()