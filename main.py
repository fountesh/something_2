from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any
import uvicorn


app = FastAPI()

users: List[Any] = []

class User(BaseModel):
    id: int
    username:str
    email: str
    

@app.get("/users", response_model=list[User])
def get_all_users():
    
    return users


@app.get("/users/{user_id}", response_model=User)
def get_user_by_id(user_id: int):
    
    return users[user_id]    


@app.post("/create_user", response_model=User)
def create_user(user: User):
    users.append(user)
    
    return user

if __name__ == "__main__":
    uvicorn.run("my_app:app", host="localhost", port=1000, reload=True)