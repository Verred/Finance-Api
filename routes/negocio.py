from fastapi import APIRouter, HTTPException, status
from typing import List
from config.db import conn
from models.negocio import negocios
from schemas.negocio import Negocio
import config.db as db

negocio = APIRouter()

@negocio.get("/negocios", response_model=List[Negocio], tags=["Negocios"])
def get_all_negocios():
    return conn.execute(negocios.select()).fetchall()

@negocio.post("/negocios", response_model=Negocio, status_code=status.HTTP_201_CREATED, tags=["Negocios"])
def create_negocio(negocio: Negocio):
    new_id = conn.execute(negocios.insert().values(negocio.dict())).lastrowid
    return conn.execute(negocios.select().where(negocios.c.id == new_id)).first()

@negocio.get("/negocios/{id}", response_model=Negocio, tags=["Negocios"])
def get_negocio(id: int):
    negocio = conn.execute(negocios.select().where(negocios.c.id == id)).first()
    if not negocio:
        raise HTTPException(status_code=404, detail="Negocio not found")
    return negocio

@negocio.put("/negocios/{id}", response_model=Negocio, tags=["Negocios"])
def update_negocio(id: int, negocio: Negocio):
    conn.execute(negocios.update().where(negocios.c.id == id).values(negocio.dict()))
    return conn.execute(negocios.select().where(negocios.c.id == id)).first()

@negocio.delete("/negocios/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Negocios"])
def delete_negocio(id: int):
    conn.execute(negocios.delete().where(negocios.c.id == id))
    return {"message": f"Negocio with id {id} successfully deleted!"}
