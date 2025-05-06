import streamlit as st
from chatbot import simple_chatbot

st.set_page_config(page_title="Finance Chatbot", page_icon="💬")
st.title("💬 Financial Data Chatbot")
st.markdown("Ask a question about the 3 company financials (2022–2025).")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input field and submit button
with st.form(key="chat_form", clear_on_submit=True):
    user_query = st.text_input("You:")
    submit = st.form_submit_button("Ask")

# Process submission
if submit and user_query.strip():
    if user_query.lower() in ["exit", "quit"]:
        st.session_state.history.append((user_query, "Goodbye!"))
    else:
        response = simple_chatbot(user_query)
        st.session_state.history.append((user_query, response))

# Display styled chat history
st.markdown(
    """
    <style>
    .user-msg {
        background-color: #1e3a8a;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .bot-msg {
        background-color: #374151;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

for user_msg, bot_msg in st.session_state.history:
    st.markdown(
        f'<div class="user-msg"><b>You:</b> {user_msg}</div>', unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="bot-msg"><b>Chatbot:</b> {bot_msg}</div>', unsafe_allow_html=True
    )
