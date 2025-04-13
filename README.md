# llm_service_architecture# LLM Service Architecture

A modular and flexible architecture for serving multiple LLMs (OpenAI, HuggingFace, LocalAI) through an API interface using FastAPI and LangChain.

---

##  Project Structure

```
llm_service_architecture/
├── api-gateway/             # Gateway to orchestrate routes (WIP)
├── model-orchestrator/     # FastAPI app with LangChain integration
│   ├── chains/             # Logic flows for tasks like chat, email
│   │   ├── chat_chain.py
│   │   └── generation_chain.py
│   ├── models/             # Wrappers for model providers
│   │   ├── openai_wrapper.py
│   │   ├── huggingface_wrapper.py
│   │   └── localai_wrapper.py
│   ├── main.py             # Entry point for the FastAPI server
│   └── requirements.txt
├── models/                  # Reserved for future local models
└── README.md
```

---

##  How It Works

1. User sends a POST request to `/chat` (or future endpoints like `/generate-email`).
2. The orchestrator handles the request via FastAPI.
3. A specific chain (e.g. `get_chat_response`) is triggered.
4. The chain calls the right model (OpenAI / HuggingFace / LocalAI).
5. Response is returned back to the user.

---

## Running Locally

### 1. Build Docker image
```bash
cd model-orchestrator
docker build -t model-orchestrator .
```

### 2. Run container
```bash
docker run -p 8000:8000 --env OPENAI_API_KEY=your_key_here model-orchestrator
```

### 3. Test endpoint
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, who are you?"}'
```

Expected Output:
```json
{"response": "Hello! I am an AI virtual assistant..."}
```

---

##  What's Next

-  Add `generate-email` chain
-  Plug in HuggingFace & LocalAI wrappers
-  Add API Gateway with auth and routing
-  Add usage stats, memory optimization options

---

##  Contributors
- [@serhiiSotskyi](https://github.com/serhiiSotskyi)

---

## 📄 License
MIT License

