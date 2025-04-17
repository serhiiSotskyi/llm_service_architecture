# model-orchestrator/chains/generation_chain.py


from models.openai_wrapper import generate_with_openai
from models.huggingface_wrapper import generate_with_huggingface


def generate_marketing_copy(prompt: str, model_name: str = "openai") -> str:
    if model_name == "openai":
        return generate_with_openai(prompt)
    elif model_name == "huggingface":
        return generate_with_huggingface(prompt)
    else:
        return "Unsupported model specified"