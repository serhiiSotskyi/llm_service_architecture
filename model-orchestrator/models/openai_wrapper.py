# model-orchestrator/models/openai_wrapper.py

# New
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os

# Ensure you have your OpenAI key in .env or environment
openai_api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-3.5-turbo")

def chat_with_openai(prompt: str) -> str:
    messages = [HumanMessage(content=prompt)]
    result = chat(messages)
    return result.content