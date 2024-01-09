from fastapi import FastAPI
import models


app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello Worldd"}
