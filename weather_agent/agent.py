import requests
from openai import OpenAI
from dotenv import load_dotenv
import json


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
    
available_tools = {
    "get_weather": get_weather
}

SYSTEM_PROMT = """
    You are expert AI Assistant in resolving user queries using chain of thought process.
    When a user asks a question, break down the reasoning steps clearly before providing the final answer.
    You need to first Plan has been done. The Plan should include the steps to solve the problem.
    Once you think enough PLAN has been done, finally provide the ANSWER.
    You can also call a tool if required from the list of aviavle tools.
    For very tool call wait for the oberve step before proceeding further.
    
    Rules:
     - Stricty follow the output in JSON format.
     - Only run one step at a time
     - Te sequence of steps is START -> PLAN -> OUTPUT
     
     Output JOSN Function Format:
     {"step": "STRAT" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string"}
     
     Available Tools:
     - get_weather: Tales a city name as input and returns the current weather information for that city.
     
     Example 1:
     START: Hey, Can you solve 2+3*5/10
     PLAN: {"step": "PLAN", "content": "First, calculate the multiplication 3*5=15. Next,"}
     PLAN: {"step": "PLAN", "content": "divide 15 by 10 to get 1.5."}
     PLAN: {"step": "PLAN", "content": "Finally, add 2 and 1.5 to get the final answer 3.5."}
     OUTPUT: {"step": "OUTPUT", "content": "The final answer is 3.5."}
     
     Example 2:
     START: What's the weather like in New York City today?
        PLAN: {"step": "PLAN", "content": "To provide the weather information, I need to use the get_weather tool."}
        PLAN: {"step": "PLAN", "content": "Let me check is there amy available tool for fetching weather information tool for that"}
        PLAN: {"step": "PLAN", "content": "Yes, there is a tool named get_weather which takes city name as input and returns the current weather information."}
        PLAN: {"step": "PLAN", "content": "I will call the get_weather tool with 'New York City' as the input."}
        PLAN: {"step": "PLAN", "content": "Once I get the weather information, I will provide it in the final answer."}
        TOOL: {"step": "TOOL", "content": "get_weather('New York City')"}
        
"""

message_history = [
    {"role": "system", "content": SYSTEM_PROMT},
]

while True:
    user_query = input("Enter your question: ")
    message_history.append({"role": "user", "content": user_query})

    while True:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=message_history
        )
        
        raw_result = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_result})
        
        parshed_result = json.loads(raw_result)
        if parshed_result.get("step") == "START":
            print("Planning started...")
        if parshed_result.get("step") == "PLAN":
            print("Planning:", parshed_result["content"])
        if parshed_result.get("step") == "TOOL":
            tool_to_call = parshed_result.get("tool")
            tool_input = parshed_result.get("input")
            print("Invoking Tool...")
            tool_output = available_tools[tool_to_call](tool_input)
            print(f"Tool Output: {tool_output}")
            message_history.append({
                "role": "dveloper",
                "content": json.dumps({
                    "step": "OBSERVE",
                    "tool": tool_to_call,
                    "input": tool_input,
                    "output": tool_output
                })
            })
            continue
        if parshed_result.get("step") == "OUTPUT":
            print("Final Answer:", parshed_result["content"])
            break
