# This is a sample Python script for learning fastapi

# imports
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return({"message": "Hello Donald"})

