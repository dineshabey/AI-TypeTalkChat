# app.py

from transformers import pipeline
import streamlit as st



# Set up Streamlit app title and page width
st.set_page_config(page_title='Simple Chatbot with Streamlit', layout='wide')

# Load conversational pipeline
chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Read the CSS file
with open("./style/style.css") as f:
    css = f.read()

# Inject CSS into the Streamlit app
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Define Streamlit app layout
st.markdown("<h1 style='color: orange;'>💬 Chatbot</h1>", unsafe_allow_html=True)
st.caption("🚀 Chat bot created By :- [Dinesh Abeysinghe](https://www.linkedin.com/in/dinesh-abeysinghe-bb773293)")

# Create text area for user input
user_input = st.text_input("", placeholder="Your message")

# Define Streamlit app behavior
if st.button('Send'):
    if not user_input.strip():  # Check if input is empty or whitespace
        st.error('Please enter a chat')
    else:
        chat_history = st.session_state['chat_history']
        chat_history.append({"role": "user", "message": user_input})

        with st.spinner(text='Thinking ...'):
            conversation_bot_result = chatbot(user_input)
        
        bot_response = conversation_bot_result[0]["generated_text"]
        chat_history.append({"role": "bot", "message": bot_response})

        # Update chat history in session state
        st.session_state['chat_history'] = chat_history

# Create text area for chat history
chat_area = st.empty()

# Display the chat history with alternating user and bot messages
chat_text = ""
user_messages = [chat for chat in st.session_state['chat_history'] if chat['role'] == 'user']
bot_messages = [chat for chat in st.session_state['chat_history'] if chat['role'] == 'bot']

for user_chat, bot_chat in zip(reversed(user_messages), reversed(bot_messages)):
    chat_text += f"<div class='user-message'>{user_chat['message']}</div>\n"
    chat_text += f"<div class='bot-message'>{bot_chat['message']}</div>\n"

# Add any remaining user messages if there are more user messages than bot messages
for user_chat in reversed(user_messages[len(bot_messages):]):
    chat_text += f"<div class='user-message'>{user_chat['message']}</div>\n"

chat_area.markdown(f"<div class='chat-container'>{chat_text}</div>", unsafe_allow_html=True)
