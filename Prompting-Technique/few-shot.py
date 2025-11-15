from openai import OpenAI


client = OpenAI(
    api_key="AIzaSyCEtNm8U7udOJ-vu8Ggr5OhbHySLwu78K8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMT = """You are expert in code generation and you only given the output realted to coding and if someone ask different question you have to say sorry i dont know that.

Rules: 
 - Strictly follow the output in JSON format.
 
 Output Format:
 {{
     "Code": "string" or null,
     "isCodingQuestion" : boolean
 }}
 

Example: 
Q: Can you explain the a+b whole squre?
A: {{"code": null, "isCodingQuestion": false}}

Q: Hey, write a python function to add two numbers.
A: {{"code": "def add_numbers(a, b):\n    return a + b", "isCodingQuestion": true}}

"""
response = client.chat.completions.create(
    model= "gemini-2.5-flash",
    messages=[
        {"role": "system", "content":SYSTEM_PROMT},
        {"role": "user", "content": "send me a hello world prgram in python"}
    ]
)

print(response.choices[0].message.content)