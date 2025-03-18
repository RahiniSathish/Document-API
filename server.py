import uvicorn
from app.main import app  # ensure correct relative import

if __name__ == "__main__":
    print("🚀 Starting FastAPI Server from server.py...")
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)