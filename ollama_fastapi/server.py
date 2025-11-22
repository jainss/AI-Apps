from fastapi import FastAPI
from ollama import Client

app = FastAPI()
client = Client(host="http://localhost:11434")


@app.get("/")
def read_root():
    return {"Hello": "Sahil"}


@app.post("/chat")
def chat(
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
):
    response = client.chat(model="gemma:2b", messages=messages)
    return {"response": response.message['content']}
