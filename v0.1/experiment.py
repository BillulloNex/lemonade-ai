import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

# Load environment variables (e.g., API keys)
load_dotenv()

# Initialize the OpenAI model (e.g., GPT-4) with streaming enabled
llm = ChatOllama(model="llama3.2:1b", temperature=0.5)

# Initialize Tavily Search tool for retrieving information
tavily_tool = TavilySearchResults(max_results=3)

# Create the agent using create_react_agent
agent_executor = create_react_agent(llm, [tavily_tool])

async def stream_response(input_text):
    # Stream the response from the agent word by word
    for step in agent_executor.stream({"messages": [HumanMessage(content=input_text)]}, stream_mode="updates"):
        print(step)
        # Assuming step contains the text output from the model
        if 'content' in step:
            # Print each word as it is generated
            for word in step['content'].split():
                print(word, end=' ', flush=True)
            print()  # New line after each complete response
        await asyncio.sleep(0)  # Allow other tasks to run

# Main interaction loop
async def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the conversation.")
            break
        
        await stream_response(user_input)

# Run the main loop
if __name__ == "__main__":
    asyncio.run(main())
