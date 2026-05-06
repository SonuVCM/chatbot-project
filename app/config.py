import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

# Recommended model
MODEL_NAME = "gemini-3-flash-preview"