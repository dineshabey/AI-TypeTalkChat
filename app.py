from transformers import pipeline
import streamlit as st

# Set up Streamlit app title and page width
st.set_page_config(page_title='Simple Chatbot with Streamlit', layout='wide')

# Load conversational pipeline
chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Define Streamlit app layout
st.markdown("<h1 style='color: orange;'>💬🗣️ AI Type Talk Chat</h1>", unsafe_allow_html=True)
st.caption("🚀 Chat bot developed By :- [Dinesh Abeysinghe](https://www.linkedin.com/in/dinesh-abeysinghe-bb773293) | [GitHub Source Code](https://github.com/dineshabey/AI-TypeTalkChat.git) | [About model](https://arxiv.org/abs/2004.13637) ")

# Create text area for user input
with st.form(key='user_input_form'):
    st.markdown("<div style= 'text-align: center;'>The chatbot demonstrates engaging conversation, active listening, knowledge sharing, empathy, and consistent personality traits. <span style='color: orange;'>Please click like button</span>❤️ and support me and enjoy it.</div>", unsafe_allow_html=True)
    user_input = st.text_input("", placeholder="Your message")
    submitted = st.form_submit_button("Send")
 
    if submitted:
        if not user_input.strip():  # Check if input is empty or whitespace
            st.error('Please enter a chat')
        else:
            chat_history = st.session_state['chat_history']
            with st.spinner(text='Thinking ...'):
                conversation_bot_result = chatbot(user_input)
            
            bot_response = conversation_bot_result[0]["generated_text"]
            chat_history.append({"role": "user", "message": user_input})
            chat_history.append({"role": "bot", "message": bot_response})

            # Update chat history in session state
            st.session_state['chat_history'] = chat_history

# Display the chat history in LIFO order with user messages first
for chat in reversed(st.session_state['chat_history']):
    if chat['role'] == 'user':
        with st.chat_message("user"):
            st.write(chat['message'])
    else:
        with st.chat_message("assistant"):
            st.write(chat['message'])
            
