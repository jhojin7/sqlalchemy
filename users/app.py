from fastapi import FastAPI
import os
from db import get_session

import requests
from fastapi.responses import RedirectResponse
# https://fastapi.tiangolo.com/advanced/custom-response/#redirectresponse


app = FastAPI()

@app.get("/")
def root():
    session = get_session()
    return f"hello world from {session}"

@app.get("/rooms")
def rooms_service():
    # return RedirectResponse("http://localhost:5557")
    # return requests.get("http://localhost:5557").text
    return requests.get("rooms:5557").text

@app.get("/reservations")
def reservations_service():
    # return RedirectResponse("http://localhost:5558")
    return requests.get("http://localhost:5558").text