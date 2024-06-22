from pydantic import BaseModel

class TasaInteres(BaseModel):
    id_interes: int
    tipo_tasa: str
    valor_tasa: float

    class Config:
        orm_mode = True
