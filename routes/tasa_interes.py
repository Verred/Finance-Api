from fastapi import APIRouter, HTTPException, status
from typing import List
from config.db import conn
from models.tasa_interes import tasa_interes
from schemas.tasa_interes import TasaInteres
from config.db import conn

Tasa_interes = APIRouter()

@Tasa_interes.get("/tasa_interes", response_model=List[TasaInteres], tags=["TasaInteres"])
def get_all_tasa_interes():
    return conn.execute(tasa_interes.select()).fetchall()

@Tasa_interes.post("/tasa_interes", response_model=TasaInteres, status_code=status.HTTP_201_CREATED, tags=["TasaInteres"])
def create_tasa_interes(tasa_interes: TasaInteres):
    new_id = conn.execute(tasa_interes.insert().values(tasa_interes.dict())).lastrowid
    return conn.execute(tasa_interes.select().where(tasa_interes.c.id_interes == new_id)).first()

@Tasa_interes.get("/tasa_interes/{id_interes}", response_model=TasaInteres, tags=["TasaInteres"])
def get_tasa_interes(id_interes: int):
    tasa = conn.execute(tasa_interes.select().where(tasa_interes.c.id_interes == id_interes)).first()
    if not tasa:
        raise HTTPException(status_code=404, detail="Tasa de interes not found")
    return tasa

@Tasa_interes.put("/tasa_interes/{id_interes}", response_model=TasaInteres, tags=["TasaInteres"])
def update_tasa_interes(id_interes: int, tasa: TasaInteres):
    conn.execute(tasa_interes.update().where(tasa_interes.c.id_interes == id_interes).values(tasa.dict()))
    return conn.execute(tasa_interes.select().where(tasa_interes.c.id_interes == id_interes)).first()

@Tasa_interes.delete("/tasa_interes/{id_interes}", status_code=status.HTTP_204_NO_CONTENT, tags=["TasaInteres"])
def delete_tasa_interes(id_interes: int):
    conn.execute(tasa_interes.delete().where(tasa_interes.c.id_interes == id_interes))
    return {"message": f"Tasa de interes with id {id_interes} successfully deleted!"}
