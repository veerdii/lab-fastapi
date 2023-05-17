from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
async def root():
    
    return {"message": "Hello World"}


class StudentCreateSchema(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item