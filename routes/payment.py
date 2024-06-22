from fastapi import APIRouter, HTTPException, status
from config.db import conn
from models.payment import pagos
from schemas.payment import Pago
from typing import List
from fastapi import Depends
import config.db as db


pago = APIRouter()

@pago.get("/payments", response_model=List[Pago], tags=["Payments"])
def get_all_payments():
    with db.engine.connect() as conn:
        return conn.execute(pagos.select()).fetchall()

@pago.post("/payments", response_model=Pago, status_code=status.HTTP_201_CREATED, tags=["Payments"])
def create_payment(payment: Pago):
    with db.engine.connect() as conn:
        result = conn.execute(pagos.insert().values(payment.dict()))
        return conn.execute(pagos.select().where(pagos.c.id == result.lastrowid)).first()

@pago.get("/payments/{id}", response_model=Pago, tags=["Payments"])
def get_payment(id: int):
    with db.engine.connect() as conn:
        payment = conn.execute(pagos.select().where(pagos.c.id == id)).first()
        if not payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
        return payment

@pago.delete("/payments/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Payments"])
def delete_payment(id: int):
    with db.engine.connect() as conn:
        result = conn.execute(pagos.delete().where(pagos.c.id == id))
        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
        return {"message": f"Payment with id {id} deleted successfully!"}

