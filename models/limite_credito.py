from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float,Numeric
from config.db import meta, engine

limitecredito = Table(
    "limite_creditos",
    meta,
    Column("id_limite_credito", Integer, primary_key=True),
    Column("monto_maximo", Numeric(10, 2)),
    Column("id_cliente", Integer, ForeignKey("users.id_cliente")),  # Asumiendo que users tiene id_usuario

)


meta.create_all(engine)
