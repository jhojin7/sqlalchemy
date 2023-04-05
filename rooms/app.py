from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def rooms_service():
    return "hello from rooms_service"