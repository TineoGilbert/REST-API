from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4 as uuid
from typing import Optional

class Users(BaseModel):
    id: Optional[str]
    name: str
    email: str
    created_at: datetime = datetime.now()

app = FastAPI(
    title="API CRUD",
    version="0.0.2",
    contact={
        "name": "Gilbert E. Tineo",
        "email": "tineogilbert@gmail.com"
    },
    license_info={
        "name": "MIT"
    }
)

db = [];


@app.get("/")
async def root():
    return "Fast API"

@app.get("/users")
async def get_users():
    return db


@app.post("/createuser")
async def create_user(user: Users):
    user.id = str(uuid())
    db.append(user.dict());
    return db[-1]


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    for user in db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not Found")


@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    for index, user in enumerate(db):
        if user["id"] == user_id:
            db.pop(index)
            return "User Eliminated!"
    raise HTTPException(status_code=404, detail="User not Found")

@app.put("/users/{user_id}")
async def update_user(user_id: str, updateUser: Users):
    for index, user in enumerate(db):
        if user["id"] == user_id:
            db[index]["name"] = updateUser.name
            db[index]["email"] = updateUser.email
            return "User Updated"
    raise HTTPException(status_code=404, detail="User not Found")

