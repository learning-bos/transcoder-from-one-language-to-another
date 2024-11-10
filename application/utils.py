from streamlit import _SessionStateProxy
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

def set_session(session: _SessionStateProxy) -> _SessionStateProxy:
    if "llm" not in session:
        session.llm = ChatOllama(
            model="codellama:13b",
            temperature=0.1
        )
    if "prompt " not in session:
        session.prompt = ChatPromptTemplate.from_messages(
            [
                (   "human", "{input}"),
                (
                    "system"," You are a code classifier expert, based on the text provided by the user you should tell the programming language used with the following output strategy: {{ \"programming_language\": \"<THE PROGRAMMING LANGUAGE>\"}}, dont use any other output strategies.",
                ),
            ]
        )
    if "chain" not in session:
        session.chain = session.prompt | session.llm

    if "messages" not in session:
        session.messages = []

    return session

import json

def is_valid_json(string):
    try:
        json.loads(string)
    except ValueError:
        return False
    return True