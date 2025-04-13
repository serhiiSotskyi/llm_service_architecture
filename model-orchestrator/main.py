# model-orchestrator/main.py

from fastapi import FastAPI, Request
from chains.chat_chain import get_chat_response

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body.get("message")
    if not user_input:
        return {"error": "Missing 'message' in request body"}
    
    response = get_chat_response(user_input)
    return {"response": response}
