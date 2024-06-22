from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from routes.user import user
from routes.tasa_interes import Tasa_interes


from routes.product import product


from routes.negocio import negocio
from routes.limite_credito import limitecredito
from routes.parametro_credito import parametrocredito
from routes.credito import credito
from routes.venta import  venta_router as venta
from routes.payment import pago

app = FastAPI(
    title="Finance",
    description="A simple finance API using FastAPI and MySQL",
    version="0.1.0"
)

origins = [
    "https://finanze.app",
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(negocio)
app.include_router(parametrocredito)
app.include_router(limitecredito)
app.include_router(product)
app.include_router(credito)
app.include_router(Tasa_interes)

app.include_router(venta)
app.include_router(pago)



@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs", status_code=status.HTTP_303_SEE_OTHER)

