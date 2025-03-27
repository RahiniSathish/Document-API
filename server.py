import uvicorn
from app.main import app 
if __name__ == "__main__":
    print("Starting FastAPI Server from server.py...")
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
