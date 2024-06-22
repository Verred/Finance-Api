from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float, DateTime
from config.db import meta, engine

pagos = Table(
    "pagos",
    meta,
    Column("id_pago", Integer, primary_key=True),
    Column('id_venta', Integer, ForeignKey('ventas.id_venta')),
    Column("monto_pago", Float),
    Column("fecha_pago", DateTime)
)

meta.create_all(engine)