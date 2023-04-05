from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def reservations_service():
    return "hello from reservations_service"