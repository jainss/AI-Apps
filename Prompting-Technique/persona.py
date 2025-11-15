from openai import OpenAI


client = OpenAI(
    api_key="AIzaSyCEtNm8U7udOJ-vu8Ggr5OhbHySLwu78K8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMT = """
You are an AI persona Assistant of Sahil specialized in code generation. 
You should only provide outputs related to coding tasks.

Example: 
Q: Hey
A: hey, whatup bro
"""
response = client.chat.completions.create(
    model= "gemini-2.5-flash",
    messages=[
        {"role": "system", "content":SYSTEM_PROMT},
        {"role": "user", "content": "hey who are you?"}
    ]
)

print(response.choices[0].message.content)