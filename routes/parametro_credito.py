import logging
from fastapi import APIRouter, HTTPException, status
from config.db import conn
from models.parametro_credito import parametrocredito
from schemas.parametro_credito import ParametroCredito
from typing import List

parametrocredito=APIRouter()




@parametrocredito.get("/parametrocredito", response_model=List[ParametroCredito], tags=["Parametro Credito"])
def get_all_parametroscredito():
    try:
        with conn.begin() as transaction:
            result = conn.execute(parametrocredito.select()).fetchall()
        return result or []  # Devuelve una lista vacía si result es None
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")







@parametrocredito.post("/parametrocredito", response_model=ParametroCredito, tags=["Parametro Credito"])
def create_parametrocredito (parametrocredito: ParametroCredito):
    try:
        with conn.begin() as transaction:
            new_parametrocredito = {
                "plazo_gracia": parametrocredito.plazo_gracia,
                "tasa_moratoria": parametrocredito.tasa_moratoria,
            }
            result = conn.execute(parametrocredito.insert().values(new_parametrocredito))
            created_bank = conn.execute(parametrocredito.select().where(parametrocredito.c.id == result.lastrowid)).first()
        return created_bank
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")






@parametrocredito.get("/parametroscredito/{id}", response_model=ParametroCredito, tags=["Parametro Credito"])
def get_parametrocredito(id: int):
    try:
        parametro = conn.execute(parametrocredito.select().where(parametrocredito.c.id_parametro_credito == id)).first()
        if parametro is not None:
            return parametro
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="ParametroCredito not found"
            )
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")





@parametrocredito.put("/parametroscredito/{id}", response_model=ParametroCredito, tags=["Parametro Credito"])
def update_bank(id: int, parametrocredito: ParametroCredito):
    try:
        with conn.begin() as transaction:
            conn.execute(
                ParametroCredito.update()
                .where(parametrocredito.c.id == id)
                .values(
                    plazo_gracia=parametrocredito.plazo_gracia,
                    tasa_moratoria=parametrocredito.tasa_moratoria,
                )
            )
            updated_parametrocredito = conn.execute(parametrocredito.select().where(parametrocredito.c.id == id)).first()
        return updated_parametrocredito
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")


@parametrocredito.delete("/parametroscredito/{id}", status_code=status.HTTP_204_NO_CONTENT,
                                tags=["Parametro Credito"])
def delete_parametrocredito(id: int):
    try:
        with conn.begin() as transaction:
            deleted = conn.execute(parametrocredito.delete().where(parametrocredito.c.id == id))
            if deleted.rowcount == 0:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="ParametroCredito not found"
                )
    except Exception as e:
        # Log the error
        logging.error(f"An unhandled error occurred: {e}")
        conn.rollback()  # Rollback en caso de error
        raise HTTPException(status_code=500, detail="Internal Server Error")


