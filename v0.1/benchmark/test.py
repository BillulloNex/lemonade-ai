from ollama import chat
from pydantic import BaseModel
import json

class Country(BaseModel):
    name: str
    capital: str
    languages: list[str]

response = chat(
    messages=[
        {
            'role': 'user',
            'content': 'Tell me about Canada.',
        }
    ],
    model='smollm2:360m',
    format='json'  # Specify 'json' as the format
)

# Parse the JSON response manually
country_data = json.loads(response['message']['content'])
country = Country.model_validate(country_data)
print(country)