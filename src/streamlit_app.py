# import streamlit as st
# from chatbot import chatbot_response, log_conversation

# # Streamlit page config
# st.set_page_config(page_title="Chatbot V3", page_icon="💬", layout="centered")

# st.title("💬 Chatbot V3")
# st.write("Powered by Hugging Face Models")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state["messages"] = []

# # Display chat history
# for message in st.session_state["messages"]:
#     role = message["role"]
#     text = message["text"]
#     if role == "user":
#         st.markdown(f"**🧑 You:** {text}")
#     else:
#         st.markdown(f"**🤖 Bot:** {text}")

# # Chat input box
# if "input" not in st.session_state:
#     st.session_state["input"] = ""

# user_input = st.text_input("Type your message:", key="input")

# # Handle message submission
# if user_input.strip() != "":
#     # Save user message
#     st.session_state["messages"].append({"role": "user", "text": user_input})

#     # Get bot response
#     with st.spinner("🤖 Thinking..."):
#         response = chatbot_response(user_input)

#     # Save bot response
#     st.session_state["messages"].append({"role": "bot", "text": response})

#     # Clear input box
#     st.session_state["input"] = ""

#     # Rerun to display updated chat
#     st.experimental_rerun()

# # Save chat button
# if st.button("💾 Save Chat"):
#     filepath = log_conversation(st.session_state["messages"])
#     st.success(f"Chat saved to {filepath}")

###TEST

import streamlit as st
from chatbot import chatbot_response, log_conversation

# Page config
st.set_page_config(page_title="Chatbot V3", page_icon="💬", layout="centered")
st.title("💬 Chatbot V3")
st.write("Powered by Hugging Face Models")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "submit" not in st.session_state:
    st.session_state["submit"] = False

# Display chat history
for message in st.session_state["messages"]:
    role = message["role"]
    text = message["text"]
    if role == "user":
        st.markdown(f"**🧑 You:** {text}")
    else:
        st.markdown(f"**🤖 Bot:** {text}")

# Chat input box (no session state assignment)
user_input = st.text_input("Type your message:")

# Send button
if st.button("Send"):
    if user_input.strip():
        # Save user message
        st.session_state["messages"].append({"role": "user", "text": user_input})
        st.session_state["submit"] = True

# Handle bot response
if st.session_state["submit"]:
    with st.spinner("🤖 Thinking..."):
        response = chatbot_response(st.session_state["messages"][-1]["text"])
    st.session_state["messages"].append({"role": "bot", "text": response})
    st.session_state["submit"] = False
    st.rerun()

# Save chat
if st.button("💾 Save Chat"):
    filepath = log_conversation(st.session_state["messages"])
    st.success(f"Chat saved to {filepath}")
