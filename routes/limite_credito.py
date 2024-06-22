import logging
from fastapi import APIRouter, HTTPException, status
from config.db import conn
from models.limite_credito import limitecredito
from schemas.limite_credito import LimiteCredito
from typing import List

limitecredito= APIRouter()


@limitecredito.get("/limitecredito", response_model=List[LimiteCredito], tags=["Limite Credito"])
def get_all_limitescredito():
    try:
        with conn.begin() as transaction:
            result = conn.execute(limitecredito.select()).fetchall()
        return result or []  # Devuelve una lista vacía si result es None
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")







@limitecredito.post("/limitecredito", response_model=LimiteCredito, tags=["Limite Credito"])
def create_limitecredito (limitecredito: LimiteCredito):
    try:
        with conn.begin() as transaction:
            new_limitecredito = {
                "monto_maximo": limitecredito.monto_maximo,

            }
            result = conn.execute(limitecredito.insert().values(new_limitecredito))
            created_limitecredito = conn.execute(limitecredito.select().where(limitecredito.c.id == result.lastrowid)).first()
        return created_limitecredito
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")








@limitecredito.get("/limitescredito/{id}", response_model=LimiteCredito, tags=["Limite Credito"])
def get_limitecredito(id: int):
    try:
        limite = conn.execute(limitecredito.select().where(limitecredito.c.id_limite_credito == id)).first()
        if limite is not None:
            return limite
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="LimiteCredito not found"
            )
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")



@limitecredito.put("/limitescredito/{id}", response_model=LimiteCredito, tags=["Limite Credito"])
def update_bank(id: int, limitecredito: LimiteCredito):
    try:
        with conn.begin() as transaction:
            conn.execute(
                LimiteCredito.update()
                .where(limitecredito.c.id == id)
                .values(

                    monto_maximo=limitecredito.monto_maximo,
                )
            )
            updated_limitecredito = conn.execute(limitecredito.select().where(limitecredito.c.id == id)).first()
        return updated_limitecredito
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")


@limitecredito.delete("/limitescredito/{id}", status_code=status.HTTP_204_NO_CONTENT,
                                tags=["Limite Credito"])
def delete_limitecredito(id: int):
    try:
        with conn.begin() as transaction:
            deleted = conn.execute(limitecredito.delete().where(limitecredito.c.id == id))
            if deleted.rowcount == 0:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="LimiteCredito not found"
                )
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")