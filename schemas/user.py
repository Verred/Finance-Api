from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id_cliente: int
    nombre_cliente: str
    Contrasena: str
    Fecha_creacion: datetime
    estado_usuario: bool
    edad: int
    dni: str
    correo: str
    celular: str


