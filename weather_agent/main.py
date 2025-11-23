from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()

client = OpenAI(
    api_key="AIzaSyCEtNm8U7udOJ-vu8Ggr5OhbHySLwu78K8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Sorry, I couldn't fetch the weather information right now."
    else:
        return f'The weather in {city} is: + {response.text}'


def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "user", "content": user_query}
        ]
    )
    
    print("Response:", response.choices[0].message.content)
    

print(get_weather("Goa"))
