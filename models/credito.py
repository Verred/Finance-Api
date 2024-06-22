from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from config.db import meta, engine

creditos = Table(
    "creditos", meta,
    Column("id_credito", Integer, primary_key=True),
    Column("id_cliente", Integer, ForeignKey("users.id_cliente")),  # Asumiendo que users tiene id_usuario
    Column("id_interes", Integer, ForeignKey("tasa_interes.id_interes")),  # Asumiendo una tabla de intereses
    Column("id_negocio", Integer, ForeignKey("negocios.id_negocio")),  # Asumiendo una tabla de intereses
    Column("tipo_credito", String(255)),
    Column("estado_credito", Boolean)
)

meta.create_all(engine)
