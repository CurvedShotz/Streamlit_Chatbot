import streamlit as st
from src.chatbot import chatbot_response
from src.chatbot import chatbot_response, log_conversation

# Streamlit page config
st.set_page_config(page_title="Chatbot V3", page_icon="💬", layout="centered")

st.title("💬 Chatbot V3")
st.write("Powered by Hugging Face Mistral-7B Instruct")

# Store chat history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for message in st.session_state["messages"]:
    role, text = message
    if role == "user":
        st.markdown(f"**🧑 You:** {text}")
    else:
        st.markdown(f"**🤖 Bot:** {text}")

# Chat input box
user_input = st.text_input("Type your message:", key="input")

# When user submits a message
if user_input:
    # Save user message
    st.session_state["messages"].append(("user", user_input))

    # Get bot response
    with st.spinner("Thinking..."):
        response = chatbot_response(user_input)

    # Save bot response
    st.session_state["messages"].append(("bot", response))

    # Rerun to refresh UI with new message
    st.experimental_rerun()


# Add a save button below chat
if st.button("💾 Save Chat"):
    filepath = log_conversation(st.session_state["messages"])
    st.success(f"Chat saved to {filepath}")