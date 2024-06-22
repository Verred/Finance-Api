from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

# Definición de la tabla negocio
negocios = Table(
    "negocios", meta,
    Column("id_negocio", Integer, primary_key=True),
    Column("id_cliente", Integer, ForeignKey("users.id_cliente")),  # Asumiendo que users tiene id_usuario
    Column("nombre_administrador", String(30)),
    Column("nombre_negocio", String(30)),
    Column("contrasenna", String(30)),
    Column("ruc", String(30))
)
meta.create_all(engine)