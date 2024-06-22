from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float, Numeric, String, DateTime
from config.db import meta, engine

ventas = Table(
    "ventas",
    meta,
    Column("id_venta", Integer, primary_key=True),
    Column("fecha_venta", DateTime),
    Column("monto_venta", Numeric(precision=10, scale=2)),
    Column("id_credito", Integer, ForeignKey("creditos.id_credito")),  # Asumiendo una tabla de intereses
    Column("id_producto", Integer, ForeignKey("productos.id_producto"))

)
meta.create_all(engine)