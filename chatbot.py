# chatbot.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class ChatBot:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = "gpt-3.5-turbo"
        self.client = OpenAI(api_key=self.api_key)

    def get_response(self, user_question):
        try:
            messages = [
                {"role": "system", "content": "You are a helpful medical assistant providing information about pneumonia and other lung issues. Provide concise and accurate responses."},
                {"role": "user", "content": user_question}
            ]
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=150,
                stop=None
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {e}"

# Create an instance of the ChatBot class
chatbot = ChatBot()