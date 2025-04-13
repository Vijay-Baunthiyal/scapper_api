from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import APIKeyHeader

app = FastAPI()

# Set your desired API key here
API_KEY = "Hitarth123"
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# Auth function
async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

def run_main_script_logic():
    # Your secure logic here
    return {"status": "Script logic executed", "data": [1, 2, 3]}

@app.get("/")
async def root():
    return {"message": "Welcome to the public endpoint"}

# Secure route
@app.get("/secure")
async def secure_route(api_key: str = Depends(verify_api_key)):
    result = run_main_script_logic()
    return result