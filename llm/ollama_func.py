from ollama import chat
from ollama import ChatResponse

class model:
    def __init__(self, model: str = 'smollm2:360m'):
        self.model = model
        self.messages = []
    
    def get_chat_response(self,prompt: str) -> str:
        self.messages.append({'role': 'user', 'content': prompt,})
        response: ChatResponse = chat(model=self.model, messages= self.messages)
        self.messages.append(response.message)
        return response.message.content

    def stream_chat_response(self, prompt: str):
        if prompt == 'history':
            print(self.messages)
            pass
        elif prompt == 'exit':
            exit()
        self.messages.append({'role': 'user', 'content': prompt,})
        stream = chat(
            model=self.model,
            messages=self.messages,
            stream=True,
        )

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
        self.messages.append(chunk['message'])


