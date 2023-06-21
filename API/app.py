import streamlit as st
from Clickbait_generator import generator

#giving a title
st.title("Clickbait Generator")

clickbait=''

if st.button('Generate clickbait!'):
    clickbait=generator()
    
st.success(clickbait)