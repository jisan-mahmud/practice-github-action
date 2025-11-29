from fastapi import FastAPI
import os
import sys

app = FastAPI()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@app.get('/')
async def hello():
    return "Hello Fastapi"