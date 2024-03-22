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
st.markdown('''
    <button class='relative flex items-center overflow-hidden from-red-50 to-transparent dark:from-red-900 px-1.5 py-1 hover:bg-gradient-to-t focus:outline-none' title='Unlike'>
        <svg class='left-1.5 absolute' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' aria-hidden='true' focusable='false' role='img' width='1em' height='1em' preserveAspectRatio='xMidYMid meet' viewBox='0 0 32 32' fill='currentColor'>
            <path d='M22.45,6a5.47,5.47,0,0,1,3.91,1.64,5.7,5.7,0,0,1,0,8L16,26.13,5.64,15.64a5.7,5.7,0,0,1,0-8,5.48,5.48,0,0,1,7.82,0L16,10.24l2.53-2.58A5.44,5.44,0,0,1,22.45,6m0-2a7.47,7.47,0,0,0-5.34,2.24L16,7.36,14.89,6.24a7.49,7.49,0,0,0-10.68,0,7.72,7.72,0,0,0,0,10.82L16,29,27.79,17.06a7.72,7.72,0,0,0,0-10.82A7.49,7.49,0,0,0,22.45,4Z'></path>
        </svg>
        <svg class='absolute text-red-500 origin-center transform transition-transform ease-in left-1.5' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' aria-hidden='true' focusable='false' role='img' width='1em' height='1em' preserveAspectRatio='xMidYMid meet' viewBox='0 0 32 32' fill='currentColor'>
            <path d='M22.5,4c-2,0-3.9,0.8-5.3,2.2L16,7.4l-1.1-1.1C12,3.3,7.2,3.3,4.3,6.2c0,0-0.1,0.1-0.1,0.1c-3,3-3,7.8,0,10.8L16,29l11.8-11.9c3-3,3-7.8,0-10.8C26.4,4.8,24.5,4,22.5,4z'></path>
        </svg>
        <span class='ml-4 pl-0.5'>like</span>
    </button>
''', unsafe_allow_html=True)


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
            
