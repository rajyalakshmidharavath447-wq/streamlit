import streamlit as st
from dotenv import load_dotenv
import os
from google import genai
#load environment variables
load_dotenv()
#get api key 
api_key=os.getenv("GEMINI_API_KEY")
#create gemini client
client=genai.Client(api_key=api_key)
#page configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)
#Title
st.title("Gemini AI Chatbot")
st.write("Ask Gemini anything!!")
#user prompt
prompt=st.text_area(
    "Enter your prompt:",
    placeholder="Explain Aritfical Intelligence in simple words..."
)
#create button
if st.button("Generate Response"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            response=client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )
        st.success("Response generated!")
        st.write(response.text)
    else:
        st.warning("Please enter a prompt.")str