import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie Animation
lottie_animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_hzgq1iov.json")

# Streamlit app UI
st_lottie(lottie_animation, height=300)
st.title("🚜 InfusionAI 3.0 — Farmer Chatbot")

# Set up Gemini API Key (stored in Streamlit secrets)
gemini_api_key = st.secrets["AIzaSyBhJszyHs6iH1oLAz2TNDCWuTRzjmC4344"]

# Gemini API URL
gemini_api_url = "https://api.gemini.com/v1/assistant"  # Replace with actual Gemini API endpoint

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Chat input
user_input = st.chat_input("👨‍🌾 Ask your farming question:")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner('Thinking... 🤔'):
        # Make the request to Gemini API
        response = requests.post(
            gemini_api_url,
            headers={"Authorization": f"Bearer {gemini_api_key}"},
            json={"input": user_input}
        )

        if response.status_code == 200:
            bot_reply = response.json().get("response", "Sorry, I couldn't get an answer.")
        else:
            bot_reply = "Error: Could not connect to Gemini API."

    # Add bot reply to history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display latest bot reply
    st.chat_message("assistant").markdown(bot_reply)
