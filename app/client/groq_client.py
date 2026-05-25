## Handles the interaction with the Groq API, including authentication and query execution.

from groq import Groq
from app.config.settings import settings

client= Groq(api_key=settings.GROQ_API_KEY) ## Initialize the Groq client with the API key from settings

## Send the prompt to the Groq API and return the response

def ask_groq(prompt: str):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
            temperature = 0.2, ## Adjust the temperature for more or less creative responses
            
        )

    return response.choices[0].message.content ## Return the content of the first message in the response