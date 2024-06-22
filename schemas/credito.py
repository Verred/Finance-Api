from pydantic import BaseModel

class Credito(BaseModel):
    id_credito: int
    id_usuario: int
    id_intereses: int
    tipo_credito: str
    estado_credito: bool

    class Config:
        orm_mode = True
