# package
from fastapi import FastAPI

# initial fastapi app
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}
