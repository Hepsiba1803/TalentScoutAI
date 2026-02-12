import os
from dotenv import load_dotenv
from google import genai

# loading api key from .env file into computer memory
load_dotenv()

# 1. READ THE KEY EXPLICITLY
api_key = os.getenv("GEMINI_API_KEY")

# 2. CHECK IF KEY EXISTS (Debugging Step)
if not api_key:
    raise ValueError("API Key not found! Check your .env file.")

# 3. INITIALIZE DIRECTLY (No try/except here so we see the real error)
gemini = genai.Client(api_key=api_key)

def get_ai_responses(messages):

    try:
        # seperate system instruction from user messages
        system_instruction = messages[0]['content']
       
        # translating messages to list of strings(Gemini format)
        chat_contents=[]
        for msg in messages[1:]:
            role= "user" if msg['role']== 'user' else 'model'
            chat_contents.append(role +":" + msg["content"])
        
        # If chat_contents is empty, it means this is the very first turn.
        # We send a hidden prompt to trigger the greeting.
        if not chat_contents:
            chat_contents = ["Hello, please start the interview."]

        # calling Gemini API 
        response=gemini.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=chat_contents,
            config={
                "system_instruction": system_instruction,
                "temperature":0.1
            }
        )
        return response.text
    except Exception as e:
        return f'Error generating AI response: {e}'
