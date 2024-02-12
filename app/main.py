from fastapi import FastAPI
from app.endpoints.api import router


app = FastAPI()

app.include_router(router)

@app.get("/")
def hello():
    return {"message": "Hello page!"}
