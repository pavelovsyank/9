import uvicorn 
from app.config import settings

if __name__ == "__main__":
    #print(f"port = {settings.port}")
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.port, log_level="info")
