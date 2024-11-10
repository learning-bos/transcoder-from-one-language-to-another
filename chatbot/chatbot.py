import streamlit as st
from utils import set_session

st.session_state = set_session(st.session_state)

st.title("Chabot codellama:13b")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = st.session_state.chain.invoke(prompt).content
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})


