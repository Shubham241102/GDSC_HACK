import google.generativeai as genai
import streamlit as st
import os

genai.configure(api_key=st.secrets['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="Irsaad", page_icon="📝", layout="centered")

st.header("EK SHAYRI DIJIYE")
st.subheader("Enter your topic below and the AI will generate a shayri for you !!")

topic = st.text_input("Enter your topic here")

col1, col2 = st.columns([5, 5])

with col1:
    num_words = st.number_input("Number of words", min_value=50, max_value=500, value=100, step=50)
    language = st.selectbox("Choose language", ["English", "Hindi"])

with col2:
    readability = st.selectbox("Choose readability", ["Easy", "Medium", "Hard"])

submit = st.button("SUBMIT")

if submit:
    prompt = "Write a shayri about " + topic + " in " + language + " in a style that is " + readability + " to read. The blog should be " + str(num_words) + " words long."
    with st.spinner("Rukiyee"):
        try:
            response = get_response(prompt)
            st.success("YE rahi Aapki Shayri !!!")
            st.write(response)
        except Exception as e:
            print(e)
            st.error("Something went wrong. Please try again.")
