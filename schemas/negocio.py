from pydantic import BaseModel

class Negocio(BaseModel):
    id: int
    id_usuario: int
    nombre_administrador: str
    nombre_negocio: str
    contrasenna: str
    ruc: str

    class Config:
        orm_mode = True
