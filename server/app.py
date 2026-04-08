from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Green Audit Agent is Running"}

@app.post("/reset")
def reset():
    return {"status": "Environment Reset Successful"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
