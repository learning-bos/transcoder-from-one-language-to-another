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
                (
                    "system",
                    "You are a helpful assistant that help the user to code",
                ),
                (   "human", "{input}"),
            ]
        )
    if "chain" not in session:
        session.chain = session.prompt | session.llm

    if "messages" not in session:
        session.messages = []

    return session