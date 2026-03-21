
import google.generativeai as genai
from app.config import API_KEY, MODEL_NAME

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(MODEL_NAME)

def get_chatbot():
    return model.start_chat(history=[])