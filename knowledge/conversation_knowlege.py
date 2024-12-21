from llmware.agents import LLMfx

class ChatHistory:
    def __init__(self):
        self.messages = []
        
    def add_message(self, role: str, content: str):
        """Add a message to the conversation history."""
        self.messages.append({"role": role, "content": content})
        
    def get_history(self):
        """Return the complete conversation history."""
        return self.messages
        
    def clear_history(self):
        """Clear all messages from the conversation history."""
        self.messages = []
        
    def get_last_message(self):
        """Return the last message in the conversation."""
        return self.messages[-1] if self.messages else None
    
    def summarize(self):
        agent = LLMfx()
        agent.load_work(str(self.messages))
        agent.load_tool_list(['answer'])
        result = agent.answer('write a summary and remove any unecessary texts', key='summary')
        summary = result['llm_response']
        self.clear_history()
        self.add_message("user", summary)

def example():
    chat = ChatHistory()
    chat.add_message("user", "Hi! Can you help me learn about AI?")
    chat.add_message("assistant", "Of course! What would you like to know?")
    chat.add_message("user", "What is machine learning?")
    chat.add_message("assistant", "Machine learning is a branch of AI where systems learn from data.")
    chat.add_message("user", "Can you give me an example?")
    chat.add_message("assistant", "Sure! Image recognition is a common example. AI learns to identify objects in photos.")
    chat.add_message("user", "That's interesting! How does it work?")
    chat.add_message("assistant", "It analyzes patterns in pixels and features to recognize objects.")
    chat.add_message("user", "Thank you for explaining!")
    chat.add_message("assistant", "You're welcome! Let me know if you have more questions.")
    chat.summarize()
    print(chat.messages)
