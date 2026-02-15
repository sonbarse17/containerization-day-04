from fastapi import FastAPI
from app.utils import add
 
app = FastAPI()
 
@app.get("/")
def root():
    return {"message": "App is running"}
 
@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    return {"result": add(a, b)}