from google import genai

client = genai.Client(
    api_key="AIzaSyCEtNm8U7udOJ-vu8Ggr5OhbHySLwu78K8"
)

response = client.models.generate_content(
    model= "gemini-2.5-flash",
    contents= "Hello There! what is 2+2?"
)

print(response.text)