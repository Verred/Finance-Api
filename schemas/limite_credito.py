from pydantic import BaseModel
from typing import Optional

class LimiteCredito(BaseModel):
    id_limite_credito: Optional[int]
    monto_maximo:float