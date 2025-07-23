from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

@app.get("/")
async def getData():
    return {"message":"Hello!"}