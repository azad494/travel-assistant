# planner.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_itinerary(prompt: str) -> str:
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  # Use "gpt-3.5-turbo-instruct" if GPT-4 fails
            prompt=prompt,
            max_tokens=1200,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"❌ Error: {e}"
