import streamlit as st
import requests
import json

st.title("HACK BOT")

# Create placeholder for chat history

data = st.text_input("Enter your text", value="")
json_data = json.dumps({"text": data})

if st.button('Send'):
    headers = {"Content-Type": "application/json"}
    res = requests.post(url="https://calm-garden-60655.herokuapp.com/predict", data=json_data, headers=headers)
    result = res.json()
    language = result["language"]
    st.subheader(f"Hack Bot: {language}")
