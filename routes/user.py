from fastapi import APIRouter, HTTPException, status
from config.db import conn
from models.user import users
from schemas.user import User
from typing import List
from fastapi import Depends
import config.db as db


user = APIRouter()

@user.get("/users", response_model=List[User], tags=["Users"])
def get_all_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users", response_model=User, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user: User):
    new_id = conn.execute(users.insert().values(user.dict())).lastrowid
    return conn.execute(users.select().where(users.c.id_cliente == new_id)).first()

@user.get("/users/{id_cliente}", response_model=User, tags=["Users"])
def get_user(id_cliente: int):
    user = conn.execute(users.select().where(users.c.id_cliente == id_cliente)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user.put("/users/{id_cliente}", response_model=User, tags=["Users"])
def update_user(id_cliente: int, user: User):
    conn.execute(users.update().where(users.c.id_cliente == id_cliente).values(user.dict()))
    return conn.execute(users.select().where(users.c.id_cliente == id_cliente)).first()

@user.delete("/users/{id_cliente}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id_cliente: int):
    conn.execute(users.delete().where(users.c.id_cliente == id_cliente))
    return {"message": f"User with id {id_cliente} successfully deleted!"}