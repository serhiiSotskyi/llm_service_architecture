# model-orchestrator/models/openai_wrapper.py

from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage

def chat_with_openai(message: str) -> str:
    chat = ChatOpenAI()
    response = chat.invoke([HumanMessage(content=message)])
    return response.content

def generate_with_openai(prompt: str) -> str:
    llm = ChatOpenAI()
    response = llm.invoke(prompt)
    return response.content
