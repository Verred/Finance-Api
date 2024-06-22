from pydantic import BaseModel
from typing import Optional

class ParametroCredito(BaseModel):
    id_parametro_credito: Optional[int]
    plazo_gracia: int
    tasa_moratoria: float

