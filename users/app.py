from fastapi import FastAPI
import os
from db import get_session

app = FastAPI(host="0.0.0.0", port="5556", )

@app.get("/")
def root():
    session = get_session()
    return {"hello world":f"{session}"}