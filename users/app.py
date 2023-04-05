from fastapi import FastAPI
import os
from db import get_session

app = FastAPI(host="0.0.0.0", port="5556", )
# app = FastAPI()

@app.get("/")
def root():
    session = get_session()
    return \
    f"""
    return "hello from users service"
    # {session}
    # {session.info}
    """ 