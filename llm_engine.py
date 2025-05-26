import os
import requests

OPENROUTER_API_KEY = "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"

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
