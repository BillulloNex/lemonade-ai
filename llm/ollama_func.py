from ollama import chat
from ollama import ChatResponse

def get_chat_response(prompt: str, model: str = 'smollm2:360m') -> str:
    response: ChatResponse = chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    return response.message.content

def stream_chat_response(prompt: str, model: str = 'smollm2:360m'):
    stream = chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

# Example usage:
print(get_chat_response('Why is the sky blue?'))
stream_chat_response('Why is the sky blue?')

