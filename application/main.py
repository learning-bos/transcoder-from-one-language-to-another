import streamlit as st

# Upload file
uploaded_file = st.file_uploader("Upload your file")

if uploaded_file is not None:
    # Do something with the file here
    pass