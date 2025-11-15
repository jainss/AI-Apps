from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyCEtNm8U7udOJ-vu8Ggr5OhbHySLwu78K8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model= "gemini-2.5-flash",
    messages=[
        {"role": "user", "content": "Hello There!"}
    ]
)

print(response.choices[0].message.content)