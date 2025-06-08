from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from routes import router
from auth import router as auth_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(router) 

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running for TEST"}

@app.get("/TEST")
def say_test():
    return {"message": "Hello, FastAPI!"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "message": f"User {user_id} Find."}

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Created item!", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": f"Item {item_id} Updated!", "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted!"}