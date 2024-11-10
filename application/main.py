import streamlit as st
from transformers import pipeline

# Upload file
uploaded_file = st.file_uploader("Upload your file")

if uploaded_file is not None:
    # Read file content
    content = uploaded_file.read().decode("utf-8")

    # Display file content (optional)
    st.text("File Content:")
    st.text(content)

    # Load a pre-trained LLM for programming language detection
    classifier = pipeline("text-classification", model="xlm-roberta-base")

    # Predict the programming language
    prediction = classifier(content[:512])  # Limiting to the first 512 tokens

    # Display the prediction
    st.text("Predicted Programming Language:")
    st.write(prediction)
