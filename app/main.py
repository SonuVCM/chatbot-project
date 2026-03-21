
from app.llm_client import get_chatbot
from app.utils import format_response

def run_chat():
    chat = get_chatbot()

    print("🤖 Chatbot started! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        try:
            response = chat.send_message(user_input)
            print("Bot:", format_response(response.text))
        except Exception as e:
            print("Error:", str(e))