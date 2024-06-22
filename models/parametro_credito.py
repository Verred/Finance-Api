from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float, Numeric
from config.db import meta, engine

parametrocredito = Table(
    "parametro_creditos",
    meta,
    Column("id_parametro_credito", Integer, primary_key=True),
    Column("plazo_gracia", Integer),
    Column("id_interes", Integer, ForeignKey("tasa_interes.id_interes")),
    Column("tasa_moratoria", Numeric(10, 2)),
)


meta.create_all(engine)
