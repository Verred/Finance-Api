from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Venta(BaseModel):
    id_venta: int
    fecha_venta: datetime
    monto_venta: float
    id_credito: int
    id_producto: int