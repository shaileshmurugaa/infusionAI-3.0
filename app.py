import streamlit as st
import openai
from streamlit_lottie import st_lottie
import requests

# Page configuration
st.set_page_config(page_title="InfusionAI 3.0 - Farmer Chatbot", page_icon="🌾", layout="centered")

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# OpenAI API Key from Streamlit Secrets
openai.api_key = st.secrets["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"]

# Function to load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load an agriculture-themed animation
lottie_farming = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_Cc8Bpg.json")

# Title Section with Animation
st_lottie(lottie_farming, height=200, key="farming")
st.title("🌾 InfusionAI 3.0 - Farmer Chatbot")
st.subheader("Ask anything about farming, crops, or agriculture!")

# Chatbot Function
def farmer_chatbot(user_query):
    system_message = {
        "role": "system",
        "content": "You are a helpful and friendly farming expert. Give simple, short, and practical farming advice. Use a friendly tone."
    }
    user_message = {
        "role": "user",
        "content": user_query
    }
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[system_message, user_message]
    )
    return response['choices'][0]['message']['content']

# User Input
user_input = st.text_input("🌱 What would you like to ask:")

# Bot Response
if user_input:
    with st.spinner('Thinking... 🚜💭'):
        reply = farmer_chatbot(user_input)
    st.success("🤖: " + reply)

# Footer
st.markdown("<hr><center>Made with ❤️ for Farmers | Powered by InfusionAI 3.0</center>", unsafe_allow_html=True)
