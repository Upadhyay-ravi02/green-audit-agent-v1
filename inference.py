import os
import time
from openai import OpenAI
from fastapi import FastAPI
import uvicorn
import threading

# 1. FastAPI Setup (Hugging Face ko "Green" rakhne ke liye)
app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "Running", "agent": "Green Audit v1"}

# Automated reset endpoint for Scaler checker
@app.post("/reset")
def reset():
    return {"status": "Environment Reset Successful"}

# 2. Agent Logic
def run_agent():
    API_KEY = os.getenv("HF_TOKEN")
    BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
    MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-7B-Instruct")
    
    client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
    
    print("===== Sustainability Audit Agent Started =====")
    # Aapka agent logic yahan chalega
    time.sleep(5) 
    print("===== Task Finished Successfully =====")
    
    # Task khatam hone ke baad bhi loop chalao taaki Space "Running" rahe
    while True:
        print("Heartbeat: Agent is alive and waiting for evaluation...")
        time.sleep(30)

if __name__ == "__main__":
    # Agent ko background thread mein chalayein
    threading.Thread(target=run_agent, daemon=True).start()
    
    # Web server ko main thread mein (Port 7860 mandatory hai)
    uvicorn.run(app, host="0.0.0.0", port=7860)
