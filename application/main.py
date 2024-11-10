import streamlit as st
from utils import set_session, is_valid_json

st.session_state = set_session(st.session_state)

# Upload file
uploaded_file = st.file_uploader("Upload your file")

if uploaded_file is not None:
    chain = st.session_state.chain
    messages = st.session_state.messages
    # Read file content
    text_file = uploaded_file.read().decode("utf-8")

    # Call llm with instruction chatprompttemplate
    with st.chat_message("assistant"):

        response = chain.invoke(text_file).content

        if not is_valid_json(response):
            response = "{ 'programming_language': 'unknown' }"    
        st.markdown(response)
        messages.append({"role": "assistant", "content": response})

        # TODO: after loading the file do not display the browse anymore until you finish with this
        # TODO: let the user select the language to convert the provided file
        # TODO: let the user decide whether the conversion is okay or is not


