from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Float, Numeric, String
from config.db import meta, engine

productos = Table(
    "productos",
    meta,
    Column("id_producto", Integer, primary_key=True),
    Column("name_product", String(30)),
    Column("type_product", String(30)),
    Column("price_product", Float)
)
meta.create_all(engine)