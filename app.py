import google.generativeai as genai
import streamlit as st
import os
import base64
import json
import requests

genai.configure(api_key='AIzaSyBFCeAPTlZiYw9NYrrRPvw4pETGFo6Awuc')
generation_config_b64 = 'eyJ0ZW1wZXJhdHVyZSI6MC45LCJ0b3BfcCI6MSwidG9wX2siOjEsIm1heF9vdXRwdXRfdG9rZW5zIjoyMDQ4LCJzdG9wX3NlcXVlbmNlcyI6W119' # @param {isTemplate: true}
safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d' # @param {isTemplate: true}
generation_config = json.loads(base64.b64decode(generation_config_b64))
safety_settings = json.loads(base64.b64decode(safety_settings_b64))
model = genai.GenerativeModel('gemini-pro')

def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="BLOGGSS", page_icon="📝", layout="centered")

st.header("BLOGZILLA  🧾🧾")
st.subheader("Enter your topic below and the AI will generate a BLOG for you !!")

with st.sidebar:
    st.write('With an intuitive user interface and a user-friendly design, this web application invites users to embark on a creative odyssey. By simply providing a few details about the user"s interests the application harnesses the transformative power of Gemini Pro to generate a quality Blog with  emotional depth.')

aoi = [
    "Reading",
    "Writing",
    "Listening to music",
    "Watching movies",
    "Playing ",
    "Traveling",
    "Cooking",
    "Gardening",
    "Photography",
    "Learning new skills",
    "Meditation",
    "Family Time",
    "Volunteering",
    "Technology",
    "Science",
    "History",
    "Politics",
    "Economics",
    "Philosophy",
    "Psychology",
    "Sociology",
    "Art",
    "Music",
    "Literature",
    "Fashion",
    "Travel",
    "Food and drink",
    "Health and wellness",
    "Sports",
    "Current events",
    "Sports",
    "Researching",
    "Spiritual Journeys"
]


col1, col2 , col3 = st.columns(3)


with col1:
    name = st.text_input('Name')
    age = st.text_input('Age')
    gender = st.selectbox('Gender',options=['Male','Female'])
    

with col2:
    interest = st.multiselect('Interests',options=aoi)
    blog_style = st.selectbox("Choose blog style", ["Modern", "Classic", "Formal", "Casual", "Futuristic", "Research"])
    readability = st.selectbox("Choose Your readability", ["Easy", "Medium", "Hard"])

with col3:
    num_words = st.number_input("Number of words", min_value=50, max_value=500, value=100, step=50)
    language = st.selectbox("Choose language", ["English", "Hindi", "French", "German", "Spanish"])


topic = st.text_input("Enter your topic here")



contents = 'A person whose name is '+name+'. Gender is '+gender+'. Age is '+age+'. Area of interest are '+",".join(interest)
contents += 'Write a  quality blog describing the person"s specified topic which will be a masterpiece when read by a user . Language of the poem would be'+language+'.'

submit = st.button("SUBMIT")

if submit:
    prompt = "Write a blog post about " + topic + " in " + language + " in a " + blog_style + " style that is " + readability + " to read. The blog should be " + str(num_words) + " words long."
    with st.spinner("Close your eyes, the story's about to unfold…"):
        try:
            response = get_response(contents)
            st.success("Drumroll please... your result is here to steal the show!")
            
            st.write(response)
            st.balloons()
            st.write(response)
        except Exception as e:
            print(e)
            st.error("I think You may have entered the wrong spell..." ,  icon="😵")
            st.snow()
            
