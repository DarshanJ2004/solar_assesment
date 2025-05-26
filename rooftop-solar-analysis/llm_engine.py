import os
import requests
from dotenv import load_dotenv
load_dotenv()

# Get API key from environment variable
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_report(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    json_data = {
        "model": "gpt-4o-mini",  # or any supported model
        "messages": [
            {"role": "system", "content": "You are a rooftop solar analysis expert."},
            {"role": "user", "content": prompt},
        ],
    }

    try:
        response = requests.post(url, headers=headers, json=json_data)
        response.raise_for_status()  # raise error for bad status
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        if response.status_code == 429:
            return "API quota exceeded on OpenRouter."
        return f"HTTP error occurred: {e}"
    except Exception as e:
        return f"Error: {e}"
