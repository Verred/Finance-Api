import logging
from fastapi import APIRouter, HTTPException, status
from config.db import conn
from models.venta import ventas
from schemas.venta import Venta
from typing import List

venta_router = APIRouter()  # Cambiado de 'venta' a 'router' para evitar conflictos

@venta_router.get("/ventas", response_model=List[Venta], tags=["Ventas"])
def get_all_ventas():
    try:
        with conn.begin() as transaction:
            result = conn.execute(ventas.select()).fetchall()
        return result or []  # Devuelve una lista vacía si result es None
    except Exception as e:
        logging.error(f"An unhandled error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@venta_router.post("/ventas", response_model=Venta, tags=["Ventas"])
def create_venta(venta_data: Venta):
    try:
        new_venta = {
            "fecha_venta": venta_data.fecha_venta,
            "monto_venta": venta_data.monto_venta,
        }
        with conn.begin() as transaction:
            result = conn.execute(ventas.insert().values(new_venta))
            created_venta = conn.execute(ventas.select().where(ventas.c.id_venta == result.lastrowid)).first()
        return created_venta
    except Exception as e:
        logging.error(f"An unhandled error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@venta_router.get("/ventas/{id}", response_model=Venta, tags=["Ventas"])
def get_venta(id: int):
    try:
        venta = conn.execute(ventas.select().where(ventas.c.id_venta == id)).first()
        if venta is not None:
            return venta
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Venta not found"
            )
    except Exception as e:
        logging.error(f"An unhandled error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@venta_router.put("/ventas/{id}", response_model=Venta, tags=["Ventas"])
def update_venta(id: int, venta_data: Venta):
    try:
        with conn.begin() as transaction:
            conn.execute(
                ventas.update()
                .where(ventas.c.id_venta == id)
                .values(
                    fecha_venta=venta_data.fecha_venta,
                    monto_venta=venta_data.monto_venta,
                )
            )
            updated_venta = conn.execute(ventas.select().where(ventas.c.id_venta == id)).first()
        return updated_venta
    except Exception as e:
        logging.error(f"An unhandled error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@venta_router.delete("/ventas/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Ventas"])
def delete_venta(id: int):
    try:
        with conn.begin() as transaction:
            deleted = conn.execute(ventas.delete().where(ventas.c.id_venta == id))
            if deleted.rowcount == 0:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Venta not found"
                )
    except Exception as e:
        logging.error(f"An unhandled error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")