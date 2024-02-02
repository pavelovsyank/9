import uvicorn 
from app.config import settings

if __name__ == "__main__":
    #print(f"port = {settings.port}")
    uvicorn.run("app.main:app", port=5000, log_level="info")
