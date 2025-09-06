import requests
import streamlit as st
import os
import json
from datetime import datetime

# Load API key from Streamlit secrets
API_KEY = st.secrets["huggingface"]["api_key"]

# Hugging Face Inference API endpoint (Mistral 7B Instruct)
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

# HTTP headers
headers = {"Authorization": f"Bearer {API_KEY}"}


def query_huggingface(prompt: str, max_tokens: int = 200, temperature: float = 0.7) -> str:
    """
    Send a prompt to Hugging Face Inference API and return the response.
    Includes timeout and error handling.
    """
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_tokens,
            "temperature": temperature
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()

        # Hugging Face API returns a list with 'generated_text'
        return result[0].get("generated_text", "⚠️ No text returned by model.")

    except requests.exceptions.Timeout:
        return "⚠️ API Timeout: model took too long to respond."
    except requests.exceptions.RequestException as e:
        return f"⚠️ API Error: {e}"
    except (KeyError, IndexError, TypeError):
        return "⚠️ Unexpected API response format."


def chatbot_response(user_input: str) -> str:
    """
    Wrapper for chatbot response logic.
    """
    # Strip input to avoid sending empty messages
    if not user_input.strip():
        return "⚠️ Please enter a message."
    
    return query_huggingface(user_input)


def log_conversation(messages, folder="data/chat_logs"):
    """
    Save chat history to a JSON file.
    Each session gets a timestamped filename.
    """
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(folder, f"chat_{timestamp}.json")

    # Save messages as list of dictionaries for readability
    json_messages = [{"role": role, "text": text} for role, text in messages]

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(json_messages, f, indent=2, ensure_ascii=False)

    return filepath
