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

/prompt: A list of recipes of great prompts (inspired by Fabric)

# Develop like a game

A game contains an init function & a game loop
The init function contains:

- Setup user information
- Create or read chat history (one history per app)
- Create a fast-to-use chat_history interface
- Initiate any other configuration variables

The game loop contains:

- A trigger (user prompt or something changes)
- Processing the information
- Output LLM response

