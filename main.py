from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.get("/me")
def read_me():
    return {"Hello": "Me!"}