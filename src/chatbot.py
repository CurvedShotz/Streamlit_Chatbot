# Chatbot logic will go here

import requests
import streamlit as st

# Load API key from Streamlit secrets
API_KEY = st.secrets["huggingface"]["api_key"]

# Hugging Face Inference API endpoint (Mistral 7B Instruct)
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

# HTTP headers
headers = {"Authorization": f"Bearer {API_KEY}"}


def query_huggingface(prompt: str) -> str:
    """
    Send a prompt to the Hugging Face Inference API and return the response.
    """
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return f"⚠️ API Error {response.status_code}: {response.text}"

    # API returns a list of dictionaries
    result = response.json()
    try:
        return result[0]["generated_text"]
    except (KeyError, IndexError, TypeError):
        return "⚠️ Unexpected API response format."


def chatbot_response(user_input: str) -> str:
    """
    Wrapper for chatbot response logic.
    """
    return query_huggingface(user_input)
