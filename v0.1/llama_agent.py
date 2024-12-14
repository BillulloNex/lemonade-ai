from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_ollama import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Global conversation instance
conversation = None

def init_chat():
    """Initialize the chat agent once"""
    global conversation
    if conversation is None:
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        chat_model = ChatOllama(
            model="llama3.2:1b",
            callback_manager=callback_manager,
            temperature=0.7,
        )
        memory = ConversationBufferMemory()
        conversation = ConversationChain(
            llm=chat_model,
            memory=memory,
            verbose=False
        )
    return conversation

def chat(message: str) -> str:
    """Simple function to send a message and get a streaming response"""
    global conversation
    if conversation is None:
        init_chat()
    return conversation.predict(input=message)

# Example usage:
if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'quit':
            break
        if user_input:
            chat(user_input)
