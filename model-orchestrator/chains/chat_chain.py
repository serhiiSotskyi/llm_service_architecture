# model-orchestrator/chains/chat_chain.py

from models.openai_wrapper import chat_with_openai


def get_chat_response(message: str, language: str = "en") -> str:
    if language == "en":
        return chat_with_openai(message)
    elif language == "fr":
        return f"[HF Chat simulated response to '{message}' using model 'mistralai/Mistral-7B-Instruct-v0.2']"
    elif language == "uk":
        return f"[HF Chat simulated response to '{message}' using model 'google/flan-t5-base']"
    else:
        return f"[LocalAI simulated response to]: {message}"
