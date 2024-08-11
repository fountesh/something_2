from fastapi import FastAPI
import uvicorn
from typing import List 
from pydantic import BaseModel

app = FastAPI

users: List[any] = []

class User(BaseModel):
    id:int
    username:str
    email:str

@app.get("/users", response_model=list[User])
def get_all_users(user_list=users):
    
    return users

@app.get("/users/{user_id}", response_model=User)
def get_user_by_id(user_id:int):
    
    return users[user_id]

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=1000, reload=True)
