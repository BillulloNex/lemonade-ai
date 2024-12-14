# Import necessary libraries
from dotenv import load_dotenv

# Load environment variables (e.g., API keys)
load_dotenv()


# Import relevant functionality
from langchain_ollama import ChatOllama
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

import time

# Create the agent
memory = MemorySaver()
model = ChatOllama(model="llama3.2:1b", temperature=0.5)
search = TavilySearchResults(max_results=2)
tools = [search]
agent_executor = create_react_agent(model, tools, checkpointer=memory)

# Use the agent and save chunks to file
config = {"configurable": {"thread_id": "abc123"}}

with open('chunk.txt', 'w') as f:
    start_time = time.time()
    for chunk in agent_executor.stream(
        {"messages": [HumanMessage(content="hi im bob! and i live in sf, whats the weather where I live?")]}, config
    ):
        print(chunk)
        print("----")
        f.write(str(chunk) + "\n----\n")
        print("Elapsed time: ", time.time() - start_time)
        start_time = time.time()
    print("Total elapsed time: ", time.time() - start_time)