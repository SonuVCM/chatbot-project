from app.llm_client import get_chatbot
from app.config import MODEL_NAME

def run_chat():
    client = get_chatbot()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=user_input
        )

        print("Bot:", response.text)