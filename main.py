from fastapi import FastAPI

app = FastAPI(title="Music Board", description="Small project to improve fastapi ", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Hello World"}

