from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Pago(BaseModel):
    id_pago: int
    id_venta: int
    monto_pago: float
    fecha_pago: datetime
