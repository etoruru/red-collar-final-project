

from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def root():
    return {"message": "Hello from Python!git "}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}