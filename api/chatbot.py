import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

print("ALL ENV VARS:", os.environ)

class ChatBot:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        print("OPENAI_API_KEY in production:", self.api_key)
        if not self.api_key:
            raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        self.model = "gpt-3.5-turbo"
        self.client = OpenAI(api_key=self.api_key)

    def get_response(self, context, user_question):
        try:
            messages = [
                {"role": "system", "content": "You are a helpful medical assistant providing information about lung conditions, including pneumonia and tuberculosis. Provide concise and accurate responses."},
                {"role": "user", "content": f"{context}\n\nUser question: {user_question}"}
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
            return f"Error: {str(e)}"

def get_chatbot():
    return ChatBot()

# Create an instance of the ChatBot class
try:
    chatbot = ChatBot()
except ValueError as e:
    print(f"Error initializing ChatBot: {str(e)}")
    chatbot = None 