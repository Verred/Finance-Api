from fastapi import APIRouter, HTTPException, status
from typing import List
from config.db import conn
from models.credito import creditos
from schemas.credito import Credito

credito = APIRouter()

@credito.get("/creditos", response_model=List[Credito], tags=["Creditos"])
def get_all_creditos():
    return conn.execute(creditos.select()).fetchall()

@credito.post("/creditos", response_model=Credito, status_code=status.HTTP_201_CREATED, tags=["Creditos"])
def create_credito(credito: Credito):
    new_id = conn.execute(creditos.insert().values(credito.dict())).lastrowid
    return conn.execute(creditos.select().where(creditos.c.id_credito == new_id)).first()

@credito.get("/creditos/{id_credito}", response_model=Credito, tags=["Creditos"])
def get_credito(id_credito: int):
    credito = conn.execute(creditos.select().where(creditos.c.id_credito == id_credito)).first()
    if not credito:
        raise HTTPException(status_code=404, detail="Credito not found")
    return credito

@credito.put("/creditos/{id_credito}", response_model=Credito, tags=["Creditos"])
def update_credito(id_credito: int, credito: Credito):
    conn.execute(creditos.update().where(creditos.c.id_credito == id_credito).values(credito.dict()))
    return conn.execute(creditos.select().where(creditos.c.id_credito == id_credito)).first()

@credito.delete("/creditos/{id_credito}", status_code=status.HTTP_204_NO_CONTENT, tags=["Creditos"])
def delete_credito(id_credito: int):
    conn.execute(creditos.delete().where(creditos.c.id_credito == id_credito))
    return {"message": f"Credito with id {id_credito} successfully deleted!"}
