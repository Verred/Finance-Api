from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id_product: int
    name_product: str
    type_product: str
    price_product: float