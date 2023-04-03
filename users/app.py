from fastapi import FastAPI
import os
# from db import get_session

# app = FastAPI(host="0.0.0.0", port="5556", )
app = FastAPI()

@app.get("/")
def root():
    return "hello from users service"

@app.get("/dbinfo")
def db_info():
    # session = get_session()
    db_url = os.getenv("DB_URL")
    db_name = os.getenv("DB_NAME")
    db_port = os.getenv("DB_PORT")
    db_username = os.getenv("DB_USERNAME")
    # db_password

    return \
    f"""
    {db_url,db_name,db_port,db_username}
    """ 
    # {session}
    # {session.info}