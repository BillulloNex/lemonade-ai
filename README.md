# lemonade-ai
A simple to build RAG AI Agent system that works on 


# Codebase structure

/config: This contains all configuration for apps & users. This includes:

- LLM choice (Smollm2, Qwem2, etc.)
- Knowledge source (Youtube, file, database, etc.)
- Output format (stream, text, code, voice, etc.)
- User information (background, hopes & dreams)

/knowledge: This contains all the code pertaining to how knowledge is acquired

/llm: This contains functions to make it simple to call an LLM

/output: This contains all the functions to convert stream of response into desired output type

/prompt: A list of recipes of great prompts