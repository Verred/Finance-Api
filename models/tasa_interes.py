from sqlalchemy import Table, Column, Integer, String, Float
from config.db import meta, engine

tasa_interes = Table(
    "tasa_interes", meta,
    Column("id_interes", Integer, primary_key=True),
    Column("tipo_tasa", String(255)),
    Column("valor_tasa", Float)
)
meta.create_all(engine)