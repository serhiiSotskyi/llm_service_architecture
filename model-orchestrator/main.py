# model-orchestrator/main.py (add to existing FastAPI app)

from fastapi import FastAPI, Request
from chains.chat_chain import get_chat_response
from chains.generation_chain import generate_marketing_copy

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body.get("message")
    language = body.get("language", "en")

    if not user_input:
        return {"error": "Missing 'message' in request body"}

    response = get_chat_response(user_input, language=language)
    return {"response": response}



@app.post("/generate")
async def generate(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    model = body.get("model", "openai")

    if not prompt:
        return {"error": "Missing 'prompt' in request body"}

    response = generate_marketing_copy(prompt, model_name=model)
    return {"response": response}
