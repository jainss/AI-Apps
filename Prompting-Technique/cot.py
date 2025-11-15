from openai import OpenAI
import json


client = OpenAI(
    api_key="AIzaSyCEtNm8U7udOJ-vu8Ggr5OhbHySLwu78K8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMT = """
    You are expert AI Assistant in resolving user queries using chain of thought process.
    When a user asks a question, break down the reasoning steps clearly before providing the final answer.
    You need to first Plan has been done. The Plan should include the steps to solve the problem.
    Once you think enough PLAN has been done, finally provide the ANSWER.
    
    Rules:
     - Stricty follow the output in JSON format.
     - Only run one step at a time
     - Te sequence of steps is START -> PLAN -> OUTPUT
     
     Output JOSN Function Format:
     {"step": "STRAT" | "PLAN" | "OUTPUT", "content": "string"}
     
     Example:
     START: Hey, Can you solve 2+3*5/10
     PLAN: {"step": "PLAN", "content": "First, calculate the multiplication 3*5=15. Next,"}
     PLAN: {"step": "PLAN", "content": "divide 15 by 10 to get 1.5."}
     PLAN: {"step": "PLAN", "content": "Finally, add 2 and 1.5 to get the final answer 3.5."}
     OUTPUT: {"step": "OUTPUT", "content": "The final answer is 3.5."}
"""
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMT},
        {"role": "user", "content": "Hey, Write a code to add n number in js"},
    ]
)

print(response.choices[0].message.content)
