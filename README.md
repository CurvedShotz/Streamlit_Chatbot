# Chatbot V3

# 💬 Chatbot V3  
An interactive chatbot built with **Streamlit** and powered by **Hugging Face’s Mistral-7B Instruct** model.  

This project demonstrates how to build a simple, production-style AI app that connects to a large language model (LLM) via API. It includes:  
- A clean **Streamlit UI** for chatting.  
- Integration with **Hugging Face Inference API**.  
- **Session-based chat history**.  
- An optional **chat logging system** that saves conversations as JSON files.  

---

## 🚀 Features
- **Chat Interface** → User-friendly Streamlit app with persistent chat history.  
- **LLM Integration** → Uses Hugging Face’s `mistralai/Mistral-7B-Instruct-v0.2`.  
- **Secrets Management** → API keys handled securely with Streamlit secrets.  
- **Logging** → Save conversations locally to `data/chat_logs/`.  

---

### 🔑 API Key Setup
This app uses the **Hugging Face Inference API**, which requires an access token.

1. Sign up for a free account at [Hugging Face](https://huggingface.co).  
2. Go to [Settings → Access Tokens](https://huggingface.co/settings/tokens).  
3. Generate a new token with **read** permissions.  
4. Add it to `.streamlit/secrets.toml` like this:

```toml
[huggingface]
api_key = "hf_your_token_here"



Chatbot_V3/
│── README.md # Project overview
│── requirements.txt # Dependencies
│── .gitignore # Ignore venv, secrets, cache
│
├── data/
│ └── chat_logs/ # Saved conversations (JSON)
│
├── src/
│ │── init.py
│ │── chatbot.py # API calls + logging
│ │── streamlit_app.py # Streamlit interface
│
└── tests/
└── test_chatbot.py # (Optional) unit tests