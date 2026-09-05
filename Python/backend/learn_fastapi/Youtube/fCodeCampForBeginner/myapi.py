from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "root"}


uvicorn.run(app, port=8006)
