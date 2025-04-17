# model-orchestrator/chains/generation_chain.py

from models.openai_wrapper import generate_with_openai

def generate_marketing_copy(prompt: str, model_name: str = "openai") -> str:
    if model_name == "openai":
        return generate_with_openai(prompt)
    elif model_name == "huggingface":
        return generate_with_huggingface(prompt)
    else:
        return "Unsupported model specified"
    
def generate_with_huggingface(prompt: str) -> str:
    # Simulated response (replace with real API if needed)
    return f"[HF Model Response to]: {prompt}"
