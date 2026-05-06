from google import genai
from app.config import API_KEY, MODEL_NAME

# Create client
client = genai.Client(api_key=API_KEY)

def get_chatbot():
    return client

# 👉 PUT YOUR FUNCTION HERE
def generate_response(client, prompt):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text