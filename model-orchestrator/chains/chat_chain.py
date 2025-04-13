# model-orchestrator/chains/chat_chain.py

from models.openai_wrapper import chat_with_openai


def get_chat_response(user_input: str) -> str:
    response = chat_with_openai(user_input)
    return response
